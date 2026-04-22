# SOLUSITE — DECISIONS LOG

**Format:** YYYY-MM-DD — Decision (one line). [Source chat or context]
**Write rule:** Append-only. Never edit. Never delete. Most recent at the bottom.

---

## 2026 — FEBRUARY

**2026-02** — Founded lead-scraper concept. Target: well-performing businesses on Google with NO website, sectors that benefit most from having one. Chose service businesses over e-commerce due to Lovable's inventory limitations. [Web scraping businesses - Multi scraper]

**2026-02** — Chose Google Places API over direct scraping (against Google's ToS). 4+ stars / 5+ reviews / no website as V1 filter. [Web scraping businesses - Multi scraper]

**2026-02** — V1 scraper built and shipped. Accompanying ChatGPT prompt template written for Lovable prompt generation from scraped data. [Web scraping businesses - Multi scraper]

## 2026 — MARCH

**2026-03** — V1 LEARNING: Established businesses with no website and lots of reviews are the HARDEST to convert. Thriving word-of-mouth businesses don't feel the need for a site. "No website listed" ≠ "no website exists." Best converts had OLD/BAD/SHELL sites — they already understood web value. [Web scraping businesses - Multi scraper]

**2026-03** — DECISION: Pivot from V1 (no-website filter) to V2 (multi-stage gap-based scraper). Tier 1 HOT = FB-only / broken / redirects / new biz with 5-20 reviews. Tier 2 WARM = old / non-mobile / no-SSL / placeholder. Tier 3 COLD = established no-website (deprioritized). [Web scraping businesses - Multi scraper]

**2026-03** — Industry taxonomy: 67 service industries across 4 cities (Cape Town, Joburg, Durban, Pretoria), ranked CRITICAL / HIGH / MEDIUM / LOW by website necessity. [Web scraping businesses - Multi scraper]

**2026-03** — DECISION: Use Google Sheets export over CSV-only. OAuth (`client_secret.json`) instead of service account because Google blocked service account creation on Ian's project. [Web scraping businesses - Multi scraper]

**2026-03-26** — V2 3-module pipeline built: Stage 1 (broad capture) → Stage 2 (website checker) → Stage 3 (sheets export) + `run_all_stages.py` master. [Web scraping businesses - Multi scraper]

**2026-03-26** — LEARNING: First handover document written and used as bootstrap for new chat. This becomes the prototype for the HANDOVER.md system in `solusite-context`. [Web scraping businesses - Multi scraper → Handover - multi-scraper Opus 4.6]

**2026-03** — DECISION: "You don't need 67 templates. You need about 6." Consolidated industries into 6 archetypes: Trades & Home Services / Beauty & Wellness / Events & Creative / Food & Hospitality / Professional Services / Education & Training. [Recycling rejected client websites as templates]

**2026-03** — DECISION: Recycle rejected client sites as archetype templates rather than Lovable-building from scratch. siteConfig.ts pattern established on Roelf's Auto Electrical (11 files wired). Riakona Electrical 80% done on same pattern. [Recycling rejected client websites as templates]

**2026-03** — LEARNING: 13,000 raw leads in Stage 1 but Stage 2 scored all as priority 7 — bug. Root cause: Text Search API doesn't return `website`/`phone` fields. Fix: introduce Stage 1b enrichment via Place Details API. [Handover - multi-scraper Opus 4.6]

**2026-03** — DECISION: Scoring logic for no-website leads must be INVERTED from original — fewer reviews = higher priority, not lower. Applied to `quick_export.py` and `fix_scores.py`. Main script (`scraper_stage2_website_checker.py`) still has old logic — open item. [Handover - multi-scraper Opus 4.6]

**2026-03** — Google Cloud $300 trial clarified — actual budget constraint, not 10k/month. $291 remaining, expires 2026-05-19. [Handover - multi-scraper Opus 4.6]

**2026-03** — Homebrew + `gh` CLI installed. Permanent git auth. No more per-session PAT pasting. [Handover - multi-scraper Opus 4.6]

## 2026 — APRIL

**2026-04-08** — Ross Images Photography (Stefanie Ross) built as first wedding photographer. Template-ready siteConfig.ts. Becomes Archetype 3 (Events & Creative) base. [Handover - multi-scraper Opus 4.6]

**2026-04** — LEARNING: 5 consecutive sites built with generic green/cream/sage palettes. Ian flagged as template-blast appearance. [Solusite handover fixes and lead generation]

**2026-04** — RULE: Brand research first (Facebook cover, Instagram, logo). If nothing found, character-driven palette from personality observation. Archetype defaults are last resort only. Never reuse same default twice in a row. [Solusite handover fixes and lead generation]

**2026-04-11** — DECISION: Pricing anchor is R5,000 framed as "R8,500 introductory rate of R5,000." Retainer per archetype. Fallback split R2,500 upfront + R2,500 on completion within 1 week. Never lead with price. [Solusite handover fixes and lead generation]

**2026-04-11** — DECISION: Industry budget filter overrides website-gap tier. Deprioritize wellness/PT/physio/yoga/small spas (high need, low budget). Prioritize industries with clear per-customer revenue. [Solusite handover fixes and lead generation]

**2026-04-11** — RULE: Never mention Pretoria or geography in client-facing copy. Solusite is a capability, not a locality. [Solusite handover fixes and lead generation]

**2026-04-13** — DECISION: Hired junior salesman to handle CLOSING calls only, not outbound. Ian sends warm WhatsApp (trust anchor). Salesman's opening is suggested template, not script. [Solusite handover fixes and lead generation]

**2026-04-14** — The Villa 442 B&B recycle executed. Exposed three recycling failure modes: hardcoded content outside siteConfig, empty optional fields rendering as blank UI, local image imports breaking across recycles. All fixed via conditional rendering, Unsplash URLs in siteConfig, and missing config fields added. [Recycling rejected client websites as templates]

**2026-04-14** — LEARNING: HANDOVER.md URL bootstrap mechanism failed in production (404). New chat couldn't fetch the supposed single source of truth. [Recycling rejected client websites as templates]

**2026-04-15** — DECISION: Clean-archetype repo strategy over remixing client repos. Dedicated `archetype-*` repos with placeholder siteConfig values. Strip once, never strip again. 8 archetype repos planned. [Consolidating website scraper project context]

**2026-04** — DECISION: Automation stack architecture — Airtable (data) + n8n self-hosted (orchestration) + Claude Code (reasoning) + Vercel (hosting) + GitHub. WhatsApp stays manual. n8n end-state has 2 human handoff points per lead (batch review + WhatsApp send). [Consolidating website scraper project context]

**2026-04** — LEARNING: Nexia SAB&T false positive (national accounting firm with working main site, scraper caught a broken branch). Triggered mandatory web_search verification per lead. [Solusite handover fixes and lead generation]

**2026-04** — DECISION: Verify every lead with web_search before building. Scraper false-positive rate ~27% on modern JS-rendered sites. [Consolidating website scraper project context]

**2026-04** — LEARNING: Lovable "Try to fix" repopulates siteConfig team arrays with original template data. Check team/services/projects after every auto-fix. [Solusite handover fixes and lead generation]

**2026-04** — LEARNING: Practice page component on legacy-portfolio had hardcoded MEG team members — siteConfig.team was not the only source of truth. Affected all 5 architect/interior recycles. Now fixed on child sites; upstream fix still pending. [Solusite batch 2 deployment tasks]

**2026-04** — DECISION: Facebook activity check is pre-build hard gate. Origin: Prana Love (closing) and Dayyaans (defunct) both burned build time. [Solusite handover fixes and lead generation]

**2026-04-21** — DECISION: Business number transition. All future outbound from +27 66 269 8553. Personal number retired from business use. 13-message follow-up batch crafted for clients who saw the original pitch from personal number. [Consolidating website scraper project context]

**2026-04-21** — Solusite landing page built (solusite-media.lovable.app). Dark editorial aesthetic. Domain solusitemedia.co.za purchased on GoDaddy. WhatsApp Business catalog (5 items) live. Brand blue shifted from legacy #2B7BCC to #3B82F6. [Consolidating website scraper project context]

**2026-04-22** — DECISION: Dayyaan is a WARM REFERRER, not a lost lead. He closed his driving school but loves the site, asked for a neutral business card to send referrals. Follow through fast. [Consolidating website scraper project context]

**2026-04-22** — LEARNING: A new chat rejected leads in the 15-lead batch for not being based in Pretoria. This is a rule violation — geography is not a criterion. The "no Pretoria in copy" rule was conflated with a non-existent "leads must be in Pretoria" rule. Drift caused by rule fragments surviving across chats without full context. [Consolidating website scraper project context]

**2026-04-22** — DECISION: HANDOVER.md has itself become a drift vector. Replacing with 4-file system: RULES.md (non-negotiable, append-only) + STATE.md (current reality, overwritten) + DECISIONS.md (this file, append-only chronological) + CONTEXT.md (long-form onboarding). Plus `scripts/` folder consolidating all project automation. [Consolidating website scraper project context — successor chat]

**2026-04-22** — RULE: Documentation Protocol codified in RULES.md Section 1. Every chat bootstraps from RULES + STATE, confirms back before starting work, produces end-of-session update block autonomously. `solusite-context` made public (contains no secrets). [Consolidating website scraper project context — successor chat]

---

*Append new decisions here. Never edit existing entries.*
