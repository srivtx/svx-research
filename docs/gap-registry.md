# SVX Gap Registry — the living ranked list

**This is the only handshake point between research and products.**
Research agents update it; product agents build from it. The report
(Table 4, Chapter 10) is the dated snapshot; this file is the living
version. Status conventions are defined in
[`AGENT-MISSION.md`](../AGENT-MISSION.md).

Last full verification: **2026-09** (original research window).
Re-verify any row before building — the AI-infrastructure rows move
fastest.

| # | Opportunity | Lens | Why the field is open | First ship | Status | Last verified |
|---|--------------|------|----------------------|------------|--------|---------------|
| 1 | Evals-in-CI adapter | AI infra | Eval platforms monetize dashboards, not the CI gate; no agreed green/red semantics exist | GitHub Action wrapping existing eval suites | **BUILT** — [svx-evalgate](https://github.com/srivtx/svx-evalgate) v2.1.0 | 2026-09 |
| 2 | AI-code verification ledger | Links | No attestation standard for code authorship; regulation creating demand | OSS CLI + PR badge | OPEN | 2026-09 |
| 3 | Integration observability proxy | Plumbing | iPaaS monetizes volume, not reliability; nobody watches post-setup | Read-only proxy with replay | OPEN | 2026-09 |
| 4 | Self-verifying docs (doc tests) | Tooling/Links | Freshness tools measure age, not truth; RAG made rot worse | README checker, OSS-first | OPEN | 2026-09 |
| 5 | Flaky-test root-cause repair | Tooling | Everyone detects and retries; nobody diagnoses or fixes | CI plugin filing diagnosis PRs | OPEN | 2026-09 |
| 6 | CRM as observation system | Categories | 79% of data never entered; entry-system model is structurally dead | Call capture to structured fields, rep-first | OPEN | 2026-09 |
| 7 | AI FinOps allocation and guardrails | AI infra | Token counters everywhere; allocation and runaway-agent policy nowhere | OSS engine on gateway/OTel data | OPEN | 2026-09 |
| 8 | Permission census scanner | Plumbing | SCIM is enterprise-gated; permission graphs invisible | Headless-browser audit crawler | OPEN | 2026-09 |
| 9 | Spec-to-test trace linter | Links | SDD surge is one-directional; return path unchecked | GitHub Action for SDD repos | OPEN | 2026-09 |
| 10 | Flat-priced small-team observability | Tooling | Enterprise pricing punishes small teams; 30+ alternatives, no winner | One binary, one price, OTel-native | OPEN | 2026-09 |
| 11 | Construction sub-tier estimating | Unsexy | Tools priced for GCs; 85% of estimating still in Excel | One trade, camera takeoff, association channel | OPEN | 2026-09 |
| 12 | Excel absorption layer | Plumbing | Killers demand rebuilds; nobody absorbs the workbook | Schema + audit log around the live file | OPEN | 2026-09 |

## Research backlog (never-searched territory)

Verticals identified during the original research but never searched —
all attempts died on rate limits. Highest-value unexplored ground:

- [ ] Small-manufacturing ERP/MES
- [ ] Field service (HVAC/plumbing) operations software
- [ ] Government legacy (COBOL) modernization tooling
- [ ] Elder care / home healthcare operations
- [ ] SMB supply chain
- [ ] Model portability across LLM vendors

Candidate future lenses: security/supply-chain, accessibility,
climate-tech software, education tooling, developer economics.

## Change log for this file

| Date | Change | Agent |
|------|--------|-------|
| 2026-09 | Registry seeded from report Table 4; gap #1 marked BUILT (svx-evalgate v2.1.0) | main |
| 2026-09-30 | File created; backlog + lens candidates added | main |

When updating: set the status, update last-verified, add a row to this
change log. One-line justification for any reordering.
