# SOLUSITE MEDIA — HANDOVER DOCUMENT
**Last updated:** Saturday 12 April 2026
**Bootstrap:** Paste this URL into any new Claude chat or Claude Code session:
`https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md`

---

## WHO

Ian Spies, Pretoria, South Africa. Runs **Solusite Media** (web dev + digital marketing) alongside a day job as Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server). Also runs Spies Construction and DFFRNT (athletic wear). Fiancée runs **Silverbrook Media** (social media management, shares pipeline infrastructure). Collaborator: **Markus** (lead handling).

**Communication style:** Direct, concise, no preamble. Voice-to-text input. Only change what was asked. Never assume — ask. One consolidated answer beats three partial ones.

**Preferred name for Claude:** "Jarvis" — personal preference, not roleplay. Claude remains Claude with all standard capabilities.

---

## BUSINESS MODEL

1. Scrape SA business leads via multi-stage Python scraper
2. Qualify by website gap (Facebook-only > broken > old > none)
3. Build a demo site using recycled archetype template
4. Send personalized pre-call WhatsApp with live demo link
5. Phone the lead next morning to discuss
6. Convert to paying client + offer monthly retainer

**Pricing:**
- Website build: R5,000–R12,000 once-off (varies by archetype — see SKILL.md)
- Monthly retainer: R500–R900/month (varies by archetype)
- Blog add-on: R500/month for 2 posts per site
- Never lead with price — handle in negotiation

---

## LEAD GENERATION — V2 MULTI-STAGE SCRAPER

### Architecture
- **Stage 1:** `scraper_stage1_broad_capture.py` — Google Places API, 67 industries × 4 cities → `raw_leads.csv`
- **Stage 1b:** Place Details enrichment → `enriched_leads.csv`
- **Stage 2:** `scraper_stage2_website_checker.py` — visits each website, checks quality → `qualified_leads.csv`
- **Stage 2 v2:** `scraper_stage2_website_checker_v2.py` — Playwright-based replacement, fixes false positives. **NOT YET RUN.** Located at `~/Documents/lead-scraper/`. Run overnight, ~6-8 hours.
- **Stage 3:** `scraper_stage3_sheets_export.py` — exports to Google Sheets with handler dropdown, status dropdown, priority score, gap notes, one tab per industry
- **Master:** `run_all_stages.py` runs all 3 stages sequentially
- **Repo:** `github.com/Spies-ang/lead-scraper` (private)
- **Output:** 11,120+ qualified leads across 67 industry tabs in Google Sheets (`1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`)

### V2 Lead Priority (learned from V1 failures)
**TIER 1 HOT:** FACEBOOK_ONLY, BROKEN_WEBSITE, REDIRECTS_TO_FACEBOOK, new businesses (5-20 reviews)
**TIER 2 WARM:** OLD_OR_BAD_WEBSITE, non-mobile-responsive, no SSL, placeholders
**TIER 3 COLD:** Established no-website (50+ reviews) — hardest sell, V1 confirmed

### Known Issues
- Stage 2 v1 has false positives — flags modern React/Next.js/JS-rendered sites as BROKEN. Fix: Stage 2 v2 (Playwright). Deprioritized until first call batch validates conversion.
- "No website listed on Google" ≠ no website exists. Manual verification required.

---

## ARCHETYPE TEMPLATES — CURRENT STATE

