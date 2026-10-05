# SVX Gap Registry — the living ranked list

**This is the only handshake point between research and products.**
Research agents update it; product agents build from it. The report
(Table 4, Chapter 10) is the dated snapshot; this file is the living
version. Status conventions are defined in
[`AGENT-MISSION.md`](../AGENT-MISSION.md).

Last full verification: **2026-09-30** (wave 2: gaps #2–#5 re-verified
plus all six never-searched verticals). Rows #6–#12 last verified
2026-09 — re-verify before building. The AI-infrastructure rows move
fastest.

| # | Opportunity | Lens | Why the field is open | First ship | Status | Last verified |
|---|--------------|------|----------------------|------------|--------|---------------|
| 1 | Evals-in-CI adapter | AI infra | Eval platforms monetize dashboards, not the CI gate; no agreed green/red semantics exist | GitHub Action wrapping existing eval suites | **BUILT** — [svx-evalgate](https://github.com/srivtx/svx-evalgate) v2.1.0; R11 (2026-09-30) flagged the **provider-axis portability extension** as the product's next natural surface — see evalgate `AGENT-GOALS.md` Goal 6 | 2026-09-30 |
| 2 | AI-code verification ledger | Links | No attestation standard for code authorship; regulation creating demand. R12: EU AI Act Art. 50 duties live since 2026-08-02; attribution exists only as telemetry (Typo, Port, larridin) — no attestations, no PR-badge product | OSS CLI + PR badge | OPEN | 2026-09-30 |
| 3 | Integration observability proxy | Plumbing | iPaaS monetizes volume, not reliability; nobody watches post-setup. R12: edges being-closed — Notilens + Watchflow. **V3 (2026-09-30): Notilens confirmed a real shipped product** (real-time fail+silence detection for n8n/Zapier/Make, free tier, Android app, paid ladder — notilens.com, live 2026-09-30) but **alerting-only, no replay**; demand intact (n8n error handling still DIY — synkrai.com Jul 6 2026). Gap narrows to read-only proxy **+ replay** against an unproven freemium incumbent | Read-only proxy with replay | OPEN (being-closed at edges) | 2026-09-30 |
| 4 | Self-verifying docs (doc tests) | Tooling/Links | Freshness tools measure age, not truth; RAG made rot worse. R12: 2026 doc-tool market is 100% AI generators — zero verification tools in any 2026 listicle. **2026-10-04 (direct GitHub read): Doc Detective verified ALIVE** — 134 stars, v4.38.1 (Aug 2026), commits through Oct 2026, agent-tools offshoot (Sep 2026) — the OSS framework exists and is maintained; gap narrows to the **commercial/adoption layer** (hosted CI doc verification, RAG-rot detection), not a README checker that collides with it | Hosted doc-verification CI service, OSS-first | OPEN (narrowed — commercial layer) | 2026-10-04 |
| 5 | Flaky-test root-cause repair | Tooling | Everyone detects and retries; nobody diagnoses or fixes. R12: Sep-2026 roundups still categorize the space as "detection". **V3: Trunk now live-markets "detect, quarantine, and eliminate flaky tests automatically"** + flake-aware merge queue (trunk.io 2026-09-30; single-source report of an AI root-cause agent — zenml.io); Launchable stays detection/selection (similarlabs Feb 27 2026). Platform-locked end being-closed; open slice narrows to **platform-neutral diagnosis filing fix PRs** | CI plugin filing diagnosis PRs | OPEN (being-closed at platform-locked end) | 2026-09-30 |
| 6 | CRM as observation system | Categories | 79% of data never entered; entry-system model is structurally dead | Call capture to structured fields, rep-first | OPEN | 2026-09 |
| 7 | AI FinOps allocation and guardrails | AI infra | Token counters everywhere; allocation and runaway-agent policy nowhere | OSS engine on gateway/OTel data | OPEN | 2026-09 |
| 8 | Permission census scanner | Plumbing | SCIM is enterprise-gated; permission graphs invisible | Headless-browser audit crawler | OPEN | 2026-09 |
| 9 | Spec-to-test trace linter | Links | SDD surge is one-directional; return path unchecked | GitHub Action for SDD repos | OPEN | 2026-09 |
| 10 | Flat-priced small-team observability | Tooling | Enterprise pricing punishes small teams; 30+ alternatives, no winner | One binary, one price, OTel-native | OPEN | 2026-09 |
| 11 | Construction sub-tier estimating | Unsexy | Tools priced for GCs; 85% of estimating still in Excel | One trade, camera takeoff, association channel | OPEN | 2026-09 |
| 12 | Excel absorption layer | Plumbing | Killers demand rebuilds; nobody absorbs the workbook | Schema + audit log around the live file | OPEN | 2026-09 |
| 13 | Legacy differential-validation harness | Plumbing / AI infra | Translation is commoditized (watsonx Z, Amazon Q Transform, Copilot for IBM Z) but validation is the bottleneck: 70% of mainframe exits fail, 80% of migrations miss deadlines on delayed testing; Mechanical Orchard's Imogen owns the method but sells a platform, not a harness; AveriSource/TSRI sell analysis+transformation; **no vendor-neutral capture→replay→deterministic-compare harness is sold to the fixed-price SIs who carry the risk**. **V1 kill pass (2026-09-30): no standalone parallel-run/capture-replay/differential product in 7 phrasings across 3 passes; BMC AMI DevX Total Test + Broadcom automated testing named and bounded (on-platform z/OS DevOps scope, not migration-equivalence; Forrester TEI 33% change-failure reduction proves testing pays on-platform while the cross-system version is unowned); Amazon Q Transform validation resolved as embedded in its proprietary pipeline+runtime. Build gate: verify Imogen's AWS Marketplace listing "Rhino Agentic Mainframe Modernization" — if software SKU, wedge shifts to vendor-neutral/works-with-any-engine**. **2026-10-04 gate RESOLVED (direct browser read): "Imogen by Mechanical Orchard" = private-offer SaaS, harness embedded ("automates a rigorous testing harness… byte-for-byte equivalence"), Thoughtworks + Perficient partner listings alongside; MO's funnel keeps client code in MO-controlled environments — the row stays OPEN, narrowed to the engine-agnostic / SI-owned / any-target slices Imogen structurally cannot serve; V4 killed the standalone VSAM/DB2 reconciliation slice (Arbutus Analyzer + DataChecks.io) — see svx-parityrun `docs/gate-log.md` | OSS core (JCL batch first): capture→replay→deterministic compare; SI channel, fixed-price risk framing | **PRODUCTIZED** — [svx-parityrun](https://github.com/srivtx/svx-parityrun) task brief + CI shipped 2026-09-30, gates resolved 2026-10-04; OPEN, narrowed to vendor-neutral slices | 2026-10-04 |
| 14 | Home-care back-office agent layer | Unsexy / overlay | A human-outsourcing industry operates *inside* the software (BPOs sell "Remote AlayaCare Outsourcing" — customers hiring humans to run the software IS the gap); caregiver turnover ~75%/yr flat for years; buyers purchase "audit readiness" while caregivers suffer the data entry (buyer≠user in pure form); Axxess absorbed AI notes for skilled home health only; AI-native challenger Careswitch is capital-light and demands platform switching; **API gate passes**: AlayaCare + AxisCare have public APIs (Axxess excluded — CEHRT-only endpoints). **V2 kill pass (2026-09-30): workaround priced $700–$1,000/mo per offshore AlayaCare VA (onlinejobs.ph Mar 7 2026); AxisCare API vendor-confirmed + live third-party production integration importing caregiver records (support.patientrewardshub.com Sep 3 2026); Sandata closed to overlays (EVV API serves states/vendors only — supergood.ai F grade); AxisCare announced in-house 2026 AI automation (Jun 15 2026) = absorption clock. Platform order flips to AlayaCare-first (gated on one endpoint-depth pass); sub-$700/mo pricing; do NOT build intake (sagecare.ai Mar 25 2026) or scheduling optimization (on AxisCare's own roadmap)**. **2026-10-04 gates RESOLVED (direct reads): API gate PASSED decisively — developer.alayacare.com documents 397 endpoints incl. EVV records, visit/task/schedule CRUD, write paths (`post_visits-{id}-notes`, `patch_visits`, `put_visits-lock`); absorption gate FIRES partially — AlayaCare announced agentic AI / AI Form Assistant / Clinical Agent (Mar–May 2026, "reclaim 80% of time and costs") — clock now runs on BOTH platforms; strategic core re-frames to cross-platform neutrality (the slice no incumbent will copy) — see svx-careops `docs/gate-log.md` | Read-only AlayaCare integration drafting EVV-exception fixes + billing-ready notes for one-person approval; HCAOA/franchise channels, VA firms as channel | **PRODUCTIZED** — [svx-careops](https://github.com/srivtx/svx-careops) task brief + CI shipped 2026-09-30, gates resolved 2026-10-04; OPEN, narrowing — cross-platform slice | 2026-10-04 |
| 15 | Unified consumer money-dates radar | **Consumer (new lens, R16)** | The subscription economy's model *depends* on forgetting (negative-option defaults). Quantified pools: $21–23B unspent gift cards (47% of US adults, avg $175–187); avg sub spend $1,080/yr; 62–70% keep paying for subs they forgot to cancel; 80% of store cards with 0% APR carry deferred-interest clawback (WalletHub via CNBC Dec 2025). Incumbents: bank-linked fee'd leader (Rocket Money — premium-fee complaint record, bank link required) or fragmented single-class mobile apps (Subby/ReSubs/Finny/Bobby/SubTracky = subscriptions-only; VoucherCue = gift cards iOS; one iOS warranty tracker) — **no unified local-first web PWA with $-at-risk framing exists**. Behavior proof: food-expiry apps (NoWaste/Fango) thrive — consumers adopt expiry trackers for vegetables, not yet for money. Platform absorption bounded to platform-billed subs (Apple receipts don't cover Netflix/gym/gift cards/warranties/APRs/IDs/domains). **R16 naming record: ExpiryRadar, DueDay, Unlapse, NeverDue all taken; PocketVeto clean** | Local-first PWA (no account, no bank link): one radar for every money date + live $-at-risk ticker + cancel/claim/redeem/payoff playbooks; MIT OSS | **PRODUCTIZED** — [pocketveto](https://github.com/srivtx/pocketveto) v1.0.0 shipped same day as the research pass (2026-10-05) | 2026-10-05 |

## Searched-and-closed candidates (kill-list outcomes)

These candidates were attacked and died — do not re-open without new
evidence. Closers are named. This is the system working: a gap closed
by the market is a successful finding. Full evidence in the
[`research/track-reports/`](../research/track-reports/) files cited.

| Candidate | Closed by | Track |
|---|---|---|
| Small-shop FAI/AS9102/PPAP packet generation | Ideagen QC (ex-InspectionXpert), SOLIDWORKS Inspection, 1factory, High QA, QA-Report (₹399–$500/mo bracket) | R6, R13a |
| Truck-stock/parts inventory overlay for cheap FSM tier | Ply (truck/warehouse/supplier/job/FSM/accounting) + Jobber native tracking + FieldPulse | R7, R13a |
| SMB supplier-communication layer (as drafted) | SourceDay (now Medius P2P) + Anvyl (now Sage Supply Chain Intelligence); SMB-priced slice = pricing question → watchlist | R10, R13b |
| Better job-shop ERP | ProShop, Fulcrum, Odoo + partner ecosystem | R6 |
| Shop-floor data capture / digital travelers / OEE monitoring | MachineMetrics, Guidewheel, Datanomix, SensrTrx, Mingo, Scytec, L2L, MaintainX (crowded, funded) | R6 |
| Maintenance/CMMS for small manufacturers | MaintainX, Augury, UpKeep | R6 |
| Professional estimating for machine shops | Paperless Parts (ITAR-compliant, category leader) | R6 |
| CMMC compliance-as-software | active vCISO/consultant services market | R6 |
| Mid-tier FSM platform ("the missing middle") | Fieldy, Contractor+, QuoteIQ, Sera (challenger war) | R7 |
| Flat-rate price books; QuickBooks invoice sync | table stakes at every tier / solved feature-matrix item | R7 |
| ServiceTitan exit-cost advocacy | real pain, but a services play, not software | R7 |
| COBOL program inventory / dependency mapping | SMART TS XL, Compuware, Rocket + 2026 AI wave (LegacyLens, atx, Swimm) | R8 |
| COBOL-understanding copilots | Copilot for IBM Z, watsonx Code Assistant for Z, Claude Code | R8 |
| Direct-to-agency sales motion (gov modernization) | procurement moat — sell to the SIs instead | R8 |
| AI visit-note scribe (skilled home health) | Axxess Care 2.0 ambient voice-to-text (shipped) | R9 |
| Standalone EVV compliance tool | bundled in every platform | R9 |
| AI-native home-care platform | Careswitch occupies the shape (capital-light, switching-demand) | R9 |
| Generic SMB planning / multichannel inventory | Netstock, Slimstock, Cin7, Linnworks, Zoho, Orderhive (crowded $31–47/user/mo mid-tier) | R10 |
| Cheap enterprise-planning clone | fights the crowded tier, not the $380–520K/yr enterprise vacuum | R10 |
| LLM gateway / unified API / cost routing | LiteLLM, OpenRouter, Portkey, Cloudflare, Kong, Helicone, Bifrost (crowded) | R11 |
| Generic multi-provider prompt regression | promptfoo | R11 |
| Tool-schema portability layer | MCP | R11 |
| Standalone VSAM/DB2 data-migration reconciliation | Arbutus Analyzer (native DB2/IMS/ADABAS/VSAM/ISAM reads, "RECONCILE THE MIGRATION") + DataChecks.io (agent-driven output-parity, cloud-DW); residual survives only on 4 axes (automated+statistical+CI+vendor-neutral) | V4 |
| Truck-stock residual (SMB-priced slice) | Ply $8.5M strategic round (Dec 4 2025) + native Housecall Pro integration (Jan 20 2026) + SMB/free positioning (Sep 14 2026) | V5 |
| AI phone answering for trades/home services | Avoca (enterprise home-services AI) + Sameday (YC-backed) + Numa (pivoted automotive) + crowded field (Rosie/Smith.ai/Goodcall/Podium/Whippy) | V5 |
| Commissions/spiff tracking for contractors | ServiceTitan native commission tracking + Salesforce Spiff/QuotaPath SPM class; zero contractor demand voice | V5 |
| Tariff landed-cost cockpit (as drafted) | Free/crowded 2026 calculator layer (tariffstool, zonos) + Borderline Genius, iCustoms AI + comparison listicles; continuous PO-integrated alerting residual logged as low-priority | V5 |
| LLM gateway security monitoring | Absorbed by gateway tier: Bifrost audit logging, TrueFoundry compliance-grade logs (EU AI Act mapped, Jun 23 2026), llmgateway.io attestation; injection detection owned by ARMO + Azure Prompt Shields | V4 |
| Below-enterprise security/supply-chain generic layer | FOSSA down-market business tier + free CRA funnel (Aug 2025); SOC 2 automation crowded (Vanta/Drata/Secureframe/Sprinto); SMB vuln-management listicle category exists; secrets detection free-tiered; attestation ossifying into standards (SLSA/in-toto, Docker Hardened $0) | R14 |
| Education-ops tooling (sub mgmt, small-school SIS, parent comms, teacher-AI, teacher-facing IEP drafting) | Served layers: substitute mgmt $500–5K/yr/school tiers; SchoolCues $1.2K/yr budget tier vs Sycamore $4.8K; ParentSquare $3K/yr vs free ClassDojo; MagicSchool district contracts (Jul 2026); teacher-AI crowded | R15 |
| Consumer single-class trackers (standalone warranty vault, gift-card-only tracker, meal planner, photo dedup, freelancer invoice chaser, family doc vault) | R16 scoring matrix: unified radar 33/35 vs best single-class 25/35 (gift cards); each single-class slice already has an app or a structural weakness (trust barrier, email infra, desktop-only) | R16 |
| Consumer tracker names: ExpiryRadar, DueDay, Unlapse, NeverDue, Vigilo | taken (Play/App Store apps or GitHub claims — see R16 §10) | R16 |

## Research backlog

### Never-searched verticals — cleared 2026-09-30 (wave 2), 2026-10-04 (wave 4)

- [x] Small-manufacturing ERP/MES — searched (R6 + R13a + V5): middle is served (ProShop/Katana tier), shop-floor capture crowded, FAI killed by existing class; Katana-sentiment check RESOLVED (complaint axis is pricing, not margin visibility — weakens the margin-overlay demand case); margin overlay remains the one weak survivor → user-forum reads
- [x] Field service (HVAC/plumbing) — searched (R7 + R13a + V5): truck-stock overlay killed by Ply + Jobber native (Ply residual confirmed dead by V5: $8.5M round + Housecall Pro integration); mid-tier is a challenger war; AI answering closed (Avoca/Sameday/Numa+field); commissions closed (ServiceTitan native); Workiz/ST tiers resolved (missing middle real and priced — stays killed); warranty workflows demoted (OEM portals + human adjudication; no third-party software, no pain voice — next step HVAC-talk forum reads)
- [x] Government legacy (COBOL) modernization — searched (R8 + R13b + V1 + 2026-10-04 gates): **row 13 confirmed-open, narrowed** — vendor-neutral harness slices (Imogen SaaS listing verified; TSRI not a closer; no differential-OSS to reuse)
- [x] Elder care / home healthcare operations — searched (R9 + R13b + V2 + 2026-10-04 gates): **row 14 confirmed-open, narrowed** — cross-platform slice (AlayaCare 397-endpoint API verified; absorption clock on both platforms)
- [x] SMB supply chain — searched (R10 + R13b + V5): supplier-communication killed (SourceDay/Anvyl); tariff cockpit killed as drafted; container visibility → low-priority residual
- [x] Model portability across LLM vendors — searched (R11 + V4): resolved as gap-#1 provider-axis extension; model-EOL tracker being-closed at platform-locked end (Fiddler/Tencent/Salesforce) — cross-vendor frozen-baseline slice noted on evalgate Goal 6
- [x] Security / supply-chain (below enterprise) — searched (R14): **vertical closed at the generic layer**; one watch-list item (CRA-response tooling for small vendors — duties live Sep 11 2026, race already started: venvera listicle Jul 2026, Attestra, FOSSA funnel) → 2-quarter re-check
- [x] Education / school operations — searched (R15): **near-closed**; one thin survivor (IEP compliance-layer overlay — buyer≠user pure form, FTE-labor workaround, but fails the R9 row bar: no priced BPO industry, API/absorption unverified) → two direct-read follow-ups

### Still-unverified (next missions — run the owed kill-searches)

Priority order by consequence. Wave-4 (V4/V5/R14/R15 + direct reads, 2026-10-04) and wave-5 pivot (R16, 2026-10-05) outcomes applied — most items are now resolved; the list is short and honest:

- [ ] **pocketveto competitive watch**: ReSubs/Subby/SubTracker feature drift toward multi-class tracking or web PWA (direct reads of their listing pages, 1-quarter cadence) — R16
- [ ] **pocketveto notification-honesty audit**: verify Web Notification + service-worker behavior on iOS Safari vs Android Chrome vs desktop (direct device testing) — R16
- [ ] **IEP compliance-overlay gates** (R15's thin survivor — direct reads, not search): Frontline/PowerSchool/SEAS product pages for 2026 AI features; r/specialed thread 1qkvqrs; IEP-coordinator FTE salary as the price anchor — R15
- [ ] **CRA-response tooling for small vendors** (watch-list — duties live since Sep 11 2026; re-check in 2 quarters for consolidation/movement: venvera, Attestra, FOSSA) — R14
- [ ] Per-job margin overlay (weak survivor, 2 fresh phrasings exhausted the product-query angle — next pass hits user forums: practicalmachinist, r/manufacturing) — R6/R13a/V5
- [ ] Carrier/Trane OEM warranty workflows (demoted — next step is HVAC-talk forum reads, not search) — R13a/V5
- [ ] Paperless Parts pricing (retired from search — 3 strikes; next: direct reads of review pages + the practicalmachinist thread) — R13a/V5
- [ ] WellSky PC API depth (careops second platform — read vendor docs directly) — V2
- [ ] EU AI Act Art. 50 code-authorship guidance (gap #2 scope) — R12
- [ ] SI fixed-price-risk framing (direct reads of SI/procurement literature, not search) — V4
- [ ] Model-migration war stories (HN/engineering-blog evidence) — R11
- [ ] EU AI Act + model-EOL cross-vendor frozen-baseline slice (evalgate Goal 6 follow-on capability — only after portability lands) — V4

**Retired from web search** (3 failed query runs each — resolve by direct product-page/literature reads, not more queries):
- Family-communication layer for home care (row-14 adjacent) — R9/R13b/V2
- Caregiver documentation-time quantification — R9/R13b/V2
- EVV-exception standalone solver landscape — R12/V2
- "Parallel run" phrasing family (mainframe) — solved 2026-10-04 via agent-browser direct read — R8/R13b/V1
- Ply pricing — solved V5 via funding/integration evidence — R13a/V5
- Doc Detective momentum — solved 2026-10-04 via GitHub API read — R12/V3

**Resolved this wave (2026-10-04):** Imogen marketplace listing (private-offer SaaS, harness embedded — row 13 narrowed); AlayaCare endpoint depth (397 endpoints, write paths — row 14 gate passed); AlayaCare absorption (fires — agentic AI/Form Assistant/Clinical Agent Mar–May 2026); VSAM/DB2 standalone (closed — Arbutus/DataChecks); differential-testing OSS (confirmed none for mainframe); TSRI (not a closer); model-EOL tracker (being-closed platform-locked, cross-vendor slice → evalgate note); LLM gateway security (closed — absorbed); Ply residual (closed — $8.5M + HCP); AI answering (closed); commissions (closed); tariff cockpit (closed as drafted); Workiz/ST tiers (resolved — missing middle priced, stays killed); Katana sentiment (resolved — pricing axis, weakens margin-overlay demand); Doc Detective (alive — gap #4 narrows to commercial layer); SI fixed-price framing (partial: $1,000–2,200/function-point single-source).

- [x] **Consumer money-dates (owner-directed pivot)** — searched (R16, 2026-10-05): **row 15 opened and productized same day** (pocketveto); 6 alternative consumer candidates scored and killed; 5 candidate names killed by collision checks

Candidate future lenses (unstarted): accessibility, climate-tech
software, developer economics. (Security/supply-chain and education
tooling were cleared 2026-10-04; the consumer money-dates lens was
opened and productized 2026-10-05 — see above.)

## Process tooling (2026-10-04)

Search agents should use [`tools/svxsearch.py`](../tools/svxsearch.py)
(junk detection, query manifest, retry discipline, pacing) and follow
[`tools/SEARCH-PLAYBOOK.md`](../tools/SEARCH-PLAYBOOK.md) — the
accumulated degradation map, direct-read recipes, and the 3-strike
phrasing-retirement rule, encoded from passes R1-R15/V1-V5.

## Change log for this file

| Date | Change | Agent |
|------|--------|-------|
| 2026-09 | Registry seeded from report Table 4; gap #1 marked BUILT (svx-evalgate v2.1.0) | main |
| 2026-09-30 | File created; backlog + lens candidates added | main |
| 2026-09-30 | Wave 2: gaps #2–#5 re-verified (all OPEN; #3 being-closed at edges — Notilens/Watchflow); rows 13–14 added OPEN-NEW (differential-validation harness; home-care back-office overlay); 22 candidates searched-and-closed with closers named; model-portability backlog resolved as gap-#1 provider-axis extension; all six never-searched verticals cleared; 20 still-unverified follow-ups seeded | main + R6–R13b |
| 2026-09-30 | Wave 3 (V1/V2/V3): row 13 verified OPEN (medium-high) + PRODUCTIZED as svx-parityrun; row 14 verified OPEN (narrowing, absorption clock) + PRODUCTIZED as svx-careops; gap #3 amended (Notilens real, no replay); gap #5 amended (Trunk being-closed at platform-locked end); Sandata closed to overlays; 3 query phrasings retired from search (3 failed runs each); follow-up list re-prioritized | main + V1–V3 |
| 2026-10-04 | Wave 4 (V4/V5/R14/R15 + direct reads): row-13 and row-14 build gates RESOLVED (Imogen = private-offer SaaS, harness embedded → vendor-neutral slices; AlayaCare = 397 endpoints, write paths; AlayaCare absorption fires Mar–May 2026 → cross-platform core); gap #4 narrowed (Doc Detective alive — commercial layer); VSAM/DB2 standalone, Ply residual, AI answering, commissions, tariff cockpit, gateway security, security/supply-chain generic layer, education-ops vertical all closed with closers named; model-EOL cross-vendor slice noted on evalgate Goal 6; two new lenses cleared (R14 closed, R15 near-closed with IEP thin survivor); search tooling shipped (svxsearch.py + SEARCH-PLAYBOOK.md); follow-up list reduced to 10 honest items | main + V4/V5/R14/R15 |

When updating: set the status, update last-verified, add a row to this
change log. One-line justification for any reordering.
