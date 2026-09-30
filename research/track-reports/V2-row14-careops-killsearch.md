# V2 — Row 14 Kill-Search: Home-Care Back-Office Agent Layer (Care Ops)

**Task:** V2 (Verification Agent) — targeted kill-searches against gap-registry Row 14, "Home-care back-office agent layer" (read-only overlay on AlayaCare/AxisCare that ingests EVV/visit/schedule data and drafts EVV-exception fixes + billing-ready notes for one-person approval). Deliver a firm verdict: OPEN / BEING-CLOSED / CLOSED, plus the technical-feasibility (API) gate. Run date 2026-09-30.

**Method:** z-ai `web_search` CLI (10-result pages), staggered 240s behind sibling V1, `sleep 15–30` between queries; junk/empty → one rephrased b-retry; 429 → retry once; hard-fail twice → move on and note it. Raw JSON saved incrementally to `research/raw-search-results/v2/` (immutable, never edited). Report skeleton written BEFORE searching and filled at hard stop. Priority order per work order: API depth (AlayaCare → AxisCare) → competitive gap → EVV-exception → billing automation → BPO/VA rates → WellSky → registry follow-ups.

**Evidence window:** search snapshot 2026-09-30; sources 2024–2026 preferred, older flagged.
**Search count:** **17 web_search invocations / 10 files saved / 7 hard-429 failures** (q01b ×2, q04b ×2, q07, q07b, q09 — the recurring serper-400-wrapped-in-429 degradation documented since R7). Usable sets: **q02, q03, q06 (full); q01 (partial — one gem amid generic noise)**. Junk sets: q04 (1 junk result), q05, q05b, q09b, q10, q10b (the documented OSRS-Scribd / JBoss-dictionary artifact classes). Hard stop on new searches at ~minute 12–14 of the search window; the ~14-call budget was consumed (17 invocations incl. retries) — extras (AlayaCare marketplace integrations, EVV-exception workflow cost, AxisCare reviews) never ran.

---

## Verdict summary table

