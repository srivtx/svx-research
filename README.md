# SVX Research — The Missing Software

**SVX Industry Gap Analysis 2025–2026** · five parallel research tracks into what the software industry has not built.

![SVX](https://img.shields.io/badge/SVX-Research-298959?style=flat-square)
![Report](https://img.shields.io/badge/report-27%20pages%20%2F%20PDF-456454?style=flat-square)
![Tracks](https://img.shields.io/badge/tracks-R1%E2%80%93R13-4fbb85?style=flat-square)
![Evidence](https://img.shields.io/badge/evidence-267%20raw%20search%20sets-77817c?style=flat-square)

---

## What this is

In September 2026, SVX Research ran a multi-agent investigation into a single question, asked at the level of the whole industry:

> **What is the software industry missing?**

Not "which product could be incrementally better" — which tools, connective links, and whole categories have *never been built*, or have been built *so badly* that they function as open wounds. The research deliberately prioritized gaps where nobody has done the work, or where everyone has done it badly, over crowded markets with strong incumbents.

Five independent research agents executed roughly sixty web searches, harvested evidence predominantly from 2024–2026, and discarded every candidate gap that turned out to be already served by a strong solution. **Everything in the final report survived a deliberate attempt to kill it.**

On **September 30, 2026**, the loop ran again: eight more agents (R6–R13) cleared all six never-searched verticals, re-verified the top registry rows, and ran the owed kill-searches on every provisional candidate. Two new rows survived (rows 13–14 in the [registry](docs/gap-registry.md)); twenty-two candidates died with their closers named — which is the method working.

## Repository layout

| Path | Contents |
|------|----------|
| [`report/`](report/) | The final deliverable: `SVX-Industry-Gap-Analysis-2025-2026.pdf` (27 pages, A4, Edition 2) + cover HTML source |
| [`research/track-reports/`](research/track-reports/) | The fourteen full track reports (R1–R13, ~41,800 words total) |
| [`research/raw-search-results/`](research/raw-search-results/) | The raw search-result corpus (267 JSON sets) — the auditable evidence base |
| [`build/`](build/) | Reproducible report build: ReportLab pipeline, chart generation, green cascade palette |
| [`docs/research-worklog.md`](docs/research-worklog.md) | The multi-agent work log — who researched what, agent by agent |
| [`AGENT-MISSION.md`](AGENT-MISSION.md) | The whole story + the continuous research loop — how agents feed this repo, how products spin out of it |
| [`docs/gap-registry.md`](docs/gap-registry.md) | The living ranked gap list — the only handshake point between research and products |
| [`AGENTS.md`](AGENTS.md) | Agent onboarding — repo mechanics, corpus rules, brand |

## The five tracks

| Track | Question | Report |
|-------|----------|--------|
| **R1** — Developer tooling | What does the daily workflow still lack? | [`R1-dev-tooling-gaps.md`](research/track-reports/R1-dev-tooling-gaps.md) |
| **R2** — Integration & data | What is broken underneath working systems? | [`R2-integration-data-gaps.md`](research/track-reports/R2-integration-data-gaps.md) |
| **R3** — Missing links | What exists on both ends but was never connected? | [`R3-missing-links.md`](research/track-reports/R3-missing-links.md) |
| **R4** — Badly-built categories | Why does hated software stay hated? | [`R4-badly-built-categories.md`](research/track-reports/R4-badly-built-categories.md) |
| **R5** — Frontier gaps | What does the AI era lack underneath it? | [`R5-frontier-gaps.md`](research/track-reports/R5-frontier-gaps.md) |

### Wave 2 (2026-09-30): the never-searched verticals + verification

| Track | Question | Report |
|-------|----------|--------|
| **R6** — Small-manufacturing ERP/MES | What do job shops actually run — and where does Excel still sit? | [`R6-small-mfg-erp-mes.md`](research/track-reports/R6-small-mfg-erp-mes.md) |
| **R7** — Field service (HVAC/plumbing) | Is there room under ServiceTitan — or above the cheap tier? | [`R7-field-service-ops.md`](research/track-reports/R7-field-service-ops.md) |
| **R8** — Government legacy (COBOL) | Is translation solved and validation not? | [`R8-gov-cobol-modernization.md`](research/track-reports/R8-gov-cobol-modernization.md) |
| **R9** — Elder care / home healthcare | What runs inside the agency back office? | [`R9-elder-care-ops.md`](research/track-reports/R9-elder-care-ops.md) |
| **R10** — SMB supply chain | What's left below the $380K/yr enterprise planners? | [`R10-smb-supply-chain.md`](research/track-reports/R10-smb-supply-chain.md) |
| **R11** — Model portability | Does my agent survive a model swap? | [`R11-model-portability.md`](research/track-reports/R11-model-portability.md) |
| **R12** — Registry recheck | Did the market close gaps #2–#5? | [`R12-registry-gaps-2-5-recheck.md`](research/track-reports/R12-registry-gaps-2-5-recheck.md) |
| **R13a/R13b** — Verification passes | The owed kill-searches on every provisional candidate | [`R13a`](research/track-reports/R13a-verification-pass.md), [`R13b`](research/track-reports/R13b-verification-pass.md) |

## Three headline conclusions

1. **The industry has a translation problem, and AI just changed the economics of it.** Nearly every durable gap found — design to code, spec to test, docs to runtime, prose to formal properties — stayed unbuilt because translating between two representations cost more than the failures it prevented. That translation cost collapsed in 2025–2026, which is why so many decades-old gaps suddenly became buildable.

2. **The deepest gaps are ownership vacuums, not technology vacuums.** Integrations break silently because nobody is paid to watch them; documentation rots because no test suite goes red; permission graphs drift because identity syncs accounts, not access. Connectivity exists almost everywhere — ownership does not.

3. **Buyer-user mismatch is the one pattern AI does not fix.** In hated categories (CRM entry, expense reports, timesheets), the person who suffers is not the person who buys. The viable wedge is bottom-up: sell the suffering user a tool that removes their work, then sell the clean exhaust data to the buyer.

## The ranked shortlist (top 5 of 12)

Full table in Chapter 10 of the report; the living version is [`docs/gap-registry.md`](docs/gap-registry.md) (now 14 rows, gaps #2–#5 re-verified 2026-09-30). Field positions as of September 2026 — re-verify before building.

| # | Opportunity | Why the field is open |
|---|-------------|----------------------|
| 1 | **Evals-in-CI adapter** | Eval platforms monetize dashboards, not the CI gate; no agreed green/red semantics exist for non-deterministic systems |
| 2 | AI-code verification ledger | No attestation standard for code authorship; regulation creating demand |
| 3 | Integration observability proxy | iPaaS monetizes volume, not reliability; nobody watches post-setup |
| 4 | Self-verifying docs | Freshness tools measure age, not truth; RAG made rot worse |
| 5 | Flaky-test root-cause repair | Everyone detects and retries; nobody diagnoses or fixes |

**Gap #1 is now being built** as the follow-on product repo: **EvalGate** — deterministic statistics for AI evals at the merge gate.

## Quantified pain (samples)

- **96%** of developers do not fully trust AI-generated code, yet only **48%** always verify it — SonarSource, Jan 2026
- **$315K** average vendor lock-in cost per enterprise migration — Kong, Jun 2026
- **79%** of opportunity data reps collect never enters the CRM — DevRev, 2026
- **85%** of construction estimating still runs in Excel — PremierCS, 2026
- **362** documented AI incidents in 2025, up from 233 in 2024
- Enterprise LLM API spend **doubled in six months**: $3.5B → $8.4B

Every statistic in the report traces to a dated source seen directly in the search corpus; none were invented or extrapolated.

## Reproducing the report

```bash
cd build
python3 gen_charts.py          # 2 charts, SVX green family (hue ~150°)
python3 build_report.py        # body PDF via ReportLab (TOC + page numbering)
node html2poster.js cover.html --output assets/cover.pdf --width 794px
python3 merge_finalize.py      # cover + body → A4-normalized final PDF
```

Requires: Python 3.12+, ReportLab, pypdf, matplotlib, Pillow, Node + Playwright (cover render).
The green cascade palette is generated with `design_engine.py palette-cascade --intent nature --mode minimal --harmony monochrome --seed 7`.

## License

MIT — see [`LICENSE`](LICENSE). The research corpus and report may be reused with attribution.
