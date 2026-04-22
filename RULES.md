# SOLUSITE — RULES

**Status:** Non-negotiable. Every chat reads this first. Append-only — never edit or delete existing rules.
**Last updated:** 22 April 2026

---

## SECTION 1 — DOCUMENTATION PROTOCOL (READ FIRST)

This repo is the single source of truth for the Solusite project. It contains four documents and a scripts folder. Every chat that works on Solusite MUST understand this structure and follow the write rules below WITHOUT being asked.

### The four documents

**`RULES.md` (this file)** — non-negotiable rules. Append-only. Only Ian adds to it.
**`STATE.md`** — current reality only. No history. Overwritten every time reality changes.
**`DECISIONS.md`** — append-only chronological log of strategic decisions and logic changes.
**`CONTEXT.md`** — long-form onboarding. Why the project works the way it does. Read once per new chat if reasoning about strategy.

Plus `scripts/` — all project automation lives here, documented in `scripts/README.md`.

### Bootstrap rule — how a new chat starts work on Solusite

At the start of every new chat where Ian asks for Solusite work, the chat MUST:

1. Fetch `RULES.md` and `STATE.md` from `https://raw.githubusercontent.com/Spies-ang/solusite-context/main/`
2. Confirm back to Ian in one short message: (a) the top 3 rules relevant to the requested task, (b) what STATE says about the current work area, (c) any ambiguity or apparent staleness
3. Wait for Ian to confirm or correct before starting work

If the chat skips this step or starts work without confirming, that chat is in violation of this protocol and Ian should stop and restart.

### End-of-session update protocol

At the end of any session that changed reality, the chat MUST produce an update block in this exact format, without being asked:

```
=== SOLUSITE-CONTEXT UPDATE ===

STATE.md changes:
- [section name]: [specific change, e.g. "Lisa Rorich row: pricing sent → awaiting reply"]
- [section name]: [specific change]

DECISIONS.md append (only if a strategic decision was made or logic changed):
- YYYY-MM-DD — [one-line decision] [chat title or ID]

scripts/ changes (only if code was added or modified):
- [filename]: [what changed]

=== END UPDATE ===
```

If nothing changed in a section, omit that section entirely. Do not pad. Do not explain unless Ian asks.

Ian pastes this block into Claude Code. Claude Code applies the changes to the repo files and pushes. That is the only write path into `solusite-context`.

### What belongs in which file

- **New non-negotiable rule** → propose for RULES.md at end of session. Ian decides whether to add it. Never auto-write.
- **Strategic decision or logic pivot** → DECISIONS.md
- **Status change to any work in flight** → STATE.md
- **Script written or modified** → `scripts/` directly, plus note in update block
- **Learning that shaped approach** → DECISIONS.md (with "learning" label) AND consider proposing a rule to Ian
- **Per-lead operational work** (WhatsApp sent, build pushed, reply received) → STATE.md only

### What does NOT belong in these files

- Per-session chat transcripts
- Draft copy that wasn't sent
- Speculation about future leads
- Explanations that duplicate CONTEXT.md
- Code snippets (those live in `scripts/`)

---

## SECTION 2 — LEAD QUALIFICATION RULES

2.1. **Geography is NEVER a lead filter.** Leads come from all 4 SA cities (Cape Town, Johannesburg, Durban, Pretoria). Rejecting a lead for being in or out of Pretoria is a rule violation.

2.2. **The "no Pretoria in copy" rule applies ONLY to client-facing text** (WhatsApp messages, salesman scripts, demo site copy). It has nothing to do with where the lead is based.

2.3. **V2 qualifying criteria — ALL must be true:**
  - Website gap is Tier 1 (FACEBOOK_ONLY, BROKEN_WEBSITE, WEBSITE_UNREACHABLE, REDIRECTS_TO_FACEBOOK) or Tier 2 (OLD_OR_BAD_WEBSITE, non-mobile, no SSL, placeholder)
  - Rating ≥ 4.0
  - Reviews between 5 and 30
  - Phone present
  - Industry is in the prioritized list (not deprioritized)
  - Web-search verified: no alternative working site found, not a franchise/subsidiary, not a competitor, real standalone business

2.4. **Prioritized industries:** hospitality with commission pain (hotels, B&Bs, guesthouses, lodges); professional services with project fees (architects, lawyers, accountants, consulting, agencies); education with course fees (driving schools, music schools, tutoring, training providers); event-driven (wedding photographers, event venues, catering, tour operators); established restaurants.

