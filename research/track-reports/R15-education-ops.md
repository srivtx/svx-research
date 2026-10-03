# R15 — Education / School-Operations Software (2024–2026)

Research task R15 (first researcher in the never-searched education-operations lens — the operational software layer, NOT consumer edtech/tutoring). Sub-topics: teacher workload & documentation burden; district-vs-teacher procurement (buyer≠user); substitute-teacher ops; small-school admin (private/Montessori/charter); IEP/special-ed paperwork; parent-communication layers; grading/feedback workflows; and the BPO signal (humans hired to operate school software — the R9 pattern). Kill-list discipline applied to every candidate gap.

**Method:** z-ai web_search; 15 query attempts (q01–q15), 15 files saved immutable in `research/raw-search-results/r15/` (every call succeeded; zero 429/400 failures; zero retries; one junk-adjacent set q05 and two thin sets q06/q15 — no OSRS/Scribd/JBoss artifacts this run). Evidence prioritized 2024–2026; pre-2024 stats flagged; single-source claims flagged. Report built incrementally (skeleton before searching) per runtime discipline.
**Evidence window:** search snapshot 2026-10-03, 23:16–23:23 UTC.
**Search count:** 15 calls / 15 files / ~11 usable sets, ~3 partial, ~1 weak. Sibling-stagger sleep 240s honored before first query.

---

## 1. Headline findings

1. **Teacher administrative burden is verified, quantified, and current — but it is the *most attacked* pain in consumer-facing edtech.** Average teacher spends **7.3 hrs/week on administrative tasks** per 2025 NCES data (pulseconnect.us, Apr 5 2026, single attribution of NCES — treat stat as NCES-derived); **7 hrs/week on manual tasks despite digital tools** (ecampusnews.com, Feb 9 2026); **93% of secondary teachers call admin burden excessive** (sedaily.com, Apr 12 2026, single-source survey); >1/3 report heavy administrative burden in EU (cedefop.europa.eu, Apr 21 2026). The remedy space (AI teacher assistants) is a crowded, funded VC category — see kill-list.
2. **IEP/special-ed paperwork is the strongest structural signal in the lens — buyer≠user in pure form, with a 30-page-per-IEP data-entry burden and NO district-side AI absorption surfaced.** Reddit r/specialed (q02, thread 1qkvqrs): teacher on SEAS — "very little training on it. Some IEPs that I manage require **up to 30 pages from start to finish**." Teachers DIY workarounds with free Google-Form templates (edutopia.org); "IEP writing burnout is real" is a teacher-blog genre (mrsdscorner.com); SET burnout→attrition is peer-reviewed (Brunsting 2023, eric.ed.gov, cited 126×). Districts buy compliance systems (Frontline, PowerSchool, SEAS); teachers do the entry. The AI that exists is **teacher-facing drafting** (MagicSchool AI "IEP drafting", Playground IEP "goal writing" — aitoolsbakery.com 2026 roundup; a NJ district contracted MagicSchool for 2026-27 — tapinto.net board minutes, Jul 21 2026) — **no evidence of an AI/compliance overlay on the incumbent district IEP systems themselves**.
3. **The human-workaround signal exists, but as FTE labor and charter back-office *services*, not a priced offshore-VA-inside-the-SIS market like home care.** **263 open "IEP Coordinator" jobs in New York alone** (Indeed, q15) — districts hire full-time humans to track IEP deadlines/meetings/compliance. Charter back-office outsourcing is a real services industry (Alameda CLC "fully-outsourced solution", alamedaclc.org; **EdTec** running charter business ops — NetSuite case study, netsuite.com, *2011, pre-2024*; Creative Back Office for Sequoia Grove Charter Alliance, resources.finalsite.net May 16 2024; FL DOE procurement framework explicitly contemplates outsourced back-office, fldoe.gov). NBOA = the business-officers association channel exists. This is the R9 pattern's *shape* with weaker pricing evidence.
4. **Substitute-teacher ops: the pain is staffing-shaped, and the software layer is served at every price point.** Standalone sub-management platforms run **$1,000–$5,000/yr per school** (openeducat.org, Feb 18 2026); budget tier exists at **$500/school or $6/employee** (ezschoolapps.com); incumbents Tyler Tech Absence & Substitute (tylertech.com), ReadySub (capterra.com), Frontline-class systems (tcpsoftware.com comparison). Fill-rate pain is real but dated: ~70% of public schools have admins cover classes when subs unavailable (theashlandchronicle.com, May 17 2024); CA high-needs schools filled only 42% of daily positions (CalMatters via teachingchannel.com, Jul 7 2022 — *pre-2024*); a 2026 National Substitute Survey + Advisory Council exists (eschoolnews.com, May 21 2026). Not a software gap.
5. **Parent communication and grading/feedback are closed, crowded categories** (kill-list below), and **small-school admin has a real budget tier** (SchoolCues ~$1,200/yr @100 students vs Sycamore $4,800/yr — sycamoreleaf.com comparison, undated; Populi from ~$1.49/mo — sourceforge.net; sub-$50/mo plans common — goodfirms.co).

