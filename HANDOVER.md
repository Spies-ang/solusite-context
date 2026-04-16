# SOLUSITE MEDIA — HANDOVER DOCUMENT
**Last updated:** Wednesday 16 April 2026
**Bootstrap:** Paste this URL into any new Claude chat or Claude Code session:
`https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md`

---

## CURRENT STATE (16 April 2026)

**Batch 1 (6 sites):** Driving schools (Revo, TJs, Rightway, Skill on Wheels, Dayyaans) + Lat Wai Farm Venue. All built, WhatsApps sent. Mixed responses (see Client Responses below).

**Batch 2 (7 sites) — COMPLETE:** MW Architects (Pretoria), Lisa Rorich Architects (Durban), Rono Architects (Joburg), Ndibali Interior Designs (Joburg), Blue Sky Interior Design (Joburg), CodeFlash Photography Studio (Pretoria), Meintjes Catering (Pretoria). All pushed and deployed on Lovable. WhatsApps NOT YET SENT.

**Nexia SAB&T dropped** — verified as 8th largest accounting firm in SA with a working main site. Scraper picked up a broken branch/subdomain URL. False positive. Need 1 replacement lead before sending batch 2.

---

## WHO

Ian Spies, Pretoria, South Africa. Runs **Solusite Media** (web dev + digital marketing) alongside a day job as Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server). Also runs Spies Construction and DFFRNT (athletic wear). Fiancée runs **Silverbrook Media** (social media management, shares pipeline infrastructure). Collaborator: **Markus** (lead handling). **NEW: hired a young salesman** to handle closing calls after Ian's warm WhatsApp intro — Ian builds and warms, salesman closes.

**Communication style:** Direct, concise, no preamble. Voice-to-text input. Only change what was asked. Never assume — ask. One consolidated answer beats three partial ones.

**Preferred name for Claude:** "Jarvis" — personal preference, not roleplay. Claude remains Claude with all standard capabilities.

---

## BUSINESS MODEL — TWO-STAGE SALES HANDOFF

The flow as of 13 April 2026:

1. **Scrape & qualify** — Multi-stage Python scraper finds leads with website gaps
2. **Build** — Recycle the matching archetype template, customize siteConfig.ts for the lead, push to GitHub, Lovable auto-deploys
3. **Ian sends warm intro WhatsApp** — Personal hook + gap framing + live demo URL + "important to know" placeholder disclaimer + commits to a callback window. Stays in Ian's name to preserve the trust anchor ("a real person noticed me")
4. **Ian sends salesman briefing card** — Structured summary of the lead so the salesman can dial cold-but-prepared
5. **Salesman calls** — **Suggested opening template** (not law, adapt to the lead): "Hi, this is [name] from Solusite Media — Ian asked me to follow up on the website he sent you yesterday." This phrasing keeps Ian as the trust anchor and positions the salesman as a colleague.
6. **Salesman closes the meeting**, not the deal — goal is a 30-45 min meeting where the client hands over real photos and details
7. **Convert** to paying client + monthly retainer

### Pricing

**All archetypes anchor at R5,000 once-off.** Frame it as: *"Our builds usually go for R8,500 — you're getting the introductory rate of R5,000."* Retainer varies per archetype (see table).

**Fallback payment plan** (offer only if price is the blocker): R2,500 upfront + R2,500 on completion within 1 week.

Blog add-on: R500/month for 2 SEO posts per site. Payment plan handled in negotiation. Never lead with price.

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

## SALES HANDOFF — REQUIRED OUTPUTS PER LEAD

For every lead that gets a built demo site, generate TWO documents:

### 1. WhatsApp message (for Ian to send to the client)
- Personal hook in first sentence (specific detail you noticed about THEIR business)
- Gap framing ("I noticed you're running off Facebook" / "I noticed your domain shows Coming Soon")
- Live demo URL
- "Important to know" placeholder paragraph — explicitly flags photos, prices, hours as placeholders
- Specific callback window: "Someone from our team will give you a call tomorrow between 10am and 12pm" (NOT "I'll call" — handoff is now to salesman)
- Low-pressure close

**Rule: never mention being Pretoria-based in client comms.** No "we're a Pretoria agency," no "local to you in Pretoria," no geographic framing at all. Solusite pitches as a capability, not a locality. Applies to WhatsApp messages, salesman scripts, demo site copy — everything client-facing.

Stays in Ian's name. The "we" reframing happens naturally on the salesman's call, not in the WhatsApp.

