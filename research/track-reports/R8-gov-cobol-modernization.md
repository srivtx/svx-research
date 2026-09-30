# R8 — Government Legacy (COBOL) Modernization Tooling (2023–2026)

**Task:** R8 — the never-searched backlog vertical "Government legacy (COBOL) modernization tooling" (gap-registry research backlog; AGENT-MISSION.md first-missions list).

**Method:** 25 web searches (z-ai CLI, 10-result pages) run by agent R8; raw JSON in `research/raw-search-results/r8/` (q01–q25 incl. b/c retries for empty or rate-limited queries; query text was passed as argv and not persisted, so sub-topic attribution below is inferred from result content). R8 hit its full search target but was killed by the execution deadline before writing a single line of report. This report was synthesized by S8 on 2026-09-30 from R8's raw evidence only — zero new searches, per salvage rules.

**Evidence window:** usable core Jan 2023 – Sep 2026 (watsonx launch coverage Aug 2023 → Mechanical Orchard verification essay Jun 2026, arXiv SEDCoT Jul 2026, kodebaze Sep 25 2026); older workforce statistics (2017–2021) kept only as flagged context. Roughly half the result files carried signal; the noise map is documented in Deadline notes. ~14 of 25 queries produced usable evidence.

**Cross-track context:** R5 Part B explicitly queued "government legacy crisis" as never-searched (rate-limit deaths) — R8's searches close that backlog item. No overlap with the existing 12 registry gaps (nearest in *shape*, not domain: #1 evals-in-CI and R5-A3 AI-code trust — see Synthesis). Candidate new lens: **modernization verification**.

---

## Headline findings

1. **The famous scale numbers are real but softer than the folklore.** "220 billion lines of COBOL still in production" is corroborated by four independent 2025–2026 sources: codeaura.ai (May 7, 2025), phasechange.ai (Oct 6, 2025), pragmaticcoders.com (Oct 2, 2025), and the arXiv SEDCoT paper (Jul 5, 2026), which attributes the figure to Reuters. The "800 billion lines" number appears **only** as the upper bound of one vendor's "220–800 billion" range (phasechange.ai) — no standalone source for 800B was seen in this evidence base. "95% of ATM card swipes flow through COBOL-based systems" recurs (pragmaticcoders.com, Oct 2025; metaintro.com, Mar 17, 2026). GAO-derived spending numbers circulate with **conflicting denominators**: "GAO 2025: 80% of $83B federal IT budget goes to operations and maintenance" (eltexsoft.com) vs. "approximately 80 percent of over $100 billion in annual IT and cyber-related investment" (mlogica.com) — both secondary; the primary GAO text was never captured.

