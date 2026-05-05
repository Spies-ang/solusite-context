# SOLUSITE — STATE

**Last updated:** 29 April 2026
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
- Sky Travel ZA — declined, not interested (2026-04-29)
- Florida Palms Guesthouse — confirmed false positive, site already live, no further action (2026-04-29)

---

## CURRENT LEAD BATCH (28–29 April 2026)

12 leads across two batches (7 Ian-built + 5 Armand-built). All sites built and deployed. Outreach sent or scheduled as of 2026-04-29.

**Confirmed false positives (closed):**
- Bigfoot Car Detailing — `bigfootdetailing.co.za` live, Rupes SA subsidiary
- KayShots VisualZ — `kayshots.co` live + photography competitor
- Boulevard Storage — `boulevardstorage.co.za` live, Faircape subsidiary
- Florida Palms Guesthouse — `floridapalms.co.za` live at time of outreach. Demo built unnecessarily. CLOSED.

**Closed — not interested:**
- Sky Travel ZA — declined, not interested.

**WhatsApp sent — awaiting reply (mobile numbers confirmed):**
- La-Mich Hair & Beauty Salon — 082 442 0014. Demo: la-mich-salon.lovable.app
- OE Nails Beauty Salon — 067 034 7218. Demo: oe-nails-beauty-salon.lovable.app
- Royal Decor & Turfs — 079 501 1362. Demo: royaldecorturfs.lovable.app
- The Comb Club — 061 006 8106. Demo: thecombclub.lovable.app
- Italian Panelbeaters — 011 615 9552. Demo: italianpanelbeaters.lovable.app

**Landline only — phone call required (no WhatsApp possible):**
- Skyscape Architects — 012 346 8937. Demo: skyscape-blueprint.lovable.app
- Nijhuis Attorneys — 010 630 0333. Demo: nijhuis-attorneys.lovable.app
- Silverline Accounting / Sal-Tax — 012 543 3736. Demo: silverline-accounting.lovable.app
- Cape Town Dental — 021 023 3950. Demo: capetowndental.lovable.app
- Bayvet CC — 011 492 3477. Demo: bayvetcc.lovable.app

**Deprioritised (not skipped):**
- Sheikh Motors — bottom of queue. Build pending Trades archetype completion.

**Still to verify / on hold:**
- Zeki Pups — VERIFIED, solo operator (Heather Edwards, COAPE DipCABT), 4 reviews, Tokai CT — split-payment pitch. Not in current build queue.
- Plain Blue Wedding Photo & Film (Cape Town) — not yet verified.

---

## ARCHETYPES

| # | Archetype | Repo | Live demo | Hardened? | Notes |
|---|---|---|---|---|---|
| 1 | Education & Training | `pass-prep-pro` | studentechdrivertraining.lovable.app | ✅ | Commit `077d8a8` |
| 2 | Hospitality | `garden-gateways` | gardenpointguesthouse.lovable.app | ⚠️ | Location.tsx per-repo fix needed |
| 3 | Professional / Portfolio | `legacy-portfolio` | megarchitects.lovable.app | ⚠️ | Child sites fixed; upstream fix pending. Recycle prompts for Skyscape/Nijhuis/Silverline pre-fill all arrays as workaround. |
| 4 | Photography | `ross-images-studio` | — | ❌ | Missing fields |
| 5 | Beauty & Wellness | `prana-template-suite` | pranaloveyoga.lovable.app | — | — |
| 6 | Trades | `roelfsautoelectrical` + `riakonaelectrical` | — | — | Roelf done, Riakona 80% |
| 7 | Outdoor Transformation / Landscaping | TBD — post Royal Decor build | — | — | Seeded by Royal Decor & Turfs build. Repo to be created after build completes. |
| — | Beauty v1 | `beauty-bloom-template-54d0c7e3` | — | — | La Belle hero broken, needs Lovable revert |

### Clean archetype repos (created 2026-04-23)

| Archetype repo | Source | Status | Manual fixes remaining |
|---|---|---|---|
| `archetype-professional-services` | legacy-portfolio | Stripped ⚠️ | 8 local image imports; services/testimonials/emails arrays; verify Practice.tsx team array |
| `archetype-beauty-wellness` | prana-template-suite | Stripped ⚠️ | 6 local image imports; testimonials array |
| `archetype-hospitality` | garden-gateways | Stripped ⚠️ | 12 local image imports; testimonials/rooms arrays |
| `archetype-education-training` | pass-prep-pro | Stripped ⚠️ | 2 local image imports; packages/testimonials/faqs arrays. Note: .env removed, consider rotating Supabase anon key |
| `archetype-photography` | ross-images-studio | **Clean** ✅ | services/packages/testimonials arrays only — no local images |

All repos: MANUAL_FIXES.md and SCAN_REPORT.md committed. Next step per archetype: replace local image imports with Unsplash URLs in siteConfig.images, clear complex arrays to placeholder entries, link Lovable project.

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
8. **Landline-only leads in current batch have no email addresses found yet** — Skyscape, Nijhuis, Silverline, Cape Town Dental, Bayvet CC. Per §2.10, email must be found before qualifying. Phone call outreach is blocked until email is in hand or explicitly waived.

---

## NEXT BATCH PULL (when current batch is processed)

Use correct criteria per RULES.md §2.3–2.5. Expect to drop ~25–30% as scraper false positives. Mark processed leads as Sent/Closed in the Sheet so they're excluded from subsequent pulls.

---

*STATE is truth-as-of-now. If this file is longer than ~150 lines, it has accumulated non-state content and needs trimming.*