2.5. **Deprioritized industries:** wellness studios, personal trainers, physiotherapists, yoga studios, small independent spas. High need, low budget, unproven conversion.

2.6. **Facebook activity check is a pre-build hard gate.** If the lead's last Facebook post is > 60 days old, or there's a closure announcement, skip. Do not build.

2.7. **Web-search verification is mandatory before building.** Scraper false-positive rate is ~27%. Industry-category qualification from scraper metadata alone is insufficient.

2.8. **Established no-website businesses (50+ reviews, no gap) do not convert.** Thriving businesses without websites don't feel the need. This is validated from V1 and is settled logic — do not re-propose targeting them.

---

## SECTION 3 — CLIENT COMMUNICATIONS

3.1. **Ian sends the warm WhatsApp.** Salesman handles closing calls only. No cold outbound from salesman.

3.2. **Never mention Pretoria or geography in client-facing copy.** Solusite is a capability, not a locality.

3.3. **Suggested salesman opening** (template, not script): *"Hi, this is [name] from Solusite Media — Ian asked me to follow up on the website he sent you yesterday."*

3.4. **No em dashes in client-facing documents.** Ian's preference.

3.5. **Business number is +27 66 269 8553.** Personal number retired from business use as of 21 April 2026.

3.6. **Pricing anchor: R5,000** framed as *"Our builds usually go for R8,500 — you're getting the introductory rate of R5,000."* Fallback payment plan (only if price is the blocker): R2,500 upfront + R2,500 on completion within 1 week. Never lead with price.

---

## SECTION 4 — TECHNICAL RULES

4.1. **Repos stay PRIVATE** except `solusite-context` which is PUBLIC by design (contains no secrets).

4.2. **Never commit API keys to any repo**, even private ones.

4.3. **Lovable RLS bug:** All Supabase RLS policies generate as RESTRICTIVE. After every Lovable prompt → Security → "Try to fix all (Free)".

4.4. **Always `.maybeSingle()` not `.single()`** — `.single()` throws on zero rows.

4.5. **Address fields:** `GooglePlacesAutocomplete` restricted to `{ country: "za" }`.

4.6. **Prerender.io required** on every Lovable site before SEO matters.

4.7. **GitHub edits preferred over Lovable prompts** for simple fixes. Auto-deploys in ~60s, no credit cost.

4.8. **Lovable version history is the first response to a bad Lovable prompt.** Revert, don't rebuild.

4.9. **Lovable prompts must be surgical.** Long multi-change prompts break. Color swap prompts must explicitly say *"do not touch siteConfig.ts, do not regenerate sections."*

4.10. **Claude Code handles all git operations.** Browser chats write prompts; Claude Code executes.

---

## SECTION 5 — WORKING STYLE

5.1. Direct, concise, no preamble. Voice-to-text input is expected.

5.2. Only change what was asked. Never fill gaps. Ask first.

5.3. One consolidated answer beats three partial ones. Batch and consolidate before acting.

5.4. Claude is addressed as "Jarvis" — personal preference, not roleplay. Claude remains Claude.

5.5. Pretoria location context in user memory is about where Ian lives, not where leads must come from.

---

## SECTION 6 — DO-NOT-RE-DEBATE LIST

These were decided and are closed. A chat proposing to re-open them is drifting.

- **V1 vs V2 scraper philosophy.** V2 won. Established no-website businesses don't convert.
- **Six archetypes, not 67 templates.** Trades, Beauty & Wellness, Events & Creative, Hospitality, Professional Services, Education & Training.
- **Demo-first pitch.** Build before calling. Non-negotiable.
- **Salesman closes, Ian warms.** Ian's WhatsApp is the trust anchor.
- **Pricing anchor is R5,000 framed as R8,500 introductory.** Fallback is R2,500 + R2,500. Retainer is per-archetype.
- **Clean-archetype repos over remixing client repos.** Decided 15 April 2026.
- **The business number for all outbound is +27 66 269 8553.**

---

*If you are a Claude instance reading this file for the first time: do not proceed to any Solusite task until you have (a) also read STATE.md, and (b) produced the bootstrap confirmation defined in Section 1. Skipping the bootstrap is a rule violation and will introduce drift.*
