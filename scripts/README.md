# Solusite Scripts

**Location:** `~/Documents/solusite-context/scripts/`
**Purpose:** All project automation lives here. Consolidated from previously scattered locations (`~/Documents/lead-scraper/`, `~/Downloads/`, various repos) into one place that tracks alongside the source-of-truth docs.

**Write rule:** Any chat that writes or modifies a script must note it in the end-of-session update block per RULES.md §1.

---

## CATALOG

### Scraper pipeline

Located at `~/Documents/lead-scraper/` (separate repo: `github.com/Spies-ang/lead-scraper`, PRIVATE).

Not duplicated here — the lead-scraper repo is the authoritative location for scraper code. Listed for reference:

- `scraper_stage1_broad_capture.py` — Google Places API → `raw_leads.csv`
- `scraper_stage1b_enrich.py` — Place Details per lead for website + phone → `enriched_leads.csv`
- `scraper_stage2_website_checker.py` — visits each website → `qualified_leads.csv`. **Known issue: scoring fix still pending on this file.**
- `scraper_stage2_website_checker_v2.py` — Playwright-based rewrite. **Saved, not yet run.** Fixes ~27% false-positive rate.
- `scraper_stage3_sheets_export.py` — exports to Google Sheets
- `run_all_stages.py` — master script
- `quick_export.py` — ad-hoc exports with corrected scoring logic
- `fix_scores.py` — scoring recalculation utility
- `fetch_new_leads.py` — reads Google Sheet directly, applies RULES.md §2 criteria, returns top scored leads

### Archetype management

- `strip_archetype.py` — **pending move from `~/Downloads/`.** Stdlib-only Python 3.8+. Sequential scan → report → pause → skeletonize. Outputs SCAN_REPORT.md and MANUAL_FIXES.md. Refuses to run with uncommitted git changes unless `--force`. Tested locally, not yet run on a real repo.

### Automation (planned, not yet built)

- n8n workflows for the Airtable → Claude subagent → site generation → Airtable update flow. See CONTEXT.md "Automation end-state" section.

---

## HOW TO ADD A SCRIPT

1. Place file in this folder with a descriptive name
2. Add an entry to this README under the appropriate section
3. Include in your end-of-session update block:
   ```
   scripts/ changes:
   - scripts/[filename]: [what it does, one line]
   ```
4. Claude Code applies the update and pushes

---

## HOW TO USE A SCRIPT FROM A NEW CHAT

If Claude Code is running and needs a script that already exists in this folder:

```bash
cd ~/Documents/solusite-context && git pull
cd scripts/
# script is available
```

If the script is in the separate `lead-scraper` repo:
```bash
cd ~/Documents/lead-scraper && git pull
# script is available
```
