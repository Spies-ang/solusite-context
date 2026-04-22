# SOLUSITE MEDIA — HANDOVER DOCUMENT
**Last updated:** Wednesday 22 April 2026 (evening)
**Bootstrap:** Paste this URL into any new Claude chat or Claude Code session:
`https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md`

> **NOTE:** This document is being replaced by a 4-file system (`RULES.md`, `STATE.md`, `DECISIONS.md`, `CONTEXT.md`) that are being built in the same session as this handover fix. Once those are live, this single HANDOVER.md is archived and new chats bootstrap from RULES.md + STATE.md only. This version exists to be the final corrected single-file handover for continuity.

---

## CURRENT STATE (22 April 2026, evening)

**Batch 1 (6 sites):** Driving schools (Revo, TJs, Rightway, Skill on Wheels, Dayyaans) + Lat Wai Farm Venue. All built. First-round WhatsApps sent from personal number. Second-round follow-ups sent from new business number (+27 66 269 8553) in a 13-message batch covering both Batch 1 non-responders and Batch 2.

**Batch 2 (7 sites):** MW Architects, Lisa Rorich Architects, Rono Architects, Ndibali Interior Designs, Blue Sky Interior Design, CodeFlash Photography Studio, Meintjes Catering. All built, deployed on Lovable, first-round WhatsApps sent from personal number. Second-round follow-ups included in the 13-message batch above.

**Solusite landing page:** Live at solusite-media.lovable.app. Domain solusitemedia.co.za purchased on GoDaddy, propagating. Hero headline / footer / business number / work examples fix prompt sent to Lovable.

**WhatsApp Business profile:** Active on new business number +27 66 269 8553. Dark diamond logo on #0A0A0A, off-white alt, 5 catalog items matching the landing page visual system.

**Practice page hardcoded-team bug:** RESOLVED on all 5 architect/interior sites (MW, Lisa Rorich, Rono, Ndibali, Blue Sky). Verified live. Fix still needs to be pushed upstream to `legacy-portfolio` archetype so future recycles inherit it.

**Current lead batch (22 April):** 15 pulled via `fetch_new_leads.py`. Ian selected 10 to build for. Verification pass identified several scraper false positives (KayShots, Royal Decor, Boulevard Storage, Bigfoot — all have working sites). Remaining leads need proper re-verification using the correct criteria — NOT geography-based.

---

## WHO

Ian Spies, Pretoria, South Africa. Runs **Solusite Media** (web dev + digital marketing) alongside a day job as Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server). Also runs Spies Construction and DFFRNT (athletic wear). Fiancée runs **Silverbrook Media** (social media management, shares pipeline infrastructure). Collaborator: **Markus** (lead handling). **Hired a junior salesman** to handle closing calls after Ian's warm WhatsApp intro — Ian builds and warms, salesman closes.

**Business number:** +27 66 269 8553 (new, as of 21 April 2026). Personal number retired from business use.

**Communication style:** Direct, concise, no preamble. Voice-to-text input. Only change what was asked. Never assume — ask. One consolidated answer beats three partial ones.

**Preferred name for Claude:** "Jarvis" — personal preference, not roleplay. Claude remains Claude with all standard capabilities.

---

## BUSINESS MODEL — TWO-STAGE SALES HANDOFF

1. **Scrape & qualify** — Multi-stage Python scraper finds leads with website gaps
2. **Build** — Recycle the matching archetype template, customize siteConfig.ts for the lead, push to GitHub, Lovable auto-deploys
3. **Ian sends warm intro WhatsApp** — Personal hook + gap framing + live demo URL + placeholder disclaimer + callback window. Stays in Ian's name to preserve the trust anchor.
4. **Ian sends salesman briefing card** — Structured summary so the salesman can dial cold-but-prepared
5. **Salesman calls** — Suggested opening: *"Hi, this is [name] from Solusite Media — Ian asked me to follow up on the website he sent you yesterday."*
6. **Salesman closes the meeting**, not the deal — goal is a 30-45 min meeting where the client hands over real photos and details
7. **Convert** to paying client + monthly retainer

### Pricing

**All archetypes anchor at R5,000 once-off.** Frame: *"Our builds usually go for R8,500 — you're getting the introductory rate of R5,000."*

**Fallback payment plan** (offer only if price is the blocker): R2,500 upfront + R2,500 on completion within 1 week.

