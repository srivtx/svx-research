# R13a — Verification Pass: R6 (Small-Mfg ERP/MES) + R7 (Field Service) Owed Kill-Searches (2026-09-30)

**Task:** R13a. Run the kill-searches R6 and R7 died before executing; convert provisional SURVIVED/UNVERIFIED candidates into firm verdicts (CONFIRMED-OPEN / KILLED / STILL-UNVERIFIED).
**Method:** 22 web-search executions via z-ai `web_search` (18 raw JSON files saved to `research/raw-search-results/r13a/`, immutable; 4 executions hard-failed on 429 with no file: q07, q09, q09b, q12). Sleep-staggered 20–30s behind a concurrent sibling agent; thin/junk returns retried once rephrased; both CRITICAL kill-searches (FAI tooling, truck-stock) were run first and both landed productive evidence before the service degraded. Every claim below traces to a named qNN.json file; no raw files from prior agents were touched.
**Evidence window:** searches run 2026-09-30 (~06:10–06:24); cited sources span 2018–Sep 2026, load-bearing evidence 2026-dated (older flagged).
**Service honesty note:** the search API degraded hard mid-run — 11 of 18 saved files are junk (recurring OSRS/Scribd "zoberetimifid" garbage, the identical degradation pattern R7, R9, and R12 documented), and 4 calls hard-failed on 429. Usable evidence sets: 6 productive (q01, q03, q05, q05b, q06b, q11b) + 2 marginal (q04b, q05). Against a 14–17 successful-search target, ~6–7 landed. Both proposed registry rows were nevertheless directly kill-searched — the two items that outranked everything both got verdicts.

---

## R6 CANDIDATE 1 (CRITICAL) — SMB-priced FAI/AS9102/PPAP compliance-packet generation (proposed Row 13)

**R6's original claim (SURVIVED, provisional):** aerospace/defense buyers mandate certs, lot traceability, FAI, revision control ("administrative burdens" — shamrockprecision.com); CMMC costs underestimated for small business (regulations.gov, Dec 26, 2023); supply side showed only enterprise QMS (ETQ Reliance) and FAI-as-a-suite-feature — "No SMB-priced, standalone 'produce the buyer's compliance packet' product appeared in 29 searches" (R6 §7). Owed kill-search: the DISCUS/InspectionXpert class, which never surfaced in R6's evidence.

**Fresh evidence:**

- **q01 / bzness.ai (undated):** "Ideagen Quality Control, formerly InspectionXpert (inspectionxpert.com): ballooning software that generates AS9102 and PPAP reports, starting around $125/month…" — the exact product class R6 said it never saw, with a sub-$150/mo entry price signal.
- **q01 / cadnexa.com (Jun 23, 2026):** comparison page for AS9102/PPAP tooling — "High QA is sold by custom quote, not a public price. For a small shop. AS9102/PPAP… Custom quote, per seat / yr; Free tier; ₹399/mo+ (…)" — i.e., the comparison table includes a free tier and a ₹399/mo (~US$5/mo) entry option, evidence the category has a low-cost SMB end, not just enterprise seats.
- **q03 / sourceforge.net (comparison page):** "$10,000 base + $2,500/user/year" vs "Starting Price: $500/month" for tools including "…Control (formerly InspectionXpert), automates quality inspections and…" — a second, higher pricing read (attribution between the two compared products is ambiguous in the snippet; treat as bracket: the category spans ~$125–$500/mo starts up to $10K-base enterprise deals).
- **q03 / cbinsights.com:** InspectionXpert "was acquired by Ideagen" in September 2018 (pre-2024, corporate history) — the specialist is now owned by an enterprise-QMS parent (Ideagen), explaining both its reach and its price ladder.
- **q11b / getapp.sg:** "1factory Software — PDF Drawing Ballooning and First Article Inspection (FAI)… quality control plans" — another dedicated ballooning/FAI specialist.
- **q11b / bobcad.com (SOLIDWORKS reseller):** "SOLIDWORKS Inspection enables you to create inspection reports and ballooned drawings in just minutes, for time savings of up to 90%…" — mainstream CAD-ecosystem coverage of the exact workflow (ballooned drawing + inspection report), distributed through ordinary CAD resellers.
- **q11b / blog.qa-report.com:** "QA-Report gives manufacturers, machine shops, and quality engineers a platform where every best practice described here is built into the workflow" — a purpose-built quality-report product aimed explicitly at machine shops.
- **q11b / facebook.com (vendor post, undated):** a tool that balloons and does "instant creation of PPAP inspection reports… streamlines the generation of various reports and documents such as PPAP…" — further PPAP-report tooling.
- **q02, q02b (both junk), q11 (junk):** three executions returned nothing usable — the dedicated DISCUS pricing question specifically never landed (DISCUS never surfaced by name in any usable result).