### 2. Salesman briefing card (for Ian to send to the salesman)
Structured format, scannable in 30 seconds before dialing. Required sections:

```
LEAD: [Business Name]
STATUS: [Interested / Pending callback / Cold]

CONTACT
Phone, WhatsApp, Email, Address, Live demo URL

ABOUT THEM
3-5 bullet points on what the business does, scale, reputation

THE PAIN POINT (LEAD WITH THIS)
The specific gap and why it costs them money/credibility/clients.
Include math angle if possible (e.g. commission costs, lost SEO traffic).

COMPETITIVE ADVANTAGES TO MENTION
4-5 bullet points on why Solusite specifically (demo-first, archetype-tuned, etc.)
DO NOT mention Pretoria / geography.

WHAT THEY ALREADY KNOW (from Ian's WhatsApp)
What's been disclosed so the salesman doesn't repeat or contradict

PRICING (KEEP IN HEAD, DON'T LEAD WITH IT)
Anchor: R8,500. Actual: R5,000 introductory. Retainer per archetype.
Fallback split: R2,500 upfront + R2,500 on completion within 1 week.

THE CLOSE
What the goal of this specific call is. Usually a meeting, not a deal.
Suggested closing phrase.

OBJECTIONS TO PREP FOR
3-4 likely objections + responses

NAME TO USE / WHO TO ASK FOR
If known
```

This format is the standard. Every recycling chat output should include both documents.

---

## LEAD GENERATION — V2 MULTI-STAGE SCRAPER

### Architecture
- **Stage 1:** `scraper_stage1_broad_capture.py` — Google Places API → `raw_leads.csv`
- **Stage 1b:** Place Details enrichment → `enriched_leads.csv`
- **Stage 2:** `scraper_stage2_website_checker.py` — visits each website → `qualified_leads.csv`
- **Stage 2 v2:** `scraper_stage2_website_checker_v2.py` — Playwright-based, fixes false positives. **NOT YET RUN.** Located at `~/Documents/lead-scraper/`. Run overnight, ~6-8 hours.
- **Stage 3:** `scraper_stage3_sheets_export.py` — exports to Google Sheets
- **Master:** `run_all_stages.py` runs all 3 stages
- **Repo:** `github.com/Spies-ang/lead-scraper` (private)
- **Output:** 11,120+ qualified leads across 67 industry tabs in Google Sheets `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`

### V2 Lead Priority (by website gap)
**TIER 1 HOT:** FACEBOOK_ONLY, BROKEN_WEBSITE, REDIRECTS_TO_FACEBOOK, new businesses (5-20 reviews)
**TIER 2 WARM:** OLD_OR_BAD_WEBSITE, non-mobile-responsive, no SSL, placeholders
**TIER 3 COLD:** Established no-website (50+ reviews) — V1 confirmed hardest sell

### Industry Budget Filter (CRITICAL — apply before pulling leads)

Website-gap tier alone is not enough. Industry determines whether the lead can actually pay. Close rate is **uncertain** across archetypes — conversion data is still thin — so prioritize industries with clear, per-customer revenue over industries with high need but thin margins.

**DEPRIORITIZE (high need, lower budget, close rate unproven):**
- Wellness studios, personal trainers, physiotherapists, yoga studios, small independent spas
- These businesses often *need* a site more than anyone, but the monthly cash flow rarely supports a R5,000 build + R700 retainer without negotiation friction

**PRIORITIZE (clear revenue per customer, defensible ROI pitch):**
- **Hospitality with commission pain:** hotels, B&Bs, guesthouses, lodges — Booking.com/Airbnb commissions are a math-based pitch
- **Professional services with project fees:** architects, lawyers, accountants, consulting firms, agencies
- **Education with course fees:** driving schools, music schools, tutoring businesses, training providers
- **Event-driven with per-booking revenue:** wedding photographers, event venues, catering, tour operators
- **Restaurants** (established, not street-food tier)

The scraper should filter on both gap tier AND industry category before a lead hits Ian's desk.

### Known Issues
- Stage 2 v1 false positives — flags React/Next.js as BROKEN. Fix: Stage 2 v2 (Playwright). Deferred until calls validate.
- Manual verification still required before building demos.

---

## ARCHETYPE TEMPLATES — CURRENT STATE