Blog add-on: R500/month for 2 SEO posts per site.

| Archetype | Build | Retainer |
|---|---|---|
| Events & Creative | R5,000 | R900 |
| Hospitality (B&B, hotel) | R5,000 | R900 |
| Professional Services | R5,000 | R900 |
| Beauty & Wellness | R5,000 | R700 |
| Food & Restaurants | R5,000 | R700 |
| Health & Fitness | R5,000 | R500–R800 |
| Education & Training | R5,000 | R500–R600 |
| Trades | R5,000 | R700 |

---

## LEAD GENERATION — CORRECT QUALIFYING CRITERIA

**The V2 criteria are non-negotiable and have been the foundation of the project since March 2026.** Every chat re-briefing them is a sign of drift.

### Criteria (ALL must be true)
1. Website gap is Tier 1 or Tier 2
2. Rating ≥ 4.0
3. Reviews between 5 and 30 (sweet spot — not new-new, not established)
4. Phone present
5. Industry is in the prioritized list (not deprioritized)
6. Web-search verification passed:
   - No working website found under an alternative URL (false positive check)
   - Not a franchise/subsidiary of a corporate brand
   - Not a direct competitor (agency, web dev, graphic designer, photographer using web presence)
   - Real standalone business with a findable owner

### What is NOT a criterion
- **Geography.** Leads come from all four SA cities (Cape Town, Joburg, Durban, Pretoria). Being in or out of Pretoria has no bearing on qualification.
- **The "don't mention Pretoria" rule applies only to client-facing copy**, not lead filtering.

### Tier system (by website gap)
- **TIER 1 HOT:** FACEBOOK_ONLY, BROKEN_WEBSITE, WEBSITE_UNREACHABLE, REDIRECTS_TO_FACEBOOK
- **TIER 2 WARM:** OLD_OR_BAD_WEBSITE, non-mobile-responsive, no SSL, placeholders
- **TIER 3 COLD:** Established no-website (50+ reviews) — V1 confirmed hardest sell, deprioritized

### Industry budget filter

Website-gap tier alone is not enough. Industry determines budget capacity.

**DEPRIORITIZE (high need, lower budget, close rate unproven):**
Wellness studios, personal trainers, physiotherapists, yoga studios, small independent spas.

**PRIORITIZE (clear revenue per customer, defensible ROI pitch):**
- Hospitality with commission pain: hotels, B&Bs, guesthouses, lodges — Booking.com/Airbnb math pitch
- Professional services with project fees: architects, lawyers, accountants, consulting firms, agencies
- Education with course fees: driving schools, music schools, tutoring businesses, training providers
- Event-driven with per-booking revenue: wedding photographers, event venues, catering, tour operators
- Restaurants (established, not street-food tier)

### Facebook activity check (pre-build hard gate)
Before building any demo site: check the lead's Facebook. If last post > 60 days ago or announcing closure, skip. This rule originated from Prana Love (closing studio) and Dayyaans (defunct) — both burned build time that was preventable.

---

## LEAD GENERATION PIPELINE — V2 MULTI-STAGE SCRAPER

### Architecture
- **Stage 1:** `scraper_stage1_broad_capture.py` — Google Places API → `raw_leads.csv`
- **Stage 1b:** `scraper_stage1b_enrich.py` — Place Details per lead for website + phone → `enriched_leads.csv`
- **Stage 2:** `scraper_stage2_website_checker.py` — visits each website → `qualified_leads.csv`
- **Stage 2 v2:** `scraper_stage2_website_checker_v2.py` — Playwright-based, fixes false positives. **NOT YET RUN.** Located at `~/Documents/lead-scraper/`. Run overnight, ~6-8 hours.
- **Stage 3:** `scraper_stage3_sheets_export.py` — exports to Google Sheets
- **Master:** `run_all_stages.py` runs all stages
- **Repo:** `github.com/Spies-ang/lead-scraper` (private)
- **Output:** 11,120+ qualified leads across 67 industry tabs in Google Sheets `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`
- **Direct Sheet Reader:** `fetch_new_leads.py` at `~/Documents/lead-scraper/` — reads the Sheet directly, respects Status column, loops all tabs, applies criteria filter, returns top scored leads.

### Known issues

