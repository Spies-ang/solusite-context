#!/usr/bin/env python3
"""
strip_archetype.py

Converts a Solusite client repo into a clean archetype skeleton.

USAGE:
    python3 strip_archetype.py /path/to/repo [--archetype-name NAME]

WHAT IT DOES (sequential, with prompts between stages):
  Stage 1 — SCAN: read-only pass that builds a report of everything
           business-specific found in src/*.tsx and src/*.ts
  Stage 2 — REVIEW: prints the report, pauses for confirmation
  Stage 3 — SKELETONIZE: rewrites src/siteConfig.ts (or src/config/siteConfig.ts)
           with placeholder sentinels; flags component-level hardcoding
           for manual follow-up
  Stage 4 — REPORT: writes SCAN_REPORT.md + MANUAL_FIXES.md to repo root

REQUIREMENTS:
  - Python 3.8+
  - No external deps (stdlib only)

SAFETY:
  - Git revert is your undo button. Commit before running.
  - Script refuses to run if repo has uncommitted changes (override with --force)
  - All file writes are logged; originals backed up to .strip_backup/
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict


# ============================================================
# PATTERNS — the "things that look business-specific" heuristics
# ============================================================

# South African phone number patterns
PHONE_PATTERNS = [
    re.compile(r'\+27\s?\d{2}\s?\d{3}\s?\d{4}'),              # +27 83 653 9823
    re.compile(r'\b0\d{2}\s?\d{3}\s?\d{4}\b'),                # 083 653 9823
    re.compile(r'\b0\d{9}\b'),                                 # 0836539823
]

# Email
EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Local image imports (the recycling killer)
LOCAL_IMAGE_IMPORT = re.compile(
    r'import\s+\w+\s+from\s+["\']@?/?assets/[\w\-./]+\.(?:jpg|jpeg|png|webp|svg)["\']'
)

# Hardcoded arrays that should come from siteConfig — catches .map() over literals
# e.g. const team = [{ name: "Tienie", role: "..." }, ...]
HARDCODED_ARRAY_PATTERN = re.compile(
    r'const\s+(\w+)\s*=\s*\[\s*\{[^}]*(?:name|title|role|service|project)[^}]*\}',
    re.IGNORECASE | re.DOTALL
)

# South African city names (partial list — catches the common ones)
SA_CITIES = [
    "Pretoria", "Johannesburg", "Joburg", "Sandton", "Cape Town", "Durban",
    "Bloemfontein", "Port Elizabeth", "Gqeberha", "East London", "Polokwane",
    "Nelspruit", "Kimberley", "Stellenbosch", "Centurion", "Midrand",
    "Randburg", "Roodepoort", "Germiston", "Boksburg", "Benoni",
    "Hatfield", "Brooklyn", "Menlyn", "Waterkloof", "Lynnwood",
    "Sandton City", "Rosebank", "Fourways", "Bryanston", "Constantia",
    "Camps Bay", "Sea Point", "Umhlanga", "Ballito", "La Lucia",
]
CITY_PATTERN = re.compile(r'\b(' + '|'.join(SA_CITIES) + r')\b')

# Suspicious JSX text — hardcoded strings inside components that look like content
# (long strings in JSX that aren't CSS classes or variables)
# We look for strings 10+ chars appearing between > and < in JSX, OR assigned to title/name/heading props
JSX_HARDCODED_TEXT = re.compile(
    r'>([A-Z][a-zA-Z0-9,. \-&\']{15,})<'
)

# siteConfig import check — components SHOULD be importing from siteConfig
SITECONFIG_IMPORT = re.compile(
    r'import\s+\{[^}]*siteConfig[^}]*\}\s+from\s+["\'][^"\']*siteConfig["\']'
)


# ============================================================
# DATA CLASSES
# ============================================================

@dataclass
class Finding:
    file: str
    line: int
    category: str
    snippet: str
    severity: str  # "critical" | "warning" | "info"
    note: str = ""


@dataclass
class ScanResult:
    findings: List[Finding] = field(default_factory=list)
    files_scanned: int = 0
    siteconfig_path: str = ""
    components_missing_siteconfig: List[str] = field(default_factory=list)

    def critical(self) -> List[Finding]:
        return [f for f in self.findings if f.severity == "critical"]

    def warnings(self) -> List[Finding]:
        return [f for f in self.findings if f.severity == "warning"]

    def info(self) -> List[Finding]:
        return [f for f in self.findings if f.severity == "info"]


# ============================================================
# UTILITIES
# ============================================================

def run_git(repo: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True
    )


def check_git_clean(repo: Path, force: bool = False) -> bool:
    result = run_git(repo, "status", "--porcelain")
    if result.returncode != 0:
        print(f"[warn] Not a git repo or git unavailable — proceeding anyway")
        return True
    if result.stdout.strip():
        if force:
            print("[warn] Uncommitted changes detected — proceeding anyway (--force)")
            return True
        print("[error] Uncommitted changes detected. Commit first or pass --force.")
        print(result.stdout)
        return False
    return True


def prompt_continue(message: str) -> bool:
    print(f"\n{'=' * 60}")
    print(message)
    print('=' * 60)
    answer = input("Continue? [y/N]: ").strip().lower()
    return answer in ("y", "yes")


def find_siteconfig(repo: Path) -> Path:
    """Solusite repos put siteConfig in one of two places."""
    candidates = [
        repo / "src" / "siteConfig.ts",
        repo / "src" / "config" / "siteConfig.ts",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError(
        f"No siteConfig.ts found at {candidates[0]} or {candidates[1]}"
    )


def iter_source_files(repo: Path):
    """Yield all .tsx and .ts files in src/, skipping node_modules and ui/ primitives."""
    src = repo / "src"
    if not src.exists():
        return
    skip_parts = {"node_modules", ".git", "ui", "dist", "build"}
    for path in src.rglob("*"):
        if path.is_file() and path.suffix in (".tsx", ".ts"):
            if any(part in skip_parts for part in path.parts):
                continue
            yield path


# ============================================================
# STAGE 1 — SCAN
# ============================================================

def scan(repo: Path) -> ScanResult:
    result = ScanResult()

    try:
        result.siteconfig_path = str(find_siteconfig(repo).relative_to(repo))
    except FileNotFoundError as e:
        print(f"[error] {e}")
        sys.exit(1)

    for path in iter_source_files(repo):
        rel = path.relative_to(repo)
        result.files_scanned += 1

        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        lines = content.split("\n")
        is_siteconfig = str(rel).endswith("siteConfig.ts")
        is_component = rel.parts[0] == "src" and rel.suffix == ".tsx"

        # Check siteConfig import presence for component files
        if is_component and not SITECONFIG_IMPORT.search(content):
            # Only flag if the component has visible text content (not pure layout)
            if JSX_HARDCODED_TEXT.search(content):
                result.components_missing_siteconfig.append(str(rel))

        for lineno, line in enumerate(lines, 1):
            # Skip comment-only lines
            stripped = line.strip()
            if stripped.startswith("//") or stripped.startswith("*") or stripped.startswith("/*"):
                continue

            # Phone numbers
            for pat in PHONE_PATTERNS:
                for m in pat.finditer(line):
                    result.findings.append(Finding(
                        file=str(rel), line=lineno, category="PHONE",
                        snippet=m.group(0),
                        severity="critical" if not is_siteconfig else "info",
                        note="" if is_siteconfig else "Phone number in component — should come from siteConfig"
                    ))

            # Email
            for m in EMAIL_PATTERN.finditer(line):
                # Skip obvious placeholders
                if m.group(0).lower() in ("example@example.com", "test@test.com"):
                    continue
                result.findings.append(Finding(
                    file=str(rel), line=lineno, category="EMAIL",
                    snippet=m.group(0),
                    severity="critical" if not is_siteconfig else "info",
                    note="" if is_siteconfig else "Email in component — should come from siteConfig"
                ))

            # Local image imports
            if LOCAL_IMAGE_IMPORT.search(line):
                result.findings.append(Finding(
                    file=str(rel), line=lineno, category="LOCAL_IMAGE",
                    snippet=stripped,
                    severity="critical",
                    note="Local asset import breaks across recycles — replace with Unsplash URL in siteConfig"
                ))

            # Hardcoded SA cities (only in components, not siteConfig)
            if not is_siteconfig:
                for m in CITY_PATTERN.finditer(line):
                    # Skip if it's inside a comment or obvious string literal in a CSS context
                    if 'className' in line or 'placeholder' in line.lower():
                        continue
                    result.findings.append(Finding(
                        file=str(rel), line=lineno, category="HARDCODED_CITY",
                        snippet=line.strip()[:120],
                        severity="warning",
                        note=f"City name '{m.group(0)}' in component — verify this isn't a hardcoded location string"
                    ))
                    break  # one hit per line is enough

        # File-level: check for hardcoded arrays (multi-line regex)
        if not is_siteconfig:
            for m in HARDCODED_ARRAY_PATTERN.finditer(content):
                var_name = m.group(1)
                # Find line number of the match
                lineno = content[:m.start()].count("\n") + 1
                result.findings.append(Finding(
                    file=str(rel), line=lineno, category="HARDCODED_ARRAY",
                    snippet=f"const {var_name} = [...]",
                    severity="critical",
                    note=f"Hardcoded array '{var_name}' in component — this is the MEG team bug. Replace with siteConfig.{var_name}.map()"
                ))

    return result


# ============================================================
# STAGE 3 — SKELETONIZE siteConfig
# ============================================================

# Map of siteConfig field patterns → placeholder values
# Ordered roughly by specificity — more specific keys matched first
SKELETON_RULES = [
    # business identity
    (r'(businessName:\s*)"[^"]*"',              r'\1"[BUSINESS_NAME]"'),
    (r'(shortName:\s*)"[^"]*"',                 r'\1"[SHORT_NAME]"'),
    (r'(tagline:\s*)"[^"]*"',                   r'\1"[TAGLINE]"'),
    (r'(longTagline:\s*)"[^"]*"',               r'\1"[LONG_TAGLINE]"'),
    (r'(description:\s*)"[^"]*"',               r'\1"[BUSINESS_DESCRIPTION]"'),

    # contact
    (r'(phone:\s*)"[^"]*"',                     r'\1"[PHONE_DISPLAY]"'),
    (r'(phoneTel:\s*)"[^"]*"',                  r'\1"[PHONE_TEL]"'),
    (r'(phoneInternational:\s*)"[^"]*"',        r'\1"[PHONE_INTL]"'),
    (r'(whatsapp:\s*)"[^"]*"',                  r'\1"[WHATSAPP_NUMBER]"'),
    (r'(whatsappMessage:\s*)"[^"]*"',           r'\1"[WHATSAPP_MESSAGE]"'),
    (r'(email:\s*)"[^"]*"',                     r'\1"[EMAIL]"'),
    (r'(cellPhone:\s*)"[^"]*"',                 r'\1"[CELL_PHONE]"'),

    # location
    (r'(address:\s*)"[^"]*"',                   r'\1"[ADDRESS]"'),
    (r'(suburb:\s*)"[^"]*"',                    r'\1"[SUBURB]"'),
    (r'(city:\s*)"[^"]*"',                      r'\1"[CITY]"'),
    (r'(area:\s*)"[^"]*"',                      r'\1"[AREA]"'),
    (r'(province:\s*)"[^"]*"',                  r'\1"[PROVINCE]"'),
    (r'(googleMapsUrl:\s*)"[^"]*"',             r'\1"[GOOGLE_MAPS_URL]"'),
    (r'(googleMapsEmbed:\s*)"[^"]*"',           r'\1"[GOOGLE_MAPS_EMBED]"'),

    # trust signals
    (r'(rating:\s*)"[^"]*"',                    r'\1"[RATING]"'),
    (r'(reviewCount:\s*)"[^"]*"',               r'\1"[REVIEW_COUNT]"'),
    (r'(accreditation:\s*)"[^"]*"',             r'\1"[ACCREDITATION]"'),
    (r'(accreditationFull:\s*)"[^"]*"',         r'\1"[ACCREDITATION_FULL]"'),
    (r'(experienceYears:\s*)"[^"]*"',           r'\1"[EXPERIENCE_YEARS]"'),
    (r'(ownerName:\s*)"[^"]*"',                 r'\1"[OWNER_NAME]"'),

    # social
    (r'(instagram:\s*)"[^"]*"',                 r'\1"[INSTAGRAM_HANDLE]"'),
    (r'(facebook:\s*)"[^"]*"',                  r'\1"[FACEBOOK_URL]"'),
    (r'(linkedin:\s*)"[^"]*"',                  r'\1"[LINKEDIN_URL]"'),

    # about copy
    (r'(aboutIntro:\s*)"[^"]*"',                r'\1"[ABOUT_INTRO]"'),
    (r'(roomsHeroTitle:\s*)"[^"]*"',            r'\1"[ROOMS_HERO_TITLE]"'),

    # dates
    (r'(established:\s*)\d{4}',                 r'\1[YEAR_ESTABLISHED]'),
]

# Flag these as needing manual review (complex structures)
MANUAL_REVIEW_KEYS = [
    "team", "services", "projects", "packages", "testimonials",
    "images", "rooms", "directions", "trustBar", "faqs", "suburbs",
    "emails",  # plural nested object
]


def skeletonize_siteconfig(siteconfig_path: Path) -> Dict[str, List[str]]:
    """
    Rewrite siteConfig.ts replacing scalar string values with placeholders.
    Returns a dict of {key: reason} for fields that need manual review.
    """
    content = siteconfig_path.read_text(encoding="utf-8")
    original = content

    # Apply scalar replacements
    for pattern, replacement in SKELETON_RULES:
        content = re.sub(pattern, replacement, content)

    # Find which complex keys are present and flag them
    needs_review = {}
    for key in MANUAL_REVIEW_KEYS:
        # Look for `keyname: [` or `keyname: {`
        if re.search(rf'\b{key}:\s*[\[\{{]', content):
            needs_review[key] = (
                f"Complex structure detected — replace contents with placeholder "
                f"entries manually. Keep the field and type but clear real data."
            )

    # Backup
    backup_dir = siteconfig_path.parent / ".strip_backup"
    backup_dir.mkdir(exist_ok=True)
    backup_path = backup_dir / siteconfig_path.name
    backup_path.write_text(original, encoding="utf-8")

    # Write skeletonized version
    siteconfig_path.write_text(content, encoding="utf-8")

    return needs_review


# ============================================================
# STAGE 4 — REPORTS
# ============================================================

def write_scan_report(repo: Path, result: ScanResult, archetype_name: str):
    report = []
    report.append(f"# Strip Scan Report — {archetype_name}\n")
    report.append(f"**Files scanned:** {result.files_scanned}")
    report.append(f"**Total findings:** {len(result.findings)}")
    report.append(f"**siteConfig path:** `{result.siteconfig_path}`\n")

    # Summary
    report.append("## Summary\n")
    report.append(f"- **Critical:** {len(result.critical())} (must fix before archetype is clean)")
    report.append(f"- **Warnings:** {len(result.warnings())} (verify these)")
    report.append(f"- **Info:** {len(result.info())} (siteConfig entries — expected)\n")

    if result.components_missing_siteconfig:
        report.append("## Components Missing siteConfig Import\n")
        report.append("These component files have visible text content but don't import siteConfig. "
                      "Likely hardcoded content that should be moved to siteConfig.\n")
        for c in result.components_missing_siteconfig:
            report.append(f"- `{c}`")
        report.append("")

    # Group findings by category
    by_category = {}
    for f in result.findings:
        by_category.setdefault(f.category, []).append(f)

    for category in ["HARDCODED_ARRAY", "LOCAL_IMAGE", "PHONE", "EMAIL", "HARDCODED_CITY"]:
        if category not in by_category:
            continue
        items = by_category[category]
        # Skip PHONE/EMAIL in siteConfig (info-level)
        visible = [i for i in items if i.severity != "info"] if category in ("PHONE", "EMAIL") else items
        if not visible:
            continue
        report.append(f"## {category.replace('_', ' ').title()} ({len(visible)})\n")
        for f in visible:
            report.append(f"**{f.file}:{f.line}** — `{f.snippet}`")
            if f.note:
                report.append(f"  - {f.note}")
            report.append("")

    out = repo / "SCAN_REPORT.md"
    out.write_text("\n".join(report), encoding="utf-8")
    return out


def write_manual_fixes_report(repo: Path, needs_review: Dict[str, str],
                              result: ScanResult, archetype_name: str):
    report = []
    report.append(f"# Manual Fixes Required — {archetype_name}\n")
    report.append("After running the strip script, these items need human attention "
                  "before the archetype is ready for remixing.\n")

    # siteConfig complex structures
    if needs_review:
        report.append("## siteConfig.ts — Complex Structures\n")
        report.append(
            "The script only replaces scalar strings. These nested arrays and objects "
            "still contain the original client's data. Replace each with a single "
            "placeholder entry so the structure is preserved but the data is generic.\n"
        )
        for key, reason in needs_review.items():
            report.append(f"### `{key}`")
            report.append(f"{reason}\n")
            report.append(f"Suggested placeholder pattern:\n")
            report.append(f"```ts")
            if key in ("team",):
                report.append(f"{key}: [")
                report.append(f'  {{ name: "[TEAM_MEMBER_1]", role: "[ROLE]", desc: "[BIO]" }},')
                report.append(f"]")
            elif key in ("services",):
                report.append(f"{key}: [")
                report.append(f'  {{ slug: "[SLUG]", name: "[SERVICE_NAME]", description: "[DESC]" }},')
                report.append(f"]")
            elif key in ("projects", "packages"):
                report.append(f"{key}: [")
                report.append(f'  {{ title: "[PROJECT_TITLE]", description: "[DESC]", image: "[UNSPLASH_URL]" }},')
                report.append(f"]")
            elif key == "testimonials":
                report.append(f"{key}: [")
                report.append(f'  {{ name: "[CLIENT_NAME]", quote: "[QUOTE]", role: "[ROLE]" }},')
                report.append(f"]")
            elif key == "images":
                report.append(f"{key}: {{")
                report.append(f'  hero: "[UNSPLASH_HERO_URL]",')
                report.append(f'  about: "[UNSPLASH_ABOUT_URL]",')
                report.append(f"}}")
            else:
                report.append(f"{key}: [/* replace with generic placeholder entries */]")
            report.append(f"```\n")

    # Hardcoded arrays in components (the MEG bug)
    crit = [f for f in result.findings if f.category == "HARDCODED_ARRAY"]
    if crit:
        report.append("## Component Hardcoded Arrays (CRITICAL)\n")
        report.append(
            "These components have hardcoded arrays that should be reading from "
            "siteConfig. This is the bug that caused MEG team names to appear on "
            "other clients' sites. Fix each one: delete the hardcoded array and "
            "replace with `siteConfig.{fieldname}.map(...)`.\n"
        )
        for f in crit:
            report.append(f"- `{f.file}:{f.line}` — {f.snippet}")
        report.append("")

    # Local image imports
    local_imgs = [f for f in result.findings if f.category == "LOCAL_IMAGE"]
    if local_imgs:
        report.append("## Local Image Imports (CRITICAL)\n")
        report.append(
            "These files import local image assets. Local images break on every "
            "recycle because the files belong to the original client. Replace with "
            "Unsplash URLs in siteConfig.images.\n"
        )
        for f in local_imgs:
            report.append(f"- `{f.file}:{f.line}` — `{f.snippet}`")
        report.append("")

    # Components missing siteConfig import
    if result.components_missing_siteconfig:
        report.append("## Components Not Reading from siteConfig\n")
        report.append(
            "These components display text but don't import siteConfig. Either "
            "they're purely structural (safe to ignore) or they have hardcoded "
            "content that needs migrating.\n"
        )
        for c in result.components_missing_siteconfig:
            report.append(f"- `{c}`")
        report.append("")

    # Verification checklist
    report.append("## Verification Checklist\n")
    report.append("Before marking this archetype as ready for remixing:\n")
    report.append("- [ ] All placeholders in siteConfig.ts are obvious (`[PLACEHOLDER]` format)")
    report.append("- [ ] All nested arrays (team/services/projects) have placeholder entries only")
    report.append("- [ ] No local image imports remain — all images via Unsplash URLs in siteConfig")
    report.append("- [ ] Every component text field traces back to siteConfig")
    report.append("- [ ] Optional fields have conditional rendering (`{siteConfig.x && ...}`)")
    report.append("- [ ] README.md added explaining what fields need filling per archetype")
    report.append("- [ ] Repo named `archetype-{industry}` (e.g. `archetype-professional-portfolio`)")
    report.append("- [ ] `npm run build` succeeds locally")
    report.append("- [ ] Lovable project linked to this repo and loading correctly")

    out = repo / "MANUAL_FIXES.md"
    out.write_text("\n".join(report), encoding="utf-8")
    return out


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("repo", help="Path to the repo to strip")
    parser.add_argument("--archetype-name", default="", help="Archetype name (e.g. professional-portfolio)")
    parser.add_argument("--force", action="store_true", help="Proceed with uncommitted changes")
    parser.add_argument("--auto", action="store_true", help="Skip confirmation prompts (for CI)")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.exists():
        print(f"[error] Repo not found: {repo}")
        sys.exit(1)

    archetype_name = args.archetype_name or repo.name

    print(f"\n{'=' * 60}")
    print(f"Solusite archetype strip — {archetype_name}")
    print(f"Target: {repo}")
    print('=' * 60)

    # Pre-flight
    if not check_git_clean(repo, force=args.force):
        sys.exit(1)

    # STAGE 1 — SCAN
    print("\n[Stage 1/3] Scanning...")
    result = scan(repo)
    print(f"  Files scanned: {result.files_scanned}")
    print(f"  Findings:      {len(result.findings)}  "
          f"(critical: {len(result.critical())}, "
          f"warnings: {len(result.warnings())}, "
          f"info: {len(result.info())})")

    # STAGE 2 — REVIEW (generate preview report, pause)
    preview = write_scan_report(repo, result, archetype_name)
    print(f"  Scan report: {preview.relative_to(repo)}")

    if not args.auto:
        if not prompt_continue(
            "Stage 2 complete. Review SCAN_REPORT.md above before proceeding.\n"
            "Stage 3 will MODIFY siteConfig.ts (backup saved to .strip_backup/)."
        ):
            print("Aborted. No changes made.")
            sys.exit(0)

    # STAGE 3 — SKELETONIZE
    print("\n[Stage 3/3] Skeletonizing siteConfig.ts...")
    siteconfig_path = find_siteconfig(repo)
    needs_review = skeletonize_siteconfig(siteconfig_path)
    print(f"  Backed up: .strip_backup/{siteconfig_path.name}")
    print(f"  Rewrote:   {siteconfig_path.relative_to(repo)}")
    print(f"  Complex structures flagged for manual review: {len(needs_review)}")

    # STAGE 4 — MANUAL FIXES REPORT
    fixes = write_manual_fixes_report(repo, needs_review, result, archetype_name)
    print(f"  Manual fixes required: {fixes.relative_to(repo)}")

    print(f"\n{'=' * 60}")
    print("DONE.")
    print('=' * 60)
    print(f"""
Next steps:
  1. Read MANUAL_FIXES.md and fix the items listed
  2. Review skeletonized siteConfig.ts  (original is in .strip_backup/)
  3. Replace local image imports with Unsplash URLs in siteConfig.images
  4. Fix any hardcoded component arrays (the MEG team-name bug)
  5. Add a README.md describing what fields need filling
  6. npm run build to verify
  7. Commit + push
""")


if __name__ == "__main__":
    main()
