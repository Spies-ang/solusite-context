# SOLUSITE MEDIA — MASTER HANDOVER DOCUMENT

> **Purpose:** Single source of truth for Solusite Media. Paste the raw URL of this document into any new Claude chat to bootstrap full context in one message.
>
> **Bootstrap instruction for new chats:** *"Read this and continue the Solusite Media project: https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md"*
>
> **Last updated:** 2026-04-09
> **Maintained by:** Ian Spies + Claude (Jarvis)

---

## 0. CRITICAL CONTEXT FOR ANY NEW CHAT

**Who:** Ian Spies. Solo operator running Solusite Media (web dev for SA local service businesses) alongside a day job as Data Engineer at Belgotex.

**Where:** Pretoria, South Africa.

**What's working:** Lead scraper (11,120 qualified leads in Google Sheets), one paying client (HandymanDirect, active development).

**What's NOT working:** Conversion. First two cold calls (Stefanie Ross / Ross Images Photography on 2026-04-09) ended in "no, I'm fully booked, don't need a website". Sales pipeline unproven.

**Where Ian wants to go:** A semi-autonomous lead-to-close pipeline using Claude Code + n8n + Airtable + Twilio + Vercel. Hybrid stack validated against 2026 market practice (n8n-MCP, n8n+Claude Code production case studies). See Section 7.

**What Ian is NOT doing:** Paying for new tools beyond what he already has (Claude Pro, Lovable on existing credits, free GitHub, free Google Cloud trial). Stack must be free or near-free.

**Personality preference:** Ian likes to call Claude "Jarvis". Acknowledge and respond to the name when used. Personal preference, not roleplay — Claude remains Claude with all standard capabilities.

**Communication style Ian wants:**
- Direct and concise. No conversational filler. No preamble.
- Productive feedback every turn. Every response should include an action.
- Never fill in gaps or assume — ask first.
- Only change what was explicitly asked. No scope creep.
- One consolidated answer beats three partial ones.
- Read the GitHub repo (or ask for the raw URL) before answering code questions.
- Flag when a GitHub edit is possible instead of a Lovable prompt.
- Factual only. If unsure, ask.
- Don't ask "should we continue?" — just do the next useful thing.

---

## 1. BUSINESS OVERVIEW

