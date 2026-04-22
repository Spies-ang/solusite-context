# SOLUSITE — CONTEXT

**Purpose:** Long-form onboarding. Why the project works the way it does. Read once per new chat if reasoning about strategy or learning the project. Does not contain current state or rules — those live in STATE.md and RULES.md.

**Write rule:** Updated rarely (quarterly review or after a major pivot). Not a session log.

---

## WHO

Ian Spies, Pretoria, South Africa. Runs **Solusite Media** alongside a day job as Data Engineer at Belgotex (Microsoft Fabric, Azure Data Factory, D365 F&O, SQL Server). Also operates Spies Construction (separate business) and DFFRNT (athletic wear brand).

Collaborators in the Solusite orbit:
- **Fiancée** — runs Silverbrook Media (social media management); shares pipeline infrastructure but separate business
- **Markus** — lead handling colleague
- **Junior salesman** (hired April 2026) — handles closing calls after Ian's warm WhatsApp intro

Ian addresses Claude as "Jarvis" — personal preference, not roleplay. Working style is direct, voice-to-text, no preamble, no assumptions, ask first, only change what was asked.

---

## WHAT SOLUSITE DOES

Solusite builds websites for local South African service businesses. The core model is demo-first selling:

1. Scrape leads with Python (Google Places API across 67 industries × 4 cities)
2. Qualify by website gap, rating, review count, industry budget capacity, and web-search verification
3. Build a pre-populated demo site using a matching archetype template
4. Ian sends warm WhatsApp with the live demo link + placeholder disclaimer + callback window
5. Salesman calls to book a meeting (not close on the call)
6. Meeting captures real photos and details; convert to paying client + monthly retainer

The premise is that seeing a nearly-complete site removes the imagination gap that kills every "would you like me to build you a website" pitch.

---

## THE V1 → V2 EVOLUTION (WHY THE CURRENT CRITERIA EXIST)

**V1 (Feb–March 2026).** Filter: businesses with 4+ stars, 5+ reviews, no website listed on Google. Ran successfully. Converted poorly.

**Why V1 failed.** Three learnings from real calls:

1. Businesses thriving on word-of-mouth without a website DON'T FEEL THE NEED. Pitching them is "change what already works" — uphill.
2. "No website listed" ≠ "no website exists." Many had sites, just hadn't added them to Google Business Profile. V1 filtered them out.
3. The actual paying clients had OLD / BAD / SHELL sites — they already understood web value and were frustrated with what they had. "Upgrade" is a much easier pitch than "convince from scratch."

**V2 (March 2026–present).** Multi-stage scraper that captures broadly and qualifies by WEBSITE GAP rather than website absence.

- Tier 1 HOT: Facebook-only, broken, unreachable, redirects-to-Facebook, new businesses (5-20 reviews)
- Tier 2 WARM: old/bad websites, non-mobile, no SSL, placeholder shells
- Tier 3 COLD: established no-website (50+ reviews) — deprioritized, V1 confirmed hardest sell

This is settled logic. RULES.md §2.8 enforces it. A chat proposing to re-target established no-website businesses is drifting.

---

## THE 67 → 6 ARCHETYPE CONSOLIDATION

The original scraper targets 67 industries. That sounds like 67 different site templates. It isn't.

A plumber's site and a handyman's site are essentially the same layout with different service names. Grouped by structural similarity, the 67 industries collapse into 6 archetypes:

1. **Trades & Home Services** — plumbers, electricians, handymen, carpenters, painters, roofers, HVAC, cleaning, pest control, landscaping, pool, moving, security, appliance repair
2. **Beauty & Wellness** — beauty salons, hair, nails, barbers, spas, PTs, physios, chiros, yoga, fitness, dentists, vets
3. **Events & Creative** — wedding photographers, photography studios, event venues, wedding planners, catering
4. **Food & Hospitality** — restaurants, hotels, B&Bs, tour operators, travel agencies
5. **Professional Services** — accounting, legal, insurance, real estate, architects, interior designers, marketing agencies, web/graphic designers
6. **Education & Training** — tutoring, driving schools, music schools, language schools

