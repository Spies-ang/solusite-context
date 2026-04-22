# SOLUSITE — STATE

**Last updated:** 22 April 2026, evening
**Purpose:** Current reality only. No history. No plans. Overwritten every time state changes.
**Write rule:** End-of-session update blocks from chats, applied via Claude Code.

---

## CLIENTS IN FLIGHT

| Lead | Last action | Status | Next action | Blocker |
|---|---|---|---|---|
| Lat Wai (Wendy) | Pricing sent, she replied "will consider" | INTERESTED | Follow-up call scheduling | None |
| Lisa Rorich Architects | Fee structure sent via personal + business number follow-up | INTERESTED | Awaiting reply | None |
| MEG Architects (Tienie) | Afrikaans business-number follow-up sent | Pending callback | Wait for reply | None |
| Studentech (Vernon) | Business-number follow-up sent, "move to voice not text" framing | Pending callback | Book voice call when he replies | None |
| Dayyaan (closed business) | Committed to sending neutral business card | WARM REFERRER | **Design and send business card** | Open — overdue |
| +27 81 402 7483 | Most engaged, monthly-price objection on table | INTERESTED | Handle monthly-price objection | Open |
| Ndibali Interior Designs | First + business-number WhatsApps sent | Awaiting | Wait | None |
| Blue Sky Interior Design | First + business-number WhatsApps sent | Awaiting | Wait | None |
| CodeFlash Photography | First + business-number WhatsApps sent | Awaiting | Wait | None |
| Meintjes Catering | First + business-number WhatsApps sent | Awaiting | Wait | None |
| TJs Driving Academy | Business-number follow-up sent | Awaiting | Wait | None |
| Rightway Driving Academy | Business-number follow-up sent (disappearing messages on) | Awaiting | Wait | None |
| Skill on Wheels Academy | Business-number follow-up sent | Awaiting | Wait | None |
| Revo Driving School | First WhatsApp only (no business-number follow-up yet) | Awaiting | Send business-number follow-up | Open |
| MW Architects | First WhatsApp only (no business-number follow-up yet) | Awaiting | Send business-number follow-up | Open |
| Rono Architects | First WhatsApp only (no business-number follow-up yet) | Awaiting | Send business-number follow-up | Open |
| The Villa 442 (Hannah) | Business-number WhatsApp sent to correct owner number | Awaiting | Wait; if silent end of week, archive for recycling | None |

### Closed
- Garden Point Guest House — declined
- Prana Love Yoga — declined (closing)
- Stefanie Ross Photography — declined (fully booked)
- Dayyaans Driving School — declined (no longer in business, but kept as referrer above)

---

## CURRENT LEAD BATCH (22 April 2026)

15 pulled via `fetch_new_leads.py`. Ian selected 10 to build for. Verification pass identified 4-5 scraper false positives.

**Confirmed false positives (skip, working websites exist):**
- Bigfoot Car Detailing — `bigfootdetailing.co.za` live, Rupes SA subsidiary
- KayShots VisualZ — `kayshots.co` live + photography competitor
- Royal Decor & Turfs — `royaldecorandturfs.co.za` live
- Boulevard Storage — `boulevardstorage.co.za` live, Faircape subsidiary

**Still to verify (Ian checks before build):**
- Zeki Pups — VERIFIED, solo operator (Heather Edwards, COAPE DipCABT), 4 reviews, Tokai CT — split-payment pitch
- Skyscape Architects (Pretoria)
- Sheikh Motors (Pretoria) — VERIFIED thin footprint, Ian to drive past
- La-Mich Hair & Beauty Salon (Joburg)
- Plain Blue Wedding Photo & Film (Cape Town)
- OE Nails Beauty Salon (Pretoria) — Ian to check Facebook for proper-salon vs home-operator
- Nijhuis Attorneys (Joburg)
- Sky Travel ZA (Joburg)
- Silverline Accounting / Sal-Tax (Pretoria) — Nexia-style false-positive risk, check for separate working main site

**Note on this batch:** One prior chat rejected leads for not being based in Pretoria. This is a rule violation (see RULES.md §2.1). Re-verify the full list against the correct criteria, not geography.

---

## ARCHETYPES

| # | Archetype | Repo | Live demo | Hardened? | Notes |
|---|---|---|---|---|---|
| 1 | Education & Training | `pass-prep-pro` | studentechdrivertraining.lovable.app | ✅ | Commit `077d8a8` |
| 2 | Hospitality | `garden-gateways` | gardenpointguesthouse.lovable.app | ⚠️ | Location.tsx per-repo fix needed |
| 3 | Professional / Portfolio | `legacy-portfolio` | megarchitects.lovable.app | ⚠️ | Child sites fixed; upstream fix pending |
| 4 | Photography | `ross-images-studio` | — | ❌ | Missing fields |
| 5 | Beauty & Wellness | `prana-template-suite` | pranaloveyoga.lovable.app | — | — |
| 6 | Trades | `roelfsautoelectrical` + `riakonaelectrical` | — | — | Roelf done, Riakona 80% |
| — | Beauty v1 | `beauty-bloom-template-54d0c7e3` | — | — | La Belle hero broken, needs Lovable revert |

### Clean-archetype repos (none built yet)
Target order: professional-portfolio → catering → photography-studio → event-venue → driving-school → interior-design → accounting → restaurant.

---

## INFRASTRUCTURE

**Solusite landing page:** solusite-media.lovable.app. Domain solusitemedia.co.za on GoDaddy, propagating. Latest Lovable fix prompt sent (hero headline visibility, footer overlap, phone number update, Ndibali→Blue Sky swap). Verify on next deploy.

**WhatsApp Business:** Active on +27 66 269 8553. Catalog live with 5 items.

**Scraper:** V2 live in production. `fetch_new_leads.py` operational. Stage 2 v2 Playwright rewrite saved, not yet run.

**Lead sheet:** Google Sheets ID `1yOjcFLNigV2Rg6PD5Ql5sDMQCOgY5_r0WPmZAJNLHeI`. 11,120+ qualified leads across 67 industry tabs.

---

## OPEN BLOCKERS / OVERDUE

1. **Dayyaan's neutral business card** — committed "this week," still not designed. He is a warm referrer.
2. **Stage 2 scoring fix not applied to main script** (`scraper_stage2_website_checker.py`). Open since late March.
3. **Practice-page fix not upstreamed** to `legacy-portfolio`. Child sites are clean but next recycle inherits the bug.
4. **`strip_archetype.py`** sits in `~/Downloads/`, needs to move to `~/Documents/solusite-context/scripts/`.
5. **Exposed GitHub token** `ghp_skzIqq0...` still not rotated.
6. **Stage 2 v2 Playwright** never run — every batch continues to pay the 27% false-positive tax.
7. **Solusite landing page headline visibility bug** — fix prompt sent to Lovable, not yet verified on deploy.

---

## NEXT BATCH PULL (when current batch is processed)

Use correct criteria per RULES.md §2.3–2.5. Expect to drop ~25–30% as scraper false positives. Mark processed leads as Sent/Closed in the Sheet so they're excluded from subsequent pulls.

---

*STATE is truth-as-of-now. If this file is longer than ~150 lines, it has accumulated non-state content and needs trimming.*