---

## 2. Teacher workload & documentation burden

- Quantified: 7.3 hrs/wk admin (NCES 2025 via pulseconnect.us Apr 5 2026, single attribution); 7 hrs/wk manual (ecampusnews Feb 9 2026); 93% "excessive" (sedaily Apr 12 2026, single source); EU >1/3 heavy burden (Cedefop Apr 21 2026).
- Policy response exists (UK Workload Reduction Fund pilots 2023–2027 — theeducatoronline.com Sep 11 2026) — confirms the burden is systemic, not tool-lag alone.
- **Structural read:** the burden is real and monetizable, but the attack surface is occupied by the AI-teacher-assistant wave (§8) — which is consumer/teacher-facing, VC-crowded, and out of the SVX shape. The *operational* slice of teacher workload that survived scrutiny is IEP paperwork (§3), not general admin.

## 3. IEP / special-education paperwork — the lens's strongest signal

- **Burden, teacher voice:** "SEAS … very little training … IEPs … up to 30 pages from start to finish" (reddit.com/r/specialed, thread 1qkvqrs, q02 — user voice, date not shown in snippet, flagged); free Google-Form template to cut IEP paperwork (edutopia.org) = classic DIY-when-unserved signal; "IEP writing burnout is real" (mrsdscorner.com, teacher blog); veteran-teacher essay on a system "that left both teachers and students without" support (reacheveryvoice.org, Mar 25 2026).
- **Burnout→attrition literature:** SET burnout significant, esp. EBD-serving SETs (Brunsting 2023, eric.ed.gov, cited 126×); 2017 study: burnout directly degraded IEP outcomes (orilearning.com, secondary citation).
- **Software landscape:** district compliance systems = Frontline IEP, PowerSchool, SEAS (facebook IEP-teacher group asking which to buy, q02; circathera.com special-ed management software guide, 2026). Progress-monitoring: FrenalyticsEDU (blog.aieducator.tools, 2026).
- **AI landscape:** teacher-facing drafting tools — MagicSchool AI (IEP drafting + differentiation), Playground IEP (goal writing) (aitoolsbakery.com, 2026); ezducate.ai 2026 special-ed software guide; a district-level MagicSchool contract for 2026-27 (tapinto.net, Jul 21 2026, single source — proves district procurement of teacher-side AI is starting).
- **Buyer≠user:** district special-ed directors/compliance buy the system of record; case-managing teachers do the data entry, often untrained (SEAS quote). The compliance buyer's revenue-relevant event (state audit, due-process dispute) is a byproduct of teacher labor — same structure as R9's EVV.
- **Human workaround:** IEP Coordinator is an FTE job class — 263 open postings in NYC alone (Indeed, q15, undated snapshot). No third-party "IEP paperwork service" BPO surfaced in this run (q15 thin: ziprecruiter job ads, azed.gov guidance) — **the priced-outsourcing layer that made R9 a row does NOT surface here (yet)**.

## 4. Substitute-teacher operations

- Pain: 70% of schools — admins cover classes (theashlandchronicle May 17 2024, secondary citation of a federal survey; flagged pre-2026); 42% fill rate CA high-needs (teachingchannel Jul 7 2022, *pre-2024*); omicron-era 60% fill at FCPS (wusa9.com, Jan 19 2022, *pre-2024*); 2026 National Substitute Survey + Substitute Management Advisory Council (eschoolnews.com May 21 2026) — pain current enough to have its own national survey.
- Software: served at all tiers — Tyler Tech Absence & Substitute (tylertech.com); ReadySub (capterra.com); standalone platforms $1,000–$5,000/yr/school, district pricing higher (openeducat.org Feb 18 2026); budget tier $500/school or $6/employee (ezschoolapps.com); comparison content exists (tcpsoftware.com); agency-side relief-staffing scheduling (octopuspro.com).
- **Verdict: closed as a software gap** — crowded vendor field + the residual pain is labor-supply (a staffing problem), not tooling. A small team would be fighting Tyler/Frontline + staffing marketplaces (Swing/Kelly/ESS class, not directly surfaced this run — noted as UNVERIFIED adjacent).

