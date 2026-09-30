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
| 3 | Integration observability proxy | Plumbing | iPaaS monetizes volume, not reliability; nobody watches post-setup. R12: edges being-closed — Notilens (n8n/Make/Zapier failure detection, Apr 2026, depth unverified) + Watchflow (n8n self-monitoring); **verify Notilens depth before building** | Read-only proxy with replay | OPEN (being-closed at edges) | 2026-09-30 |
| 4 | Self-verifying docs (doc tests) | Tooling/Links | Freshness tools measure age, not truth; RAG made rot worse. R12: 2026 doc-tool market is 100% AI generators — zero verification tools in any 2026 listicle; kill attempt was search-degraded, re-check Doc Detective momentum | README checker, OSS-first | OPEN | 2026-09-30 |
| 5 | Flaky-test root-cause repair | Tooling | Everyone detects and retries; nobody diagnoses or fixes. R12: Sep-2026 roundups still categorize the space as "detection"; ML effort goes to auto-heal, not diagnosis | CI plugin filing diagnosis PRs | OPEN | 2026-09-30 |
| 6 | CRM as observation system | Categories | 79% of data never entered; entry-system model is structurally dead | Call capture to structured fields, rep-first | OPEN | 2026-09 |
| 7 | AI FinOps allocation and guardrails | AI infra | Token counters everywhere; allocation and runaway-agent policy nowhere | OSS engine on gateway/OTel data | OPEN | 2026-09 |
| 8 | Permission census scanner | Plumbing | SCIM is enterprise-gated; permission graphs invisible | Headless-browser audit crawler | OPEN | 2026-09 |
| 9 | Spec-to-test trace linter | Links | SDD surge is one-directional; return path unchecked | GitHub Action for SDD repos | OPEN | 2026-09 |
| 10 | Flat-priced small-team observability | Tooling | Enterprise pricing punishes small teams; 30+ alternatives, no winner | One binary, one price, OTel-native | OPEN | 2026-09 |
| 11 | Construction sub-tier estimating | Unsexy | Tools priced for GCs; 85% of estimating still in Excel | One trade, camera takeoff, association channel | OPEN | 2026-09 |
| 12 | Excel absorption layer | Plumbing | Killers demand rebuilds; nobody absorbs the workbook | Schema + audit log around the live file | OPEN | 2026-09 |
| 13 | Legacy differential-validation harness | Plumbing / AI infra | Translation is commoditized (watsonx Z, Amazon Q Transform, Copilot for IBM Z) but validation is the bottleneck: 70% of mainframe exits fail, 80% of migrations miss deadlines on delayed testing; Mechanical Orchard's Imogen owns the method but sells a platform, not a harness; AveriSource/TSRI sell analysis+transformation; **no vendor-neutral capture→replay→deterministic-compare harness is sold to the fixed-price SIs who carry the risk** | OSS core (JCL batch first): capture→replay→deterministic compare; SI channel, fixed-price risk framing | OPEN-NEW | 2026-09-30 |
| 14 | Home-care back-office agent layer | Unsexy / overlay | A human-outsourcing industry operates *inside* the software (BPOs sell "Remote AlayaCare Outsourcing" — customers hiring humans to run the software IS the gap); caregiver turnover ~75%/yr flat for years; buyers purchase "audit readiness" while caregivers suffer the data entry (buyer≠user in pure form); Axxess absorbed AI notes for skilled home health only; AI-native challenger Careswitch is capital-light and demands platform switching; **API gate passes**: AlayaCare + AxisCare have public APIs (Axxess excluded — CEHRT-only endpoints) | Read-only AlayaCare/AxisCare integration drafting EVV-exception fixes + billing-ready notes for one-person approval; HCAOA/franchise channels, VA firms as channel | OPEN-NEW | 2026-09-30 |

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

## Research backlog

### Never-searched verticals — cleared 2026-09-30 (wave 2)

- [x] Small-manufacturing ERP/MES — searched (R6 + R13a): middle is served (ProShop/Katana tier), shop-floor capture crowded, FAI killed by existing class; one weak survivor (per-job margin overlay) → follow-up list
- [x] Field service (HVAC/plumbing) — searched (R7 + R13a): truck-stock overlay killed by Ply + Jobber native; mid-tier is a challenger war; nothing open enough to row
- [x] Government legacy (COBOL) modernization — searched (R8 + R13b): mostly killed (procurement moat, incumbents) but **row 13 confirmed-open** — differential-validation harness sold to SIs
- [x] Elder care / home healthcare operations — searched (R9 + R13b): **row 14 confirmed-open** — back-office agent layer (API gate passed on AlayaCare/AxisCare); AI scribes killed (Axxess absorbed)
- [x] SMB supply chain — searched (R10 + R13b): supplier-communication killed as drafted (SourceDay/Anvyl); tariff cockpit + container visibility → follow-up list
- [x] Model portability across LLM vendors — searched (R11): **resolved as a gap-#1 provider-axis extension (evalgate), not a new repo** — request-format portability is closed (gateways/MCP/promptfoo), behavior portability is not

### Still-unverified (next missions — run the owed kill-searches)

Priority order by consequence:

- [ ] Per-job margin overlay on shelfware ERP + Excel (weak evidence, 2–3 sources; kill-search owed) — R6/R13a
- [ ] Notilens product depth (gap #3 edge-closer — build/no-build input) — R12
- [ ] Ply pricing/traction (kills or revives the truck-stock residual) — R13a
- [ ] VSAM/DB2 data-migration reconciliation tooling — R8/R13b
- [ ] Family-communication layer for home care (row-14 adjacent) — R9/R13b
- [ ] Carrier/Trane OEM warranty-claim workflows — R13a
- [ ] Numa/Avoca/Sameday AI answering status — R13a
- [ ] Commissions/spiff tracking for contractors — R13a
- [ ] Workiz / ServiceTitan small-shop tier — R13a
- [ ] Paperless Parts pricing (bottom-of-market instant quoting) — R13a
- [ ] Katana/MRPeasy/Fishbowl G2/Capterra sentiment — R13a
- [ ] Caregiver documentation-time quantification — R9/R13b
- [ ] Tariff landed-cost cockpit for SMB importers — R10/R13b
- [ ] Model EOL/dependency manager ("Renovate for models") — R11
- [ ] LLM gateway security monitoring — R11
- [ ] Doc Detective 2026 status / docs-as-tests momentum (gap #4) — R12
- [ ] Trunk/Launchable feature depth (gap #5) — R12
- [ ] EU AI Act Art. 50 code-authorship guidance (gap #2 scope) — R12
- [ ] Amazon Q Transform validation story — R8/R13b
- [ ] Model-migration war stories (HN/engineering-blog evidence) — R11

Candidate future lenses (unstarted): security/supply-chain,
accessibility, climate-tech software, education tooling, developer
economics.

## Change log for this file

| Date | Change | Agent |
|------|--------|-------|
| 2026-09 | Registry seeded from report Table 4; gap #1 marked BUILT (svx-evalgate v2.1.0) | main |
| 2026-09-30 | File created; backlog + lens candidates added | main |
| 2026-09-30 | Wave 2: gaps #2–#5 re-verified (all OPEN; #3 being-closed at edges — Notilens/Watchflow); rows 13–14 added OPEN-NEW (differential-validation harness; home-care back-office overlay); 22 candidates searched-and-closed with closers named; model-portability backlog resolved as gap-#1 provider-axis extension; all six never-searched verticals cleared; 20 still-unverified follow-ups seeded | main + R6–R13b |

When updating: set the status, update last-verified, add a row to this
change log. One-line justification for any reordering.
