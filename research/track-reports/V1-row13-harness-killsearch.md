# V1 — Row 13 Kill-Search: Legacy Differential-Validation Harness

**Task:** V1 (Verification Agent) — run targeted kill-searches against registry Row 13 ("Legacy differential-validation harness" — behavior capture → replay → deterministic-compare for SI-run mainframe migrations, JCL batch first) and deliver a firm OPEN / BEING-CLOSED / CLOSED verdict. Run date 2026-09-30; search snapshot = run date.

**Method:** z-ai `web_search` CLI (10-result pages) per the standard SVX pattern. Raw JSON saved incrementally and immutably to `research/raw-search-results/v1/` (qNN.json; b-suffix rephrase retries; max one retry per query); 20–30s sleeps between calls; hard 429 failures retried once. Query text logged per file in §2 (R8's lesson: argv-only queries were lost). Priority order per work order: the R8-owed "parallel run" kill-check first, then characterization/golden-master, capture-replay, the Mechanical Orchard Imogen SKU check, COBOL equivalence tools, Amazon Q Transform, data-migration reconciliation, then named-tool and depth checks (own rephrasings allowed by work order).

**Search tally:** **14 web_search calls / 12 raw files saved / 2 hard 429 failures (q04, q07 — each retried once, both retries succeeded) / ~9 usable sets.** Search window 17:16–17:27 (~10.5 min wall-clock incl. sleeps); the 14-call budget was exhausted before the minute-16 hard stop — no further searches attempted. Recurring degradation patterns confirmed again: the "parallel run" phrasing family → rfp.wiki/scribd/Apache/JBoss dictionary noise (6th and 7th noise returns across R8+R13b+V1); a fresh-content SEO-farm pattern appeared (§4); 2 of 14 calls lost to 429.

**Evidence rules:** 2024–2026 sources preferred; host + date noted for every load-bearing claim; single-source claims flagged; junk (rfp.wiki/scribd generic noise, dictionary diffs, random book/novel/course results) not counted; unsearched questions reported UNVERIFIED, never guessed.

---

## 1. Context: what Row 13 claims and why it might die

Row 13 (promoted after R13b) claims: validation — not translation — is the mainframe-modernization bottleneck; translation is commoditized (IBM watsonx Z, Amazon Q Transform, Copilot for IBM Z); validation exists only as vendor marketing claims, service bundles (TSRI, Virtusa, AveriSource), SI-internal frameworks (SyntBots/X-BRiD), consultancies (corsactech), and research (arXiv "Locksmith Loop" 2026). Mechanical Orchard's **Imogen** productizes behavior-capture → tests → behavior-matching rewrite but sells **delivered modernization, not the harness** (mechanical-orchard.com Jun 8 + Jul 8 2026; thoughtworks.com Sep 7 2026 case study: 4 JCL batch jobs → Python/AWS Batch + 3 Db2; Carahsoft public-sector channel). Proposed product: OSS vendor-neutral capture→replay→deterministic-compare harness (JCL batch first), sold to fixed-price SIs who carry delivery risk.

Kill angles tested this pass: (1) the never-successfully-executed "parallel run comparison product" phrasing; (2) general-purpose characterization/golden-master tooling adapted to legacy migration; (3) capture-replay batch harnesses; (4) whether Imogen exists as a buyable SKU (pricing/partner/marketplace); (5) named mainframe test-automation incumbents (Broadcom Mainframe Application Tester, BMC AMI DevX Total Test — the ex-Compuware line R8 only knew as Xpediter debugging); (6) Amazon Q Transform's actual validation surface (R13b quota-blocked); (7) data-migration reconciliation (R13b STILL-UNVERIFIED).

## 2. Query log (query text per file)

| File | Query text | Result quality |
|------|-----------|----------------|
| q01.json | `parallel run mainframe migration comparison testing tool` | 4 results, ALL junk (rfp.wiki DevOps comparison noise, scribd, lists.apache.org, lists.jboss.org dictionary diff) — the documented structural failure, now on its 5th attempt across passes |
| q01b.json | `mainframe parallel testing compare legacy COBOL output new system equivalence validation software product` | 2 results: 1 semi-usable listicle (codedistrict.com "best mainframe modernization tools 2025", Sep 22 2025), 1 JBoss junk |
| q02.json | `characterization testing legacy code migration tool golden master` | 4 results: 2 suspiciously-fresh SEO-farm domains describing the method (nieva.wislab.app "4 days ago", nieva.team "2 days ago" — flagged, not counted), 1 dev-agency method content (uat.devoxsoftware.com), 1 academic (researchgate.net, HyDiff differential testing) — **no product** |
| q03.json | `capture replay mainframe batch testing harness product` | 1 result, pure junk (JBoss dictionary) |
| q03b.json | `record replay production workload testing tool mainframe JCL batch jobs migration` | 4 results: xobin.com JCL *skills test for hiring* (people, not code), techdocs.broadcom.com Brightside 3.0 (DevOps CLI), gsaadvantage.gov SyncSort (irrelevant), redbooks.ibm.com Rational Performance Tester (load testing) — **no capture-replay harness** |
| q04 (NO FILE) | `Mechanical Orchard Imogen pricing partner program` | HARD FAIL 429-wrapped-400 (documented flakiness) — retried as q04b |
| q04b.json | `Mechanical Orchard Imogen platform pricing how to buy license` | 7 results, 4 usable — **KEY FINDING: AWS Marketplace listing "Rhino Agentic Mainframe Modernization"** (see §6) + sourceforge/slashdot comparison-directory presence + bbntimes + ca.talent.com; 3 junk (different Imogens) |
| q05.json | `Imogen Mechanical Orchard AWS Marketplace listing mainframe modernization` | 8 results, ALL junk (novels/academia) — listing-detail verification FAILED; no retry budget spent (budget preserved for named-tool checks) |
| q06.json | `regression testing COBOL rewritten code equivalence tool product` | 8 results, ~5 usable: thoughtworks.com Mar 2 2026, hackernoon.com Mar 25 2026, emergentmind.com Dec 25 2025 (XMainframe), cmfirstgroup.com Feb 19 2024, publibfp.boulder.ibm.com — **no harness product** |
| q07 (NO FILE) | `Broadcom Mainframe Application Tester Compuware Total Test COBOL automated testing capture` | HARD FAIL 429 — retried as q07b |
| q07b.json | `Mainframe Application Tester automated test generation COBOL Broadcom` | 3 results, all usable: docs.broadcom.com, royalcyber.com, sigmadax.com Aug 29 2026 |
| q08.json | `Amazon Q Developer Transform COBOL validation testing unit tests` | 7 results, ~5 usable: docs.aws.amazon.com (AWS Transform runtime testing prerequisites), repost.aws, zylos.ai Apr 18 2026, core.cz, fabrity.com |
| q09.json | `data migration validation reconciliation software VSAM DB2 mainframe compare source target` | 4 results: 2 adjacent-usable (bluinsights.aws, precisely.com Connect replication), 2 junk (job listings) — no reconciliation product |
| q10.json | `BMC AMI DevX Total Test mainframe unit test generation migrated code equivalence` | 7 results, all usable: bmc.com, tei.forrester.com, jenkins.io, devopsdigest.com Nov 28 2023, peerspot.com, trustradius.com May 27 2026, github.com |

Unexecuted from the work order: the SI fixed-price-risk query (#9 in the priority list) — budget went to the named-tool depth checks (q07b/q10) which were higher-value kill angles; TSRI-2026 and differential-testing-OSS extras — not reached. Both remain UNVERIFIED.

---

## 3. Q1 — The core kill-check: standalone parallel-run / comparison testing product

**Original claim:** no standalone, vendor-neutral, buyable parallel-run/differential-validation harness for third-party-run migrations exists.

**Fresh evidence.** The exact R8-owed phrasing (`parallel run mainframe migration comparison testing tool`, q01) returned 4 junk results — the identical rfp.wiki/scribd/Apache/JBoss-dictionary noise class documented on this phrasing family in R8 (q08/q08b) and R13b (q01/q01b). That is now **five consecutive structural failures on the "parallel run" phrasing across three passes** — the phrasing is confirmed unanswerable against this search service. The rephrase (q01b) landed one listicle — codedistrict.com "best mainframe modernization tools 2025" (Sep 22 2025), whose snippet is generic migration-tooling marketing — and one junk result. The capture-replay phrasings (q03/q03b) surfaced: a *hiring* skills test for JCL (xobin.com), Broadcom Brightside (a DevOps CLI for mainframe, techdocs.broadcom.com), SyncSort on GSA Advantage, and IBM Rational Performance Tester record/upload (redbooks.ibm.com — load testing, not functional equivalence). **No parallel-run, differential-comparison, or capture-replay product for migrated workloads appeared in any phrasing.**

**Verdict: SURVIVES.** The core kill-check — now attempted in seven phrasings across R8/R13b/V1 — has never surfaced a standalone product. The absence is consistent across three independent passes and multiple phrasings; the residual risk (a product invisible to this search service) is noted but cannot be reduced further by search.

## 4. Q2 — Characterization testing / golden-master tooling for legacy migration

**Original claim (implicit in Row 13):** characterization/golden-master tooling is not productized for mainframe migration contexts (general-purpose practice exists: ApprovalTests, snapshot tests).

**Fresh evidence (q02).** Four results: (1) uat.devoxsoftware.com — a dev agency describing the *method* ("Put old logic behind adapters, add approval or golden-master tests to lock in behavior, move logic into .NET libraries") — services content, not a tool; (2) researchgate.net — HyDiff, "Hybrid Differential Software Testing… to generate difference-revealing inputs" — academic (the differential-testing research lineage); (3)+(4) nieva.wislab.app ("4 days ago": "characterize the catalog BEFORE touching it. The golden master freezes the legacy's current behavior — quirks…") and nieva.team ("2 days ago": "The characterization tests tell you what behavior to preserve (including the bugs that do matter)") — **flagged as fresh SEO/AI content-farm domains** (odd subdomain patterns, no product surface, days-old): not counted as evidence of a solver, but noted as a demand signal — content farms have started keyword-targeting "golden master characterization legacy migration," which implies search demand and no established tool answering it.

**Verdict: SURVIVES.** Method content (agencies, research, SEO farms) — no tool product. Notably, zero results pointed at any general-purpose characterization tool (ApprovalTests et al.) being marketed for mainframe migration; the adaptation gap is real.

## 5. Q3 — Capture-replay harness for mainframe batch (JCL)

**Original claim:** no buyable capture→replay→compare harness for JCL batch workloads.

**Fresh evidence (q03/q03b):** see §3 — no product. The nearest named capabilities: IBM Rational Performance Tester (record/replay for *load* testing, redbooks.ibm.com) and Broadcom Brightside (mainframe scripting/DevOps CLI, techdocs.broadcom.com). Neither does functional equivalence of migrated batch jobs.

**Verdict: SURVIVES.**

## 6. Q4 — Mechanical Orchard Imogen: does the harness exist as a buyable SKU?

**Original claim (R13b):** Imogen is a delivered-modernization platform, not a licensable harness; no pricing/partner evidence.

**Fresh evidence (q04b; q05 failed to junk):**
- **KEY FINDING:** an aws.amazon.com result titled "**AWS Marketplace: Rhino Agentic Mainframe Modernization**," snippet: "Mechanical Orchard's Imogen platform to automatically refactor COBOL, PL/I, JCL, Assembler, CICS, and IMS code running on Amazon EKS." (aws.amazon.com, undated search snippet — single source; the follow-up query to open the listing detail, q05, returned pure junk.)
- Imogen now appears in software-comparison directories: "IBM Cloud Pak for Applications vs. Imogen Comparison" — "Mechanical Orchard's Imogen platform rewrites mainframe applications with confidence by using real data flows, not just code translation, to safely rebuild…" (sourceforge.net; slashdot.org — same content network).
- "Its Imogen platform launched in 2025" (bbntimes.com, Jul 23 2026).
- Hiring: "Mechanical Orchard builds Imogen, a mainframe modernization platform for rewriting the most critical and complex business applications" (ca.talent.com, Aug 25 2026 — a "Manager, Delivery Infrastructure Engineering" job posting, i.e., they are scaling *delivery*, consistent with a services-led model).

**Read:** No pricing, no partner program, no tool-only SKU surfaced. Imogen remains the rewrite engine sold as a platform/delivered outcome. BUT the AWS Marketplace presence is new and materially changes the risk picture: if "Rhino Agentic Mainframe Modernization" is a *software* listing of Imogen (or a partner product built on Imogen), then SIs could procure the whole behavior-capture+test+rewrite platform themselves — eroding the "harness-for-SIs" slice from the platform side even though no vendor-neutral harness exists. The listing's seller, type (software vs. professional services), and price are all unverified (single undated snippet; detail query returned junk). **This is the single highest-priority follow-up for Row 13 and the one plausible path from OPEN to BEING-CLOSED.**

**Verdict: SURVIVES, with a new BEING-CLOSED trigger flagged (Imogen's AWS Marketplace presence — verify before build).**

## 7. Q5 — AveriSource functional-equivalence depth

Not re-run this pass (R13b settled it on 2024–2026 sources: AveriSource = analysis + business-rules extraction + AI code transformation suite — averisource.com, prnewswire.com Jan 31 2024, rfp.wiki). Budget went to the unverified Amazon Q and named-tool angles. R13b's verdict stands: **equivalence testing at most a stage inside their transformation engagement; not a standalone product.**

## 8. Q6 — COBOL regression / equivalence testing products (general + named incumbents)

**Original claim:** no standalone equivalence-testing product for rewritten COBOL.

**Fresh evidence (q06, q07b, q10):**
- Market commentary: "The AI-based COBOL migration tools announced in February 2026 are impressive for analysis and documentation. For actual code conversion at scale…" (hackernoon.com, Mar 25 2026) — the at-scale conversion/verification gap persists in 2026 trade press.
- Consulting method, not product: "Evaluating tools other than Claude Code for modernizing legacy code — Time and effort (for both tool and human). Cost. Correctness" (thoughtworks.com, Mar 2 2026) — correctness evaluation of modernization output is a live *consulting* exercise.
- Research models, not harnesses: XMainframe, LLM fine-tuned on COBOL/mainframe domains (emergentmind.com, Dec 25 2025).
- Another analysis/transformation vendor: CM First Group, "automated tools and scripts to streamline the conversion process and ensure data integrity. Our static analysis tool, CM evolveIT" (cmfirstgroup.com, Feb 19 2024).
- **Named incumbent #1 — BMC AMI DevX Total Test** (formerly BMC Compuware Topaz for Total Test): "an automated testing solution that enables developers and testers to test mainframe…" (bmc.com); "The BMC AMI DevX Total Test extension can be used to execute either Unit or Functional test scenarios automatically" (github.com, BMC's VS Code extension repo); a Jenkins plugin with a Total Test unit-test runner for CI pipelines (jenkins.io); Forrester TEI: "the mainframe team reduces its change failure rate by 33%" (tei.forrester.com); "BMC AMI DevX helps COBOL teams modernize, migrate, and test legacy code by automating mainframe development workflows around source analysis" (sigmadax.com, Aug 29 2026); "BMC AMI DevX is primarily utilized by organizations to modernize and streamline mainframe development, testing, and maintenance processes" (trustradius.com, May 27 2026).
- **Named incumbent #2 — Broadcom:** "An encompassing solution provides facilities for automated testing and debugging, but further helps streamline the test environment setup, manage complicated…" (docs.broadcom.com — the Mainframe Application Tester / Application Quality and Testing line).

**Read:** The named-tool check that R8 never ran (Compuware appeared in R8 only as Xpediter *debugging*) now shows the two buyable mainframe test-automation incumbents. **Critical distinction:** every evidence frame positions them as *on-platform mainframe DevOps testing* — unit/functional test scenarios for COBOL running on z/OS, wired into Jenkins/VS Code — **not** cross-system capture→replay→deterministic-compare of a *rewritten target* (COBOL→Java/Python on AWS) against the legacy system. BMC's "migrate and test" phrasing (sigmadax) is the nearest incumbent language to the row; no evidence of cross-platform equivalence comparison surfaced in 3 queries (q07b, q10, and q06's tool angle). These incumbents are the most likely extenders into the gap — but as of this snapshot, the migration-equivalence slice is not theirs.

**Verdict: SURVIVES, narrowed — nearest buyable incumbents named (BMC AMI DevX Total Test, Broadcom automated testing); their scope in evidence is on-platform, not migration-equivalence.**

## 9. Q7 — Amazon Q Developer Transform: validation surface (R13b's quota-blocked item)

**Original claim:** validation exists only as marketing claims for the hyperscalers; Amazon Q Transform's validation depth never verified.

**Fresh evidence (q08):**
- "The AI agents can extract business logic from legacy COBOL and other mainframe languages, generate code, test cases and test data, even compile, fix bugs" (repost.aws — AWS's official Q&A/knowledge site).
- "Learn what prerequisites to meet before testing features of AWS Transform for mainframe Runtime for your application" (docs.aws.amazon.com — the AWS Mainframe Modernization *runtime*, the proprietary target environment where converted apps run and are tested).
- Category mapping: "Amazon Q Code Transformation converts Java 8/11 to Java 17, AWS Mainframe Modernization converts COBOL to Java. IBM watsonx Code Assistant for Z handles…" (core.cz); "Amazon Q Developer Transform supports two major migration categories" (zylos.ai, Apr 18 2026); Altisource case study — 350,000 lines of legacy Java, "25% increase in developer productivity" (fabrity.com, citing AWS).

**Read:** Amazon's validation surface = AI agents that *generate test cases and test data* as part of the transformation pipeline, plus testing inside AWS's proprietary Transform runtime. Validation is embedded in the hyperscaler's translation product and its walled-garden runtime — not standalone, not vendor-neutral, not usable by an SI to validate a migration built with *any other* engine. This **resolves** R13b's unverified item and is consistent with R8's IBM-watsonx "validate" claim class.

**Verdict: SURVIVES (validation = embedded feature claim inside translation products, confirmed for Amazon).**

## 10. Q8 — Data-migration validation / reconciliation (VSAM/DB2) — R13b STILL-UNVERIFIED

**Fresh evidence (q09):** Precisely Connect — "real-time data replication software… build streaming data pipelines and share application data across the enterprise — from mainframes" (precisely.com) — data *movement*, not source-target compare/reconciliation; AWS Blu Insights VSAM reference content (bluinsights.aws); two job-listing junk results. No reconciliation product named in this phrasing either.

**Verdict: STILL-UNVERIFIED, leaning open.** Two passes (R13b q05, V1 q09) have now produced only adjacent solvers (data replication: Precisely; masked test data: Delphix per R8) and vendor content marketing (in-com.com Apr 20 2026 per R13b: "Data validation and reconciliation are essential…"). No standalone reconciliation tool surfaced, but one thin query this pass (no retry budget) — do not promote or kill. Next-pass query: "mainframe data migration reconciliation tooling compare migrated database product" / "cutover data comparison software legacy new system."

## 11. Q9 — SI fixed-price risk angle (the buyer)

**NOT RUN this pass** — the 14-call budget was exhausted by the higher-value named-tool and Amazon-Q checks. R8 §6's five-leg confirmation of the SI/channel buyer (agencies buy through channel partners, handbook.opencoreventures.com Jan 12 2026; FedRAMP/contract-vehicle moat, knoxsystems.com Aug 3 2026; services-market structure, credenceresearch.com Jan 8 2025; hyperscalers going to market through SIs — AWS/Karsun May 7 2025, AWS/Cognizant; TMF governance friction, gao.gov) stands as the operative evidence. **UNVERIFIED for this pass; carried evidence unchallenged.**

## 12. Q10+ — Extra kill-angles

TSRI-2026 depth and differential-testing-OSS queries: not reached (budget). UNVERIFIED. The differential-testing OSS angle was partially covered by q02's HyDiff/researchgate hit (academic) and the absence of any OSS tool surfacing in 14 queries.

---

## 13. FINAL VERDICT for Row 13

**OPEN — medium-high confidence.** The harness-for-SIs slice survives its second dedicated kill pass.

What changed this pass (all narrowing, none closing):
1. **The "parallel run" phrasing is now conclusively unsearchable** on this service (5+ consecutive structural noise failures across R8/R13b/V1). The absence-of-product finding rests on 7 phrasings across 3 passes, none of which surfaced a standalone parallel-run/differential/capture-replay product — a strong negative result despite the phrasing failure.
2. **Nearest buyable incumbents named and bounded:** BMC AMI DevX Total Test (ex-Compuware Topaz for Total Test; automated unit + functional testing for mainframe COBOL, Jenkins CI, VS Code, Forrester-TEI 33% change-failure reduction) and Broadcom's automated testing/debugging solution — both scoped to on-platform mainframe DevOps in all evidence; no cross-system migration-equivalence capability surfaced.
3. **Amazon Q Transform's validation surface resolved:** AI agents generating test cases + test data inside the transformation pipeline, and testing inside the proprietary AWS Transform runtime (repost.aws; docs.aws.amazon.com). Embedded, not standalone.
4. **One new BEING-CLOSED trigger flagged:** Mechanical Orchard's Imogen has an AWS Marketplace presence — listing titled "Rhino Agentic Mainframe Modernization" (aws.amazon.com, undated snippet, single source: "Mechanical Orchard's Imogen platform to automatically refactor COBOL, PL/I, JCL, Assembler, CICS, and IMS code running on Amazon EKS") plus comparison-directory presence (sourceforge/slashdot "IBM Cloud Pak for Applications vs. Imogen"). No pricing, no partner program, no tool-only SKU anywhere in evidence, and their Aug 25 2026 job posting is delivery-side — but if the marketplace listing is a software SKU (or a partner product built on Imogen), SIs could procure the whole capture+test+rewrite platform, eroding the harness slice from the platform side. Listing detail unverified (follow-up query returned junk). **This is the top follow-up and the only identified path from OPEN to BEING-CLOSED.**
5. Characterization/golden-master and capture-replay angles: method content and research only — no tool product; a days-old SEO-farm cluster targeting "golden master characterization legacy migration" appeared (demand signal, no solver).

**Confidence: medium-high, not high**, because (a) the core phrasing remains structurally unsearchable — residual risk of an invisible product; (b) the Imogen marketplace listing is unverified in detail; (c) 2 of 14 calls lost to 429s and ~4 sets were junk; (d) TSRI depth and differential-testing OSS never queried.

**Nearest closers (named):**
- Mechanical Orchard Imogen — method owner; AWS Marketplace listing "Rhino Agentic Mainframe Modernization" (aws.amazon.com, undated) — **verify listing type/seller/price before build**.
- BMC AMI DevX Total Test (bmc.com; github.com; jenkins.io; tei.forrester.com; sigmadax.com Aug 29 2026) — buyable incumbent test automation, on-platform scope in evidence.
- Broadcom automated testing/debugging solution (docs.broadcom.com) — same class.
- Amazon Q Developer Transform / AWS Mainframe Modernization runtime (repost.aws; docs.aws.amazon.com) — embedded validation inside the hyperscaler stack.

**Product framing change:** none required — the OSS vendor-neutral capture→replay→deterministic-compare harness (JCL batch first) sold to fixed-price SIs remains the shape. Two amendments: (a) the "why open" should name BMC/Broadcom as bounded incumbents and Amazon's embedded validation as resolved, not vague; (b) a build gate should be added: verify the Imogen AWS Marketplace listing first — if it's a software SKU, re-assess the row (the wedge shifts to "vendor-neutral / works-with-any-engine," which Imogen by construction is not).

## 14. Recommended registry action (maintainer owns gap-registry.md; V1 did not edit it)

**KEEP Row 13 OPEN; amend the row:**
- Append to "why open": "V1 kill pass 2026-09-30: no standalone parallel-run/capture-replay/differential product in 7 phrasings across 3 passes; nearest buyable incumbents BMC AMI DevX Total Test + Broadcom automated testing are on-platform mainframe DevOps scope (bmc.com, docs.broadcom.com, 2024–2026), not migration-equivalence; Amazon Q Transform validation = embedded test-case/test-data generation inside the transform pipeline + proprietary runtime (repost.aws, docs.aws.amazon.com), not standalone."
- Add build gate: "Verify AWS Marketplace listing 'Rhino Agentic Mainframe Modernization' (Mechanical Orchard Imogen refactoring COBOL/PL/I/JCL/Assembler/CICS/IMS to Amazon EKS; aws.amazon.com, undated, single-source) — if software SKU, re-assess."
- Keep VSAM/DB2 data-reconciliation as UNVERIFIED (2 thin passes, adjacent solvers only).
- Log the unexecuted follow-ups: SI fixed-price query, TSRI 2026 depth, differential-testing OSS.

## 15. Evidence for the necessity case (strongest data points to quote)

1. **Failure rates concentrate in validation, not translation:** "70% of mainframe exits fail"; "80% of migrations miss deadlines on delayed testing" (softwaremodernizationservices; openlegacy — vendor-claimed stats, carried from R8); "80% of core-banking migrations fail… due to incomplete or incorrect data" (openlegacy.com, vendor-claimed). No independent counter-evidence surfaced in 3 passes.
2. **2026 trade press confirms the at-scale gap:** "The AI-based COBOL migration tools announced in February 2026 are impressive for analysis and documentation. For actual code conversion at scale…" (hackernoon.com, Mar 25 2026).
3. **The best-funded entrant differentiates on validation, not translation:** "Imogen… rewrites mainframe applications with confidence by using real data flows, not just code translation, to safely rebuild" (sourceforge.net/slashdot.org comparison listings, this pass); the method is behavior-capture → tests → behavior-matching rewrite (mechanical-orchard.com Jul 8 2026; thoughtworks.com Sep 7 2026 case study: 4 JCL batch jobs → Python on AWS Batch + 3 Db2 migrations). The method is proven; the tool is not sold separately.
4. **Hyperscaler validation is a feature claim, not a product:** Amazon Q Transform agents "generate code, test cases and test data, even compile, fix bugs" (repost.aws) — inside the translation pipeline and AWS's proprietary runtime; IBM watsonx "validate" (R8). An SI using any other engine gets nothing.
5. **Testing investment demonstrably pays on-platform, and the migration version is unowned:** Forrester TEI on BMC AMI DevX: mainframe teams "reduce their change failure rate by 33%" (tei.forrester.com) — buyable test automation exists for z/OS DevOps, yet no vendor sells cross-system equivalence for migrations (this pass, q07b/q10/q06).

## 16. Quota / deadline notes

- 14 web_search calls / 12 raw files / 2 hard 429 failures (q04, q07 — both retried successfully) / ~9 usable sets; search window ~10.5 min; call budget exhausted before the minute-16 hard stop.
- Recurring degradation: "parallel run" phrasing → dictionary/list noise (5+ consecutive failures across passes — now treated as structural); SEO-farm fresh-content pattern (nieva.wislab.app / nieva.team, days old) documented for the first time this pass; junk (rfp.wiki, scribd, novels, job listings) in ~4 sets.
- Single-source/undated claims flagged in place: the AWS Marketplace "Rhino Agentic Mainframe Modernization" snippet (undated, unverified detail — the report's most important open thread); sigmadax.com's BMC description (third-party); trustradius/peerspot review snippets (vendor-listing contexts); Forrester TEI (vendor-commissioned); fabrity/Altisource (AWS-cited case study); openlegacy/softwaremodernizationservices failure stats (vendor-claimed, carried from R8).
- Pre-2024 sources used only as flagged context: davenicolette.wordpress.com (2015, COBOL unit-testing DIY history), keyholesoftware.com (2017); all load-bearing citations are 2024–2026 except where flagged.
- Unexecuted (budget): SI fixed-price-risk query; TSRI 2026 depth; differential-testing OSS; the Imogen listing-detail retry. All listed as follow-ups — UNVERIFIED, not guessed.