| # | Archetype | Template Repo | Live URL | Status |
|---|---|---|---|---|
| 1 | Events & Creative | `Spies-ang/ross-images-studio` | — | Template-ready. Stefanie Ross declined (fully booked, doesn't need website). |
| 2 | Beauty & Wellness | `Spies-ang/prana-template-suite` | pranaloveyoga.lovable.app | **INTERESTED.** Prana Love Yoga, Michael O'Rourke, Tableview Cape Town. Color-swapped to Coastal Dawn palette. |
| 3 | Food & Hospitality | `Spies-ang/garden-gateways` | gardenpointguesthouse.lovable.app | **INTERESTED.** Garden Point Guest House, Robertsham JHB. Color-swapped to Gold Reef palette. |
| 4 | Professional Services | `Spies-ang/legacy-portfolio` | megarchitects.lovable.app | **PENDING CALLBACK.** MEG Architects, Hatfield Pretoria. Colors kept as-is (Architectural Ink). |
| 5 | Education & Training | `Spies-ang/pass-prep-pro` | studentechdrivertraining.lovable.app | **PENDING CALLBACK.** Studentech Driver Training, Rossburgh Durban. Colors kept as-is (K53 Yellow). |
| 6 | Trades & Home Services | `roelfsautoelectrical` + `riakonaelectrical` | — | Roelf's template-ready. Riakona 80% done (5 files remaining). |
| — | Beauty & Wellness (v1) | `Spies-ang/beauty-bloom-template-54d0c7e3` | — | La Belle Hair & Beauty. Hero design upgrade BROKE the site (marquee collision). Needs revert via Lovable version history. |

### First recycling target — IN PROGRESS
- **Remix repo:** `Spies-ang/remix-of-bnb-archetype` (cloned from Garden Point template)
- **Target lead:** The Villa 442, 442 Salie St, Chantelle, Akasia, Pretoria 0182. Phone: 064 546 8891. Gap: BROKEN_WEBSITE (website is literally a Booking.com share link — same commission-dependency pitch as Garden Point). 4.9 stars, 11 reviews. Local to Ian.
- **Process:** Strip Garden Point business info from siteConfig.ts → research Villa 442 → insert new business details → push to GitHub → Lovable auto-deploys → send WhatsApp → call next day
- **Google Sheet tab:** Bed And Breakfast

### Recycling workflow (standard, repeatable)
1. In Lovable: "Remix" the archetype template into a new project → connect to new GitHub repo
2. In Claude Code (or Claude chat for prompt writing): research the new lead's business details, brand colors
3. Generate new `siteConfig.ts` with the new client's info
4. Push to GitHub → Lovable auto-deploys in ~60 seconds
5. Send pre-call WhatsApp with live URL
6. Call next morning

---

## SALES RESULTS — FIRST BATCH (11-12 April 2026)

| Lead | Archetype | Gap | Result |
|---|---|---|---|
| Prana Love Yoga (Michael O'Rourke) | Beauty & Wellness | FACEBOOK_ONLY | **INTERESTED** |
| Garden Point Guest House | Hospitality | WEBSITE_UNREACHABLE | **INTERESTED** |
| MEG Architects | Professional Services | BROKEN_WEBSITE (Coming Soon) | Pending callback |
| Studentech Driver Training | Education & Training | FACEBOOK_ONLY | Pending callback |
| Stefanie Ross Photography (V1) | Events & Creative | FACEBOOK_ONLY | **DECLINED** — fully booked, no need |

**Conversion so far:** 2 interested / 4 contacted = 50% interest rate. Hospitality (commission pain) and Beauty (Facebook-only) both converted. Validates V2 lead qualification model.

---

## DESIGN SYSTEM — BRAND RESEARCH FIRST (CRITICAL)

**April 2026 lesson learned:** Built 5 consecutive sites using generic archetype-default palettes (all variations of green/cream/sage). Ian flagged it: "you keep using green and pastel green." Every site looked like a template blast, undermining the "I built this for you" pitch.

**The fix (now codified in SKILL.md):**
1. Research the client's actual brand colors from Facebook cover, Instagram grid, Google profile photos, existing website, logo
2. If nothing found, build a character-driven palette from a specific personality observation (e.g. Gold Reef heritage for a B&B near Gold Reef City, road-sign yellow for a driving school)
3. Archetype defaults are LAST RESORT ONLY
4. Never use the same default palette twice in a row

**Palettes applied to current sites:**
- Prana Love: "Coastal Dawn" — apricot #E89B6C + ocean navy #1A2942 (sunrise on Bloubergstrand reference)
- Garden Point: "Gold Reef" — burnished gold #B8860B + wine burgundy #6B2424 (Gold Reef City heritage)
- MEG Architects: "Architectural Ink" — monochrome black/white + oxide red #B85A3E accent
- Studentech: "K53 Yellow" — bold yellow #FFD60A + black (road sign / L-plate reference)

---

## AUTOMATION STACK — PLANNED (WEEKEND SETUP)

**Architecture decided:** Airtable (data) + n8n self-hosted (orchestration) + Claude Code (reasoning) + Vercel (hosting, replacing Lovable for production) + GitHub. WhatsApp stays manual.

**Weekend bundle files (all delivered, saved locally):**
- `~/.claude/skills/solusite-build-pipeline/SKILL.md` — **INSTALLED** ✅
- `~/Documents/lead-scraper/scraper_stage2_website_checker_v2.py` — saved, not yet run
- `AUTOMATION_SETUP.md` — step-by-step guide for: Airtable base, n8n install, n8n-MCP bridge, Stage 2 v2 overnight run

**Remaining setup steps:**
1. Create Airtable Solusite Pipeline base (schema in AUTOMATION_SETUP.md)
2. Install n8n locally: `npm install -g n8n && n8n start`
3. Install n8n-MCP: clone `github.com/czlonkowski/n8n-mcp`, add to `~/.claude/mcp_settings.json`
4. Run Stage 2 v2 overnight (Playwright — `pip install playwright && python -m playwright install chromium`)
5. Build first n8n workflow (prompt provided in AUTOMATION_SETUP.md)

---

## HANDYMANDIRECT (CLIENT: VINCENT)

Active React/Supabase rebuild on Lovable.dev. Repo: `Spies-ang/handymandirectv2`. Phase 2 development underway and approved. Completed: Premium Services reorder, experience-tier colour coding, trade page architecture refactor (12 hardcoded → 1 dynamic via `seoData.ts`), Trades dropdown in nav, tier-specific booking flows, scrollable blog feed window. Pricing references removed from trade pages.

---

## TOOLS & RESOURCES

- **Build:** Lovable.dev (React + Supabase), GitHub (`Spies-ang` account)
- **Local dev:** Claude Code (Terminal), MacBook
- **Data / scraping:** Python (Google Places API, key `AIzaSyCr65TnL51BTJeZ6b-jfh9ernZdYQnRuAM`), Google Sheets (target `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`), OAuth via `client_secret.json`
- **Design / docs:** Canva MCP, ReportLab (Python PDF generation)
- **Day job stack:** Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server
- **Markets:** South Africa (Afrikaans and English)
- **Google Cloud trial:** $8.59 spent, $291 remaining, expires 2026-05-19

---

## CRITICAL TECHNICAL RULES

1. **Lovable RLS bug:** All Supabase RLS policies generate as RESTRICTIVE. After every prompt → Security → "Try to fix all (Free)"
2. **Always `.maybeSingle()` not `.single()`** — `.single()` throws on zero rows
3. **Address fields:** `GooglePlacesAutocomplete` restricted to `{ country: "za" }`
4. **Never commit API keys to public repos** — keep repos PRIVATE
5. **Prerender.io required** on every Lovable site before SEO matters
6. **Disable email confirmation** in Supabase during testing (4 emails/hour limit)
7. **Always add fallback `navigate()`** after role fetches
8. **GitHub edits preferred** over Lovable prompts for simple fixes (free, auto-deploys 60s)
9. **When Lovable prompt breaks something** → revert via version history (free), don't rebuild
10. **Long multi-change Lovable prompts break** — be surgical, single-section changes only
11. **Color swap prompts must explicitly say** "do not touch siteConfig.ts, do not regenerate sections"
12. **Git pushes need PAT in remote URL** if auth fails: `https://[user]:[token]@github.com/[org]/[repo].git`
13. **Exposed token to rotate:** `https://github.com/settings/tokens` (look for `ghp_skzIqq0...`) — manual browser step
14. **Lead-scraper remote URL already clean** (confirmed by Claude Code, no PAT embedded)

---

## MULTI-CHAT WORKFLOW

| Surface | Role | Has bash/git tools |
|---|---|---|
| Claude.ai browser — strategy chat | Strategy, research, prompts, handover updates | No |
| Claude.ai browser — recycling chat | Template recycling, lead selection, prompt writing | No |
| Claude.ai browser — HandymanDirect chat | Vincent's client work | No |
| Claude Code (Terminal) | All build/edit/deploy/git execution | Yes |
| Lovable chat panel | Per-project UI changes | Yes (Lovable-specific) |

Browser chats write prompts. Claude Code executes them. Don't paste browser-chat prompts into Claude Code Terminal or vice versa.

---

## PENDING / ON THE HORIZON

**Immediate (this weekend):**
- [ ] Complete Villa 442 recycling (strip Garden Point → insert Villa 442 → push → WhatsApp → call)
- [ ] Call back MEG Architects + Studentech (pending callbacks from yesterday)
- [ ] Follow up with Prana Love + Garden Point on next steps
- [ ] Run Stage 2 v2 Playwright overnight (Saturday night)
- [ ] Set up Airtable base
- [ ] Install n8n + n8n-MCP

**Short-term:**
- [ ] Revert La Belle hero (beauty-bloom-template) via Lovable version history
- [ ] Finish Riakona Electrical templating (5 files remaining — Services, Reviews, Contact, Index, SEOLandingPage)
- [ ] Assess legacy repos for recycling: 87 Events, GKN Plumbing, Bazil Handyman, Sagie's Plumbers, Thaba Meat Market
- [ ] Build 2 more archetype templates if needed: Food/Restaurant (separate from B&B), Trades refresh

**Medium-term:**
- [ ] Stage 1c social media presence scraper for Silverbrook Media
- [ ] Fix Stage 2 v1 scoring logic (no-website with fewer reviews should score higher)
- [ ] Begin batch outbound calling on the 11,120 leads
- [ ] Hire salespeople when conversion rate is validated at scale

---

## SILVERBROOK MEDIA (FIANCÉE'S BUSINESS)

Social media management. Higher-budget targets for social media pitch: hotels, event venues, tour operators, travel agencies, spas, restaurants, wedding photographers, real estate agents, interior designers, architects. Stage 1c scraper (social media presence check) deferred until Ian validates the website pitch through real calls.

---

## RECYCLING LESSONS — B&B Archetype (Villa 442, April 2026)

First full recycle of the B&B archetype (Garden Point → Villa 442). Identified three categories of issues that must be fixed in every archetype template before it's truly reusable:

### Issue 1: Hardcoded content outside siteConfig
Several components had business-specific strings hardcoded directly instead of reading from siteConfig:
- Home.tsx trust bar: "6 rooms", "Pet-friendly" — hardcoded from Garden Point
- Rooms.tsx hero: "Six rooms, one peaceful retreat" — hardcoded
- Location.tsx: "From Johannesburg CBD", "From Sandton" with Garden Point distances — hardcoded

**Fix applied:** Added `trustBar` (array), `roomsHeroTitle` (string), and `directions` (array of objects) to siteConfig. Components now map over these arrays. Every archetype template must be audited for hardcoded strings before it's marked as "template-ready".

### Issue 2: Empty fields rendering as blank UI elements
When siteConfig fields are empty strings (email, Instagram, Facebook), the Footer still rendered the link/icon with no content — creating visible blank spaces.

**Fix applied:** Wrapped email, Instagram, and Facebook in conditional renders: `{siteConfig.email && (...)}`. Rule going forward: every optional field in siteConfig must have conditional rendering in the component that displays it. If it's empty, it should not render at all.

### Issue 3: Images not transferable
Components imported local image files (e.g. `import heroImg from "@/assets/hero-garden.jpg"`). These break on every recycle because the files are specific to the original client.

**Fix applied:** Added an `images` object to siteConfig with URL strings (using Unsplash stock photos). Components now read image URLs from siteConfig instead of importing local files. Each room object also has an `image` field. When recycling, just swap the Unsplash URLs to match the new client's industry/vibe. Zero credits needed.

### Updated recycling checklist (B&B archetype)
1. Clone/remix the archetype repo
2. Replace ALL siteConfig.ts values with new client data
3. Replace image URLs in siteConfig.images with industry-appropriate Unsplash photos
4. Verify NO empty fields render as blank UI (check Footer especially)
5. Verify NO hardcoded strings from the previous client remain (grep for old business name)
6. Push to GitHub → Lovable auto-deploys
7. Paste surgical color-swap prompt in Lovable (1 cheap credit)
8. Send pre-call WhatsApp with preview link

### Archetype template status update
| Archetype | Template Repo | Status |
|---|---|---|
| Trades & Home Services | `roelfsautoelectrical` + `riakonaelectrical` | Roelf's complete, Riakona 80% |
| Beauty & Wellness | `beauty-bloom-template` | Initial done, needs audit |
| Events & Creative | `ross-images-studio` | Complete, template-ready |
| Hotels & Hospitality (B&B) | `remix-of-bnb-archetype` | **Template-ready after Villa 442 fixes** |
| Professional Services | MEG Architects | Built, needs templating |
| Education & Training | Studentech | Built, needs templating |
