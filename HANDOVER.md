# SOLUSITE MEDIA — MASTER HANDOVER DOCUMENT

> **Purpose:** Single source of truth for Solusite Media's business operations, technical setup, active clients, and decision history. Paste the raw URL of this document into any new Claude chat to bootstrap full context in one message.
>
> **Last updated:** 2026-04-08
> **Maintained by:** Ian Spies + Claude (collaborative edits)

---

## 1. BUSINESS OVERVIEW

**Owner:** Ian Spies
**Location:** Pretoria, South Africa
**Business:** Solusite Media — web development for SA local service businesses
**Day job:** Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server)
**Side projects:** Spies Construction, DFFRNT (athletic wear), Silverbrook Media (fiancée's social media business)
**Key collaborator:** Markus (lead handler)

### The model
1. Scrape SA business leads via multi-stage Python pipeline
2. Qualify by website gap (Facebook-only > broken > old > none)
3. Call qualified leads to confirm interest
4. Build demo site for confirmed leads using Lovable.dev
5. Pitch via WhatsApp/email with "I already built it for you" hook
6. Convert to client → offer monthly retainer

### Pricing
- **Build:** R5,000 once-off baseline (flexible/payment plans available — premium tiers up to R12,000 for high-value industries like weddings/hotels)
- **Retainer:** R700/month maintenance (R900/month for premium tier)
- **Blog add-on:** R500/month for 2 posts

### Tier-based pricing by industry (from research)
- **Events & Creative** (weddings, photographers, venues): R8,500–R12,000 build, R900/month retainer
- **Hotels & Hospitality:** R8,000–R12,000 build, R900/month
- **Beauty & Wellness:** R5,000–R7,500 build, R700/month
- **Food & Restaurants:** R5,000–R6,500 build, R700/month
- **Health & Fitness:** R5,000–R10,000 build, R500–R800/month
- **Professional Services:** R6,000–R12,000 build, R700–R900/month
- **Education & Training:** R3,500–R6,500 build, R500–R600/month
- **Trades** (plumber, electrician, handyman): R5,000 build, R700/month — hardest sell, lowest priority

---

## 2. TOOL STACK

| Category | Tool | Notes |
|---|---|---|
| Build | Lovable.dev | React + Supabase, credit-based, primary build tool |
| Backend | Supabase | DB, auth, storage, edge functions |
| Code editing | Claude Code (Terminal) | Local repo work, git operations |
| Repo hosting | GitHub (`Spies-ang`) | Keep PRIVATE — never expose API keys |
| Local dev | VS Code on MacBook | |
| Email | Resend.com | Transactional, 3,000 free emails/month |
| SEO | Prerender.io | Fixes Lovable's CSR indexing for Google |
| Blog | Inblog.ai | Connects to Lovable sites at /blog |
| Lead scraping | Google Places API | Project: "Business Scraper", $300 free trial |
| Scripting | Python 3.9.6 (Mac) | Scraper modules |
| Strategy/code | Claude (this chat) | Web interface, no direct git access |
| Auth (terminal) | gh CLI | Installed via Homebrew, persistent auth across all repos |

---

## 3. LEAD SCRAPER — STATUS: COMPLETE

**Repo:** `github.com/Spies-ang/lead-scraper` (PRIVATE — contains hardcoded API key)
**Local path:** `~/Documents/lead-scraper/`
**API key (exposed in private repo):** `AIzaSyCr65TnL51BTJeZ6b-jfh9ernZdYQnRuAM`
**Google Cloud trial:** $8.59 spent / $291 remaining, expires May 19 2026

### Pipeline
1. **Stage 1** — `scraper_stage1_broad_capture.py` — Google Places Text Search across 67 industries × 4 cities → `raw_leads.csv`
2. **Stage 1b** — `scraper_stage1b_enrich.py` — Place Details API to populate website/phone fields → `enriched_leads.csv`
3. **Stage 2** — `scraper_stage2_website_checker.py` — Visits each site, scores website quality → `qualified_leads.csv`
4. **Stage 3** — `scraper_stage3_sheets_export.py` — OAuth-based export to Google Sheets, one tab per industry
5. **Master:** `run_all_stages.py` runs all stages sequentially
6. **Helpers:** `fix_scores.py` (rescore NO_WEBSITE leads), `quick_export.py` (fast NO_WEBSITE + Facebook-only filter)

### Final results
- **13,549** raw leads enriched
- **11,120** qualified leads exported across 67 industry tabs
- **Sheet ID:** `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`
- **Sheet URL:** https://docs.google.com/spreadsheets/d/1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI

### Tier breakdown
- TIER 1 (score 9-10, hot): 932
- TIER 2 (score 6-8, warm): 4,701
- TIER 3 (score 1-5, cold): 5,487

### Gap distribution
- OLD_OR_BAD_WEBSITE: 5,648
- NO_WEBSITE: 4,357
- WEBSITE_UNREACHABLE: 395
- BROKEN_WEBSITE: 346
- FACEBOOK_ONLY: 185
- WEBSITE_TIMEOUT: 181
- REDIRECTS_TO_FACEBOOK: 6
- WEBSITE_ERROR: 2

### Known issues (deprioritized until first call batch validates)
1. **Stage 2 false positives** — Uses `requests` library (no JS execution), so modern React/Next.js/Vue sites get flagged as BROKEN/OLD because content renders client-side. Many "broken" leads have functional sites. Fix options: Playwright, modern-site detection override, or manual review.
2. **Stage 2 batch saving** — Currently saves all results at end. Should batch every 250 leads with `stage2_progress.txt` for resume support.
3. **Manual tier additions** — Ian is adding "Prospect" (light green #D9EAD3) and "Disqualified" (light grey #D9D9D9) status options to the Sheet manually via Data Validation + Conditional Formatting.

### Lead generation philosophy
**V1 lesson:** Established businesses with no website don't feel they need one. Hard sell.

**V2 priority order:**
- **TIER 1 HOT:** Facebook-only / broken / redirects to Facebook / new businesses (1-6 months, 5-20 reviews)
- **TIER 2 WARM:** Old sites / non-mobile / no SSL / placeholder / very slow
- **TIER 3 COLD:** Established businesses with NO website (50+ reviews) — uphill battle

**Priority industries (where web presence is functionally required):**
- CRITICAL: Wedding photographers, event venues, restaurants, fitness studios, yoga, catering, hotels, tour operators, spas, beauty/hair/nail, wedding planners, music schools, tutoring, driving schools
- HIGH: Personal trainers, physios, chiropractors, dentists, vets, pet grooming, interior designers, architects, real estate, accounting, legal
- MEDIUM: Barbers, auto repair, mechanics, cleaning, pest control, landscaping, pool, moving, security
- LOW: Plumbers, electricians, handymen, builders, painters, roofers — word-of-mouth dominant

---

## 4. ARCHETYPE TEMPLATES

The recycling strategy: build one site per industry archetype, strip into a `siteConfig.ts` template, then clone the repo for new clients in the same archetype by editing only the config file.

### Archetype 1 — Trades & Home Services
**Status:** 1.5 of 2 base sites templated
**Covers:** Plumber, electrician, handyman, carpenter, painter, roofer, HVAC, tiler, welder, locksmith, cleaning, pest control, landscaping, pool, moving, security, appliance repair
- **Roelf's Auto Electrical** — `github.com/Spies-ang/roelfsautoelectrical` — siteConfig templated, all 11 core files complete (work done in separate chat, may not be pushed)
- **Riakona Electrical Solutions** — `github.com/Spies-ang/riakonaelectrical` — ~80% complete, 5 files remaining (Services, Reviews, Contact, Index, SEOLandingPage)

### Archetype 2 — Beauty & Wellness
**Status:** Not started
**Covers:** Beauty/hair/nail salons, barber, spa, personal trainer, physio, chiro, yoga, fitness studio, dentist, vet
**Next action:** Spend ~10-15 Lovable credits on a fresh build

### Archetype 3 — Events & Creative ⭐ ACTIVE
**Status:** First base site complete (Ross Images Photography)
**Covers:** Wedding photographer, photography studio, event venue, wedding planner, catering
- **Ross Images Photography** — `github.com/Spies-ang/ross-images-studio` — ✅ Complete, template-ready siteConfig.ts
  - Live: https://rossimagesphotography.lovable.app/
  - Status: Awaiting visual QA + Stefanie Ross pitch call
- **87 Events** — Possibly exists as a separate repo, check before building anything new in this archetype

### Archetype 4 — Food & Hospitality
**Status:** Not started, but Thaba Meat Market repo may serve as base
**Covers:** Restaurant, hotel, B&B, tour operator, travel agency
- **Thaba Meat Market** — repo may exist on `Spies-ang`, needs assessment

### Archetype 5 — Professional Services
**Status:** Not started
**Covers:** Accounting, legal, insurance, real estate, architect, interior designer, marketing agency, web/graphic designer
**Next action:** ~10-15 Lovable credits for fresh build

### Archetype 6 — Education & Training
**Status:** Not started
**Covers:** Tutoring, driving school, music school, language school
**Next action:** ~10-15 Lovable credits for fresh build

### Other rejected client repos worth assessing for recycling
- GKN Plumbing
- Bazil Handyman
- Sagie's Plumbers

---

## 5. ACTIVE CLIENTS

### HandymanDirect.co.za (Vincent — paying client)
**Status:** Active development, Phase 2 approved
**Repo:** `github.com/Spies-ang/handymandirectv2`
**Stack:** React + Supabase + Lovable
**Team:** Vincent (owner), Trish, Jonty (their internal dev)
**Recent work:** Premium services reorder, experience-tier color coding (green/orange/blue), trade page architecture refactor (12 hardcoded → dynamic via `src/data/seoData.ts`), Trades dropdown nav, tier-specific booking flows, new trade page section order with scrollable blog feed window
**Pricing references:** Removed from trade pages

### Ross Images Photography (Stefanie Ross — pitch pending)
**Status:** Demo site built, awaiting pitch call
**Repo:** `github.com/Spies-ang/ross-images-studio` (currently public, make private after pitch)
**Live preview:** https://rossimagesphotography.lovable.app/
**Owner:** Stefanie Ross
**Location:** 338 Timothy Street, Waterkloof Glen, Pretoria
**Contact:** 082 820 5671 / info@rossimages.co.za
**Social:** Facebook RossImagesPhotography (3,755 followers), Instagram rossimagesphotography
**Old site:** rossimages.co.za (BROKEN — Cloudflare Error 1001 DNS resolution — strong pitch angle)
**Tier:** £££ premium
**Services:** Weddings, lifestyle, fine art newborn, maternity, family, cake smash, pets, motherhood
**Pitch angle:** "I noticed your website is showing a DNS error — I rebuilt it for you as a showcase"
**Target pricing:** R8,500–R10,000 build, R900/month retainer
**Pitch script:**
> "Hi Stefanie, I'm Ian from Solusite Media here in Pretoria. I noticed your website rossimages.co.za is showing a DNS error — Cloudflare can't reach the domain. I'm a local web developer and I took the initiative to rebuild the site as a showcase. Your work on Facebook and Instagram is beautiful and I thought it deserved a proper online home. Can I send you the link to have a look? No pressure at all."

---

## 6. CRITICAL TECHNICAL RULES

1. **RESTRICTIVE RLS BUG** — Lovable generates all Supabase RLS policies as RESTRICTIVE. After every Lovable prompt: Security tab → "Try to fix all (Free)" OR run SQL fix script.
2. **Always use `.maybeSingle()` not `.single()`** in Supabase queries (`.single()` throws on 0 rows, causing infinite spinners).
3. **Address fields:** Use `GooglePlacesAutocomplete` restricted to SA: `componentRestrictions: { country: "za" }`
4. **Repo privacy:** Never commit API keys to public repos. Keep all repos PRIVATE.
5. **SEO:** Prerender.io required on every Lovable site before SEO matters.
6. **Email confirmation:** Disable in Supabase Auth during testing (free tier limit: 4 emails/hour). Re-enable before go-live via Resend custom SMTP.
7. **Auth fallbacks:** Always add fallback `navigate()` after role fetches.
8. **`user_roles` table:** Needs explicit SELECT policy `user_id = auth.uid()` or role fetches fail silently.

---

## 7. WORKING PRINCIPLES & PREFERENCES

### Lovable credit strategy
- GitHub edits preferred over Lovable prompts for simple fixes (auto-deploys in ~60s, free)
- Consolidate all fixes into one Lovable prompt where possible
- Only use Lovable for new features or complex UI changes
- Security scan fixes in Lovable are always FREE — use them
- Only build demo sites for CONFIRMED interested leads (after call)
- When a Lovable prompt produces a bad result, always REVERT via Lovable's version history rather than rebuilding (free, avoids credit waste)

### Communication preferences (Ian)
- Direct and concise — no unnecessary preamble
- Productive feedback, not conversational filler
- Never fill in gaps or make assumptions — ask first
- Only change what was explicitly asked — no scope creep
- One consolidated answer beats three partial ones
- Read GitHub repo before answering code questions
- Flag when GitHub edit possible instead of Lovable prompt
- Factual only. If unsure, ask.

### Git auth setup
**Permanent fix installed:** Homebrew + `gh` CLI. Authenticated via `gh auth login` (HTTPS, web browser). All future `git push` operations work automatically across all repos. No more PAT pasting needed.

---

## 8. CLAUDE CHAT WORKFLOW

This project spans multiple Claude chats with different roles:

| Chat | Purpose | Has Claude Code? |
|---|---|---|
| **Lead scraper & client builds** (current) | Strategy, prompts, code review via raw URLs, research | No — web interface only |
| **Recycling rejected client websites** | Active templating work for Roelf/Riakona, future archetype strips | Partial — handover via prompts |
| **HandymanDirect** | Vincent's active client work | Yes — full git tools |

**Tool limitation in this chat:**
- `web_fetch` only accepts URLs explicitly pasted by Ian or returned from previous searches/fetches
- Cannot derive raw.githubusercontent.com URLs on its own
- For code review, Ian must paste the raw GitHub URL directly
- For code edits, Ian runs Claude Code in Terminal with the prompts I write

---

## 9. CURRENT PRIORITIES (rolling)

### Tomorrow morning
1. **Call Stefanie Ross** at 082 820 5671 with the broken-domain pitch
2. **Visual QA on Ross Images live preview** (5 page screenshots needed: Portfolio, Services, About, Investment, Contact)
3. **Make ross-images-studio repo PRIVATE** before sending the link to Stefanie

### This week
1. Start calling additional Wedding Photographer leads using Ross Images as the recycling template
2. Add Prospect/Disqualified statuses to Wedding Photographer tab in Google Sheet (then expand to other tabs as needed)
3. Use first call results to validate which tiers actually convert

### Short-term backlog
1. Assess existence of 87 Events repo for Events archetype base
2. Finish Riakona's remaining 5 files
3. Build Beauty & Wellness Lovable archetype (~10-15 credits)
4. Build Professional Services Lovable archetype (~10-15 credits)
5. Build Education & Training Lovable archetype (~10-15 credits)

### Medium-term
1. Fix Stage 2 scraper false positives (Playwright or modern-site detection)
2. Add Stage 2 incremental save/resume support
3. Build Silverbrook Media Stage 1c social media presence scraper (Ian's fiancée's business)
4. Consider Inblog.ai integration for blog add-on tier

---

## 10. SESSION LOG

### 2026-04-08 — Lead scraper completion + Ross Images build
- Completed Stage 2 scraper run (13,549 → 11,120 qualified)
- Fixed scoring logic for NO_WEBSITE leads (low review count = higher priority)
- Completed Stage 3 Google Sheets export (67 tabs)
- Researched SA web design pricing across 8 sources → produced industry pricing guide
- Selected Ross Images Photography as first wedding photographer client
- Built complete Lovable site with template-ready siteConfig.ts structure
- Reviewed and fixed siteConfig (testimonials genericized, packages.other pricing added, priceTier dead field removed)
- Installed Homebrew + gh CLI for permanent git auth
- Pushed cleanup commit `8e8d360` to ross-images-studio main
- Created this handover document

---

## APPENDIX — KEY FILE PATHS

**Local:**
- Scraper: `~/Documents/lead-scraper/`
- Ross Images: `~/Documents/ross-images-studio/`
- Pricing guide: previously generated, location TBD

**Remote:**
- Lead scraper repo: https://github.com/Spies-ang/lead-scraper (private)
- Ross Images repo: https://github.com/Spies-ang/ross-images-studio (currently public)
- HandymanDirect repo: https://github.com/Spies-ang/handymandirectv2
- Roelf's Auto: https://github.com/Spies-ang/roelfsautoelectrical
- Riakona Electrical: https://github.com/Spies-ang/riakonaelectrical
- Lead sheet: https://docs.google.com/spreadsheets/d/1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI

---

*End of handover document. Update incrementally as the project progresses. To bootstrap a new Claude chat: paste the raw GitHub URL of this file in the first message and Claude will read full context in one fetch.*