Each archetype has a template repo. A new client in that industry is a recycle of the archetype, not a fresh build. Recycling uses the `siteConfig.ts` pattern — all client-specific content in one file that components read from. Recycling happens via GitHub push, which Lovable auto-deploys in ~60 seconds. Zero Lovable credits consumed for a standard recycle.

**Clean-archetype repo strategy (decided April 2026).** Stop remixing actual client repos, which always inherit leftover client content that has to be stripped. Instead, build dedicated `archetype-*` repos with placeholder siteConfig values. Strip once. Every future recycle clones from clean.

---

## PRICING LOGIC

**R5,000 anchor, framed as "R8,500 introductory rate of R5,000."** This does three things: sets a higher anchor in the client's mind, positions the actual price as a favor, and creates FOMO on the introductory framing.

**Fallback: R2,500 upfront + R2,500 on completion within 1 week.** Offered ONLY if price is the blocker. Splits the risk, shortens the completion commitment.

**Retainer R500–R900/month by archetype.** Higher-revenue industries (hospitality, professional services, events) pay R900. Lower-margin (health/fitness, education) pay R500–R800. Trades and Beauty sit in the middle at R700.

**Blog add-on R500/month for 2 SEO posts.**

Never lead with price. Price is the answer to a question the client has to ask — if you surface it unprompted, it becomes the first thing they weigh instead of the site itself.

---

## THE SALES HANDOFF (WHY IAN WARMS AND SALESMAN CLOSES)

Originally Ian did everything. The handoff structure emerged because:

1. Ian's strength is the build + the personal WhatsApp. "A real person noticed me" is the trust anchor that makes the pitch land.
2. Salesman's job is the follow-through: calling, handling objections, booking the meeting.
3. The WhatsApp stays in Ian's name even after the salesman takes over — otherwise the trust anchor breaks.
4. Salesman's call goal is a meeting, not a deal. The meeting is where real photos, real prices, real details get captured. That's the actual conversion event.

Salesman's suggested opening template: *"Hi, this is [name] from Solusite Media — Ian asked me to follow up on the website he sent you yesterday."* That phrasing preserves Ian as the trust anchor and positions the salesman as a colleague, not a cold caller.

---

## THE PRETORIA RULE (AND HOW IT GETS MISREAD)

**The rule is about copy, not geography.** Solusite's demo sites, WhatsApp messages, and salesman scripts never mention Pretoria, never say "we're a local Pretoria agency," never geographically frame the service. Reason: Solusite pitches as a capability. A client in Cape Town doesn't want to hear that they're being serviced from Pretoria — it can read as either irrelevant or subtly suspicious.

**Leads themselves come from all 4 cities.** The scraper pulls Cape Town, Johannesburg, Durban, and Pretoria. Rejecting a lead because they're not in Pretoria is a rule violation. This has happened multiple times across chats and is the classic drift failure — a rule fragment surviving without its original context.

RULES.md §2.1 and §3.2 are the authoritative versions of both halves of this rule.

---

## WHY DOCUMENTS DRIFT (AND WHY WE SPLIT THE HANDOVER)

The project's original single-file HANDOVER.md tried to capture everything: current state, pending work, learnings, rules, history, technical notes, pricing, design system, automation plans. Every new chat was supposed to read it at startup and begin work caught up.

It failed in three ways:

1. **Every chat rewrote the whole doc**, introducing small factual errors that compounded over time. By mid-April 2026, the doc contained stale claims (e.g., "Batch 2 WhatsApps not yet sent" — long after they had been sent and re-sent from the business number).
2. **Chats couldn't reliably tell what was urgent** because the "Pending" section mixed today's blockers with long-term plans in the same bullet list.
3. **Rules-as-paragraphs didn't enforce themselves.** The "no Pretoria in copy" rule sat alongside geographic references to Ian being Pretoria-based. New chats mis-parsed and generated bad output.

