# SOLUSITE MEDIA — HANDOVER DOCUMENT
**Last updated:** Saturday 12 April 2026 (afternoon)
**Bootstrap:** Paste this URL into any new Claude chat or Claude Code session:
`https://raw.githubusercontent.com/Spies-ang/solusite-context/main/HANDOVER.md`

---

## WHO

Ian Spies, Pretoria, South Africa. Runs **Solusite Media** (web dev + digital marketing) alongside a day job as Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server). Also runs Spies Construction and DFFRNT (athletic wear). Fiancée runs **Silverbrook Media** (social media management, shares pipeline infrastructure). Collaborator: **Markus** (lead handling). **NEW: hired a young salesman** to handle outbound sales calls — Ian builds and warms, salesman closes.

**Communication style:** Direct, concise, no preamble. Voice-to-text input. Only change what was asked. Never assume — ask. One consolidated answer beats three partial ones.

**Preferred name for Claude:** "Jarvis" — personal preference, not roleplay. Claude remains Claude with all standard capabilities.

---

## BUSINESS MODEL — TWO-STAGE SALES HANDOFF (NEW)

The flow as of 12 April 2026:

1. **Scrape & qualify** — Multi-stage Python scraper finds leads with website gaps
2. **Build** — Recycle the matching archetype template, customize siteConfig.ts for the lead, push to GitHub, Lovable auto-deploys
3. **Ian sends warm intro WhatsApp** — Personal hook + gap framing + live demo URL + "important to know" placeholder disclaimer + commits to a callback window. Stays in Ian's name to preserve the trust anchor ("a real person noticed me")
4. **Ian sends salesman briefing card** — Structured summary of the lead so the salesman can dial cold-but-prepared
5. **Salesman calls** — Opens with: "Hi, this is [name] from Solusite Media — Ian asked me to follow up on the website he sent you yesterday." This phrasing keeps Ian as the trust anchor and positions the salesman as a colleague
6. **Salesman closes the meeting**, not the deal — goal is a 30-45 min meeting where the client hands over real photos and details
7. **Convert** to paying client + monthly retainer

### Pricing
- Website build: R5,000–R12,000 once-off (varies by archetype — see below)
- Monthly retainer: R500–R900/month (varies by archetype)
- Blog add-on: R500/month for 2 SEO posts per site
- Payment plan available — handle in negotiation
- Never lead with price

| Archetype | Build | Retainer | Anchor |
|---|---|---|---|
| Events & Creative | R8,500–R12,000 | R900 | R10,000 |
| Hospitality (B&B, hotel) | R8,500–R12,000 | R900 | R10,000 |
| Professional Services | R8,500–R12,000 | R900 | R12,000 (premium) |
| Beauty & Wellness | R5,000–R7,500 | R700 | R6,500 |
| Food & Restaurants | R5,000–R6,500 | R700 | R5,500 |
| Health & Fitness | R5,000–R10,000 | R500–R800 | R7,500 |
| Education & Training | R3,500–R6,500 | R500–R600 | R5,000 |
| Trades | R5,000 | R700 | R5,000 |

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
4-5 bullet points on why Solusite specifically (local, demo-first, archetype-tuned, etc.)

