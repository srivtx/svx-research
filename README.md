# SVX Research — The Missing Software

**SVX Industry Gap Analysis 2025–2026** · five parallel research tracks into what the software industry has not built.

![SVX](https://img.shields.io/badge/SVX-Research-298959?style=flat-square)
![Report](https://img.shields.io/badge/report-27%20pages%20%2F%20PDF-456454?style=flat-square)
![Tracks](https://img.shields.io/badge/tracks-R1%E2%80%93R5-4fbb85?style=flat-square)
![Evidence](https://img.shields.io/badge/evidence-83%20raw%20search%20sets-77817c?style=flat-square)

---

## What this is

In September 2026, SVX Research ran a multi-agent investigation into a single question, asked at the level of the whole industry:

> **What is the software industry missing?**

Not "which product could be incrementally better" — which tools, connective links, and whole categories have *never been built*, or have been built *so badly* that they function as open wounds. The research deliberately prioritized gaps where nobody has done the work, or where everyone has done it badly, over crowded markets with strong incumbents.

Five independent research agents executed roughly sixty web searches, harvested evidence predominantly from 2024–2026, and discarded every candidate gap that turned out to be already served by a strong solution. **Everything in the final report survived a deliberate attempt to kill it.**

## Repository layout

| Path | Contents |
|------|----------|
| [`report/`](report/) | The final deliverable: `SVX-Industry-Gap-Analysis-2025-2026.pdf` (27 pages, A4, Edition 2) + cover HTML source |
| [`research/track-reports/`](research/track-reports/) | The five full track reports (R1–R5, ~12,800 words total) |
| [`research/raw-search-results/`](research/raw-search-results/) | The raw search-result corpus (83 JSON sets) — the auditable evidence base |
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

## Three headline conclusions

1. **The industry has a translation problem, and AI just changed the economics of it.** Nearly every durable gap found — design to code, spec to test, docs to runtime, prose to formal properties — stayed unbuilt because translating between two representations cost more than the failures it prevented. That translation cost collapsed in 2025–2026, which is why so many decades-old gaps suddenly became buildable.

2. **The deepest gaps are ownership vacuums, not technology vacuums.** Integrations break silently because nobody is paid to watch them; documentation rots because no test suite goes red; permission graphs drift because identity syncs accounts, not access. Connectivity exists almost everywhere — ownership does not.

3. **Buyer-user mismatch is the one pattern AI does not fix.** In hated categories (CRM entry, expense reports, timesheets), the person who suffers is not the person who buys. The viable wedge is bottom-up: sell the suffering user a tool that removes their work, then sell the clean exhaust data to the buyer.

## The ranked shortlist (top 5 of 12)

Full table in Chapter 10 of the report. Field positions as of September 2026 — re-verify before building.

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
