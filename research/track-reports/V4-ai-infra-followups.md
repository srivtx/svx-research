# V4 — parityrun/evalgate-adjacent registry follow-ups (verification pass)

**Agent:** Verification Agent V4 · **Date:** 2026-09-30 · **Runtime:** ~25-min budget honored; 13 web_search calls, hard stop on new searches enforced after the 13th (minute-15 wall respected).

**Mission:** run the still-unverified items that gate or feed the two AI-infra product rows (svx-parityrun row 13; svx-evalgate gap #1/Goal 6), in priority order: (1) VSAM/DB2 data-migration reconciliation tooling (parityrun **Goal 3 gate**), (2) differential/characterization-testing OSS for legacy code (V1 unexecuted), (3) model EOL/dependency manager, (4) LLM gateway security monitoring (R11 unverified), (5) SI fixed-price-risk framing (V1 unexecuted), (6) TSRI 2026 capabilities (V1 unexecuted).

**Method:** fresh phrasings only (the four named in the mission for target 1 plus one adaptive follow-up on the Arbutus lead; mission phrasings for targets 2–6). Raw JSON evidence immutable in `research/raw-search-results/v4/` (q01–q12, q12b). 15–25 s sleeps between queries. One b-retry allowed per failed query — used once (q12→q12b, junk→usable). **Zero hard 429/400 failures this pass** (first clean pass since V-wave start; note: results arrived with empty `title` fields — URL+snippet+date usable, noted as a format quirk). Known junk patterns excluded per the 6-pass map; no OSRS artifact recurred this window. Every claim carries host+date; single-source items flagged; unsearched = UNVERIFIED, never invented.

---

## Query log

| File | Query (exact) | Quality | Target |
|---|---|---|---|
| q01 | `data reconciliation software mainframe migration` | 8 usable — Arbutus lead surfaced | 1 |
| q02 | `dataset comparison tool z/OS` | 5 weak/mixed — 1 old forum DIY signal, rest noise | 1 |
| q03 | `database migration parity validation Db2` | 8 usable — DataChecks.io, Next Pathway, AWS | 1 |
| q04 | `Precisely Connect dataset compare` | 5 — comparison-directory noise + help.precisely.com mapping docs (confirms movement-not-compare) | 1 |
| q05 | `Arbutus mainframe decommissioning data reconciliation` | 7 usable — Arbutus confirmed (adaptive follow-up on q01 lead) | 1 |
| q06 | `differential testing framework open source legacy` | 8 usable — method + domain-specific OSS only | 2 |
| q07 | `approval testing tool mainframe COBOL` | 6 mixed — no approval-testing product; demand quotes | 2 |
| q08 | `LLM model deprecation notification service` | 7 usable — absorption evidence (Fiddler/Tencent/Salesforce) | 3 |
| q09 | `AI API gateway anomaly detection prompt injection monitoring` | 7 usable — ARMO, Azure Prompt Shields | 4 |
| q10 | `LLM gateway security audit logging` | 8 usable — absorbed into gateway tier (decisive) | 4 |
| q11 | `fixed price mainframe migration risk systems integrator` | 9 usable-adjacent — no fixed-price-contract content; per-function-point pricing found | 5 |
| q12 | `TSRI transformation testing functional equivalence 2026` | 4 junk — retry fired | 6 |
| q12b | `TSRI Inc legacy modernization transformation testing` | 7 usable — JANUS Studio + customer-supplied testing | 6 |

**Unspent mission phrasings** (quota): `track OpenAI model deprecations tool` (target 3 second phrasing), `AI model lifecycle management dependency` (target 3 third phrasing). Target 1 took 5 of 13 calls by mission priority (it is the parityrun Goal 3 gate).

---

## 1. VSAM/DB2 data-migration reconciliation tooling — parityrun Goal 3 gate

**Registry question:** does a buyable compare/reconcile product exist for VSAM/DB2/IMS data migration (not just replication/movement)? Prior state: STILL-UNVERIFIED after 3 noise-failed passes (R8 q23b/q24/q24b; V1 §10 found Precisely Connect = replication only).

**Fresh evidence (q01, q03, q04, q05, q02):**

- **Arbutus Software — the closest thing to a buyable reconcile product.** Vendor site: "Enables direct, real-time access to, and analysis of, all data sources including DB2, IMS, ADABAS, VSAM, ISAM, and sequential (QSAM) flat files" (arbutussoftware.com, live/undated). Vendor whitepaper: "Decommissioning a mainframe is like an extreme data migration project, RECONCILE THE MIGRATION… Arbutus Analyzer – Lets you quickly and easily query all defined mainframe data – with no ETL programming – to quantify and identify data quality issues" (cdn2.hubspot.net Arbutus whitepaper, 11 pp., undated). Arbutus is explicitly marketed for mainframe-decommissioning reconciliation — a named product reading **native VSAM/DB2/IMS without ETL**. Shape: interactive audit-analytics (ACL/IDEA-style; analyst writes the comparisons), not an automated deterministic harness.
- **DataChecks.io — standalone parity-validation product, cloud-DW-shaped.** "The agent iterates automatically until output parity is achieved. report up to 80% reduction accelerating database or warehouse migration timelines from months" (datachecks.io, live/undated, single-source). Agent-driven output-parity validation exists as a product — for database/warehouse migrations; no mainframe/z-OS capability in evidence.
- **Embedded validation (platform-locked):** Next Pathway — "Validation and functional parity. Every migrated workload must be validated against the legacy source to confirm data accuracy and functional equivalence" (nextpathway.com, live/undated); AWS — "automated conversion, validation, and benchmarking that ensures data accuracy, performance parity, and controlled cutover" (aws.amazon.com, live/undated). Same pattern as Amazon Q Transform in V1: validation exists only inside the migration platform.
- **Precisely re-confirmed as movement-not-compare:** help.precisely.com documents "source to target data mapping" methods (help.precisely.com, refreshed ~Sep 28 2026); comparison-directory noise elsewhere in q04. VirtualZ likewise = movement ("moves mainframe data… million records in 18 minutes", virtualzcomputing.com, Sep 16 2026).
- **Method + services signals:** "Avoid phantom data through automated reconciliation, clear rollback policies, and data lineage tracking" (planetmainframe.com, Oct 14 2025 — methodology content); InterraIT sells parallel-run as a service: "lift-and-shift methodology… Parallel-run and phased deployments with zero downtime" (interrait.com, May 14 2025 — SI services, not tooling). DIY signal: practitioners asking forums how to compare two z/OS datasets (ibmmainframes.com, Jul 4 2010 — old, marginal).

**Verdict: BEING-CLOSED.** The literal gate question — "does a buyable compare/reconcile product exist?" — is now **YES**: Arbutus Analyzer is buyable, reads native VSAM/DB2/IMS, and is marketed for mainframe-decommissioning reconciliation; DataChecks.io sells agent-driven migration parity validation (cloud-DW scope). But no vendor sells an **automated, deterministic, statistical-bounds reconciliation harness for z/OS datasets, vendor-neutral and standalone, to SIs**: Arbutus is analyst-driven interactive analytics; DataChecks is cloud-DW-shaped; Next Pathway/AWS validation is embedded in their platforms; Precisely/VirtualZ are movers.

**Registry / product action (parityrun Goal 3):** the gate FIRES — do not build "reconciliation exists" as the pitch. Amended slice: `compare`/reconcile must differentiate as **automated (no analyst-authored queries), deterministic + statistical bounds (evalgate interval machinery), CI-integrated, works-with-any-engine (vendor-neutral — the axis Arbutus/DataChecks/Next Pathway/AWS all fail)**. Record Arbutus Analyzer + DataChecks.io as the named partial closers in `docs/gate-log.md`; the JCL-first capture→replay core (Goals 1–2) is untouched by this finding.

---

## 2. Differential-testing / characterization-testing OSS for legacy code (V1 unexecuted)

**Registry question:** does open-source differential/approval-testing tooling for legacy (COBOL/mainframe) code exist that would absorb or de-risk row 13's harness?

**Fresh evidence (q06, q07):**

- **Method is mature, mainframe tooling is not.** "Differential testing uses them to compare two implementations. Both receive identical input, and their outputs are compared" (coderio.com, Feb 11 2026 — method explainer, no legacy product).
- **OSS differential-testing frameworks exist only in other domains:** CYNTHIA — "an extensible open-source framework for systematically testing well-established ORM implementations" (vatlidak-org.github.io, undated, academic); differential testing of JavaScript via a 3-address subset (dl.acm.org, Apr 10 2026, research); **Kaizen — "a metamorphic fuzzing and differential testing framework for evaluating the correctness of LLM-translated HPC code"** (researchgate.net, Jul 9 2026 — research artifact; the closest conceptual neighbor: differential testing *for LLM-translated code*, but HPC-scoped, not a product).
- **No approval-testing tool for COBOL surfaced** (q07): a Testing+COBOL category exists in the mainframe-software directory (lookupmainframesoftware.com, live/undated) but no approval/golden-master product is named; Compuware/BMC unit-testing content recurs (blogs.bmc.com, undated — the V1-bounded on-platform incumbent); a 2017 best-practices article on testing COBOL you plan to migrate (mydigitalpublication.com / Enterprise Tech Journal, Sep 22 2017); practitioner DIY on forums (ibmmainframeforum.com, undated).
- **Demand quote:** "Testing COBOL Mainframes remains a challenge and lacks focus in the testing world… Only Testing Mainframe code via the front-end or…" (testingmind.com, Dec 8 2020 — old but on-thesis; flagged pre-2024).

**Verdict: CONFIRMED-OPEN (the OSS slice).** Two fresh phrasings surface no differential- or approval-testing OSS for legacy/mainframe code — only method content and domain-specific frameworks (ORMs, JS, HPC research). Nothing to reuse; row 13's harness must be built, and the approval-testing concept (golden-master verification) has no mainframe port to collide with.

**Registry action:** append to row 13's why-open: "no differential/approval-testing OSS exists for legacy code (V4, 2026-09-30) — method mature, mainframe tooling absent; nearest OSS is domain-specific (CYNTHIA/ORMs, Kaizen/LLM-translated HPC — research)."

---

## 3. Model EOL / dependency manager ("Renovate for models") — lean-open after R11/V3

**Registry question:** does a dedicated LLM-model deprecation/EOL tracking or dependency-management product exist?

**Fresh evidence (q08):**

- **Absorption underway at the platform layer:** Fiddler's LLM Gateway now surfaces "Model Deprecation Cues in the Model Pickers. Model pickers now show when a model is scheduled for retirement or no longer available" (docs.fiddler.ai, live docs, Sep 2026); Tencent Cloud exposes "(Model Pending Deprecation)… the model is about to be taken offline" status in its model service (intl.cloud.tencent.com, Sep 16 2026); Salesforce ships admin guidance "Prepare for Model Deprecation and Rerouting" (help.salesforce.com, live docs, undated). Pattern: each platform tells you about **its own** models' retirement — no cross-vendor view.
- **No standalone solver surfaced.** The hits are thesis pieces — "Model deprecation: why pinning an LLM snapshot sets a deadline… OpenAI states at least 6 months for generally available models" (synthetixis.com, Sep 17 2026) and the R11-known versioning essay (tianpan.co, Apr 17 2026) — plus an academic study of deprecated-API usage in LLM-based code (dl.acm.org, C. Wang 2025).
- **Buyer-side pain (procurement):** "A blanket 30-day pre-notice for changing any LLM appears incompatible with a managed multi-model service that adds and retires provider model versions" (ndia.org, undated — defense-procurement context; single-source, flagged).

**Verdict: BEING-CLOSED at the platform-locked end; the standalone cross-vendor slice remains unsurfaced.** Deprecation *visibility* is becoming a gateway/platform feature (Fiddler model-picker cues; Tencent status; Salesforce rerouting docs); no cross-vendor deprecation tracker + version-pinned canary-eval product appeared. Caveat: second/third mission phrasings (`track OpenAI model deprecations tool`, `AI model lifecycle management dependency`) went unspent on quota — this verdict rests on one strong query.

**Registry action:** keep the item open but demote urgency; note that deprecation surfacing is absorbed per-platform (Fiddler/Tencent/Salesforce, Sep 2026) so the surviving shape is a **cross-vendor** view + canary evals — which is evalgate-Goal-6-shaped (a `deprecation` check could ride the swap-check's provider axis rather than being a standalone product). One more kill pass with the two unspent phrasings before any registry promotion.

---

## 4. LLM gateway security monitoring (R11 unverified)

**Registry question:** does dedicated security monitoring for LLM gateways exist as a product (audit logging, anomaly/prompt-injection detection) — or is it absorbed into the gateway tier?

**Fresh evidence (q10, q09):**

- **Audit logging is a marketed gateway feature — absorbed.** Bifrost is positioned as "the AI gateway for GenAI security, enforcing guardrails, access control, rate limits, and audit logging across your production LLM apps at scale" (getmaxim.ai, live/undated); TrueFoundry: "Govern production LLMs with virtual keys, RBAC, policy-as-code, budgets, and compliance-grade audit logs at the gateway — EU AI Act mapped" (truefoundry.com, Jun 23 2026); llmgateway.io records "every attestation change… in the audit log with the attesting user and timestamp" (docs.llmgateway.io, Sep 25 2026); SOC 2 checklists for LLM gateways are now standard content — "where logging level, retention and access scoping land in an audit" (nrouter.ai, Jun 15 2026); "Enterprise AI gateways support compliance by providing centralized logging, audit trails, and policy enforcement" (cequence.ai, live/undated); api7.ai frames AI gateways as governing "model calls, agent workflows, MCP server access, tool calls, API traffic, policies, audit logs" (api7.ai, live/undated).
- **Anomaly/injection detection is a security-vendor + provider play:** ARMO — "Prompt injection in production AI agents is an 8-stage attack chain… ARMO argues that reliable detection" requires that framing (nhimg.org, Aug 20 2026); Azure Prompt Shields "detect prompt-injection attempts in real time" (arxiv.org evaluation, Mar 23 2026); input-side injection prevention + "payload anomaly detection" on the output side as combined product claims (co-r-e.com, Jul 3 2026).

**Verdict: CLOSED (absorbed).** Gateway security monitoring is not an open gap — it is a shipped feature set of the already-crowded gateway tier (Bifrost, TrueFoundry, llmgateway.io, api7) with injection detection owned by security vendors (ARMO) and provider-side shields (Azure). R11's narrower supply-chain slice (CVE patch-lag on LiteLLM-class proxies) got no direct hit, but the umbrella opportunity is dead for a small team; the incidents themselves (PyPI malicious LiteLLM packages — think-ahead.tech, Apr 3 2026, carried from R11) remain a threat-model fact, not a product gap.

**Registry action:** mark the "LLM gateway security monitoring" follow-up RESOLVED-CLOSED with closers named (Bifrost/getmaxim; TrueFoundry compliance-grade audit logs; ARMO; Azure Prompt Shields). No new row.

---

## 5. SI fixed-price-risk framing depth (V1 unexecuted)

**Registry question:** how do SIs actually frame/price fixed-price mainframe-migration risk — is "we carry the risk" a real buying motive for a validation harness?

**Fresh evidence (q11):**

- **No fixed-price-contract/risk-transfer content surfaced.** What appeared instead: per-function-point pricing — "Cost ranges from $1,000 to $2,200 per function point. Migration effort is moderate, and correctness risk is lower than a full rewrite. The risk:…" (tech-stack.com, May 28 2026; quantifies the exposure a fixed-price bid must absorb); generic risk-reduction marketing from SIs/vendors — "Reduce risk and cost in mainframe migration projects" (adaptigent.com, undated), "comprehensive guide… cost analysis, ROI potential" (epam.com, Feb 13 2025), integration-cost dependencies (kumaran.com, Mar 23 2023), mlogica.com "reduced costs… patch vulnerabilities and resolve issues quickly" (undated); and a risk taxonomy — "Mainframe modernization risks span data, code, downtime, security, cost. Migration expands your attack surface and compliance scope" (datastealth.io, Jun 23 2026).
- The specific framing (fixed-price bids, risk transfer, who carries overruns on testing delays) did not appear in any snippet.

**Verdict: STILL-UNVERIFIED (partial support gathered).** The core question — how SIs structure/price fixed-price risk on mainframe migrations — remains unverified by search; the pass did confirm the risk-exposure is quantified publicly ($1,000–$2,200/function point, tech-stack.com May 28 2026), which is consistent with (but does not prove) the fixed-price-risk thesis. This phrasing family now has 1 fresh failure — below the 3-strike retirement bar.

**Registry action:** keep on the follow-up list with a method note: next pass should read SI/mainframe contract literature directly (fixed-price vs T&M debates, procurement case studies, e.g., GAO/the big-SI delivery publications), not web search. The parityrun README may cite the per-function-point figure as risk-exposure context (tech-stack.com, May 28 2026, single-source).

---

## 6. TSRI 2026 capabilities (V1 unexecuted)

**Registry question:** does TSRI (the transformation incumbent named in row 13's why-open) now sell testing/functional-equivalence tooling that would close the row-13 slice?

**Fresh evidence (q12 junk → q12b retry, usable):**

- **TSRI's 2026 scope is assessment + transformation.** "At the center of TSRI's approach is JANUS Studio®, an AI-driven platform that performs fully automated assessment, transformation, and…" (thinkcomputers.org, Jun 17 2026). Post-modernization, TSRI "provides a Transformation Blueprint® that includes a detailed presentation of the structure and flow of the legacy and modernized code" (defense.cioreview.com, undated) — a documentation artifact, not a test harness.
- **Testing is customer-supplied in the flagship case study:** "For the testing process, Northrop Grumman provided TSRI with the data loads, test scripts, and test scenarios deemed appropriate to test the REMIS…" (sciencedirect.com, Northrop Grumman REMIS case study, undated) — i.e., even on TSRI's marquee engagement, the **customer** owned test scripts and scenarios; TSRI sold no equivalence-testing product.
- Channel/partnership context: FNTS resells TSRI for "mainframe optimization and software modernization" (info.fnts.com, Aug 8 2024); TSRI appears in a 2026 independent roundup of legacy-modernization leaders (gartsolutions.com, Jan 28 2026).

**Verdict: CONFIRMED analysis+transformation scope — NOT a closer for row 13.** TSRI's 2026 surface is JANUS Studio (automated assessment/transformation) + Transformation Blueprint (post-hoc documentation), with testing supplied by the customer in its own case study. The registry's existing row-13 text ("AveriSource/TSRI sell analysis+transformation") is now 2026-dated-confirmed; the validation slice stays unowned by this incumbent.

**Registry action:** none required beyond dating — row 13's why-open may append "V4 (2026-09-30): TSRI scope re-confirmed — JANUS Studio = assessment+transformation; testing customer-supplied in the Northrop Grumman REMIS case (sciencedirect.com)."

---

## Summary table

| # | Target | Verdict | Key fact / nearest closer | Registry action |
|---|---|---|---|---|
| 1 | VSAM/DB2 data-migration reconciliation (parityrun Goal 3 gate) | **BEING-CLOSED** | Arbutus Analyzer = buyable, native VSAM/DB2/IMS access, marketed for decommissioning reconciliation (analyst-driven); DataChecks.io = agent-driven output-parity product (cloud-DW); Next Pathway/AWS embedded | Gate FIRES: amend Goal 3 slice to automated + statistical-bounds + CI-integrated + vendor-neutral; write closers into parityrun `docs/gate-log.md` |
| 2 | Differential/approval-testing OSS for legacy code | **CONFIRMED-OPEN** | Method mature (coderio.com Feb 11 2026); OSS only in other domains (CYNTHIA/ORMs; Kaizen/LLM-translated HPC — research Jul 9 2026); no COBOL/mainframe framework in 2 phrasings | Append to row 13 why-open; harness must be built, nothing to reuse |
| 3 | Model EOL/dependency manager | **BEING-CLOSED (platform-locked end); standalone cross-vendor slice unsurfaced** | Fiddler LLM Gateway deprecation cues in model pickers (docs.fiddler.ai); Tencent pending-deprecation status (Sep 16 2026); Salesforce rerouting docs; thesis pieces synthetixis (Sep 17 2026)/tianpan (Apr 17 2026) | Keep open, demote; run the 2 unspent phrasings before any promotion; surviving shape = cross-vendor view + canary evals → evalgate-Goal-6-shaped |
| 4 | LLM gateway security monitoring | **CLOSED (absorbed)** | Audit logging = gateway-tier feature (Bifrost/getmaxim; TrueFoundry "compliance-grade audit logs… EU AI Act mapped" Jun 23 2026; llmgateway.io Sep 25 2026); injection detection = ARMO (Aug 20 2026) + Azure Prompt Shields (Mar 23 2026) | Mark follow-up RESOLVED-CLOSED with closers; no new row |
| 5 | SI fixed-price-risk framing | **STILL-UNVERIFIED (partial support)** | No fixed-price-contract content; risk exposure quantified at $1,000–$2,200/function point (tech-stack.com May 28 2026, single-source); SI risk-reduction marketing generic | Method note: next pass reads SI/procurement literature directly, not search |
| 6 | TSRI 2026 capabilities | **CONFIRMED analysis+transformation — NOT a closer** | JANUS Studio = "fully automated assessment, transformation" (thinkcomputers.org Jun 17 2026); testing customer-supplied in Northrop Grumman REMIS case (sciencedirect.com) | Date-stamp row 13 why-open; no structural change |

**Net registry effect (for maintainer; file not edited by me per rules):** 1 follow-up resolved-CLOSED (#4, closers named); 1 gate fired with a narrowed re-frame (#1 → parityrun Goal 3 amendment); 2 items strengthened-open (#2 row-13 append; #6 date-stamp); 1 item narrowed and demoted (#3); 1 item stays unverified with a method change (#5).

## Quota / deadline notes

- 13 web_search calls / 13 raw files, 1 junk-retry (q12→q12b), **0 hard 429/400 failures** — the first clean-ratelimit pass across V1–V4; stagger and 15–25 s sleeps held. Search quality up vs V1–V3: ~10 usable sets, ~2 junk/mixed (q02, q12), no recurring OSRS artifact this window.
- Format quirk: all results arrived with empty `title` fields (URL+snippet+date intact) — harmless but worth flagging to whoever owns the search tooling, alongside the chronic 429 pattern other agents hit.
- Unspent: 2 of 3 model-EOL phrasings (quota went to the Goal 3 gate by mission priority); targets 5 and 6 got single queries each (both sufficient for their verdicts, TSRI after one retry).
- Undated items: Arbutus site/whitepaper, datachecks.io, nextpathway.com, AWS, getmaxim, cequence, api7, coderio method piece, Fiddler/Salesforce docs — live vendor pages dated by access (2026-09-30); dated claims carry their source dates inline.
