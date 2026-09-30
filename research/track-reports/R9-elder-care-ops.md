# R9 — Elder Care / Home Healthcare Operations Software (2024–2026)

Research task R9 (first researcher in this never-searched vertical): market landscape of home-care agency & home-health software, caregiver documentation/EVV burden, caregiver churn & scheduling, family communication, AI entrants 2024–2026, compliance/billing pain, and the buyer≠user test. Kill-list discipline applied to every candidate gap.

**Method:** z-ai web_search; 19 query attempts (q01–q12 incl. rephrased retries) producing 16 saved result files in `research/raw-search-results/r9/` (new files only, never edited). Evidence prioritized 2024–2026; older stats flagged. Report built incrementally (skeleton after first batch) per runtime discipline.
**Evidence window:** search snapshot 2026-09-30.
**Search count:** 19 calls, 16 files saved; 8 files yielded relevant results (q01b, q02b, q04 [thin], q05, q07, q08, q10b, q12 [partial]); 8 returned junk from a degraded upstream (serper 400-wrapped-in-429: q01, q02, q03, q03b, q03c, q09, q09b, q11); 3 calls hard-failed on 429 (q05 first attempt — retried OK; q06 Axxess-reviews and q10 EVV — q10 rephrased as q10b and recovered, q06 lost). Quota shared with a concurrent sibling agent. Queries on family-communication specifics and buyer decision-making returned garbage and remain **UNVERIFIED** — flagged below, not asserted.

---

## 1. Headline findings