**Stage 2 scoring fix NOT YET APPLIED to main script.** The corrected no-website scoring logic (fewer reviews = higher priority score) lives in `quick_export.py` and `fix_scores.py` but `scraper_stage2_website_checker.py` still has the old inverted logic. Apply before the next full scraper run. Open since end of March 2026.

**Stage 2 v1 false-positive rate ~27%** on modern JS-rendered sites (requests library can't execute JS). Stage 2 v2 Playwright rewrite exists but hasn't been run. Until it is, every batch requires manual web-search verification per lead.

**Stage 2 saves only at completion.** No batch save / resume. A crash at hour 5 of a 7-hour run loses everything.

---

## ARCHETYPE TEMPLATES — CURRENT STATE

| # | Archetype | Template Repo | Live URL | Hardened? |
|---|---|---|---|---|
| 1 | Education & Training | `Spies-ang/pass-prep-pro` | studentechdrivertraining.lovable.app | ✅ Hardened — commit `077d8a8` |
| 2 | Food, Hospitality & Events | `Spies-ang/garden-gateways` | gardenpointguesthouse.lovable.app | ⚠️ Partial — Location.tsx needs per-repo fix |
| 3 | Professional Services / Portfolio | `Spies-ang/legacy-portfolio` | megarchitects.lovable.app | ⚠️ Practice-page hardcoded-team fix applied to child sites but NOT yet upstreamed |
| 4 | Photography Studio | `Spies-ang/ross-images-studio` | — | ❌ Not hardened |
| 5 | Beauty & Wellness | `Spies-ang/prana-template-suite` | pranaloveyoga.lovable.app | — |
| 6 | Trades & Home Services | `roelfsautoelectrical` + `riakonaelectrical` | — | Roelf done, Riakona 80% |
| — | Beauty & Wellness (v1) | `Spies-ang/beauty-bloom-template-54d0c7e3` | — | La Belle — hero broke, needs Lovable revert |

### Clean-archetype repo strategy (decided 15 April 2026)

Stop remixing client repos. Build dedicated `archetype-*` repos with placeholder values. Strip once, never strip again.

**Priority order for archetype creation:**
1. `archetype-professional-portfolio` (from legacy-portfolio after upstream fix)
2. `archetype-catering` (from Meintjes after B&B→catering structural fix)
3. `archetype-photography-studio` (from ross-images-studio)
4. `archetype-event-venue` (from garden-gateways / Lat Wai)
5. `archetype-driving-school` (from pass-prep-pro — already hardened, just needs rename + placeholder siteConfig)
6-8. New builds: `archetype-interior-design`, `archetype-accounting`, `archetype-restaurant`

`strip_archetype.py` written, saved to Downloads, **needs to be moved to `~/Documents/solusite-context/scripts/`** and run on first archetype.

---

## CLIENT RESPONSES — STATE AS OF 22 APRIL 2026 EVENING

| Lead | Status | Notes / Next Action |
|---|---|---|
| Lat Wai (Wendy) | INTERESTED ✅ | Pricing sent (R5k total: R2,500 deposit + R2,500 on completion, R700/month retainer). Replied "will consider." Follow-up needed. |
| Lisa Rorich Architects | INTERESTED ✅ | Fee structure sent via personal phone after she asked. Business-number follow-up also sent. Awaiting reply. |
| MEG Architects (Tienie) | Pending callback | Afrikaans follow-up sent from business number. Interested on call. |
| Studentech (Vernon) | Pending callback | Interested on calls, no WhatsApp replies. Business-number follow-up sent — move to voice, not text. |
| Dayyaans Driving | DECLINED (closed) — but WARM REFERRER | Loves the site, asked for neutral business card to send referrals. **Business card overdue.** |
| Garden Point Guest House | DECLINED | Earlier batch. |
| Prana Love Yoga | DECLINED (closing studio) | — |
| Stefanie Ross Photography | DECLINED (fully booked) | — |
| TJs Driving Academy | No response | Business-number follow-up sent. |
| Rightway Driving Academy | No response | Business-number follow-up sent. Disappearing-messages mode on. |
| Skill on Wheels Academy | No response | Business-number follow-up sent. |
| Revo Driving School | No response | Follow-up needed. |
| MW Architects | First WhatsApp sent, no response | Business-number follow-up not yet sent — to be included in next batch. |
| Rono Architects | First WhatsApp sent, no response | Same. |
| Ndibali Interior Designs | First + business-number WhatsApps sent | Awaiting reply. |
| Blue Sky Interior Design | First + business-number WhatsApps sent | Awaiting reply. |
| CodeFlash Photography | First + business-number WhatsApps sent | Awaiting reply. |
| Meintjes Catering | First + business-number WhatsApps sent | Awaiting reply. |
| The Villa 442 (Hannah) | Business-number WhatsApp sent to owner's actual number | Awaiting reply. If silent by end of week, either follow up again or archive site for recycling. |
| +27 81 402 7483 | Most engaged | Monthly-price objection still to handle. |

---

## KEY LEARNINGS

- **Lovable auto-fix overwrites siteConfig team arrays.** After Lovable "Try to fix" runs, check team/services/projects arrays.
- **Verify every domain before building.** Nexia SAB&T was a false positive (national firm with working main site, scraper caught a broken branch URL). Spot-check required.
- **Scraper exclude list doesn't scale.** Filter by Status field in the Sheet, not hardcoded names.
- **Practice page component was hardcoded, not dynamic.** Fixing siteConfig.team alone was insufficient on legacy-portfolio child sites. Fix applied; still needs upstreaming.
- **Facebook activity check catches dead businesses.** Would have caught Prana Love and Dayyaans before build time was spent.
- **Established no-website businesses don't convert.** New or broken-website businesses convert better.
- **Demo-first selling works.** Second paying client was found because the site was already built and shown.
- **Lovable version history is always the first option.** Bad Lovable result → revert, not rebuild.
- **Batch/consolidate before acting.** All issues listed → one clean prompt → paste once.
- **GitHub edits over Lovable prompts for small fixes.** Auto-deploys in ~60s, no credit cost.

---

## DESIGN SYSTEM — BRAND RESEARCH FIRST

**Rule:** research client's actual brand colors (Facebook cover, Instagram grid, logo, existing site) BEFORE defaulting to an archetype palette. If nothing is found, build a character-driven palette from a specific personality observation. Archetype defaults are last resort only. Never use the same default palette twice in a row.

**Palettes in use:**
- Prana Love: "Coastal Dawn" — apricot #E89B6C + ocean navy #1A2942
- Garden Point: "Gold Reef" — burnished gold #B8860B + wine burgundy #6B2424
- MEG Architects: "Architectural Ink" — monochrome + oxide red #B85A3E
- Studentech: "K53 Yellow" — bold yellow #FFD60A + black
- Villa 442: "Private Retreat" — warm slate navy + terracotta + linen cream
- Solusite brand: #3B82F6 blue on #0A0A0A black (Fraunces + Instrument Serif italic + JetBrains Mono)

---

## TOOLS & RESOURCES

- **Build:** Lovable.dev (React + Supabase), GitHub `Spies-ang` (repos PRIVATE)
- **Local dev:** Claude Code (Terminal), MacBook
- **Data / scraping:** Python (Google Places API key `AIzaSyCr65TnL51BTJeZ6b-jfh9ernZdYQnRuAM`), Google Sheets ID `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`, OAuth via `client_secret.json`
- **Design / docs:** Canva MCP (Solusite logo: asset ID `MAE4eMe-2NE`), ReportLab
- **Day job stack:** Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server
- **Google Cloud trial:** $8.59 spent, $291 remaining, expires 2026-05-19

---

## CRITICAL TECHNICAL RULES

1. **Lovable RLS bug:** All Supabase RLS policies generate as RESTRICTIVE. After every prompt → Security → "Try to fix all (Free)"
2. **Always `.maybeSingle()` not `.single()`** — `.single()` throws on zero rows
3. **Address fields:** `GooglePlacesAutocomplete` restricted to `{ country: "za" }`
4. **NEVER commit API keys to public repos** — keep business repos PRIVATE. The `solusite-context` repo is an exception (public by design, contains no secrets).
5. **Prerender.io required** on every Lovable site before SEO matters
6. **Disable email confirmation** in Supabase during testing (4 emails/hour limit)
7. **Always add fallback `navigate()`** after role fetches
8. **GitHub edits preferred** over Lovable prompts for simple fixes
9. **When Lovable prompt breaks something** → revert via version history, don't rebuild
10. **Long multi-change Lovable prompts break** — be surgical, single-section changes only
11. **Color swap prompts** must say "do not touch siteConfig.ts, do not regenerate sections"
12. **Browser chats can read `solusite-context` (public)**; all other repos require Claude Code (authenticated) or temporary public toggling, or paste-in-chat
13. **Exposed token to rotate:** `https://github.com/settings/tokens` — old `ghp_skzIqq0...` still listed as open item
14. **Geography is not a lead filter.** Leads come from all 4 cities. The "no Pretoria in copy" rule is about client-facing text only.
15. **Verify every lead with web_search before building.** ~27% scraper false-positive rate means metadata qualification alone is insufficient.
16. **Facebook activity check** is a pre-build hard gate. Skip leads with no recent activity or closure posts.

---

## MULTI-CHAT WORKFLOW

| Surface | Role | bash/git | Reads private repos |
|---|---|---|---|
| Claude.ai browser — strategy chat | Strategy, research, prompts | No | No |
| Claude.ai browser — recycling chat | Template recycling, lead selection | No | No |
| Claude.ai browser — HandymanDirect chat | Vincent's client work | No | No |
| Claude Code (Terminal) | All build/edit/deploy/git execution | Yes | Yes (authenticated) |
| Lovable chat panel | Per-project UI changes | Yes (Lovable-specific) | Yes (authenticated) |

Browser chats write prompts. Claude Code executes them.

---

## PENDING / ON THE HORIZON

**Immediate — sales:**
- Business card for Dayyaan (warm referrer)
- Schedule Wendy (Lat Wai) follow-up
- Second-round WhatsApps for MW, Rono, Revo (not yet sent on business number)
- Wait on responses from Batch 2 business-number follow-ups; triage by end of week

**Immediate — pipeline:**
- Re-verify current 15-lead batch using correct criteria (NOT geography-based)
- Research and build remaining validated leads
- Pull next batch after current batch processed

**Build fixes:**
- Push Practice-page component fix upstream to `legacy-portfolio` archetype so future recycles inherit it
- Meintjes Catering structural fix (B&B → catering language in Home.tsx and Book.tsx)
- Solusite landing page Lovable fix (hero headline visibility, footer overlap, business number, swap Ndibali → Blue Sky in work examples) — prompt already sent, verify on deploy

**Template hardening:**
- Harden `legacy-portfolio` (missing fields + upstream fix)
- Harden `ross-images-studio` (missing fields)

**Infrastructure:**
- Move `strip_archetype.py` from `~/Downloads/` to `~/Documents/solusite-context/scripts/`
- Run it on `legacy-portfolio` to produce first clean archetype repo
- Apply Stage 2 scoring fix to main `scraper_stage2_website_checker.py`
- Run Stage 2 v2 Playwright overnight
- Add Stage 2 batch-save / resume
- Revert La Belle hero via Lovable version history
- Finish Riakona Electrical templating (5 files remaining)
- Rotate exposed GitHub token

**Automation stack (Airtable + n8n + Claude Code + Vercel + GitHub):**
- Create Airtable Solusite Pipeline base (schema in AUTOMATION_SETUP.md)
- Install n8n locally: `npm install -g n8n && n8n start`
- Install n8n-MCP: clone `github.com/czlonkowski/n8n-mcp`, add to `~/.claude/mcp_settings.json`
- Build first workflow (manual trigger → Airtable → Claude subagent → site generation → Airtable update)

**Medium-term:**
- Stage 1c social media scraper for Silverbrook Media
- Switch scraper exclude logic from hardcoded name list → Status field filter

**Longer-term:**
- Hire 2nd salesman if conversion rate validates
- Build archetypes for: Restaurant, Trades refresh, Health & Fitness
- Productize the offering

---

## SILVERBROOK MEDIA (FIANCÉE'S BUSINESS)

Social media management. Higher-budget targets: hotels, event venues, tour operators, travel agencies, spas, restaurants, wedding photographers, real estate agents, interior designers, architects. Stage 1c scraper deferred until Solusite pitch validates through real calls.

---

## HANDYMANDIRECT (CLIENT: VINCENT)

Active React/Supabase rebuild on Lovable.dev. Repo: `Spies-ang/handymandirectv2`. Phase 2 largely complete. Owned by separate chat.

---

*End of corrected HANDOVER.md. This file is the last single-source handover; future state lives in RULES.md + STATE.md + DECISIONS.md + CONTEXT.md.*