The 4-file system (RULES + STATE + DECISIONS + CONTEXT) separates concerns by write rule:
- RULES is append-only and only Ian writes it. Rules can't accidentally get deleted.
- STATE is overwritten and only contains reality. It can't accumulate history.
- DECISIONS is append-only chronological. You can read the project's evolution without parsing a rewritten summary.
- CONTEXT is rarely updated. It's the book.

Plus `scripts/` consolidates all automation so a chat working on the pipeline knows where to find every piece of tooling.

---

## THE AUTOMATION END-STATE

**Current (April 2026): Manual with per-lead chat overhead.** Each lead takes ~30 min of chat time for qualification, research, siteConfig, WhatsApp, briefing card. Doesn't scale past ~50-100 leads/week.

**Target: n8n-orchestrated with 2 human touch points per lead.**

| Step | Owner in end-state | How |
|---|---|---|
| Scrape | Python (existing) | Cron |
| Pull next batch | n8n cron | Reads Airtable |
| Research each lead | Claude subagent called by n8n | Web + image search |
| Qualify | Claude subagent | Applies RULES.md §2 programmatically |
| Remix archetype → new repo | n8n + `gh` CLI | `gh repo create` from archetype template |
| Fill siteConfig.ts | Claude subagent | Writes to new repo |
| Push | n8n + git | Lovable auto-deploys |
| Generate WhatsApp + briefing card | Claude subagent | Writes back to Airtable |
| Review batch | **Ian** | Airtable view |
| Send WhatsApp | **Ian** | WhatsApp app |
| Call | Salesman | Phone |

WhatsApp stays manual by choice. Everything else is automated.

**Architecture decided:** Airtable (data) + n8n self-hosted (orchestration) + Claude Code (reasoning) + Vercel (hosting) + GitHub (code).

**Why n8n will solve the chat-to-chat drift problem:** per-lead work moves out of chats and into a subagent driven by Airtable state. Airtable doesn't forget. Browser chats become strategy/debugging tools only, not production-line tools. The handover problem disappears at the per-lead layer.

---

## CRITICAL TECHNICAL LEARNINGS

- **Lovable RLS bug.** All Supabase RLS policies generate as RESTRICTIVE. Must be PERMISSIVE. After every Lovable prompt, open Security tab → "Try to fix all (Free)". Free, takes seconds, has to be done every time.
- **Lovable auto-fix overwrites siteConfig arrays.** team, services, projects. Check after any "Try to fix" run.
- **Long multi-change Lovable prompts break.** Be surgical. Single-section changes only. Color swap prompts must explicitly forbid touching siteConfig.
- **Bad Lovable result → version history first.** Never rebuild what can be reverted. Never waste credits.
- **GitHub edits auto-deploy to Lovable in 60s.** Use for simple fixes. Reserve Lovable prompts for structural changes.
- **Browser chats can't read private repos.** The `solusite-context` repo is public by design; every other business repo needs Claude Code or a temporary public toggle.

---

## TOOLS

**Build:** Lovable.dev (React + Supabase), GitHub `Spies-ang` (private repos except `solusite-context`)
**Local dev:** Claude Code (Terminal), MacBook
**Data / scraping:** Python 3.9+, Google Places API, Google Sheets (OAuth via `client_secret.json`)
**Design / docs:** Canva MCP (Solusite diamond logo: asset ID `MAE4eMe-2NE`), ReportLab
**Markets:** South Africa (Afrikaans + English)

**Scripts live in** `~/Documents/solusite-context/scripts/` (target). Currently scattered across `~/Documents/lead-scraper/`, `~/Downloads/`, and various repos. Consolidation pending.

---

*End of CONTEXT.md. If you're a new chat reading this for the first time, the next file to read is RULES.md — the non-negotiables. STATE.md tells you what's true right now.*