2. **Translation is claimed solved by the giants; validation is where everyone admits failure.** Every major vendor now claims COBOL translation: IBM watsonx Code Assistant for Z to "analyze, refactor, transform **and validate**" COBOL (venturebeat.com, Aug 21, 2023; ciodive.com, Aug 22, 2023); Amazon Q Developer "automate complex migration processes" via Cognizant (docs.aws.amazon.com); Claude Code to "speed discovery, translate COBOL, and enable 40–60% faster migrations in 2026" (solguruz.com — a dev shop's marketing claim); GitHub Copilot for IBM Z (practicallogix.com, Jul 10, 2026, citing Gartner MQ positioning Copilot as leader for the second year). Yet the failure literature points at validation and data, not translation: "70% of mainframe exits fail in 2026" and "around 80% of core-banking migrations fail, 'usually due to incomplete or incorrect data'" (openlegacy.com); "80% of application migrations miss deadlines… the primary driver of this failure is a reactive or delayed testing strategy" (softwaremodernizationservices.com, Jan 8, 2026); "Mainframe modernization is a verification problem" (mechanical-orchard.com, Jun 8, 2026).

3. **The validation slice has claimants but no standalone product.** What the evidence shows: validation as a marketing claim (IBM's "validate" verb, 2023); validation bundled inside transformation services (TSRI publishing client quotes on "functional-equivalence testing" — rfp.wiki, 2026; Virtusa's "testing automation and performance validation" — worldmetrics.org, Jun 18, 2026); validation as bespoke SI frameworks (SyntBots test design accelerator + X-BRiD automation framework — aws.amazon.com, Dec 23, 2021); validation as consultancy ("Harness Engineering for Legacy Code" — corsactech.com); validation as 2026 research (arXiv "Locksmith Loop" agentic test-synthesis, A. Ferenczi; ACM Path-Guider; ACM "LLM-Assisted Retro-Documentation for Legacy COBOL," May 13, 2026). A 2010 practitioner essay — "Migration testing uses the legacy system as the test oracle" (richard-seidl.com, Aug 31, 2010) — reads as the method still being rediscovered sixteen years later.

4. **Program inventory / dependency mapping is an occupied category.** Incumbents: SMART TS XL ("impact analysis from any symbol across the entire indexed system" — in-com.com, May 11, 2026), BMC Compuware Xpediter debuggers/interactive analysis for COBOL/Assembler/PL/I (sourceforge.net; wikirate), Rocket Enterprise Analyzer (docs.aws.amazon.com). Plus a 2026 AI entrant wave: open-source legacylens RAG for COBOL copybooks/BMS/JCL with dependency mapping and impact analysis (github.com, Mar 4, 2026), atx-mainframe-dependency-manager on PyPI with "18+ analysis tools" (socket.dev), Swimm's "Blackbox to blueprint" COBOL illumination (swimm.io), adapts.ai dependency traversal, IBA Group AI reverse-engineering to "recover lost COBOL codebases" (ibagroupit.com, Jul 29, 2026). Two generations of solvers = no small-team gap.

5. **The "sell to the Systems Integrator" hypothesis is CONFIRMED.** "Government agencies almost always buy software through channel partners" (handbook.opencoreventures.com, Jan 12, 2026); federal SaaS sales are structured by "FedRAMP authorization, contract vehicles, pipeline qualification, and prime teaming" (knoxsystems.com, Aug 3, 2026; fourinc.com on the federal channel, 2022); the North America mainframe modernization *services* market is led by "IBM Corporation, Accenture, DXC Technology, Cognizant, Microsoft Corporation, Deloitte, Amazon Web Services" (credenceresearch.com, Jan 8, 2025); AWS's own public-sector mainframe story is told through SI Karsun (aws.amazon.com Public Sector blog, May 7, 2025). The agency is not the reachable buyer for a small team; the SI carrying delivery risk is.

---

## 1. Scale of the estate and the workforce clock

**Evidence (dated, with provenance):**
- 220B lines in production: codeaura.ai (May 7, 2025); phasechange.ai (Oct 6, 2025, as "220–800 billion… processing trillions in daily transactions"); pragmaticcoders.com (Oct 2, 2025); arXiv SEDCoT (Jul 5, 2026, citing Reuters). The 800B figure: **single source, as a range ceiling only**.
- 95% of ATM transactions on COBOL: pragmaticcoders.com (Oct 2025); metaintro.com "The $3 Trillion Code Nobody Knows How to Fix" (Mar 17, 2026), which also gives "average developer age hitting 55."
- Workforce: codeaura.ai claims "68% of COBOL programmers will retire by the end of 2025" (vendor estimate, May 2025). *Older, flagged:* average COBOL programmer age 58 with ~10% retiring annually and "84,000 unfilled" positions projected (techchannel.com, Oct 25, 2019); experts aged 50–70 (afcea.org, Jul 1, 2020); "retiring at an alarming rate" (infoq.com, Oct 11, 2017).
- **Counter-narrative (2026):** "the workforce is getting younger… the talent picture is more nuanced than ever" (ensono.com); "mainframe careers in 2026 aren't disappearing – they're changing shape" (planetmainframe.com, Jan 21, 2026); 2026 Arcati survey shows workforce challenges around "transition, integration" (planetmainframe.com, Jan 29, 2026).
- **Low-credibility aggregator data:** mainframemodernization.org's "Legacy Talent Gap Tracker" asserts "14,293 COBOL developers retiring in 2026," "18 New COBOL graduates in 2025," and — visibly corrupted — "7.6 Average mainframe engineer age." Methodology invisible; treat as unverified.

**Why it matters:** the retirement-crisis narrative that justifies the whole modernization wave is itself contested in 2026 sources. The panic numbers are either vendor marketing (codeaura, phasechange are COBOL-tool vendors) or pre-2020 trade-press stats. This does not kill the market — the estate is undeniably large — but it flags every "COBOL cliff" statistic in vendor decks as needing primary verification.

**AI economics:** workforce scarcity is the demand engine for AI translation tools; but note that if ensono/planetmainframe are right that careers are stabilizing, the urgency premium deflates and modernization stays a services business.

---

## 2. The 2023–2026 AI-for-COBOL wave: what shipped vs. what is claimed

**Evidence (timeline from search results):**
- **Aug 2023 — IBM launches watsonx Code Assistant for Z.** "The watsonx code assistant can be used to analyze, refactor, transform and validate COBOL applications using gen AI" (venturebeat.com, Aug 21, 2023); positioned "as an alternative to other tools that convert COBOL to Java while preserving native COBOL" (fierce-network.com, Aug 22, 2023); HN discussion frames the real bet as "using LLMs to translate large amounts of legacy COBOL systems to more modern languages like Java" (news.ycombinator.com, Dec 3, 2023).
- **2024 — productization.** "IBM watsonx code assistant for Z brings generative AI to mainframe application modernization… speeding up code development" (itpro.com, Jul 1, 2024).
- **2025–2026 — hyperscalers + SIs.** "Cognizant uses Amazon Q Developer to automate complex migration processes" (docs.aws.amazon.com); AWS Transform uses "agentic AI to transform .NET Framework applications, UI frameworks, and SQL Server databases" (repost.aws — Windows mainframe-adjacent); re:Invent 2025 mainframe sessions describe converting "your database to a more modern SQL engine running on RDS" (zenn.dev, Dec 3, 2025); AWS Public Sector blog profiles Karsun's mainframe-exit approach (aws.amazon.com, May 7, 2025); Slalom sells Bedrock/Q-based transformation (slalom.com).
- **2026 — general AI assistants absorb COBOL.** GitHub Copilot marketed for "legacy modernization with COBOL… IBM Z Development with AI" (linkedin.com); Claude Code credited with "40–60% faster migrations" (solguruz.com); Gartner MQ crowns Copilot leader for the second year (practicallogix.com, Jul 10, 2026).
- **Research wave:** SEDCoT — LLM-based COBOL code translation enhancement (arXiv, Jul 5, 2026); Path-Guider — "a chat-based agentic system for COBOL program understanding, debugging, and impact analysis" (dl.acm.org); LLM-assisted retro-documentation for financial-institution COBOL (dl.acm.org, May 13, 2026).
- **Boutique consultancies:** Royal Cyber sells CA VISION→COBOL migration (royalcyber.com); IBA Group sells AI reverse-engineering (ibagroupit.com, Jul 29, 2026).

**Tried & failed / what's merely claimed:** the striking pattern is that every claim bundle includes a validation verb ("transform *and validate*") with zero evidence in this corpus of what validation actually consists of. The only concrete validation artifacts named anywhere are SI-built: SyntBots/X-BRiD (Syntel-lineage, via an AWS partner post, Dec 2021) — i.e., custom frameworks built per engagement, not products. "40–60% faster migrations" (solguruz) is a marketing number with no methodology in evidence.

**AI economics:** translation is now a **commoditized claim** — IBM, AWS, Microsoft, Anthropic plus every consultancy repeat it. A small team cannot win the translation race. The economics that remain open are downstream of translation: proving the translation (and the data migration) correct.

---

## 3. Translation solved, validation not — where projects actually fail

**Evidence:**
- "70% of Mainframe Exits Fail in 2026. The 30% Playbook." — and "around 80% of core-banking migrations fail, 'usually due to incomplete or incorrect data.' The estate is the reason projects fail" (openlegacy.com).
- "80% of Application Migrations Miss Deadlines… The primary driver of this failure is a reactive or delayed testing strategy. Teams often defer critical testing until the final stages" (softwaremodernizationservices.com, Jan 8, 2026).
- "Most legacy modernization projects fail not because the code is too old, but because teams underestimate the complexity hidden in dependency…" (kodebaze.com, Sep 25, 2026).
- "Mainframe modernization is a verification problem… Modernization fails in three ways. Programs are too slow to deliver. The new code carries subtle defects that surface in production. The act of…" [snippet truncated] (mechanical-orchard.com, Jun 8, 2026).
- Testing on mainframes: "Traditionally, mainframe tests required manual intervention, leading to delays and inconsistent results" (octopus.com); "Legacy COBOL systems face testing hurdles due to absent standard tools and complex customizations, prompting reliance on Java-based APIs" (testerhq.com, Jun 4, 2026); a StackExchange thread on unit-testing code you don't understand (softwareengineering.stackexchange.com, Jun 19, 2019 — older, but the method vacuum persists).
- The canonical method: "Migration testing uses the legacy system as the test oracle. Seven steps, from code measurement to coverage, prove both systems behave the same" (richard-seidl.com, Aug 31, 2010).
- The 2026 research frontier: the "Locksmith Loop" — "a novel agentic test-synthesis method… initiated by preparing two runtime environments" (arXiv, A. Ferenczi, 2026); "Harness Engineering for Legacy Code" orchestrating "automated unit and integration tests, static analysis, security checks, regression tests, and comparison tests to verify the legacy…" (corsactech.com).
- Historical precedent: EPA's Year 2000 guidance defined regression testing as standard practice for federal legacy changes (nepis.epa.gov) — the last time the federal government did mass legacy validation at scale, it was manual.
- Cutover risk: "AWS schedules and provides support during critical cutovers to minimize downtime" (repost.aws); zero-downtime strategies for mission-critical legacy (cspub-ijcisim.org); "Cloud migrations increase security incidents by 35%. Compliance audits miss the temporary attack surfaces" (satinetech.com, Jan 20, 2026).

**Why the field is open:** the failure statistics (whatever their precision — all are vendor- or consultancy-published) converge on testing and data, and the response of the market has been to bundle validation claims into transformation services rather than ship validation as a tool anyone can buy and run. The oracle method (old system = ground truth) is 16 years old in practitioner writing and is currently being re-derived in 2026 arXiv papers — the signature of a gap where research exists but productization doesn't.

**Genuine fix shape:** behavior capture → replay → differential comparison. Record production inputs/outputs of legacy COBOL batch jobs (JCL), replay them against the rewritten system, diff deterministically, report equivalence with coverage — "the legacy system is the test oracle" as a product. LLMs newly make *test synthesis* cheap (Locksmith Loop, retro-documentation prove feasibility); the comparison layer is classical deterministic engineering — the same AI-for-generation / determinism-for-verification split as svx-evalgate.

**Ownership vacuum (SVX pattern):** during a migration nobody owns equivalence — the SI owns delivery, the agency owns operations, and "a common challenge remains: ensuring efficient operations after the migration" (fedscoop.com, Jul 23, 2025). Watching the wiring between old and new is precisely the unpaid-externality shape SVX tracks.

---

## 4. Who sells validation/verification today

Catalog of everything found in 25 searches, by category:
- **Hyperscaler claim:** IBM watsonx "validate" (venturebeat.com, 2023; community.ibm.com, Jan 9, 2026 — "combining natural-language understanding with deep code analysis").
- **Transformation vendors bundling equivalence:** TSRI — client quotes on "automation, schedule, and functional-equivalence testing" (rfp.wiki, 2026); AveriSource (named in the same comparison; depth not captured); Virtusa — "testing automation and performance validation to reduce migration risk for core transaction systems" (worldmetrics.org, Jun 18, 2026).
- **SI-internal frameworks:** SyntBots test design accelerator + X-BRiD automation (aws.amazon.com, Dec 23, 2021) — bespoke, per-engagement.
- **Consultancies:** corsactech.com "harness engineering"; Royal Cyber; IBA Group.
- **A vendor claiming the positioning:** Mechanical Orchard's essay "Mainframe modernization is a verification problem" (Jun 8, 2026) — the only vendor found whose *framing* (not just feature list) is verification. Their actual product surface is not in evidence.
- **Adjacent tooling:** Delphix — "compliant, masked, and reusable data for development, testing, analytics, and AI" (rfp.wiki); BMC Compuware Xpediter debuggers/analysis (sourceforge.net, wikirate); Rocket Enterprise Developer/Analyzer (docs.aws.amazon.com); NTT DATA rehost with "XA-compliant architecture" synchronizing relational databases and VSAM files (dam-americas.nttdata.com).
- **Research:** Locksmith Loop (arXiv 2026), Path-Guider (ACM), retro-documentation (ACM 2026).

**Verdict:** nobody in this evidence base sells a standalone, vendor-neutral equivalence/parallel-run validation harness. Every solver is a claim inside a service, an SI-internal framework, or a paper. **But** — honesty requires noting that the two searches aimed squarely at equivalence testing (q08, q08b) returned pure noise (a JBoss dictionary diff, an ISPF book), and the formal-methods query (q13) also died. The kill-check for this specific gap was never successfully executed; see Kill-list.

---

## 5. Program inventory / dependency mapping / dead-code detection — an occupied category

**Evidence:** SMART TS XL cross-repository symbol search and impact analysis "from any symbol across the entire indexed system… a change to a shared function, a data field in a copybook" (in-com.com, May 11, 2026); BMC Compuware Xpediter (sourceforge.net; wikirate notes Compuware's mainframe revenue comes from financial services); Rocket Enterprise Analyzer (docs.aws.amazon.com); adapts.ai — "can a field or variable change be traced across dependencies? Dependency traversal showing upstream/downstream programs, data stores"; legacylens OSS RAG with "dependency mapping, pattern detection, impact analysis" (github.com, Mar 4, 2026); atx-mainframe-dependency-manager, "18+ analysis tools for dependency tracking, impact assessment" (socket.dev/PyPI); Swimm grouping "jobs, screens, copybooks and programs" (swimm.io); IBA Group AI reverse-engineering (ibagroupit.com, Jul 29, 2026). A 2026 category guide treats "portfolio inventory and triage" + "deep dependency and architecture analysis" as standard market stages (pixelmatters.com).

**Tried & failed (as a small-team entry):** not applicable — nothing failed; the space is simply full, on both the 30-year-incumbent tier (Compuware, SMART TS XL, Rocket) and the 2026 AI tier (legacylens, adapts, Swimm, atx). **KILLED.**

---

## 6. Government reality: procurement, funding, state UI — hypothesis test

**The hypothesis (from the mission brief): government procurement reality may make this a "sell to the Systems Integrator" market, not "sell to the agency."**

**Evidence — CONFIRMED on five independent legs:**
1. "Government agencies almost always buy software through channel partners" (handbook.opencoreventures.com Federal Sales manual, Jan 12, 2026).
2. Federal SaaS sales are gated by "FedRAMP authorization, contract vehicles, pipeline qualification, and prime teaming" (knoxsystems.com, Aug 3, 2026); "the federal channel is the process, or avenue by which OEMs get their IT solutions sold to the federal government" (fourinc.com, Jan 6, 2022); sales messaging must now align with "DOGE mandates" (forcemanagement.com).
3. The market is structurally a services market: "Leading service providers like IBM Corporation, Accenture, DXC Technology, Cognizant, Microsoft Corporation, Deloitte, Amazon Web Services" (credenceresearch.com, Jan 8, 2025).
4. The hyperscalers themselves go to market through SIs in this vertical: AWS Public Sector blog tells the mainframe story through Karsun (May 7, 2025); AWS docs showcase Cognizant on Amazon Q.
5. Funding friction: GAO on the Technology Modernization Fund — "OMB and GSA Need to…" (gao.gov), with the 2016 baseline finding that "26 federal agencies reported spending almost $61 billion" on legacy operations — the TMF was created to break exactly this cycle and GAO still found governance gaps.

**The federal estate (all secondary citations of GAO — flag):** "85% of agencies rely on 20+ year-old COBOL systems (U.S. GAO Report)" (starkdigital.net, undated); GAO 2025 report as "one of the strongest public acknowledgments of the legacy skills crisis. Key findings include: 11 critical federal…" [snippet truncated] (finextra.com, Feb 16, 2026); 80% of $83B (eltexsoft.com) vs. ~80% of $100B+ (mlogica.com) on O&M — **discrepancy unresolved in evidence**; "critical federal legacy systems cost around $337 million a year to run" (capicua.com); GAO "reconfirmed in August 2025 that 'Legacy systems create security and operational risks'" (debuglies.com, Feb 24, 2026); "68% say legacy blocks AI adoption" (eltexsoft.com).

**State-level UI systems (thin evidence — the state-UI queries mostly died):** Wisconsin counties still run "COBOL programming from the 1960s and 70s" (wicounties.org, Jul 1, 2025); Hoover Institution (Oct 12, 2025) recounts the pandemic UI-claims backlog with an official "yelled at about the COBOL in the system" pointing to "7,119 pages" [of legacy code/documentation — snippet garbled]; a COVID-era California unemployment board packet (srfecc.ca.gov, Mar 2021) documents the surge-era strain. **DOGE aimed to migrate the Social Security Administration's COBOL estate** — but this surfaced only as a Techmeme headline (q06); no follow-up evidence was captured.

**Buyer≠user mapping (SVX pattern):** buyer = agency (through channel/prime); actual daily user of modernization tooling = SI delivery engineers on fixed-price risk; beneficiary = citizens who suffer outages. The person who feels the validation pain most acutely — and can therefore buy a tool without a procurement cycle — is the SI, not the agency. This is the exact inverse of the usual bottom-up dev-tool wedge, and it is why the surviving gap must be distributed through integrators.

---

## Kill-list table

| # | Candidate gap | Existing solvers (evidence trace) | Verdict |
|---|---------------|-----------------------------------|---------|
| 1 | **Equivalence-validation harness** (parallel-run / differential testing as a standalone product) | IBM watsonx "validate" claim (venturebeat.com 2023); TSRI functional-equivalence testing bundled in service (rfp.wiki 2026); Virtusa testing automation (worldmetrics.org Jun 2026); SyntBots/X-BRiD SI-internal framework (aws.amazon.com Dec 2021); corsactech harness engineering (consultancy); Locksmith Loop (arXiv 2026, research); richard-seidl oracle method (2010); Mechanical Orchard verification positioning (mechanical-orchard.com Jun 2026, product surface not in evidence) | **SURVIVED (thin)** — no standalone, vendor-neutral, buyable harness found; every solver is a claim, a bundle, or a paper. Caveat: the dedicated kill-queries (q08/q08b equivalence, q13 formal methods) returned noise — this is the least kill-tested survivor. One targeted follow-up pass required before promotion |
| 2 | **Test-generation for untested legacy COBOL** | Locksmith Loop agentic test-synthesis (arXiv 2026); "automated test generation" as GenAI-deck claim (scribd.com); testerhq.com (Jun 4, 2026) documents absent standard tools — COBOL devs test through Java APIs; StackExchange 2019 (no product); Compuware Xpediter = debugging, not generation | **SURVIVED** — need documented by 2026 trade press, method published in research, no product found; the input half of gap #1's pipeline |
| 3 | **Program inventory / dependency mapping / dead-code detection** | SMART TS XL (in-com.com May 2026); BMC Compuware Xpediter (sourceforge, wikirate); Rocket Enterprise Analyzer (docs.aws.amazon.com); adapts.ai; legacylens OSS (github.com Mar 2026); atx PyPI (socket.dev); Swimm (swimm.io); IBA Group (ibagroupit.com Jul 2026) | **KILLED** — two independent generations of solvers (30-year incumbents + 2026 AI wave) |
| 4 | **Data-migration validation** (VSAM/IMS/DB2 reconciliation) | Failure evidence strong: 80% of core-banking migrations fail on "incomplete or incorrect data" (openlegacy.com); decommissioning = "extreme data migration… uncover undocumented data" (cdn2.hubspot.net PDF). Adjacent solvers only: NTT DATA rehost with XA-compliant VSAM sync (dam-americas.nttdata.com); Delphix masked test data (rfp.wiki); AWS Transform DB→SQL/RDS (zenn.dev Dec 2025) | **UNVERIFIED** — the kill-queries for this slice (q23b, q24, q24b) all returned noise; follow-up query needed before any verdict |
| 5 | **COBOL-understanding copilots** | GitHub Copilot for IBM Z (linkedin.com; practicallogix.com Jul 2026); Claude Code for COBOL (solguruz.com 2026); IBM watsonx (itpro.com Jul 2024); Path-Guider agentic IDE (dl.acm.org); Swimm; legacylens RAG (github.com); LLM retro-documentation (dl.acm.org May 2026) | **KILLED** — giants (Microsoft, Anthropic, IBM) plus a docs-tool wave already occupy it; no small team wins a copilot feature race here |
| 6 | **Direct-to-agency distribution** (any of the above sold straight to agencies) | Channel-partner procurement (handbook.opencoreventures.com Jan 2026); FedRAMP / contract vehicles / prime teaming (knoxsystems.com Aug 2026; fourinc.com 2022); DOGE-mandate sales alignment (forcemanagement.com); services-market structure (credenceresearch.com Jan 2025); TMF governance gaps (gao.gov) | **KILLED** as a small-team motion — procurement moat; the SI/prime is the reachable buyer |
| 7 | **Decommissioning data-archeology** (undocumented-data discovery) | One vendor PDF (cdn2.hubspot.net "Mainframes Simplified Decommissioning") + NTT DATA rehost services | **UNVERIFIED** — single-source; looks like a services pitch, not a product |

---

## Registry recommendation (for the maintainer — gap-registry.md not modified by S8)

Ranked candidate rows, evidence-traced. This vertical yields **one thin survivor, two unverified leads, and four kills** — mostly a killed vertical, which is itself a successful finding.

| Rank | Opportunity | Lens | Why the field is open | First ship | Distribution model |
|------|-------------|------|----------------------|------------|-------------------|
| 1 | **Legacy differential-validation harness** (behavior capture → replay → deterministic compare; includes test-generation front end, kill-list #2) | Modernization verification (new lens) | Validation exists only as vendor claims (IBM "validate"), service bundles (TSRI, Virtusa), SI-internal frameworks (SyntBots/X-BRiD), consultancies (corsactech) and 2026 research (Locksmith Loop); failure stats point at testing + data (openlegacy 70%/80%; softwaremodernizationservices 80% miss deadlines on delayed testing) | COBOL batch (JCL) capture-replay pack: record production job inputs/outputs, replay against rewritten code, JUnit-style equivalence reports — "legacy system as test oracle" (richard-seidl 2010) as a product, Locksmith Loop (arXiv 2026) as the AI blueprint | **Sell to modernization SIs** (Karsun-class mid-market integrators on fixed-price risk), not agencies — confirmed by procurement evidence (§6). OSS core for credibility; no FedRAMP needed because the SI holds the contract. Status: OPEN-NEW, gated on one follow-up kill-check pass |
| 2 | **Migration data-reconciliation validator** (VSAM/IMS/DB2 → target) | Modernization verification | Strong failure evidence (data is the #1 stated cause of core-banking migration failure) but zero named standalone solvers in evidence | **DO NOT PROMOTE YET** — hold until 3–4 targeted searches land (see Deadline notes) | Same SI channel if verified |
| — | Inventory/dependency tools; COBOL copilots; direct-to-agency sales | — | Occupied / procurement-closed (kill-list #3, #5, #6) | Recommend recording in the registry as CLOSED with closers named (SMART TS XL & Compuware & legacylens-wave; Copilot/Claude/watsonx; channel-partner procurement) | — |

**Honest bottom line:** if a follow-up pass finds a standalone equivalence product hiding behind TSRI/AveriSource/Amazon Q Transform marketing, this vertical closes entirely and should be recorded CLOSED — a successful finding. As it stands, R8's 25 searches produce negative knowledge of high value (don't build copilots, don't build inventory tools, don't sell to agencies) plus one genuinely open, SVX-shaped crack: **verification, sold to the people who carry the risk.**

**Synthesis with prior tracks:** "translation commoditized, verification open" is now a recurring SVX pattern across domains — R5-A1 (evals for stochastic AI output), R5-A3 (trust layer for AI-generated code), and now R8 (equivalence for AI-translated COBOL). Three tracks, one shape: deterministic verification plumbing riding on top of commoditized generation. The family thesis holds.

---

## Deadline notes — what the kill left unfinished

1. **No query log.** Query text was argv-only (run_search.py); sub-topic attribution in this report is inferred from result content. A future agent should re-log queries with the JSON.
2. **Noise map (≈11 of 25 queries):** q08/q08b (equivalence testing — the critical kill-check for the surviving gap — returned a JBoss dictionary diff and an ISFP book), q13 (formal methods — noise), q15/q15b, q17, q18b, q20 (all pure noise), q23b/q24/q24b (data-migration validation — noise), q06 (5 of 6 results noise; 1 relevant headline), q14/q11/q22b (single thin results).
3. **Unverified famous claims needing primary sources:** the 800B-lines figure (single vendor range); GAO 80%-of-$83B vs. 80%-of-$100B+ discrepancy (eltexsoft vs. mlogica); "85% of agencies on 20+ year-old COBOL" (starkdigital, undated); GAO "11 critical federal…" (finextra snippet truncated); mainframemodernization.org tracker numbers (incl. the corrupted "average age 7.6" field).
4. **Missing evidence entirely:** state UI modernization case studies 2024–2026 (q25 mostly noise — only wicounties.org and the Hoover anecdote landed); DOGE/SSA migration beyond one Techmeme headline; Mechanical Orchard's actual product; TSRI/AveriSource product depth (comparison-site snippets only); pricing for anything; procurement cycle lengths; any named customer running a parallel-run harness.
5. **Follow-up queries for the next agent with quota (in priority order):** (a) "parallel run mainframe migration comparison testing tool" — the kill-check for survivor #1; (b) "TSRI AveriSource functional equivalence testing product capabilities"; (c) "VSAM DB2 data migration reconciliation validation tooling"; (d) GAO 2025 federal legacy systems report (primary text, GAO-25-…); (e) "state unemployment insurance modernization project 2025"; (f) "Mechanical Orchard mainframe product"; (g) "Amazon Q Developer Transform COBOL validation."

---

## Key sources (grouped by host)

- **Scale/workforce:** codeaura.ai (May 2025), phasechange.ai (Oct 2025), pragmaticcoders.com (Oct 2025), arxiv.org SEDCoT (Jul 2026), metaintro.com (Mar 2026), ensono.com, planetmainframe.com (Jan 2026), techchannel.com (2019), afcea.org (2020), infoq.com (2017), mainframemodernization.org.
- **AI wave:** venturebeat.com / ciodive.com / fierce-network.com (Aug 2023), news.ycombinator.com (Dec 2023), itpro.com (Jul 2024), community.ibm.com (Jan 2026), docs.aws.amazon.com, repost.aws, aws.amazon.com (May 2025, Dec 2021), zenn.dev (Dec 2025), solguruz.com, practicallogix.com (Jul 2026), linkedin.com, dl.acm.org (Path-Guider; retro-doc May 2026), scribd.com.
- **Failure/validation:** openlegacy.com, softwaremodernizationservices.com (Jan 2026), kodebaze.com (Sep 2026), mechanical-orchard.com (Jun 2026), octopus.com, testerhq.com (Jun 2026), richard-seidl.com (2010), corsactech.com, arxiv.org (Locksmith Loop 2026), cspub-ijcisim.org, satinetech.com (Jan 2026), epam.com (Mar 2025), skmgp.com (Mar 2026), keyholesoftware.com, in-com.com, softwareengineering.stackexchange.com (2019).
- **Inventory tools:** in-com.com (May 2026), sourceforge.net, wikirate, docs.aws.amazon.com (Rocket), adapts.ai, github.com/legacylens (Mar 2026), socket.dev, swimm.io, pixelmatters.com, ibagroupit.com (Jul 2026), royalcyber.com.
- **Government/procurement:** starkdigital.net, finextra.com (Feb 2026), eltexsoft.com, mlogica.com, debuglies.com (Feb 2026), capicua.com, espresso-labs.com, gao.gov, handbook.opencoreventures.com (Jan 2026), knoxsystems.com (Aug 2026), fourinc.com (2022), forcemanagement.com, close.com (May 2026), gsa.gov (Feb 2025), credenceresearch.com (Jan 2025), fedscoop.com (Jul 2025), wicounties.org (Jul 2025), hoover.org (Oct 2025), srfecc.ca.gov (2021), govinfo.gov (Jan 2026), techmeme.com (DOGE/SSA), nepis.epa.gov (Y2K).