## 5. Small-school admin (private / Montessori / charter)

- Served and tiered: SchoolCues ~$1,200/yr @100 students vs Sycamore $4,800/yr — "the question is what each one includes" (sycamoreleaf.com, undated comparison content); Populi from $1.49/mo (sourceforge.net); sub-$50/mo plans common (goodfirms.co); MySchoolWorx unified portal for grades/homework/tuition/comms (myschoolworx.com, Apr 30 2026); childcare/Montessori tier: Playground (tryplayground.com), ChildPilot (getapp.com), iCare (icaresoftware.com); tuition rails: FACTS (woodsmontessori.com, Dec 12 2025); getapp/softwareworld/sourceforge listicles dense.
- **Verdict: closed as drafted.** A budget tier demonstrably exists (SchoolCues/Populi class); no priced-out small-operator evidence strong enough to row. The *interesting* neighbor is the charter back-office services industry (§9), which serves the smallest charter schools with humans, not software.

## 6. District procurement & buyer≠user

- Direct procurement-complaint evidence did **not** surface: q05 returned weak/mixed results (digital-accessibility complaints — nspra.org; TCEA conference coverage — edtechmagazine.com Feb 6 2026; generic ERP marketing). **"Teachers hate the software the district bought" as a quantified phenomenon: UNVERIFIED this run.**
- Buyer≠user is nonetheless **structurally confirmed in the IEP segment** (§3): the system of record is purchased for compliance/audit defensibility; the data entry falls on the teacher; the teacher has zero purchasing power. This is the R4/R9 pattern, but evidenced in one segment only.

## 7. Parent-communication layers

- q06 (fragmentation complaints) returned weak/indirect results — the eschoolnews "fragmentation" hit was about instructional fragmentation, not app sprawl. **Fragmentation-pain quantification: UNVERIFIED.**
- Crowding check (q12): ParentSquare ~$3,000/yr (sourceforge.net pricing entry), ClassDojo (free, classroom-management-shaped), Seesaw, Bloomz, TalkingPoints, BeeNet — active 2026 comparison content (beenet.app, May 18 2026); small-school SIS bundles ship parent portals natively (MySchoolWorx).
- **Verdict: closed — crowded, funded, and bundled.** No gap for a small team.

## 8. Grading / feedback workflows

- The AI angle is fully occupied: AI teacher-assistant category reviews cover ClassDojo AI, Classcraft, Navi by SchoolAI (aimadefor.com, Jun 3 2026); report-writing/grading AI tooling roundups (reportflowpro.com Jan 18 2025; zazadraft.com Jan 15 2025; honestaireview.org 2026; emmple.com Apr 15 2026); teacher-AI benefit studies (edtechinnovationhub.com May 7 2026).
- This is the crowded consumer-adjacent zone the mission brief explicitly scoped OUT. **Verdict: closed/out-of-scope — nothing SVX-shaped.**

## 9. BPO / outsourcing signal (humans inside the software) — the R9 probe