| # | Question | Prior status (R9/R13b) | Fresh evidence (this run) | Verdict |
|---|----------|------------------------|---------------------------|---------|
| a | AlayaCare API depth (EVV/visits/schedules/notes/clients endpoints) | "Restful APIs" (crozdesk, one line) | No AlayaCare developer docs surfaced; q01b (API Report Card phrasing) 429'd twice. Indirect: AlayaCare hiring developers in Montreal (ca.indeed.com job posting). **No new endpoint-level evidence** | **STILL-UNVERIFIED at endpoint level** (API existence stands on R13b's crozdesk line) |
| b | AxisCare API depth | Public docs, admin token (crm.coach) | **Vendor's own docs subdomain: "AxisCare's API is available for customers who want to build custom functionality by connecting external systems to AxisCare" (static.axiscare.com)**; Celigo iPaaS connector with Admin > API token flow (docs.celigo.com, Sep 25 2025); a live third-party integration "import caregiver records" from AxisCare (support.patientrewardshub.com, Sep 3 2026) | **CONFIRMED-OPEN (strengthened)** — customer API, token flow, production read-integration on caregiver records |
| c | WellSky Personal Care API | "extensive public API documentation" (single source) | Both queries 429'd (q07, q07b) — no new evidence | **STILL-UNVERIFIED** (quota-blocked) |
| d | Funded AI back-office overlay on incumbent platforms | None found (R9) | **AxisCare itself announces "the latest AI innovations coming to AxisCare in 2026, including new automation, scheduling intelligence and workflow enhancements" (axiscare.com, Jun 15 2026)**; **sagecare.ai sells AI intake software for home care — "cut post-call admin from 30 minutes to under 5" (sagecare.ai, Mar 25 2026)**; CareSmartz360 markets "AI-powered home care software" for "field and back-office teams" (caresmartz360.com, Apr 3 2026); HCHB AI tools (hchb.com, Sep 30 2025); "agentic AI" arriving in care-coordination platforms (neonhealth.com, Mar 4 2026) | **No solver for the core wedge (EVV-exception fixes + billing-ready notes overlay), but the gap is narrowing at the edges — incumbent absorption has STARTED on AxisCare** |
| e | Standalone EVV-exception management solver | UNVERIFIED | q04 returned 1 junk result; both q04b rephrase attempts 429'd. Adjacent: Sandata's EVV REST API "serves states and EVV vendors under contract, not a public program" (supergood.ai, API Report Card — Sandata graded F) | **STILL-UNVERIFIED** (3rd consecutive run where EVV-exception queries fail on service degradation) |
| f | Home-care billing automation (AI) | Content-only signal | q05 junk (gist/OSRS), q05b junk (Nokia-audit/city-gov noise) | **STILL-UNVERIFIED** (quota/junk-blocked) |
| g | BPO/VA market alive? $/hr rates | staffingly.com etc., no pricing | **AlayaCare VA compensation "$700 – $1,000 USD per month" (onlinejobs.ph, Mar 7 2026 — Philippines outsourcing job posting)** — the human workaround is priced and active | **CONFIRMED + PRICED** (single-source posting; consistent with R9's BPO findings) |
| h | Family-communication layer (registry follow-up) | STILL-UNVERIFIED ×2 runs | q09 429'd; q09b returned 6 junk results (rfp.wiki membership software, city-gov noise) | **STILL-UNVERIFIED ×3 runs** (5+ failed query attempts total — phrasing family structurally unanswerable against this search service) |
| i | Caregiver documentation time per visit (registry follow-up) | STILL-UNVERIFIED ×2 runs, no stat | q10 returned the OSRS-Scribd artifact; q10b returned the JBoss-dictionary artifact | **STILL-UNVERIFIED ×3 runs** (6+ failed attempts total — no stat asserted, none invented) |

---

## 1. API feasibility — AlayaCare (q01)

**Claim under test (R13b §4):** AlayaCare "offers Restful APIs" (crozdesk Q&A) — endpoint depth (EVV, visits, schedules, notes, clients) never verified.

**Fresh evidence (q01):** the query "AlayaCare API documentation endpoints" returned 8 mostly-generic results. The one load-bearing hit is adjacent rather than direct: **supergood.ai's "API Report Card" — "Sandata grades F on The API Report Card. A real-time EVV REST API exists, but it serves states and EVV vendors under contract, not a public program."** This confirms supergood.ai grades home-care/EVV platform APIs (the same source R13b used to close Axxess) and newly closes **Sandata** as an overlay target: its EVV API serves states and EVV vendors under contract, not agencies or third parties. Also: a Pennsylvania state interface spec for "the Sandata Real Time Interface" (pa.gov, Dec 20 2016 — pre-2024, flagged) confirms Sandata's interface world is state-contract-shaped. For AlayaCare itself, only an indirect hiring signal landed ("AlayaCare Greater Montreal Area, QC Mentor developers… endpoint or a Python data pipeline" — ca.indeed.com job posting, undated). The dedicated rephrase (q01b, "API Report Card AlayaCare AxisCare WellSky home care API grade") hard-failed on 429 twice.

**Verdict: STILL-UNVERIFIED at endpoint level.** AlayaCare's API *existence* stands on R13b's crozdesk line ("offers Restful APIs") plus the BPO ecosystem operating inside it (R9); this run added no endpoint inventory. Next-pass query: `AlayaCare developer portal API reference visits EVV` or a direct read of AlayaCare's developer docs (the API Report Card source, supergood.ai, likely holds a grade — its Axxess and Sandata pages are proven).

## 2. API feasibility — AxisCare (q02)

**Fresh evidence (q02):**
- **Vendor's own domain:** "AxisCare's API is available for customers who want to build custom functionality by connecting external systems to AxisCare" (static.axiscare.com — AxisCare's docs/assets subdomain; the de-facto official API page).
- **Integration-platform confirmation:** Celigo (iPaaS) ships an AxisCare connector; auth = "Sign in to your AxisCare account → Admin > API token > Create new token → Copy the API token" (docs.celigo.com, Sep 25 2025).
- **Production proof:** a third-party product's support guide for "setting up your AxisCare integration… seamlessly import caregiver records" (support.patientrewardshub.com, Sep 3 2026) — a live, dated, non-AI integration already reading caregiver records out of AxisCare agencies.
- AxisCare maintains an integrations marketplace ("integrates with top companies in the home care industry," axiscare.com).
- Noise flagged: developer.axis.com is Axis Communications (cameras), not AxisCare.

**Verdict: CONFIRMED — the strongest API leg in the registry row's evidence base.** Customer-available API (vendor-confirmed), documented token flow, and a production read-integration on caregiver records as of Sep 2026. Endpoint-level inventory (EVV/visits/schedules specifically) still not itemized in public snippets, but the gate for a read-only overlay on core agency records is proven by an existing third party doing exactly that.

## 3. API feasibility — WellSky Personal Care (q07)

Both phrasings ("WellSky Personal Care API integration", "WellSky Personal Care API documentation") hard-failed on 429. The only evidence remains R13b's single-source claim ("extensive public API documentation," homecaregroup.com). **Verdict: STILL-UNVERIFIED (quota-blocked).** Next-pass query: `WellSky Personal Care API developer documentation ClearCare`.

## 4. Competitive gap — funded AI back-office overlay on AlayaCare/AxisCare/WellSky (q03, q05)

**Fresh evidence (q03 — the run's most important landing):**
- **AxisCare (incumbent) is shipping AI itself:** "Discover the latest AI innovations coming to AxisCare in 2026, including new automation, scheduling intelligence and workflow enhancements" (axiscare.com, Jun 15 2026). This is a dated, vendor-authored absorption signal on the very platform R13b named as a first-ship target.
- **A standalone single-workflow AI overlay exists:** "AI intake software for home care can cut post-call admin from 30 minutes to under 5. See what it does, what it costs, and how to evaluate it" (sagecare.ai, Mar 25 2026 — vendor content page; product depth/funding unverified, single-source). Intake ≠ EVV-exceptions/billing, but it proves the overlay shape (AI on top of the agency back office) is being productized.
- **Incumbent AI marketing everywhere:** CareSmartz360 "a leading AI-powered home care software… mobile-first design helps keep both field and back-office teams connected in real [time]" (caresmartz360.com, Apr 3 2026); HCHB "AI tools that enhance data visibility and automate workflows" (hchb.com, Sep 30 2025 — skilled home health side); "agentic AI" listed as an evaluation criterion for care-coordination platforms (neonhealth.com, Mar 4 2026 — the horizontal wave R9 predicted is arriving).
- Billing-automation-specific queries (q05 "home care billing automation AI agency"; q05b rephrase) returned pure junk both times — no dedicated billing-AI solver surfaced, but the search failed rather than returned absence.

**Verdict: the core wedge (EVV-exception fixes + billing-ready notes, read-only overlay, one-person approval) remains UNSOLVED in evidence — but the gap is no longer edge-empty.** Three closing forces are now visible: (1) AxisCare's own 2026 AI roadmap (automation + scheduling intelligence + workflow enhancements), (2) sagecare.ai's intake overlay occupying an adjacent back-office workflow, (3) AI-marketing saturation across incumbents (CareSmartz360, HCHB, Axxess Care 2.0 per R9). None of these, as evidenced, drafts EVV-exception fixes or billing-ready notes on a third-party platform. The absorption clock has started, primarily on AxisCare.

## 5. EVV exception management — standalone solver? (q04)

q04 ("EVV exception management software") returned a single junk result (aquarius.riversideca.gov). Both q04b rephrases ("electronic visit verification exception handling workflow home care agency software"; "EVV exception management home care software tool") hard-failed on 429. Adjacent evidence: supergood.ai's API Report Card shows Sandata's real-time EVV REST API "serves states and EVV vendors under contract, not a public program" — i.e., EVV *data access* itself is platform-gated, which both constrains overlay targets (Sandata out) and explains why a standalone EVV-exception solver hasn't formed around it.

**Verdict: STILL-UNVERIFIED — third consecutive run in which EVV-exception-specific queries fail (R9 q10 lost to 429; R13b never reached it; V2 junk + double-429).** No solver surfaced; no absence claimed beyond evidence. Next-pass query: `EVV visit note correction software agency payroll mismatch` (phrasings avoiding "exception management" — a term that attracts noise).

## 6. Home-care billing automation (q05)

Both attempts junk (q05: gist.github.com domain-prefix list + OSRS-Scribd; q05b: Nokia strategic audit, city-gov pages, 1995 radio-licensing archive — the documented degradation classes). **Verdict: STILL-UNVERIFIED (quota/junk-blocked).** Adjacent coverage via q03 (sagecare.ai intake; CareSmartz360 AI; neonhealth agentic-AI survey) suggests billing-specific AI remains unevidenced either way.

## 7. Channel/market — BPO/VA outsourcing rates (q06)

**Fresh evidence (q06):** one result, directly on point — a Philippines outsourcing job posting: "Learn To Outsource Pricing Real Results. SALARY $700 - $1000 USD per month… AlayaCare - Compensation $700 – $1,000 USD per month" (onlinejobs.ph, Mar 7 2026). The human workaround around AlayaCare is priced: **a dedicated offshore AlayaCare VA costs an agency ~$700–$1,000/month.**

**Verdict: CONFIRMED — the workaround market is active as of Mar 2026 and now has a price anchor.** Single-source posting (flagged), but it is consistent with and quantifies R9's structural finding (staffingly.com's "Remote AlayaCare Outsourcing"). Pricing implication for the row: a per-agency overlay priced below ~$700/mo undercuts the VA line item with software. The BPO/VA-firm channel hypothesis is reinforced — those firms are buying AlayaCare-literate labor at this rate, and an agent that removes grunt work is either their tool or their competitor.

## 8. Registry follow-up #1 — family-communication layer (q09)

q09 ("family portal home care agency software AlayaCare WellSky features" — R13b's ready next-pass query) 429'd; q09b ("family communication app home care agency software") returned 6 junk results (rfp.wiki "Communal" membership software, city-transit and job-board noise). **Verdict: STILL-UNVERIFIED — third run, 5+ failed attempts.** R13b's lean-closed read (bundled friends-and-family portals exist on ≥1 platform) stands as the only signal. This phrasing family should be retired from search-service passes; if needed, verify by direct product-page reads (AlayaCare/WellSky/Aaniie family-portal feature pages) rather than web search.

## 9. Registry follow-up #2 — caregiver documentation time per visit (q10)

q10 ("caregiver documentation time per visit study minutes") returned the OSRS-Scribd artifact; q10b ("home health nurse documentation burden hours per visit study") returned the JBoss-dictionary artifact (lists.nceas.ucsb.edu 2009, lists.jboss.org 2008, mail-archive.com 2017). **Verdict: STILL-UNVERIFIED — third run, 6+ failed attempts; no stat exists in this project's evidence base and none was invented.** Same recommendation: answer via primary literature (PHI, Activated Insights benchmarking reports, journal studies) rather than this search service.

---

## 10. FINAL VERDICT for Row 14 (home-care back-office agent layer)

**OPEN — narrowing; the absorption clock has started. Confidence: MEDIUM-HIGH.**

- **Technical feasibility (API gate): PASS, with the platform ranking changed.** AxisCare is now the *best-evidenced* platform leg: vendor-confirmed customer API (static.axiscare.com), documented token flow (docs.celigo.com Sep 25 2025), and a live third-party integration importing caregiver records in production (support.patientrewardshub.com Sep 3 2026). AlayaCare's API stands on thinner, third-party evidence (crozdesk "Restful APIs," R13b) with endpoint depth still unverified. WellSky unverified (429s). Sandata is newly **out** (EVV API serves states/EVV vendors only — supergood.ai F grade). Axxess out (R13b, CEHRT-only).
- **Competitive gap: no solver found for the core wedge** (EVV-exception fixes + billing-ready notes on a third-party platform) across R9, R13b, and this run — but the edges are closing: AxisCare's own Jun 2026 AI announcement (automation, scheduling intelligence, workflow enhancements) is the single most important strategic fact this run produced, and sagecare.ai occupies the adjacent intake workflow.
- **Market/channel: CONFIRMED and now priced.** The workaround the row's thesis rests on costs $700–$1,000/mo per offshore AlayaCare VA (onlinejobs.ph Mar 7 2026); caregiver turnover 75.5% flat in 2025 with ~$2,600/departure (R9, carried) keeps the ops-exception churn that generates the back-office workload.
- **Framing changes (recommended):**
  1. **Platform order flips to AlayaCare-first, AxisCare-second.** Rationale: AxisCare — the best-evidenced API — is also the platform whose vendor just announced its own AI automation roadmap; an overlay built there races the incumbent's own features. AlayaCare carries the thickest BPO/VA workaround market (staffingly's "Remote AlayaCare Outsourcing"; the $700–$1,000/mo VA postings are AlayaCare-labeled), and no AlayaCare in-house AI absorption signal surfaced this run. Condition: one verification pass on AlayaCare endpoint depth before build (next-pass query listed in §1).
  2. **Workflow order: EVV-exception + billing-note drafting first; do NOT build intake** (sagecare.ai occupies it, Mar 2026); do not lead with scheduling intelligence (explicitly on AxisCare's own 2026 roadmap — head-on collision).
  3. **Pricing: sub-$700/mo per agency** undercuts the documented VA line item.
- **Nearest closers (name + URL + date):**
  1. **AxisCare in-house AI** — "AI innovations coming to AxisCare in 2026, including new automation, scheduling intelligence and workflow enhancements" (axiscare.com, Jun 15 2026). The incumbent absorbing the wedge on its own platform.
  2. **sagecare.ai** — AI intake software for home care, "cut post-call admin from 30 minutes to under 5" (sagecare.ai, Mar 25 2026). Single-workflow overlay; intake slice taken, expansion risk.
  3. **CareSmartz360 AI** — "AI-powered home care software" for field and back-office teams (caresmartz360.com, Apr 3 2026). Incumbent AI marketing; depth unverified.
  4. **HCHB AI tools** (hchb.com, Sep 30 2025) — skilled-side incumbent automation; boundary pressure from the top of the market.
  5. *(Carried)* **Careswitch** — AI-native agency OS, ~$100K raised, switch-shaped (Tracxn Aug 20 2026, via R9) — not currently a closer but the shape that would close it if funded.
- **Re-verify trigger:** AxisCare AI features reaching GA, any EVV-exception/billing-note AI product surfacing, or AlayaCare shipping native AI back-office features → re-run this kill-search before build.

## 11. Recommended registry action (main agent owns the registry)

**KEEP Row 14 OPEN; amend, don't promote-and-forget.** Suggested amendments:
- Append to why-open: "Feasibility strengthened: AxisCare API vendor-confirmed with production caregiver-record imports (static.axiscare.com; support.patientrewardshub.com Sep 3 2026); workaround priced at $700–$1,000/mo per offshore AlayaCare VA (onlinejobs.ph Mar 7 2026); Sandata closed as target (EVV API serves states/EVV vendors only, supergood.ai API Report Card)."
- Add closers-to-watch: AxisCare in-house 2026 AI (Jun 15 2026); sagecare.ai intake overlay (Mar 25 2026).
- Flip first-ship platform to **AlayaCare** (from "AlayaCare or AxisCare"), gated on one AlayaCare endpoint-depth verification pass; add the sub-$700/mo pricing note; add the re-verify trigger above.
- Record the two registry follow-ups (family-communication, documentation-time) as **unanswerable via this search service after 3 runs each** — resolve by direct product-page/literature reads, not more queries; they do not gate the row.
- Record STILL-UNVERIFIED legs of this pass: AlayaCare endpoint depth; WellSky PC API; EVV-exception standalone solver; billing-automation AI landscape — each with its next-pass query (§1, §3, §5, §6).

## 12. Evidence for the necessity case (strongest data points)

1. **The back-office workload is a priced full-time job:** agencies pay $700–$1,000/month per offshore AlayaCare-literate VA (onlinejobs.ph, Mar 7 2026) — software that requires human operators is the incumbent state, and the anchor an agent must undercut.
2. **The workload's raw material keeps regenerating:** caregiver turnover 75.5% flat in 2025 (Activated Insights via HHAeXchange, Jul 29 2026, carried from R9) at ~$2,600/departure (PHI via EngineHire, Mar 25 2026, carried) — a permanently churning workforce guarantees schedule gaps, missed check-ins, and EVV exceptions to fix.
3. **The integration pattern is proven in production:** a non-AI third party already reads caregiver records out of AxisCare via its customer API (support.patientrewardshub.com, Sep 3 2026) — the overlay's technical core is demonstrated by a smaller-scope product.
4. **The vendor validates the demand:** AxisCare — a market incumbent — is putting "automation, scheduling intelligence and workflow enhancements" on its own 2026 roadmap (axiscare.com, Jun 15 2026). The back-office automation demand is real enough for incumbents to chase; the open slice is doing it across platforms for agencies that won't switch.
5. **Adjacent workflow economics are benchmarked:** AI intake software claims post-call admin cut "from 30 minutes to under 5" (sagecare.ai, Mar 25 2026 — vendor-claimed) — the single-workflow AI-overlay shape is sellable in this exact market; EVV/billing is a bigger, still-unclaimed workflow.
6. **EVV data access is platform-gated** (Sandata's EVV REST API "serves states and EVV vendors under contract, not a public program" — supergood.ai, API Report Card): first-ship platform choice is load-bearing, and two of five major platforms (Sandata, Axxess) are already closed to overlays.

## 13. Query log (file → query text → outcome)

| File | Query | Outcome |
|------|-------|---------|
| q01.json | `AlayaCare API documentation endpoints` | 8 results; generic noise + 1 gem (supergood.ai API Report Card / Sandata F) |
| q01b (no file) | `API Report Card AlayaCare AxisCare WellSky home care API grade` | 429 ×2 — hard-fail, moved on |
| q02.json | `AxisCare API documentation developers` | 5 results; 4 usable (vendor API page, Celigo, live integration) |
| q03.json | `home care back office automation AI software 2026` | 7 results; all relevant (run's best landing) |
| q04.json | `EVV exception management software` | 1 junk result |
| q04b (no file) | `electronic visit verification exception handling workflow home care agency software` / `EVV exception management home care software tool` | 429 ×2 — hard-fail, moved on |
| q05.json | `home care billing automation AI agency` | 2 junk (gist + OSRS-Scribd) |
| q05b.json | `AI home care agency billing software claims automation 2026` | 8 junk (Nokia audit, city-gov, radio archive) |
| q06.json | `remote AlayaCare outsourcing virtual assistant pricing` | 1 result; directly on point ($700–$1,000/mo) |
| q07, q07b (no file) | `WellSky Personal Care API integration` / `WellSky Personal Care API documentation` | 429 ×2 — hard-fail, moved on |
| q09 (no file) | `family portal home care agency software AlayaCare WellSky features` | 429 |
| q09b.json | `family communication app home care agency software` | 6 junk (rfp.wiki Communal, city-gov) |
| q10.json | `caregiver documentation time per visit study minutes` | 1 junk (OSRS-Scribd artifact) |
| q10b.json | `home health nurse documentation burden hours per visit study` | 4 junk (JBoss-dictionary artifact class) |

**Never reached (quota):** `home care agency software AI agent back office 2026` (q08 — unnecessary, q03 landed fully); `AlayaCare marketplace integrations`; `home care EVV exception workflow cost`; `AxisCare review pros cons 2026`.

## Quota / deadline notes

- 17 web_search invocations / 10 raw files / 7 hard-429 failures — over the ~14-call budget because 429-retries counted as invocations; hard stop enforced at ~minute 12–14 of active searching (started 17:21 UTC, stopped 17:30 UTC after q09b), report written immediately after.
- Upstream degradation matches the documented cross-agent pattern (R7/R9/R12/R13a): the identical OSRS-Scribd artifact (q05, q10), the JBoss/dictionary class (q10b), city-gov noise (q05b, q09b), and 400-wrapped-in-429 hard failures clustering mid-run (q01b, q04b, q07, q07b, q09). Roughly 6 of 10 saved files were junk; the 4 usable sets were high-yield.
- Single-source flags: onlinejobs.ph $700–$1,000/mo (one posting, but exactly the datum sought); supergood.ai Sandata grade (undated page); sagecare.ai 30→5-minute claim (vendor content); all q03 incumbent-AI items are vendor marketing pages — depth/funding of sagecare.ai and AxisCare's AI features unverified.
- Pre-2024 source flagged: pa.gov Sandata interface spec (Dec 20 2016) — used only as context for Sandata's state-contract orientation, not for any verdict.
- No verdict rests on an unsearched premise: the four STILL-UNVERIFIED legs (AlayaCare endpoints, WellSky API, EVV-exception solver, billing-AI landscape) are stated as unverified with next-pass queries, per rules.