| # | Archetype | Template Repo | Live URL | Status | Hardened? |
|---|---|---|---|---|---|
| 1 | Education & Training | `Spies-ang/pass-prep-pro` | studentechdrivertraining.lovable.app | Pending callback | ✅ Hardened — commit `077d8a8` |
| 2 | Food, Hospitality & Events | `Spies-ang/garden-gateways` | gardenpointguesthouse.lovable.app | DECLINED | ⚠️ Partial — Location.tsx needs per-repo fix (hardcoded city strings) |
| 3 | Professional Services / Portfolio | `Spies-ang/legacy-portfolio` | megarchitects.lovable.app | Pending callback | ❌ NOT hardened — missing fields trigger Lovable auto-fix loop (overwrites team arrays). ALSO: Practice page component has hardcoded MEG team names that ignore siteConfig.team entirely. |
| 4 | Photography Studio | `Spies-ang/ross-images-studio` | — | Template-ready | ❌ NOT hardened — missing fields cause same Lovable auto-fix issue |
| 5 | Beauty & Wellness | `Spies-ang/prana-template-suite` | pranaloveyoga.lovable.app | DECLINED | — |
| 6 | Trades & Home Services | `roelfsautoelectrical` + `riakonaelectrical` | — | Roelf done, Riakona 80% | — |
| — | Beauty & Wellness (v1) | `Spies-ang/beauty-bloom-template-54d0c7e3` | — | La Belle — hero broke, needs Lovable revert | — |