**Verdict: KILLED** (as R6 framed it — "no SMB-priced standalone FAI/ballooning/compliance-packet generator"). The class R6 hypothesized about exists and is populated: **Ideagen Quality Control (formerly InspectionXpert)** — the closer — plus **SOLIDWORKS Inspection**, **1factory**, **High QA**, and **QA-Report**, with visible entry pricing from a free tier/₹399-mo option (cadnexa.com, Jun 23, 2026) to an "~$125/month" signal (bzness.ai) and a $500/mo-start/$10K-base enterprise bracket (sourceforge). R6's proposed first ship ("Ballooned-drawing + AS9102 form generator from inspection/ERP data") is precisely what these products already do. Demand-side evidence stands; the ownership-vacuum framing does not.

**Caveats, honestly stated:** pricing evidence is thin and conflicting (bzness.ai is undated and single-source; sourceforge attribution ambiguous), and DISCUS specifically was never priced. A residual wedge may exist in *full-packet assembly beyond ballooning* — OCR of material certs, cert-package compilation, revision-controlled audit trail, per-packet pricing — none of which was evidenced as owned. But the burden of proof has flipped: any revived row must show why the existing FAI class doesn't absorb it.

**Recommended registry action:** DO NOT promote R6's proposed Row 13. Record in the registry backlog as a searched-and-closed finding: "Small-shop FAI/AS9102/PPAP packet generation — CLOSED 2026-09-30 by existing FAI/ballooning class (Ideagen Quality Control ex-InspectionXpert ~$125–$500/mo signals, SOLIDWORKS Inspection, 1factory, High QA, QA-Report); residual cert-OCR/full-packet assembly wedge unverified" (trace: R13a q01, q03, q11b).

---

## R6 CANDIDATE 2 — Bottom-of-market instant/assisted quoting (Paperless Parts pricing)

**R6's original claim (UNVERIFIED):** professional estimating KILLED by Paperless Parts; most small shops still estimate in Excel (practicalmachinist.com, Jul 25, 2024); shops want instant-quote sites (Jan 31, 2024); Paperless Parts' pricing never surfaced, so "who's still priced out" is unknown.

**Fresh evidence:** q04 ("Paperless Parts pricing per month cost job shop quoting") returned 1 off-target result (rfp.wiki, ProShop content); the q04b retry ("\"Paperless Parts\" how much does it cost review") returned 1 marginal result — gitnux.org (Mar 12, 2026) describing Paperless Parts' structured DFM feedback, no pricing. Two attempts, zero pricing.