WHAT THEY ALREADY KNOW (from Ian's WhatsApp)
What's been disclosed so the salesman doesn't repeat or contradict

PRICING (KEEP IN HEAD, DON'T LEAD WITH IT)
Anchor price + drop-to price + retainer + blog + payment plan note

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

### V2 Lead Priority
**TIER 1 HOT:** FACEBOOK_ONLY, BROKEN_WEBSITE, REDIRECTS_TO_FACEBOOK, new businesses (5-20 reviews)
**TIER 2 WARM:** OLD_OR_BAD_WEBSITE, non-mobile-responsive, no SSL, placeholders
**TIER 3 COLD:** Established no-website (50+ reviews) — V1 confirmed hardest sell

### Known Issues
- Stage 2 v1 false positives — flags React/Next.js as BROKEN. Fix: Stage 2 v2 (Playwright). Deferred until calls validate.
- Manual verification still required before building demos.

---

## ARCHETYPE TEMPLATES — CURRENT STATE

| # | Archetype | Template Repo | Live URL | Status |
|---|---|---|---|---|
| 1 | Events & Creative | `Spies-ang/ross-images-studio` | — | Template-ready. Stefanie Ross declined (V1 lesson). |
| 2 | Beauty & Wellness | `Spies-ang/prana-template-suite` | pranaloveyoga.lovable.app | **DECLINED** — closing the studio (Facebook update Ian saw later, scraper missed). |
| 3 | Food & Hospitality | `Spies-ang/garden-gateways` | gardenpointguesthouse.lovable.app | **INTERESTED** ✅ — needs salesman closing call. |
| 4 | Professional Services | `Spies-ang/legacy-portfolio` | megarchitects.lovable.app | **PENDING CALLBACK** — second attempt needed. |
| 5 | Education & Training | `Spies-ang/pass-prep-pro` | studentechdrivertraining.lovable.app | **PENDING CALLBACK** — second attempt needed. |
| 6 | Trades & Home Services | `roelfsautoelectrical` + `riakonaelectrical` | — | Roelf's done, Riakona 80% done (5 files remaining). |
| — | Beauty & Wellness (v1) | `Spies-ang/beauty-bloom-template-54d0c7e3` | — | La Belle. Hero design upgrade BROKE site. Needs revert via Lovable version history. |

### Active recycling — IN PROGRESS
- **Remix repo:** `Spies-ang/remix-of-bnb-archetype` (cloned from Garden Point template)
- **Target lead:** **The Villa 442**, 442 Salie St, Chantelle, Akasia, Pretoria 0182. Phone 064 546 8891. 4.9 stars, 11 reviews. BROKEN_WEBSITE — their "website" is literally a Booking.com share link (https://www.booking.com/Share-9NNlQY). Same commission-dependency pitch as Garden Point. Local to Ian.
- **Status:** Recycling chat is currently working on this. Both repos need to be temporarily public for the chat to access them.

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
- Hospitality with commission pain is the strongest converting archetype so far
- Always check the lead's recent Facebook activity before building (would have caught Prana Love closing)
- Two pending callbacks are not failures — second attempts standard

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

**Immediate (this weekend):**
- [ ] Complete Villa 442 recycling (currently in recycling chat)
- [ ] Generate Villa 442 WhatsApp + salesman briefing card (recycling chat job, must include both)
- [ ] Call back MEG Architects + Studentech (salesman job, briefing cards already written above)
- [ ] Salesman closes Garden Point Guest House (briefing card already written)
- [ ] Find and qualify next 3-5 leads for the salesman to keep momentum

**Short-term:**
- [ ] Run Stage 2 v2 Playwright overnight (Saturday or Sunday night)
- [ ] Set up Airtable base
- [ ] Install n8n + n8n-MCP
- [ ] Revert La Belle hero (beauty-bloom-template) via Lovable version history
- [ ] Finish Riakona Electrical templating (5 files remaining)

**Medium-term:**
- [ ] Build first n8n workflow (manual trigger → Airtable → Claude subagent → site generation → Airtable update)
- [ ] Stage 1c social media scraper for Silverbrook Media
- [ ] Fix Stage 2 v1 scoring logic
- [ ] Begin batch outbound on remaining 11,000+ leads

**Longer-term:**
- [ ] Hire 2nd salesman if conversion rate validates at scale
- [ ] Build templated archetype for: separate Restaurant (not B&B), Trades refresh, Health & Fitness
- [ ] Productize the offering: standard package, standard upsells, standard onboarding

---

## SILVERBROOK MEDIA (FIANCÉE'S BUSINESS)

Social media management. Higher-budget targets: hotels, event venues, tour operators, travel agencies, spas, restaurants, wedding photographers, real estate agents, interior designers, architects. Stage 1c scraper deferred until Solusite pitch validates through real calls.