**Future archetype — Interior Design:**
Blue Sky Interior Design (Spies-ang/blue-sky-interior) can become the Interior Design archetype after a Lovable restyle (interior imagery replacing architectural exteriors, primary color #2D5B4E sage green). This avoids building a new template from scratch. Zero credit cost since the structure is identical to legacy-portfolio — just needs visual differentiation.

### Active recycling — IN PROGRESS
- **Remix repo:** `Spies-ang/remix-of-bnb-archetype` (cloned from Garden Point template)
- **Target lead:** **The Villa 442**, 442 Salie St, Chantelle, Akasia, Pretoria 0182. Phone 064 546 8891. 4.9 stars, 11 reviews. BROKEN_WEBSITE — their "website" is literally a Booking.com share link (https://www.booking.com/Share-9NNlQY). Same commission-dependency pitch as Garden Point.
- **Status:** Recycling chat is currently working on this. Both repos need to be temporarily public for the chat to access them.

---

## ARCHETYPE ARCHITECTURE — CLEAN REPO STRATEGY (decided 15 April 2026)

### The problem
Every remix inherits leftover client content from the source repo. The strip script catches siteConfig fields but misses hardcoded component strings (MEG team names, Cape Town directions, palette values). Each recycle wastes Claude Code time and Lovable credits fixing inherited mess.

### The fix
Create dedicated clean archetype repos that exist purely for remixing. Each archetype:
- Has siteConfig.ts with obvious placeholder values ("[BUSINESS_NAME]", "[CITY]", "[PHONE]")
- Has ZERO hardcoded client content in any component — everything reads from siteConfig
- Has default Unsplash images matching the industry (not a specific client's photos)
- Has a README.md explaining what fields need filling
- Gets stripped and hardened ONCE, then never needs the strip script again

The strip script becomes a one-time archetype creation tool, not a per-recycle step.

### Recycle flow (new)
Clean archetype repo → Lovable remix (free) → fill siteConfig via Claude Code → push → Lovable auto-deploys → cosmetic Lovable pass if needed

### Archetype repos to create

| # | Repo Name | Source | Industries | Key structure |
|---|---|---|---|---|
| 1 | archetype-professional-portfolio | legacy-portfolio (MEG) | Architects, interior designers, engineers, consultants | Practice/team, projects gallery, services, contact |
| 2 | archetype-interior-design | blue-sky-interior (after restyle) | Interior designers, decorators, furniture designers | Same as above, interior imagery, warmer palette |
| 3 | archetype-photography-studio | ross-images-studio | Photography studios, videographers | Gallery-heavy, packages, booking, photographer bio |
| 4 | archetype-driving-school | pass-prep-pro | Driving schools, training providers | Already hardened. Packages, FAQ, test centre, K53 |
| 5 | archetype-event-venue | garden-gateways (Lat Wai) | Event venues, function halls, wedding venues | Venue spaces, enquiry form, directions, amenities |
| 6 | archetype-catering | meintjes-catering (after fix) | Caterers, event décor | Packages, event types, décor. Different from venue |
| 7 | archetype-accounting | NEW BUILD | Accountants, auditors, tax advisors | Credentials, IRBA/SAICA, industries served, no portfolio |
| 8 | archetype-restaurant | NEW BUILD | Restaurants, cafés | Menu, hours, reservations, gallery, location |

### Creation process (per archetype)
1. Clone source repo to new name (archetype-xxx)
2. Run strip_siteconfig.py
3. Fix any hardcoded component issues found in scan report
4. Replace siteConfig values with obvious placeholders
5. Add README.md with field documentation
6. Commit and push as new repo under Spies-ang
7. Create matching Lovable project linked to this repo
8. All future remixes come from the Lovable project, never from a client repo

### n8n automation flow (future)
1. Trigger: new lead marked "Build" in Airtable
2. n8n clones matching archetype repo to new client repo name
3. Claude subagent researches lead online, generates siteConfig content
4. n8n pushes filled siteConfig to the new repo
5. Lovable auto-deploys within 60 seconds
6. n8n updates Airtable with live demo URL
7. Ian reviews, cosmetic Lovable pass if needed, sends WhatsApp

### Priority order
1. archetype-professional-portfolio (highest volume leads right now)
2. archetype-catering (Meintjes fix creates this as byproduct)
3. archetype-photography-studio (CodeFlash fix creates this)
4. archetype-event-venue (Lat Wai already mostly clean)
5. archetype-driving-school (already hardened, just rename + placeholder siteConfig)
6-8. New builds when those industries come up

---

## SALES RESULTS

| Lead | Archetype | Gap | Result |
|---|---|---|---|
| Garden Point Guest House | Hospitality | WEBSITE_UNREACHABLE | **INTERESTED** ✅ |
| Prana Love Yoga | Beauty & Wellness | FACEBOOK_ONLY | DECLINED (closing studio) |
| MEG Architects | Professional Services | BROKEN_WEBSITE (Coming Soon) | Pending callback |
| Studentech Driver Training | Education & Training | FACEBOOK_ONLY | Pending callback |
| Stefanie Ross Photography (V1) | Events & Creative | FACEBOOK_ONLY | DECLINED (fully booked) |

**Validated learnings:**
- Always check the lead's recent Facebook activity before building (would have caught Prana Love closing)

Sample size is too small to claim anything about which archetype converts best. Do not infer archetype performance from N=1.

---

## CLIENT RESPONSES

| Lead | Batch | Status | Notes |
|---|---|---|---|
| Lat Wai (Wendy) | 1 | **INTERESTED** ✅ | Pricing sent (R5k total: R2,500 deposit + R2,500 on completion, R700/month retainer). She replied "will consider and come back." Keep following up. |
| Lisa Rorich Architects | 2 | **INTERESTED** ✅ | Asked for fee structure. Pricing reply needed. |
| Garden Point Guest House | 1 | **DECLINED** | Earlier batch. |
| Dayyaans Driving School | 1 | **DECLINED** | No longer in business. |
| Prana Love Yoga | 1 | **DECLINED** | Closing studio. |
| TJs Driving Academy | 1 | No response | Follow-up call needed. |
| Rightway Driving Academy | 1 | No response | Follow-up call needed. |
| Skill on Wheels Academy | 1 | No response | Follow-up call needed. |
| Revo Driving School | 1 | No response | Follow-up call needed. |
| MEG Architects | 1 | Pending callback | Second attempt needed. |
| Studentech Driver Training | 1 | Pending callback | Second attempt needed. |
| Batch 2 (all 7) | 2 | Not yet sent | WhatsApps pending. |

---

## KEY LEARNINGS

- **Lovable auto-fix overwrites siteConfig team arrays.** When Lovable runs "Try to fix" on missing fields, it repopulates team arrays with the original template data (e.g. MEG team members appearing on Rono/Ndibali). Always restore via Claude Code after any Lovable "Try to fix" run. Check team, services, projects arrays specifically.
- **Verify every domain before building.** Nexia SAB&T false positive — scraper flagged a broken branch URL but main site is live and professional. Manual spot-check required before committing build time.
- **Scraper exclude list doesn't scale.** Filtering out already-contacted leads via a hardcoded name list in the script is fragile. Filter by Status field in the Google Sheet instead — mark contacted leads as "Sent" or "Closed" and exclude non-"New" rows.
- **Established firms with working sites don't need us.** Even if the scraper flags a URL as broken, a firm with 8 SA offices and a working primary domain is not a prospect. Scraper should weight review count + website quality together, not just URL status.
- **Facebook activity check catches dead businesses.** Would have caught Prana Love closing and Dayyaans no longer operating before build time was spent.
- **Practice page component is hardcoded, not dynamic.** Fixing siteConfig.team alone is NOT enough on legacy-portfolio sites. The Practice.tsx (or Team.tsx) component contains a hardcoded array with MEG team members (Tienie van der Merwe, Lizette van der Merwe, Associate Architect). Must grep for these names in src/ and replace the hardcoded array with siteConfig.team.map(). This affects ALL 5 current legacy-portfolio recycles (MW, Lisa Rorich, Rono, Ndibali, Blue Sky) and needs fixing upstream in the archetype. Claude Code prompt for this fix exists in chat history.

---

## DESIGN SYSTEM — BRAND RESEARCH FIRST (CRITICAL)

**April 2026 lesson learned:** Built 5 consecutive sites using generic archetype-default palettes (all variations of green/cream/sage). Ian flagged it: "you keep using green and pastel green." Every site looked like a template blast.

**The fix (codified in SKILL.md):**
1. Research client's actual brand colors from Facebook cover, Instagram grid, Google profile photos, existing website, logo
2. If nothing found, build a character-driven palette from a specific personality observation (e.g. Gold Reef heritage for B&B near Gold Reef City, road-sign yellow for a driving school)
3. Archetype defaults are LAST RESORT ONLY
4. Never use the same default palette twice in a row

**Palettes applied to current sites:**
- Prana Love: "Coastal Dawn" — apricot #E89B6C + ocean navy #1A2942
- Garden Point: "Gold Reef" — burnished gold #B8860B + wine burgundy #6B2424
- MEG Architects: "Architectural Ink" — monochrome + oxide red #B85A3E accent
- Studentech: "K53 Yellow" — bold yellow #FFD60A + black

---

## AUTOMATION STACK — PLANNED (WEEKEND SETUP, STILL OUTSTANDING)

**Architecture decided:** Airtable (data) + n8n self-hosted (orchestration) + Claude Code (reasoning) + Vercel (production hosting) + GitHub. WhatsApp stays manual.

**Bundle status:**
- `~/.claude/skills/solusite-build-pipeline/SKILL.md` — **INSTALLED** ✅
- `~/Documents/lead-scraper/scraper_stage2_website_checker_v2.py` — **saved, not yet run**
- `AUTOMATION_SETUP.md` — guide saved, not yet executed

**Remaining setup steps (do anytime — not blocked to a specific chat):**
1. Create Airtable Solusite Pipeline base (schema in AUTOMATION_SETUP.md)
2. Install n8n locally: `npm install -g n8n && n8n start`
3. Install n8n-MCP: clone `github.com/czlonkowski/n8n-mcp`, add to `~/.claude/mcp_settings.json`
4. Run Stage 2 v2 overnight (Playwright)
5. Build first n8n workflow (prompt provided in AUTOMATION_SETUP.md)

**Important:** This work is NOT native to any specific chat. Any chat with Claude Code access can pick it up. Ian can come back to it after current sales batch validates conversion.

---

## HANDYMANDIRECT (CLIENT: VINCENT)

Active React/Supabase rebuild on Lovable.dev. Repo: `Spies-ang/handymandirectv2`. Phase 2 development underway and approved. Completed: Premium Services reorder, experience-tier colour coding, trade page architecture refactor, Trades dropdown, tier-specific booking flows, scrollable blog feed window. Pricing references removed from trade pages. Owned by separate chat.

---

## TOOLS & RESOURCES

- **Build:** Lovable.dev (React + Supabase), GitHub `Spies-ang` (KEEP REPOS PRIVATE)
- **Local dev:** Claude Code (Terminal), MacBook
- **Data / scraping:** Python (Google Places API, key `AIzaSyCr65TnL51BTJeZ6b-jfh9ernZdYQnRuAM`), Google Sheets (target `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`), OAuth via `client_secret.json`
- **Design / docs:** Canva MCP, ReportLab
- **Day job stack:** Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server
- **Markets:** South Africa (Afrikaans + English)
- **Google Cloud trial:** $8.59 spent, $291 remaining, expires 2026-05-19

---

## CRITICAL TECHNICAL RULES

1. **Lovable RLS bug:** All Supabase RLS policies generate as RESTRICTIVE. After every prompt → Security → "Try to fix all (Free)"
2. **Always `.maybeSingle()` not `.single()`** — `.single()` throws on zero rows
3. **Address fields:** `GooglePlacesAutocomplete` restricted to `{ country: "za" }`
4. **NEVER commit API keys to public repos** — keep repos PRIVATE
5. **Prerender.io required** on every Lovable site before SEO matters
6. **Disable email confirmation** in Supabase during testing (4 emails/hour limit)
7. **Always add fallback `navigate()`** after role fetches
8. **GitHub edits preferred** over Lovable prompts for simple fixes (free, auto-deploys 60s)
9. **When Lovable prompt breaks something** → revert via version history (free), don't rebuild
10. **Long multi-change Lovable prompts break** — be surgical, single-section changes only
11. **Color swap prompts** must say "do not touch siteConfig.ts, do not regenerate sections"
12. **Browser chats can't read private repos** — temporarily make them public, or paste the file contents into the chat
13. **Exposed token to rotate:** `https://github.com/settings/tokens` (look for `ghp_skzIqq0...`) — manual browser step
14. **Lead-scraper remote URL already clean** (no PAT embedded)

---

## MULTI-CHAT WORKFLOW

| Surface | Role | Has bash/git tools | Can read private repos |
|---|---|---|---|
| Claude.ai browser — strategy chat | Strategy, research, prompts, handover updates | No | No |
| Claude.ai browser — recycling chat | Template recycling, lead selection, prompt writing | No | No |
| Claude.ai browser — HandymanDirect chat | Vincent's client work | No | No |
| Claude Code (Terminal) | All build/edit/deploy/git execution | Yes | Yes (authenticated) |
| Lovable chat panel | Per-project UI changes | Yes (Lovable-specific) | Yes (authenticated) |

Browser chats write prompts. Claude Code executes them. Don't paste browser-chat prompts into Claude Code Terminal or vice versa.

**For recycling chats:** the strategy chat or recycling chat can write the site config and Claude Code prompt, but if it needs to read a private repo first, either (a) temporarily make the repo public, (b) paste the file contents into the chat, or (c) Ian asks Claude Code to read the file and paste it back into the browser chat.

---

## PENDING / ON THE HORIZON

**Immediate — sales:**
- [ ] Send batch 2 WhatsApps (7 messages — MW, Lisa Rorich, Rono, Ndibali, Blue Sky, CodeFlash, Meintjes — phone numbers ready in sheet)
- [ ] Reply to Lisa Rorich with pricing (she asked for fee structure)
- [ ] Schedule Wendy (Lat Wai) callback
- [ ] Follow-up calls for batch 1 non-responders: TJs, Rightway, Skill on Wheels, Revo

**Immediate — pipeline:**
- [ ] Pull 1 replacement lead to replace Nexia SAB&T (same industry filter: accounting / professional services)
- [ ] Pull next batch of 8-10 leads when batch 2 WhatsApps are out

**Build fixes needed:**
- [ ] Fix Practice page hardcoded team component on all 5 architect/interior sites (MW, Lisa Rorich, Rono, Ndibali, Blue Sky) — grep for "Tienie" or "van der Merwe" in src/, replace hardcoded array with siteConfig.team.map(). Then push same fix upstream to legacy-portfolio archetype.
- [ ] Blue Sky Interior — Lovable restyle (interior design imagery, #2D5B4E sage primary)
- [ ] CodeFlash Photography — swap placeholder images with photography studio imagery (Lovable prompt)
- [ ] Meintjes Catering — structural fix (B&B → catering language in Home.tsx and Book.tsx, same pattern as Lat Wai venue conversion)

**Template hardening (do before next batch that uses these archetypes):**
- [ ] Harden `legacy-portfolio` — add all missing siteConfig fields so Lovable auto-fix doesn't trigger and overwrite team/services/projects
- [ ] Harden `ross-images-studio` — same issue, missing fields

**Short-term:**
- [ ] Run Stage 2 v2 Playwright overnight
- [ ] Set up Airtable base
- [ ] Install n8n + n8n-MCP
- [ ] Revert La Belle hero (beauty-bloom-template) via Lovable version history
- [ ] Finish Riakona Electrical templating (5 files remaining)

**Medium-term:**
- [ ] Build first n8n workflow (manual trigger → Airtable → Claude subagent → site generation → Airtable update)
- [ ] Stage 1c social media scraper for Silverbrook Media
- [ ] Fix Stage 2 v1 scoring logic (false positives on React/Next.js sites)
- [ ] Switch scraper exclude logic from hardcoded name list → Status field filter in Google Sheet

**Longer-term:**
- [ ] Hire 2nd salesman if conversion rate validates at scale
- [ ] Build templated archetype for: Restaurant (standalone), Trades refresh, Health & Fitness
- [ ] Productize the offering: standard package, standard upsells, standard onboarding

---