1. **Caregiver turnover is ~75–80%/yr and flat for years — verified across five independent sources.** Activated Insights benchmarking data: 77.1% (2022) → 79.2% (2023) (HCAOA, Jul 17 2024), ~75% in 2024 (McKnight's Home Care, Jul 20 2025), **flat at 75.5% in 2025** (HHAeXchange, Jul 29 2026); PHI: home care turnover "nearly 75 percent in 2024." Replacement cost ~$2,600/caregiver (PHI via EngineHire, Mar 25 2026). A 50-caregiver agency replaces ~37–38 people/yr (HR Cloud, Mar 12 2026).
2. **The clearest structural signal: a human-outsourcing industry has grown *around* the software.** Healthcare BPOs sell "Remote AlayaCare Outsourcing" placing "dedicated, trained staff inside the agency's own AlayaCare environment" (staffingly.com), and VA-integration guides map "where the highest-value workflows are by system" across AlayaCare/WellSky (staffingcarehome.com). When customers hire humans to operate your software, the back-office workload is the product gap.
3. **AI entrants exist but are either bundled-and-partial or underfunded.** Incumbent Axxess ships "Care 2.0" ambient voice-to-text documentation "during or immediately after a visit" for nurses *and caregivers* (axxess.com) — killing the standalone "AI visit notes" wedge in home health. The AI-native challenger Careswitch ("AI-powered operating system… automating caregiver and client management, care planning, scheduling, shift review" — Bloomberg) has raised only ~$100K (Tracxn, Aug 20 2026). No evidence found of a well-funded AI layer for the *existing* platforms' back offices.
4. **Buyer≠user confirmed in its purest form.** Agency owners buy compliance/audit platforms; caregivers suffer the data entry (Capterra reviews of AlayaCare: "caregivers having trouble clocking in and out, accessing information"; family-portal password failures); families face the portal friction. AlayaCare's own content admits "the top complaint from caregivers is 'lack of communication with the agency'" (alayacare.com).
5. **EVV is compliance table stakes, fully bundled — not a gap.** Cures Act mandate (Medicaid EVV operational since Jan 1 2023 per Oakes 2019, *pre-2024*), but every major platform (AlayaCare, HHAeXchange, CareVoyant, CareSmartz360) sells state-compliant EVV modules; NY DOH runs provider-readiness surveys. The residual pain is exception-handling when EVV data mismatches payroll/billing — which is the back-office layer again.

---

## 2. Market landscape

- **Non-medical home care (personal care):** WellSky Personal Care (formerly ClearCare — "an industry standard" but criticized, per a vendor-comparison post on Facebook), AlayaCare (cloud, "compliance-driven… praised for audit readiness and end-to-end features, but some agencies report past usability" issues), AxisCare ("user-friendly and audit-ready with flexible pricing"; higher G2 user satisfaction than Aaniie Care), HHAeXchange, CareSmartz360, Aaniie Care, myEZcare, CareVoyant (state-specific, e.g. Missouri MO HealthNet EVV). A 2026 comparison covers "FendanaCura(?), AlayaCare, ClearCare (WellSky), AxisCare, HHAeXchange, CareSmartz360" (alphaconnectionsmedical.com); TrustRadius lists MatrixCare, AxisCare, AlayaCare as top WellSky PC competitors; GetApp lists "Top 20 AlayaCare Alternatives."
- **Home health (skilled, Medicare):** Axxess — "a leading cloud-based healthcare technology platform serving home health, hospice, and home care" (medicalrecords.com review, Aug 28 2026), now shipping ambient-AI documentation (see §6); WellSky Home Health; KanTime; MatrixCare.
- **Structural read:** fragmented, feature-parity market where "audit readiness" is the buying criterion (the agency owner's fear) — classic checklist procurement. Differentiation claims are UX and pricing, not outcome. Pricing data did not surface reliably in this run (comparison pages are gated); AxisCare "flexible/affordable pricing" is the only pricing signal (LinkedIn/AxisCare marketing) — **pricing gap in evidence, not asserted further.**

## 3. Caregiver documentation & EVV burden

- **Caregiver-side friction is documented in reviews:** clock-in/clock-out failures, information access, family-portal password failures (Capterra, AlayaCare reviews, q05).
- **Office-side burden is proven by the outsourcing market** (staffingly.com; staffingcarehome.com) — agencies pay BPOs to operate their own software. The VA-integration guide framing ("where the highest-value workflows are by system") confirms the workload is substantial, recurring, and platform-shaped.
- **EVV:** federally mandated (Cures Act; Oakes 2019 in *Home Healthcare Now*, citing Medicaid.gov 2018 — *pre-2024 source, deadline Jan 1 2023*), state-by-state systems (alorahealth, Mar 4 2026; NY DOH resource library; NC Medicaid FAQ, Feb 18 2021 — *pre-2024*). Vendors market state-specific EVV compliance (CareVoyant Missouri, Apr 5 2026) and "reduce administrative burden" as the pitch — meaning the burden EVV adds is real enough to sell against.
- **Unpaid documentation time — NOT VERIFIED.** Three query phrasings (q03, q03b, q03c) returned junk. No credible quantification of caregiver unpaid documentation time was seen. This is a known literature (nurse documentation-time studies exist) but I will not invent numbers. Flagged for re-verification.

## 4. Caregiver churn & scheduling

- Turnover: see headline #1 — 75.5% flat in 2025 (2026 Activated Insights Benchmarking Report via HHAeXchange); ~75% 2024 (PHI; McKnight's); 79.2% 2023 / 77.1% 2022 (HCAOA citing 2024 report). Client turnover fell to 45.5% in 2024, a seven-year low (McKnight's, Jul 20 2025) — the *caregiver* side is the sticky problem.
- Cost: ~$2,600 per departure (PHI via EngineHire, Mar 25 2026); "the average agency is effectively rebuilding most of its workforce each year" (happyfleet.ai, Jul 22 2026).
- What the market offers: recruiting/retention content and features inside platforms (HHAeXchange "Recruiting & Retaining Caregivers in 2026"; HR Cloud retention guide, Mar 12 2026; EngineHire retention guide, Mar 25 2026) — all checklist-oriented. No search evidence surfaced of churn-prediction/early-warning tooling reading scheduling/EVV signals. **Scheduling no-show pain queries (q11) returned junk — UNVERIFIED.**

## 5. Family/client communication

- Signals seen: family-portal password failures (Capterra/q05); AlayaCare's own caregiver-communication complaint (§1); CareYaya (Jul 8 2025) auto-generating "a caregiver summary formatted for ChatGPT ingestion — families who paste it into any AI get bespoke care plans in seconds" — a hack implying families lack structured updates from agencies.
- Both dedicated family-communication queries (q09, q09b) returned garbage. **Who owns keeping families informed: UNVERIFIED this run.** Do not promote; re-verify.

## 6. AI entrants 2024–2026

- **Axxess "Care 2.0"** (axxess.com): ambient voice-to-text documentation for visits — incumbent absorption of the AI-notes layer in home health. Kills the standalone AI-scribe wedge *for skilled home health*; whether WellSky PC/AlayaCare non-medical users have equivalents is **UNVERIFIED** (their product pages didn't surface in this run).
- **Careswitch**: AI-native "operating system" for home care agencies — automating "caregiver and client management, care planning, scheduling, shift review" (Bloomberg profile), funded by 9 investors (Crunchbase) but only ~$100K disclosed (Tracxn, Aug 20 2026); feature comparison vs KanTime frames HR/intake/scheduling/billing/QA (taloflow, Feb 3 2025). Read: AI-first challenger exists but is capital-light and demands platform *switching* — the thing small agencies avoid.
- **CareYaya** (Jul 8 2025): family-facing AI summaries — consumer-side experiment, not an agency system.
- Ambient-scribe and prior-auth automation are listed among the hottest 2026 healthcare startup ideas generally (preuve.ai) — the horizontal wave is coming to this vertical; nobody evidence-attached an *overlay onto incumbent home-care platforms* specifically.

## 7. Compliance & billing

- EVV mandates are the load-bearing compliance fact (§3). Medicaid/HCBS billing is state-by-state (CareVoyant sells Missouri-specific EVV/billing compliance; NY DOH surveys providers). Medicare home-health PDGM documentation pain: **not directly evidenced this run** (queries not reached or junk). The compliance pattern seen: every platform sells "audit readiness" (the buyer's fear) and "reduce administrative burden" (the operator's pain) — evidence that the burden is real, monetized, and only partially removed.

## 8. Buyer ≠ user test — CONFIRMED

Buyer = agency owner/administrator (buys audit readiness, billing, EVV compliance — "compliance-driven platform often praised for audit readiness," q05). Users = caregivers (EVV clock-in/out, visit notes, app usability) and office staff (the workload outsourced to BPOs) and families (portal passwords). The party whose daily pain is largest (caregiver, office coordinator) has zero purchasing power; the vendor's revenue depends on the compliance byproduct, not on removing the labor. This is the R4 CRM pattern transplanted intact — and the same wedge applies (§10).

---

## 9. Kill-list table

| Candidate gap | Attack (searched for the existing solver) | Verdict |
|---|---|---|
| AI visit-note scribe for home health (skilled) | Axxess "Care 2.0" ambient voice-to-text for nurses/caregivers (axxess.com, q08) — incumbent ships it natively | **KILLED** (for home-health segment) |
| Standalone EVV compliance tool | EVV bundled in every platform: AlayaCare EVV, HHAeXchange, CareVoyant (state-specific), CareSmartz360; state mandates satisfied vendor-side (q04, q10b) | **KILLED** |
| AI-native agency platform (replacement) | Careswitch exists (Bloomberg/Tracxn Aug 2026) but ~$100K raised, requires switching | **KILLED as a gap, evidence it's under-funded** — replacement shape is the wrong wedge, not an opening |
| Agency back-office admin layer (overlay on AlayaCare/WellSky/etc.) | Searched q05/q07/q08: found human BPO/VA outsourcing (staffingly, staffingcarehome) as the workaround, no funded AI overlay found; Careswitch is replacement-shaped and tiny | **SURVIVED** (this run's searches; strongest candidate) |
| Caregiver churn early-warning / retention intelligence | Searched q02b/q11: only checklist-style retention content (HHAeXchange, HR Cloud, EngineHire); no predictive-tool evidence surfaced — but q11 (no-shows) returned junk, so solver search incomplete | **UNVERIFIED** (pain verified 75.5% flat; solver landscape not fully searched) |
| Family communication layer | q09/q09b returned garbage; only indirect signals (portal password complaints, CareYaya hack) | **UNVERIFIED** (do not promote) |
| Quantified unpaid caregiver documentation time | q03/q03b/q03c all junk | **UNVERIFIED** (no stat asserted) |

## 10. Registry recommendations (provisional, OPEN-NEW status)

| Opportunity | Lens | Why open (evidence trace) | First ship | Distribution model |
|---|---|---|---|---|
| Home-care agency back-office agent layer (overlay on AlayaCare/WellSky/AxisCare/HHAeXchange) | Unsexy / overlay shape / buyer≠user | BPOs staff humans *inside* agency platforms (staffingly, staffingcarehome, q05) — software leaves a full-time-job workload; EVV exception + billing-note + scheduling cleanup is the "highest-value workflow" by vendors' own framing; AI-native challenger is $100K-funded and switch-shaped (Tracxn q07) | Read-only integration + agent that ingests EVV/visit/schedule data from one platform (start: AlayaCare or WellSky PC API), drafts exception fixes and billing-ready notes for one-person approval; price per agency/month, undercut the VA line-item | Agency-owner associations (HCAOA), home-care franchise networks, and — deliberately — the VA/BPO firms as channel (sell them the agent that does their grunt work) |
| Caregiver churn early-warning (retention intelligence) | Worker-gap / prediction from exhaust data | Turnover 75.5% flat in 2025 (Activated Insights via HHAeXchange, q02b); $2,600/departure (PHI via EngineHire); market offers only checklist content — but solver search incomplete (q11 junk) | Overlay on scheduling/EVV data flagging churn-risk caregivers (schedule gaps, overtime patterns, long drives, missed check-ins) with a weekly digest to owners | Land-and-expand per agency; state association newsletters; free churn-risk scorecard as wedge |

**Overlap check vs existing registry:** the back-office agent row is the elder-care instance of gap #6 (CRM as observation system — entry-system labor replaced by observation/automation, bottom-up economics) and kin to #12 (absorb, don't replace). It does not duplicate either; it is a vertical instantiation with its own evidence base. Family-communication row deliberately withheld pending re-verification.

## 11. Quota / deadline notes

- 19 search calls / 16 files saved / 8 files usable; upstream returned junk (serper 400-in-429) repeatedly — sibling agent concurrency confirmed by repeated 429s (q05-retry recovered, q06/q10 lost; q10 re-run as q10b recovered). Hard stop enforced at ~minute 16 of the run; report written from what landed.
- Unverified items that MUST be re-run before any build decision: family-communication solver landscape; caregiver unpaid documentation-time quantification; PDGM documentation pain; non-medical (WellSky PC/AlayaCare) AI-notes parity with Axxess Care 2.0; platform API openness (technical feasibility of the overlay — no API documentation was examined this run).

## Key sources (hosts + dates as seen in raw files)

- hcaoa.org (Jul 17 2024); mcknightshomecare.com (Jul 20 2025); hhaexchange.com (Jul 29 2026); phinational.org (n.d., 2024 figure); enginehire.io (Mar 25 2026); hrcloud.com (Mar 12 2026); happyfleet.ai (Jul 22 2026); amesite.com (Sep 10 2024) — turnover/retention.
- capterra.com (AlayaCare reviews); staffingly.com; staffingcarehome.com; alayacare.com; cleardesk.com — complaints & outsourcing signal.
- axxess.com (Care 2.0); careyaya.org (Jul 8 2025); preuve.ai; orangesoft.co (May 7 2025); serif.ai — AI entrants.
- journals.lww.com (Oakes 2019, pre-2024); alorahealth.com (Mar 4 2026); myezcare.com (Mar 5 2026); bridgecareos.com (Apr 1 2026); carevoyant.com (Apr 5 2026); health.ny.gov; medicaid.ncdhhs.gov (Feb 18 2021, pre-2024); caresmartz360.com (Jan 28 2020, pre-2024); enzo.health — EVV/compliance.
- bloomberg.com; crunchbase.com; tracxn.com (Aug 20 2026); f4.fund; taloflow.ai (Feb 3 2025) — Careswitch.
- softwareadvice.ie; alphaconnectionsmedical.com; trustradius.com; getapp.ca; sourceforge.net; g2.com; myezcare.com (Nov 18 2025); medicalrecords.com (Aug 28 2026) — landscape.