**Verdict: STILL-UNVERIFIED** — quota/service-blocked. What the pass does add: Paperless Parts pricing is *consistently* un-findable in public sources (two dedicated attempts across two agents' evidence bases), which itself supports "quote-only / sales-assisted motion" — a pricing pattern that typically filters for shops large enough to justify a sales call. The bottom-of-market quoting question stays open-but-unproven.

**Recommended registry action:** none (hold, as R6 recommended). If a future agent takes it, target ReviewBit/capterra-style review pages and forum mentions of actual bills rather than the vendor's own site.

---

## R6 CANDIDATE 3 — Modern SMB tier sentiment (Katana / MRPeasy / Fishbowl complaints)

**R6's original claim (UNVERIFIED):** the modern-SMB tier got listicle coverage only; G2/Capterra complaint density never reached; MRPeasy had zero results in R6's 29 searches.

**Fresh evidence:** none — not reached before the search-service degradation consumed the budget (every remaining slot went to the two CRITICAL kill-searches and R7's owed items, per the mission's explicit priority rule).

**Verdict: STILL-UNVERIFIED (quota-blocked, not searched this pass).**

**Recommended registry action:** none — no candidate row depended on it. Keep on the follow-up list ("MRPeasy review small manufacturer", "Katana complaints G2").

---

## R6 CANDIDATE 4 — Per-job margin overlay on shelfware ERP + Excel (proposed Row 14, weak evidence)

**R6's original claim (SURVIVED, weak):** ERP sits as passive system of record while scheduling lives in Excel/whiteboard (digitalheroesco.com); the fix today is consultant-built BI dashboards; Odoo job-costing needs a partner (ssibtr.com; bistasolutions.com, Mar 10, 2026); $100/user/mo tiers lock out the small end.

**Fresh evidence:** none — not reached this pass (quota). No counter-evidence surfaced incidentally either.

**Verdict: STILL-UNVERIFIED (quota-blocked).** The row's evidence density remains 2–3 primary sources, exactly as R6 left it. Note the adjacent signal from this pass: servicebizhub.com (Mar 10, 2026, q06b) describes a growing "inventory tool should sync directly [with your FSM]" integration expectation in field service — the same overlay-over-incumbent shape, in the sister vertical — but that is adjacency, not verification.

**Recommended registry action:** DO NOT promote Row 14 yet. It stays a weak-evidence provisional; a dedicated pass ("job costing software small machine shop per job margin", "quote vs actual margin software job shop") is still owed.

---

## R7 CANDIDATE 1 (CRITICAL) — Truck-stock/parts inventory overlay for the Jobber/HCP tier (proposed new row)

**R7's original claim (SURVIVED, provisional):** "you cannot track parts or materials. This is one of the biggest Jobber problems" (toricentlabs.com, Jan 25, 2026); "Lack of Parts Inventory is the biggest complaint" in Housecall Pro reviews (sourceforge.net); ~$6K/yr shrinkage example (intellidriveos.com, May 14, 2026, vendor-claimed); even ServiceTitan's inventory is "invoice-oriented, not truck-oriented" (help.simplyconnectedsystems.com); "No named solver for Jobber/HCP found in the evidence."

**Fresh evidence:**

- **q05 / rfp.wiki (Jobber product page):** Jobber "+Product/service catalogs and basic inventory tracking support common parts lists" — Jobber now claims at least basic native inventory tracking.
- **q05b / fieldpulse.com (Feb 25, 2026):** "Jobber offers basic inventory tracking but lacks advanced inventory controls. [FieldPulse] helps you monitor materials across hubs and trucks. serialized…" — a competitor concedes Jobber's basic tracking while marketing its own hubs-and-trucks inventory — i.e., mid-tier FSM vendors (FieldPulse) are already selling truck-granular inventory as a differentiator.
- **q05b / myquoteiq.com (undated, competitor SEO):** "Does Jobber have inventory management for septic parts and supplies? No. Jobber has no inventory management system at any price." — directly contradicts the two hosts above; flag as vendor-mill noise (R7 documented this layer), but it shows the question is contested marketing terrain, not an unnoticed vacuum.
- **q05b / rfp.wiki (Aug 7, 2026, FSM buying-guide):** "Parts Inventory And Truck Stock Visibility. Assess whether technicians and dispatchers can see the parts needed for work, track truck stock…" — truck-stock visibility is now a *standard line item* in FSM software evaluation guides.
- **q06b / fieldservicesoftware.io (the decisive result):** "**Ply is quote-priced inventory and purchasing software for trades, connecting truck, warehouse, supplier, job, FSM, and accounting workflows.**" — a purpose-built, dedicated trades-inventory product spanning exactly R7's proposed wedge: per-truck stock + warehouse + supplier + job + FSM integration.
- **q06b / servicebizhub.com (Mar 10, 2026):** "If you're running ServiceTitan, Housecall Pro, or Jobber, the inventory tool should sync directly… integration between inventory, field…" — an integration-tooling layer around the cheap tier is already being discussed/marketed.
- **q06b / softwareadvice.com (Jul 10, 2026):** top-six FSM comparisons (Jobber, HouseCall Pro, Service Fusion, FieldPulse, Zuper, …) — the category press now routinely includes inventory capability as a compared dimension.

**Verdict: KILLED** (as an ownership-vacuum row). Two independent kill-shots: (1) **Ply** — the dedicated overlay R7 hypothesized ("mobile per-truck count/scan app that reads Jobber/HCP invoices, maintains live per-truck stock counts") already exists as a product connecting truck, warehouse, supplier, job, FSM, and accounting workflows (fieldservicesoftware.io, q06b); (2) the "cheap tier lacks parts inventory *entirely*" premise is no longer safe — Jobber itself claims basic inventory tracking (rfp.wiki, q05), a competitor concedes "basic inventory tracking" while differentiating on advanced/hubs-and-trucks controls (fieldpulse.com, Feb 25, 2026), and truck-stock visibility is a named evaluation criterion in 2026 FSM buying guides (rfp.wiki, Aug 7, 2026).

**Caveats, honestly stated:** Ply is quote-priced — its SMB accessibility is unverified (q10/q10b attempts to price it died on junk returns); the Jobber-has-inventory question rests on vendor/comparison pages, not primary Jobber documentation or user reviews; and HCP's native status specifically got no fresh evidence (the dedicated Housecall Pro query never landed). So a *narrower* residual — "SMB-*priced* truck-stock reconciliation for sub-10-truck Jobber/HCP shops" — is not strictly disproven. But the row as R7 wrote it ("cheap tier lacks parts inventory entirely… no named solver") is dead; any revival must be re-scoped against Ply and FieldPulse and priced under them.

**Recommended registry action:** DO NOT promote R7's proposed row. Record as searched-and-closed: "Truck-stock inventory overlay for cheap FSM tier — CLOSED 2026-09-30 by Ply (dedicated trades inventory: truck/warehouse/supplier/job/FSM/accounting, quote-priced) + Jobber basic native tracking + FieldPulse hubs-and-trucks inventory; residual SMB-priced reconciliation wedge unpriced vs Ply" (trace: R13a q05, q05b, q06b).

---

## R7 CANDIDATE 2 — AI answering services (Numa, Avoca, Sameday AI)

**R7's original claim (UNVERIFIED, presumed contested):** missed-call leak quantified only by vendor-claimed stats (27% missed, $1,200/call — pipelineon.com; $125K/yr — repuclinic.com); the named players never surfaced in R7's evidence.

**Fresh evidence:** four attempts, all dead — q07 (Numa/Avoca/Sameday/funding) hard-failed on 429 with no file; q07b retry returned junk (municipal documents); q12 (Avoca/Numa traction) hard-failed on 429; q12b retry ("AI receptionist answering service for plumbers electricians pricing") returned the recurring OSRS/Scribd garbage document. Zero usable evidence.

**Verdict: STILL-UNVERIFIED — service-blocked (4 failed attempts, documented).** Status exactly as R7 left it. No basis to kill or confirm; the vendor-claimed missed-call economics remain uncorroborated.

**Recommended registry action:** none. Top of the follow-up list for any future pass in this vertical.

---

## R7 CANDIDATE 3 — OEM warranty-claim processing (Carrier/Trane dealer portals)

**R7's original claim (UNVERIFIED):** consumer-side evidence only (3–7-day processing cycles — libertyhvachartford.com; adversarial home-warranty cos — hvac-talk.com, 2013, pre-2024); zero evidence on contractor-side OEM claim software or dealer-portal digitization.

**Fresh evidence:** q08 (Carrier/Trane dealer portal) returned the OSRS/Scribd garbage document; q08b retry ("HVAC warranty claim processing software dealers labor reimbursement warranty liaison") returned the *same identical* garbage document ("zoberetimifid" — the exact recurring junk result R7's late-run queries hit, now reproducing across agents). Zero usable evidence.

**Verdict: STILL-UNVERIFIED — service-blocked (2 junk attempts, same degradation artifact R7 documented).** The "black hole" hypothesis remains plausible-but-unmeasured.

**Recommended registry action:** none. Follow-up queries unchanged from R7 §9.

---

## R7 CANDIDATE 4 — Commissions/spiff tracking for contractors

**R7's original claim (UNVERIFIED, zero evidence):** never reached before R7's deadline; zero results in R7's evidence.

**Fresh evidence:** none — not reached this pass (quota consumed by the two CRITICAL kill-searches and the higher-priority R7 items).

**Verdict: STILL-UNVERIFIED (not searched this pass).**

**Recommended registry action:** none. Remains on the vertical's follow-up list.

---

## R7 CANDIDATE 5 — Workiz and ServiceTitan small-shop tier

**R7's original claim (UNVERIFIED):** Workiz never appeared in R7's evidence at all; whether ServiceTitan ships any entry tier unknown — critical to the "missing middle" claim.

**Fresh evidence:** none — q09 ("Workiz pricing small shop ServiceTitan entry tier") hard-failed on 429; the q09b retry (simplified to "Workiz pricing per user per month field service") hard-failed on 429 as well. Both attempts documented; no files saved (service-side failures, not quota choice).

**Verdict: STILL-UNVERIFIED — service-blocked (2 hard 429 failures).** The "missing middle" structure rests on R7's original five-host pricing convergence; the ST-entry-tier question stays open.

**Recommended registry action:** none on registry rows (the missing-middle was already KILLED as a row by R7 — contested replacement war — and this pass adds nothing to change that).

---

## Summary table

| # | Candidate (source report, prior verdict) | FINAL VERDICT | Closer / basis |
|---|---|---|---|
| 1 | R6: SMB-priced FAI/AS9102/PPAP packet generation — proposed Row 13 (SURVIVED, provisional) | **KILLED** | Ideagen Quality Control ex-InspXpert (~$125/mo bzness.ai; $500/mo start + $10K-base/$2.5K-user sourceforge), SOLIDWORKS Inspection, 1factory, High QA (custom quote), QA-Report; free-tier/₹399-mo entries visible in cadnexa.com comparison (Jun 23, 2026) — q01, q03, q11b |
| 2 | R6: Bottom-of-market instant quoting / Paperless Parts pricing (UNVERIFIED) | **STILL-UNVERIFIED** | 2 attempts returned 1 off-target + 1 marginal result; pricing consistently unpublished — q04, q04b |
| 3 | R6: Katana/MRPeasy/Fishbowl sentiment (UNVERIFIED) | **STILL-UNVERIFIED** | Not reached — quota went to CRITICAL items per mission priority rule |
| 4 | R6: Per-job margin overlay — proposed Row 14 (SURVIVED, weak) | **STILL-UNVERIFIED** | Not reached this pass; stays weak-evidence provisional; do not promote |
| 5 | R7: Truck-stock/parts inventory overlay for Jobber/HCP — proposed row (SURVIVED, provisional) | **KILLED** | **Ply** — dedicated quote-priced trades inventory connecting truck/warehouse/supplier/job/FSM/accounting (fieldservicesoftware.io, q06b); Jobber basic native inventory tracking (rfp.wiki q05; fieldpulse.com Feb 25, 2026); FieldPulse hubs-and-trucks inventory; truck-stock now a standard FSM buying-guide criterion (rfp.wiki, Aug 7, 2026) |
| 6 | R7: AI answering (Numa/Avoca/Sameday) (UNVERIFIED) | **STILL-UNVERIFIED** | Service-blocked: 4 attempts (2×429 hard-fail, 2×junk) — q07†, q07b, q12†, q12b |
| 7 | R7: OEM warranty-claim processing (UNVERIFIED) | **STILL-UNVERIFIED** | Service-blocked: 2 attempts, both returned the identical recurring garbage document — q08, q08b |
| 8 | R7: Commissions/spiff tracking (UNVERIFIED) | **STILL-UNVERIFIED** | Not reached (quota) |
| 9 | R7: Workiz / ST small-shop tier (UNVERIFIED) | **STILL-UNVERIFIED** | Service-blocked: 2 consecutive hard 429 failures — q09†, q09b† († = no file saved) |

**Net effect on the registry:** both proposed OPEN-NEW rows (R6's Row 13 FAI packet, R7's truck-stock overlay) are killed by this pass. No new rows are recommended. The vertical's survivors are unchanged in status but not promoted: R6's per-job margin overlay (weak evidence, own pass still owed) and the unverified stragglers (bottom-of-market quoting, AI answering, warranty claims, commissions, Workiz/ST tier, Katana/MRPeasy sentiment).

## Quota / deadline notes

- **Executions:** 22 web_search calls total; **18 files saved** (q01–q06b, q07b, q08, q08b, q10, q10b, q11, q11b, q12b — full list in the raw dir); **4 hard 429 failures** saved nothing (q07, q09, q09b, q12 — errors captured in the shell log above, documented here). Against the 14–17 successful-search budget, only ~6–7 sets carried usable evidence — well under target, and the shortfall is service-side, not prioritization: both CRITICAL kill-searches ran first and both succeeded before degradation.
- **Junk map:** q02, q02b (FAI pricing phrasing — marine/library noise), q06 (truck-stock app — OSRS), q07b (city documents), q08, q08b (identical OSRS/Scribd "zoberetimifid" document — the same artifact R7 documented across its late queries, now recurring in R13a: strong evidence of a persistent upstream index-cache failure rather than per-agent bad luck), q10, q10b (Ply pricing attempts), q11 (DISCUS), q12b. The 429s (q07, q09, q09b, q12) are the same 400-wrapped-in-429 pattern R9 and R12 logged.
- **What the deadline/service ate, in priority order for the next agent:** (1) Ply pricing and traction — the single most consequential unpriced fact this pass produced (kills or revives the truck-stock residual); (2) DISCUS pricing specifically; (3) Numa/Avoca/Sameday funding and traction (four failed attempts across two queries this pass); (4) Carrier/Trane dealer-portal contractor workflow; (5) Workiz pricing and any ServiceTitan entry tier; (6) commissions/spiff tracking; (7) Katana/MRPeasy/Fishbowl G2/Capterra complaint density; (8) per-job margin overlay kill-search (R6 Row 14); (9) Paperless Parts actual bills (review sites, not the vendor site).
- **Epistemics:** q05b contains three mutually contradictory vendor claims about Jobber inventory (rfp.wiki "basic tracking" / fieldpulse "basic but not advanced" / myquoteiq "none at any price") — the verdict above rests on the two convergent independent hosts plus Ply's existence, with the contradiction flagged. bzness.ai's $125/mo InspectionXpert figure is single-source and undated; the sourceforge $500/mo/$10K figure has ambiguous attribution. Both are reported as brackets, not facts. Pre-2024 items: cbinsights.com's 2018 Ideagen acquisition note (corporate history only).
- **No edits** were made to `docs/gap-registry.md` (main agent owns it), to R6/R7's reports, or to any prior raw-search dirs. This report + the r13a raw dir + the worklog append are the only writes.

## Key sources (per file)

- q01 (usable): bzness.ai (Ideagen/InspectionXpert ~$125/mo); cadnexa.com (Jun 23, 2026, AS9102/PPAP comparison: High QA custom quote, free tier, ₹399/mo+); g2.com (ballooning review); xranks.com (InspectionXpert positioning).
- q02, q02b (junk): no usable hosts.
- q03 (usable): sourceforge.net ($10,000 base + $2,500/user/yr vs $500/mo start, ambiguous attribution); cbinsights.com (2018 Ideagen acquisition); g2.com; trustradius.com (Ideagen QC reviews); qualityforum.zeiss.com (MES/quality discussion, marginal).
- q04 (1 off-target): rfp.wiki (ProShop). q04b (marginal): gitnux.org (Mar 12, 2026, Paperless Parts DFM).
- q05 (usable): rfp.wiki (Jobber: "product/service catalogs and basic inventory tracking").
- q05b (usable): rfp.wiki (Aug 7, 2026, truck-stock visibility criterion); fieldpulse.com (Feb 25, 2026, Jobber basic tracking / hubs-and-trucks); myquoteiq.com (contradicting vendor claim); wifitalents.com (Feb 12, 2026, ST/Jobber/HCP top-3).
- q06 (junk, OSRS). q06b (usable): fieldservicesoftware.io (Ply); softwareadvice.com (Jul 10, 2026, top-six FSM); teamengine.io (small-FSM starters); myquoteiq.com; job-dox.com (Aug 21, 2024); contractorplus.app; servicebizhub.com (Mar 10, 2026, inventory-tool-syncs-with-ST/HCP/Jobber); thecontractormatrix.com; agiled.app.
- q07 (429, no file). q07b (junk: municipal docs).
- q08, q08b (junk: identical recurring OSRS/Scribd artifact).
- q09, q09b (429, no files).
- q10, q10b (junk: NATO/OSRS-adjacent noise — Ply pricing not obtained).
- q11 (junk, OSRS). q11b (usable): getapp.sg (1factory ballooning/FAI); bobcad.com (SOLIDWORKS Inspection); blog.qa-report.com (QA-Report for machine shops); facebook.com (PPAP report tool, undated); sourceforge.net (Mavlon vs Plataine, marginal); deezer.com (machine-shop podcast snippet, marginal).
- q12 (429, no file). q12b (junk, OSRS).