**Owner:** Ian Spies
**Location:** Pretoria, South Africa
**Business:** Solusite Media — web development for SA local service businesses
**Day job:** Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server)
**Side projects:** Spies Construction, DFFRNT (athletic wear), Silverbrook Media (fiancée's social media business)
**Key collaborator:** Markus (lead handler, mentioned but not active in this workflow yet)

### The model
1. Scrape SA business leads via multi-stage Python pipeline ✅ DONE
2. Qualify by website gap (Facebook-only > broken > old > none) ✅ DONE (with known false positive issue)
3. Call qualified leads to confirm interest ⚠️ 2 attempts so far, both no
4. Build demo site for confirmed leads using Lovable.dev or recycled archetype templates ⚠️ Currently building before calling, should reverse
5. Pitch via WhatsApp/email with "I already built it for you" hook
6. Convert to client → offer monthly retainer

### Pricing (current)
- **Build:** R5,000 once-off baseline (flexible/payment plans available)
- **Retainer:** R700/month maintenance
- **Blog add-on:** R500/month for 2 posts

### Target pricing by archetype (from research)
- **Events & Creative** (weddings, photographers, venues): R8,500–R12,000 build, R900/month
- **Hotels & Hospitality:** R8,000–R12,000 build, R900/month
- **Beauty & Wellness:** R5,000–R7,500 build, R700/month
- **Food & Restaurants:** R5,000–R6,500 build, R700/month
- **Health & Fitness:** R5,000–R10,000 build, R500–R800/month
- **Professional Services:** R6,000–R12,000 build, R700–R900/month
- **Education & Training:** R3,500–R6,500 build, R500–R600/month
- **Trades** (plumber, electrician, handyman): R5,000 build, R700/month — hardest sell, lowest priority

---

## 2. CURRENT TOOL STACK

| Category | Tool | Notes |
|---|---|---|
| Build (current) | Lovable.dev | React + Supabase, credit-based, will phase out for production |
| Build (target) | Claude Code + Vercel | Free, GitHub-driven, no credit ceiling |
| Backend | Supabase | DB, auth, storage, edge functions |
| Code editing | Claude Code (Mac Terminal) | Local repo work, git operations, has bash + git tools |
| Strategy/code review | Claude.ai (this chat or new ones) | Web interface, accepts pasted raw URLs only |
| Repo hosting | GitHub (`Spies-ang`) | Keep PRIVATE — never expose API keys |
| Local dev | VS Code on MacBook | |
| Email | Resend.com | Transactional, 3,000 free emails/month |
| SEO | Prerender.io | Fixes Lovable's CSR indexing for Google |
| Blog | Inblog.ai | Connects to Lovable sites at /blog |
| Lead scraping | Google Places API | Project: "Business Scraper", $300 free trial ($291 remaining, expires 2026-05-19) |
| Scripting | Python 3.9.6 (Mac) | Scraper modules |
| Auth (terminal) | gh CLI | Installed via Homebrew, persistent auth across all repos |

---

## 3. LEAD SCRAPER — STATUS: COMPLETE

**Repo:** `github.com/Spies-ang/lead-scraper` (PRIVATE — contains hardcoded API key)
**Local path:** `~/Documents/lead-scraper/`
**API key (exposed in private repo):** `AIzaSyCr65TnL51BTJeZ6b-jfh9ernZdYQnRuAM`

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

### KNOWN ISSUE — Stage 2 False Positives ⚠️
Stage 2 uses the `requests` library which can't execute JavaScript. Modern React/Next.js/Vue sites get flagged as BROKEN/OLD/NO_VIEWPORT because content renders client-side. Many "broken" leads in the sheet have functional sites. Confirmed via manual review of wedding photographer leads (4 of 5 disqualified after manual check).

**Fix options (deprioritized until first sales validate):**
1. Switch Stage 2 to Playwright (accurate but 10x slower)
2. Add "looks modern" detection override (if site has React/Next/Vue script tags, trust it and only flag if 404)
3. Manual review before calling

### Lead generation philosophy (V2)
**V1 lesson:** Established businesses with no website don't feel they need one. Hard sell.

**V2 priority order:**
- **TIER 1 HOT:** Facebook-only / broken / redirects to FB / new businesses (1-6 months, 5-20 reviews)
- **TIER 2 WARM:** Old sites / non-mobile / no SSL / placeholder / very slow
- **TIER 3 COLD:** Established businesses with NO website (50+ reviews) — uphill battle

**Priority industries:**
- CRITICAL (web functionally required): Wedding photographers, event venues, restaurants, fitness studios, yoga, catering, hotels, tour operators, spas, beauty/hair/nail, wedding planners, music schools, tutoring, driving schools
- HIGH: Personal trainers, physios, chiropractors, dentists, vets, pet grooming, interior designers, architects, real estate, accounting, legal
- MEDIUM: Barbers, auto repair, mechanics, cleaning, pest control, landscaping, pool, moving, security
- LOW: Plumbers, electricians, handymen, builders, painters, roofers — word-of-mouth dominant

**REVISED LESSON (post-Stefanie):** Even Tier 1 leads with strong existing demand (followers, reviews, bookings) feel no pain. Need to qualify on PAIN, not just gap. The Stage 2 false positive issue compounds this.

---

## 4. ARCHETYPE TEMPLATES

The recycling strategy: build one site per industry archetype, strip into a `siteConfig.ts` template, then clone the repo for new clients in the same archetype by editing only the config file.

### Archetype 1 — Trades & Home Services
**Status:** 1.5 of 2 base sites templated (work in separate "Recycling" chat)
- **Roelf's Auto Electrical** — `github.com/Spies-ang/roelfsautoelectrical` — siteConfig templated, all 11 core files complete (may not be pushed)
- **Riakona Electrical Solutions** — `github.com/Spies-ang/riakonaelectrical` — ~80% complete, 5 files remaining

### Archetype 2 — Beauty & Wellness ⚠️ PAUSED
**Status:** First base site built, design upgrade attempt broke it, currently in revert state needed
- **La Belle Hair and Beauty Salon** (Pretoria, Montana Park)
  - Repo: `github.com/Spies-ang/beauty-bloom-template-54d0c7e3`
  - Live preview: https://id-preview--ad09b8c3-525a-4d9b-a01f-84cede7271c8.lovable.app/
  - **State:** Initial build completed with clean siteConfig.ts. A second prompt attempted to upgrade the visual design with editorial elements (Fraunces typography, scrolling marquee, asymmetric hero, oversized numbered sections). The marquee collided with the navbar and the entire upgrade is broken. **Needs to be reverted in Lovable's version history (free)** or fixed via Claude Code edits.
  - **Lead source:** La Belle, 318 Veda Ave, Montana Park, Pretoria. Phone: 082 730 9796. Facebook-only, 19 reviews, 4.9⭐. Confirmed services from Fresha listing: Cuts, Colour, Highlights, Balayage, Keratin, Extensions, Children's Cuts, Beauty Treatments.
  - **Decision:** Pause until weekend. Focus on recycling Ross Images template for more wedding photographer calls today.

### Archetype 3 — Events & Creative ⭐ ACTIVE
**Status:** First base site complete (Ross Images Photography), template-ready
- **Ross Images Photography** — `github.com/Spies-ang/ross-images-studio`
  - Live: https://rossimagesphotography.lovable.app/
  - **Outcome:** Pitched 2026-04-09. Stefanie Ross said no. Reasoning: "always fully booked, has good Facebook following, doesn't need a website." Confirmed the V2 lesson — strong existing demand = no pain.
  - **siteConfig.ts is template-ready** — testimonials genericized with (sample) tags, packages.other has pricing, priceTier dead field removed. Last commit: `8e8d360`.
  - **Use case going forward:** This is now the wedding photographer recycling template. Clone repo, swap siteConfig, push, deploy. Estimated 10-15 min per new client.
- **87 Events** — Ian still in conversation with them, hold on cloning that repo

### Archetype 4 — Food & Hospitality
**Status:** Not started. Thaba Meat Market repo may serve as base.

### Archetype 5 — Professional Services
**Status:** Not started

### Archetype 6 — Education & Training
**Status:** Not started

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

### Ross Images Photography (Stefanie Ross — DECLINED 2026-04-09)
- Demo site exists but no sale
- Repo will be templated for next photographer (no need to delete)
- Make repo PRIVATE before reusing
- Lessons learned: she had no pain point — strong existing demand from Facebook following meant the website pitch had no leverage

### La Belle Hair and Beauty Salon (Beauty pilot — PAUSED)
- Demo site exists but in broken state
- No call attempted yet
- Pick up next weekend after resolving the broken hero state

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

### Lovable workflow rules
- GitHub edits preferred over Lovable prompts for simple fixes (auto-deploys in ~60s, free)
- Consolidate all fixes into one Lovable prompt where possible
- Only use Lovable for new features or complex UI changes
- Security scan fixes in Lovable are always FREE — use them
- Only build demo sites for CONFIRMED interested leads (after call) — but currently violating this; see strategic plan in Section 7
- When a Lovable prompt produces a bad result, always REVERT via Lovable's version history rather than rebuilding (free, avoids credit waste)
- Long Lovable prompts that try to do too many design changes at once will produce broken results (confirmed by La Belle hero failure). Surgical, single-section prompts work better. Even better: edit code via Claude Code + GitHub, skip Lovable for design iteration.

---

## 7. STRATEGIC ARCHITECTURE — TARGET STATE

This section is the result of extensive research validating Solusite's stack against 2026 industry practice. Multiple sources cited at end of section.

### The diagnosis
Ian's bottleneck is NOT a tool problem — it's an orchestration problem. Every site takes hours because Ian is the message bus between three Claudes (browser, Code, Lovable's internal AI), Lovable's UI, GitHub, and Terminal. Every handoff is manual copy/paste. Actual building work is ~20% of time, the other 80% is human ferrying state between systems.

### The validated stack (hybrid Claude Code + n8n)

```
                    ┌──────────────────────────────────┐
                    │           DATA LAYER             │
                    │  Airtable: leads, sites, status  │
                    │  (replaces messy Google Sheet)   │
                    └──────────────┬───────────────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
                ▼                  ▼                  ▼
       ┌────────────────┐  ┌──────────────┐  ┌────────────────┐
       │   n8n          │  │ Claude Code  │  │  Twilio        │
       │ (orchestration)│  │ (reasoning)  │  │ (WhatsApp)     │
       │                │  │              │  │                │
       │ • Schedules    │  │ • Research   │  │ • Send pitch   │
       │ • Webhooks     │  │ • Build site │  │ • Receive reply│
       │ • Retries      │  │ • QA + push  │  │                │
       │ • Loops        │  │ • Skills     │  │                │
       └────────┬───────┘  └──────┬───────┘  └────────┬───────┘
                │                 │                   │
                └─────────────────┼───────────────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │  GitHub repos    │
                        │  Auto-deploys    │
                        │  to Vercel       │
                        │  (NOT Lovable)   │
                        └──────────────────┘
```

### Why hybrid (n8n + Claude Code), not pure Claude

| Job | Best tool | Why |
|---|---|---|
| Build sites, customize configs, write code | Claude Code | Reasoning, context, no ceiling |
| Schedule "run every morning at 8am" | n8n | Built-in cron, retry logic, monitoring |
| Receive WhatsApp webhook → trigger workflow | n8n | Webhook nodes designed for this |
| Talk to Twilio, Airtable, HubSpot in one flow | n8n | 400+ native integrations |
| Decide what to do based on a 50-page document | Claude Code | LLM reasoning |
| Run the same 8-step pipeline for 50 leads in parallel | n8n | Loop nodes, queue handling |

Pure Claude can't do unattended scheduling reliably. Pure n8n can't reason about content. Both together = complete pipeline.

### IAN'S CONSTRAINTS (confirmed 2026-04-09)
- **No new paid tools.** Free tier only. Stack must work on Claude Pro + free n8n + free GitHub + free Vercel + Twilio pay-per-message.
- **WhatsApp pitch sending will stay manual** (Ian wants the personal touch + ability to deviate from script post-call). n8n is only for the build pipeline, not outbound messaging automation.
- **Time-pressured**, day job means tooling work happens on weekends.

### Tooling cost analysis (confirmed Ian-friendly)

| Tool | Cost | Status |
|---|---|---|
| Claude Code (Pro plan) | $20/month — already paying | Use it |
| n8n self-hosted on Mac | Free | Install when ready |
| n8n-MCP (community) | Free | Install when ready |
| Airtable | Free tier (1,200 rows) | Optional upgrade later |
| Vercel hosting | Free tier (covers hundreds of sites) | Replace Lovable hosting |
| GitHub | Free | Already using |
| Twilio WhatsApp | SKIP — Ian will manually send | N/A |

### Skills, Subagents, MCP — what they are

**Skills:** Folder-based playbooks Claude loads automatically. Live in `~/.claude/skills/`. Work across Claude.ai, Claude Code, and API. For Solusite: a `solusite-build-pipeline` skill bundling pricing rules, archetype configs, design system, pitch scripts, working principles. Created once, available everywhere.

**Subagents (Claude Code):** Parallel/background workers in their own context windows. Press Ctrl+B to background, `/tasks` to view. For Solusite: spawn 5 subagents to research 5 leads in parallel.

**MCP (Model Context Protocol):** How Claude talks to external tools (n8n, GitHub, Supabase, Airtable). The "Connectors" feature in claude.ai is the same thing under a different name. Currently connected: Gmail, Google Calendar, Canva, WordPress, Wix.

**Slash commands:** Custom one-word triggers for repeatable workflows. `/build-site [lead-name]` could collapse a 30-minute workflow into one command.

**Hooks:** Deterministic scripts that fire at specific points (post-commit, pre-push). For Solusite: post-commit hook that updates HANDOVER.md automatically.

### Validation sources (researched 2026-04-09)
- n8n + Claude Code via MCP: confirmed production-grade, multiple case studies (aimaker.substack.com, mindstudio.ai, claudefa.st blog)
- n8n-MCP project: 1,396 nodes documented, used by Anthropic in testing
- Production case study: agency went from 3-week backlog to 40 minutes per workflow with 3x client load using Claude Code + n8n hybrid (gofastai.medium.com Feb 2026)
- WhatsApp Business API standard pattern: Twilio + n8n is the dominant stack for AI agencies in 2026
- Skills documentation: support.claude.com, code.claude.com, github.com/anthropics/skills

---

## 8. CURRENT DECISION — WHAT WE'RE DOING NOW

**Decision made 2026-04-09 evening: STOP BUILDING. CALL TODAY. AUTOMATE LATER.**

### Reasoning
Ian has 11,120 leads, 2 half-built sites (Ross Images + La Belle), and 0 confirmed sales. The bottleneck isn't tools — it's untested pitch. Every hour spent on n8n / skills / new archetypes today is an hour not on the phone. Sales validate the system; tools don't.

### Sequencing

| When | What | Why |
|---|---|---|
| **Right now** | Update this handover doc with chat context | Preserves state before chat hits limit |
| **Today** | Use Ross Images template in recycling chat. Pull next 5 wedding photographer leads. Reskin in 10 min each via siteConfig swap. Phone all 5. | Tests recycling pipeline. Zero new credits. |
| **Tomorrow morning** | Same — 5 more wedding photographers OR pivot to beauty if Ross template converts poorly | More data, same low cost |
| **This weekend** | (1) Fix Stage 2 with Playwright (2) Set up Airtable + import leads (3) Install n8n locally and connect MCP (4) Write the solusite skill folder | Tooling work, when Ian has hours to focus |
| **Next week** | Wire n8n workflow → first batch generation → call 10 leads in one morning | Real automation, only after 5-10 calls of actual data |

### What's PAUSED
- **La Belle Beauty template** — broken hero, needs revert via Lovable history (free), pick up next weekend
- **Ross Images visual upgrade** — Stefanie said no, site is fine as-is for the next photographer
- **n8n + Airtable + MCP setup** — weekend
- **Stage 2 false positive fix** — weekend
- **Skill folder build** — Jarvis to draft tomorrow morning, Ian installs whenever
- **Beauty / Pro Services / Education archetype builds** — after Wedding Photographer pipeline is proven

---

## 9. GIT AUTH SETUP (RESOLVED 2026-04-09)

**Permanent fix installed:**
1. Homebrew installed via `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Added to PATH in `~/.zprofile`
3. `gh` CLI installed via `brew install gh`
4. Authenticated via `gh auth login` (HTTPS, web browser flow)

**Result:** All future `git push` operations work automatically across all repos. No more PAT pasting needed.

**Cleanup needed:** `~/Documents/lead-scraper/` remote URL still has an exposed PAT in plain text. Run:
```bash
cd ~/Documents/lead-scraper && git remote set-url origin https://github.com/Spies-ang/lead-scraper.git
```
Then rotate the exposed token at https://github.com/settings/tokens (look for `ghp_skzIqq0...`).

---

## 10. CLAUDE CHAT WORKFLOW

This project spans multiple Claude chats with different roles:

| Chat | Purpose | Has bash/git tools? |
|---|---|---|
| **Lead scraper & client builds** (this chat — getting long) | Strategy, research, code review via raw URLs | No (web Claude) |
| **Recycling rejected client websites** | Active templating work for archetypes | Partial — handover via prompts |
| **HandymanDirect** | Vincent's active client work | Yes — full Claude Code tools |

### Tool limitations to know
- **Web Claude (this chat):** `web_fetch` only accepts URLs explicitly pasted by Ian or returned from searches. Cannot guess raw.githubusercontent.com URLs. For code review, Ian must paste the raw URL directly.
- **Claude Code (Terminal):** Has full bash, git, file editing. This is where all execution happens. Browser Claude prompts get pasted into Claude Code for execution.

### Cross-chat handoff process
1. This doc lives at `https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md`
2. To start a new chat, paste: *"Read this and continue the Solusite Media project: [raw URL above]"*
3. New chat fetches the doc, knows everything, asks Ian what to work on next

---

## 11. ACTIVE FILE PATHS

### Local
- Scraper: `~/Documents/lead-scraper/`
- Ross Images: `~/Documents/ross-images-studio/`
- Beauty Bloom Template: `~/Documents/beauty-bloom-template-54d0c7e3/`
- Solusite Context (this doc): `~/Documents/solusite-context/HANDOVER.md`

### Remote
- Lead scraper: https://github.com/Spies-ang/lead-scraper (private, exposed PAT in remote URL — needs cleanup)
- Ross Images: https://github.com/Spies-ang/ross-images-studio (currently public, make private after pitch)
- Beauty Bloom: https://github.com/Spies-ang/beauty-bloom-template-54d0c7e3
- HandymanDirect: https://github.com/Spies-ang/handymandirectv2
- Roelf's Auto: https://github.com/Spies-ang/roelfsautoelectrical
- Riakona Electrical: https://github.com/Spies-ang/riakonaelectrical
- Solusite Context: https://github.com/Spies-ang/solusite-context (HANDOVER.md lives here)
- Lead sheet: https://docs.google.com/spreadsheets/d/1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI

---

## 12. SESSION LOG

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
- Created initial handover document
- Created `solusite-context` GitHub repo (public, will be made private)

### 2026-04-09 — Ross Images pitch + Beauty pivot + Strategic architecture
- Pitched Stefanie Ross (Ross Images Photography). Outcome: NO. Reason: fully booked, has Facebook following, no pain
- Decided to pivot to Beauty & Wellness archetype
- Pulled top 8 beauty leads from sheet
- Selected La Belle Hair and Beauty Salon (Pretoria, Montana Park) as the Beauty archetype base
- Built complete Lovable site (`beauty-bloom-template-54d0c7e3` repo) with clean siteConfig
- Attempted aggressive editorial design upgrade in single Lovable prompt — broke the layout (marquee colliding with navbar)
- Pivoted to Claude Code editing (free via GitHub auto-deploy) instead of Lovable prompts
- Cloned beauty-bloom-template-54d0c7e3 locally, attempted hero-only redesign via Claude Code
- Lovable preview build failed — reason unclear, "Preview failed" badge not clickable
- Ran `npm run build` locally to debug — paused before completion when Ian raised the broader strategic conversation
- Strategic conversation: Ian asked Claude (Jarvis) to research and validate the stack against 2026 industry practice, including third-party tools, plugins, and artifacts
- Researched n8n + Claude Code + n8n-MCP as the production hybrid stack used by AI agencies in 2026
- Recommended Airtable + n8n + Claude Code + Vercel + Twilio architecture
- Ian confirmed: stick with free tools only (Claude Code + n8n free + GitHub + Vercel free), keep WhatsApp manual, focus on calls today, automation on weekend
- Decided to pause La Belle work, pause new tooling, and use Ross Images template in recycling chat for more wedding photographer calls today
- Updated this handover doc to reflect all current state and decisions

---

## 13. APPENDIX — IMMEDIATE NEXT ACTIONS FOR NEW CHAT

If a new chat is reading this and the project is being resumed, the immediate next actions are:

1. **Confirm the date.** If it's still 2026-04-09 evening or 2026-04-10 morning, the focus is calling more wedding photographer leads. Switch to the Recycling chat and pull the next 5 wedding photographer leads from `qualified_leads.csv`, filtering for FACEBOOK_ONLY or BROKEN_WEBSITE with 10-25 reviews. Skip already-reviewed leads: Ross Images, Elri, Judith Belle, Tokgamo, Blaqjuice.

2. **For each new lead:** Research the business (Facebook, Google), clone Ross Images repo as `wedding-[business-slug]`, swap siteConfig.ts values, push, deploy, send link. Estimated 10-15 min per site.

3. **Phone immediately after build.** Use the broken-domain pitch (or the Facebook-only pitch for those leads). Track results in Google Sheet status column.

4. **End of day:** Update this handover doc with sales results (yes/no/maybe per call). This data informs whether we keep going on wedding photographers or pivot to beauty next.

5. **Weekend:** Stage 2 fix (Playwright), Airtable setup, n8n install, skill folder build.

---

*End of handover document. To bootstrap a new Claude chat: `"Read this and continue the Solusite Media project: https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md"`*