- **Charter back-office services industry confirmed:** Alameda CLC sells "a fully-outsourced solution so your school can focus on its educational mission" (alamedaclc.org, May 18 2017, *pre-2024*, flagged); Creative Back Office contracted for outsourced business services by Sequoia Grove Charter Alliance (resources.finalsite.net, May 16 2024); EdTec — charter back-office provider running operations on NetSuite, "frees up staff time, allowing scarce [resources]…" (netsuite.com case study, Jan 12 2011, *pre-2024, flagged — vendor press release*); state frameworks institutionalize the practice (FL DOE application language — describe "key back-office services to be outsourced via contract, such as business services, payroll, and auditing" — fldoe.gov, undated; Nevada CMO contract language — charterschools.nv.gov, Dec 16 2021, *pre-2024*); NBOA is the business-officers association (connect.nboa.org) = a ready channel.
- **But:** these firms sell *business-office* services (payroll/AP/enrollment/audit), not humans operating inside classroom/IEP systems. The one quasi-R9 datapoint — IEP Coordinator FTEs (§3) — is in-house labor, not priced BPO. Generic education-VA content (24x7direct.com.au — RTO/TAFE student-support admin; outsourcingangel.com — *coaches*, Oct 26 2021, off-lens) is thin and off-target.
- **Verdict: the pattern exists in shape, not in price.** No $700–$1,000/mo priced workaround surfaced (unlike home care's AlayaCare VAs). This weakens any row to "watchlist" grade.

---

## 10. Kill-list table

| Candidate gap | Attack (searched for the existing solver) | Verdict |
|---|---|---|
| AI grading / feedback / lesson-planning assistant for teachers | Crowded VC category: SchoolAI/Navi, ClassDojo AI, Classcraft, MagicSchool, report-writing AI roundups (q08, q14; aimadefor Jun 3 2026) | **KILLED** (crowded + consumer-facing, out of SVX scope) |
| Parent-communication layer | ParentSquare ($3K/yr, sourceforge) + ClassDojo/Seesaw/Remind/Bloomz/TalkingPoints/BeeNet + native SIS portals (q06, q12) | **KILLED** (crowded, bundled, free tiers) |
| Substitute-teacher management software | Tyler Tech Absence & Substitute, ReadySub, Frontline-class incumbents; $1,000–$5,000/yr standalone tier + $500/school budget tier (q03); staffing-shaped residual pain (q13) | **KILLED** (served at every price point; residual is labor supply, not software) |
| Small-school SIS / admin (private, Montessori, childcare) | SchoolCues ~$1.2K/yr, Populi ~$1.49/mo, Sycamore, MySchoolWorx, Playground, ChildPilot, iCare, FACTS (q04, q07) | **KILLED as drafted** (budget tier exists; no priced-out evidence) |
| Teacher-facing AI IEP drafting | MagicSchool AI (IEP drafting, now with district contracts — tapinto.net Jul 21 2026), Playground IEP (goal writing), ezducate, FrenalyticsEDU (q02, q14) | **KILLED** (teacher-side wedge occupied by funded AI assistants) |
| Charter back-office automation (software for the BPOs) | Services industry confirmed (EdTec, Alameda CLC, Creative Back Office, NBOA channel) but their tooling is generic ERP (NetSuite, 2011 case); no software-for-the-BPOs evidence either way | **UNVERIFIED** (pattern in shape, no pricing/tooling depth; pre-2024 sources dominate) |
| **IEP compliance-layer overlay on incumbent district systems (Frontline IEP / PowerSchool / SEAS)** | Searched q02/q10/q14/q15: pain verified (30-page IEPs, untrained users, DIY Google Forms, 263 IEP-coordinator FTE jobs in NYC, burnout literature); teacher-side AI drafting exists; **no district-side AI/overlay on the incumbent systems surfaced; no BPO service industry surfaced; incumbent AI roadmaps unverified** | **SURVIVED-THIN** (the lens's only survivor — but evidence short of row-grade: no priced workaround, no API openness check, demand not dollar-quantified) |

## 11. Registry recommendations

**Verdict on the lens: education-operations tooling is CLOSED for SVX-shaped rows this pass — with one thin, explicitly-bounded residual.**

- **No new row promoted.** The strongest survivor (IEP compliance overlay) fails the R9 row bar on three counts: (1) no priced human-outsourcing workaround surfaced (the load-bearing R9 evidence); (2) incumbent-side absorption unverified (Frontline/PowerSchool 2026 AI roadmaps not checked — q14 surfaced no announcements but absence-of-evidence); (3) API openness of Frontline IEP/SEAS/PowerSchool unverified — enterprise SIS platforms are typically procurement-gated, and the technical feasibility gate (the careops Goal-0 pattern) has not been run.
- **Record the vertical as searched-and-near-closed** in the never-searched list, with the IEP-overlay slice carried to the still-unverified list as a *direct-read* item, not a search item (the query family showed early junk-adjacent returns on q05/q06/q15 — same degradation pattern that retired three query families in previous waves).
- **Proposed still-unverified entries (for maintainer):**
  1. *IEP compliance-layer overlay* — next pass = direct reads: Frontline IEP + PowerSchool Special Programs product pages for 2026 AI features; SEAS training/support docs; the r/specialed thread 1qkvqrs in full; one district special-ed director interview if available. Promote to a row only if (a) incumbents show no AI absorption AND (b) an entry/exception burden can be priced (IEP-coordinator FTE cost is the proxy — a coordinator salary vs. an overlay fee is the R9 VA-line-item argument in waiting).
  2. *Software-for-charter-back-office-BPOs* — next pass = direct reads of EdTec/Charter Impact-class provider sites + NBOA vendor directory; check whether their stack is NetSuite/QuickBooks-shaped (absorbable) or bespoke. Low priority; pre-2024 sourcing dominated.
- **Overlap check vs existing registry:** the IEP residual is the education instance of gap #6 (CRM-as-observation / buyer≠user entry labor) and kin to row 14's overlay shape — if it ever passes its gates it would be a vertical instantiation, not a duplicate. No conflict with rows 1–14.

## 12. Quota / deadline notes

- 15/15 calls used; zero hard failures; zero retries; ~7-minute active search window (23:16–23:23 UTC) — cleanest rate-limit experience of any recent wave; results carried the known empty-title format quirk (V4's flag stands — URL+snippet+date intact, titles blank).
- Thin/weak sets: q05 (procurement complaints — junk-adjacent), q06 (fragmentation — weak), q15 (IEP-outservices — 4 results, thin). Junk-pattern classes from previous waves (OSRS/Scribd, JBoss dictionaries) did not appear.
- **Unverified items that MUST be resolved before any build decision here:** incumbent IEP-system AI roadmaps (Frontline/PowerSchool/SEAS); IEP-system API openness (overlay feasibility); dollar-quantified IEP paperwork burden (hours/week or coordinator-cost proxy); district procurement-cycle length for special-ed software (sales-motion reality check); teacher-side MagicSchool district-contract terms (is it already absorbing the compliance use case?).
- Bias note: three of the four strongest pain stats (7.3 hrs, 7 hrs, 93%) are secondary citations of NCES/survey data on vendor/content sites — single-sourced through this run; treat as leads, not gospel.

## Key sources (hosts + dates as seen in raw files)

- pulseconnect.us (Apr 5 2026); ecampusnews.com (Feb 9 2026); sedaily.com (Apr 12 2026); cedefop.europa.eu (Apr 21 2026); theeducatoronline.com (Sep 11 2026) — teacher workload.
- reddit.com/r/specialed (thread 1qkvqrs); edutopia.org; mrsdscorner.com; reacheveryvoice.org (Mar 25 2026); eric.ed.gov (Brunsting 2023); orilearning.com — IEP burden/burnout.
- blog.aieducator.tools (2026); aitoolsbakery.com; ezducate.ai; iepfocus.com; circathera.com; tapinto.net (Jul 21 2026) — IEP software/AI landscape + district AI contract.
- openeducat.org (Feb 18 2026); ezschoolapps.com; tylertech.com; capterra.com; tcpsoftware.com; octopuspro.com — substitute ops.
- sycamoreleaf.com; sourceforge.net; goodfirms.co; softwareworld.co; getapp.com; myschoolworx.com (Apr 30 2026); tryplayground.com (Apr 22 2026); icaresoftware.com; woodsmontessori.com (Dec 12 2025) — small-school admin.
- sourceforge.net (ParentSquare pricing); beenet.app (May 18 2026); notsowimpyteacher.com; subscribed.fyi — parent comms.
- aimadefor.com (Jun 3 2026); reportflowpro.com; zazadraft.com; honestaireview.org; edtechinnovationhub.com (May 7 2026); emmple.com (Apr 15 2026) — grading/AI-teacher category.
- alamedaclc.org (May 18 2017, pre-2024); resources.finalsite.net (May 16 2024); netsuite.com (Jan 12 2011, pre-2024); fldoe.gov; charterschools.nv.gov (Dec 16 2021, pre-2024); connect.nboa.org; indeed.com — BPO/charter back-office + IEP-coordinator labor market.
- theashlandchronicle.com (May 17 2024); teachingchannel.com (Jul 7 2022, pre-2024); wusa9.com (Jan 19 2022, pre-2024); eschoolnews.com (May 21 2026) — substitute shortage.
