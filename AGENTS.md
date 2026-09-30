# AGENTS.md — SVX Research

Guidance for AI agents (and humans in a hurry) working in this
repository. **Read this before changing anything.** This repo is the
evidence base and origin story for the SVX product family — treat its
integrity accordingly.

**The whole story and the continuous research loop live in
[`AGENT-MISSION.md`](AGENT-MISSION.md)** — how research agents feed
this repo and how product sub-agents spin new repos out of it. **The
living ranked gap list lives in
[`docs/gap-registry.md`](docs/gap-registry.md)** — the only handshake
point between research and products; update it when either side moves.

## What this repo is

The corpus and deliverable of a September 2026 multi-agent investigation
into a single industry-level question:

> **What is the software industry missing?**

Not "which product could be incrementally better" — which tools,
connective links, and whole categories have *never been built*, or were
built *so badly* they function as open wounds. The research deliberately
prioritized gaps where nobody has done the work, or everyone has done
it badly, over crowded markets with strong incumbents.

Five independent research agents (R1–R5) ran roughly sixty web searches,
harvested evidence predominantly from 2024–2026, and **discarded every
candidate gap that turned out to be already served by a strong
solution** — the kill-list discipline. Everything in the final report
survived a deliberate attempt to kill it.

The repo's most important downstream artifact is a product: **gap #1
(evals-in-CI adapter) is built as [svx-evalgate]
(https://github.com/srivtx/svx-evalgate)** — deterministic statistics
gate for AI evals, v2.1.0, 264 tests, zero dependencies.

## Repository map

| Path | Contents |
|---|---|
| `report/` | Final deliverable: `SVX-Industry-Gap-Analysis-2025-2026.pdf` (27pp, A4, Edition 2) + cover HTML source |
| `research/track-reports/` | The five full track reports R1–R5 (~12,800 words) — the analysis layer |
| `research/raw-search-results/` | 83 raw search-result JSON sets — the auditable evidence layer (never edit these) |
| `build/` | Reproducible report pipeline: charts (matplotlib), body (ReportLab), cover (Playwright via html2poster.js), merge (pypdf) |
| `docs/research-worklog.md` | Multi-agent work log — who researched what, in order |

Layer discipline: **raw search JSON → track reports → final report.**
Each layer only summarizes the layer below it. If a claim can't be
traced downward to a dated source in the corpus, it doesn't belong in
the report. No statistic was ever invented or extrapolated — this rule
is the repo's credibility and must survive every future edit.

## The five tracks

- **R1 — Developer tooling:** what the daily workflow still lacks.
- **R2 — Integration & data:** what is broken underneath working systems.
- **R3 — Missing links:** what exists on both ends but was never connected.
- **R4 — Badly-built categories:** why hated software stays hated.
- **R5 — Frontier gaps:** what the AI era lacks underneath it.

Headline conclusions (full argument in the report):

1. The industry has a **translation problem**, and AI just changed the
   economics of it — decades-old gaps became buildable when translation
   cost between representations collapsed in 2025-2026.
2. The deepest gaps are **ownership vacuums**, not technology vacuums.
3. **Buyer-user mismatch** is the one pattern AI does not fix; the
   viable wedge is bottom-up (sell the suffering user, then the clean
   exhaust data to the buyer).

Ranked shortlist (top 5 of 12, full table in Chapter 10): evals-in-CI
adapter (#1, now built as EvalGate), AI-code verification ledger,
integration observability proxy, self-verifying docs, flaky-test
root-cause repair. **Field positions are as of September 2026 —
re-verify before building any of them; this is a dated snapshot, not a
permanent truth.**

## Rebuilding the report

```bash
cd build
python3 gen_charts.py          # 7 charts, SVX green family
python3 build_report.py        # body PDF via ReportLab (TOC + numbering)
node html2poster.js cover.html --output assets/cover.pdf --width 794px
python3 merge_finalize.py      # cover + body → A4-normalized final PDF
```

Requires Python 3.12+, ReportLab, pypdf, matplotlib, Pillow, Node +
Playwright. The build is deterministic given the same inputs.

**Brand rules (SVX visual identity):**

- Green cascade palette only: `design_engine.py palette-cascade
  --intent nature --mode minimal --harmony monochrome --seed 7`
  (Edition 2 uses seed 77: emerald accent `#1d9459`, deep-green header
  fill `#2f5140`, light sage surfaces).
- **No blue.** The original draft was crystal-blue and was deliberately
  rebranded; pixel-verified 0% blue in Edition 2.
- Cover typography: geometric sans (Space Grotesk display + Inter) —
  near-black title on light background, hairline grid, emerald anchor
  line. No serif covers.
- New editions = design overhauls, not version bumps; the report carries
  an "Edition" number, decoupled from any semver.

## Working rules for future agents

1. **Never edit `research/raw-search-results/`.** It is the audit trail.
   New evidence goes in as *new* files; corrections happen in the layers
   above.
2. **Every new claim needs a dated, corpus-traceable source.** If a
   search quota blocks verification, say so explicitly rather than
   asserting (the R5 report documents its rate-limit gaps this way).
3. **Extending the research** = new track reports (R6+) or a new
   edition of the PDF, plus a `docs/research-worklog.md` entry. Keep the
   kill-list discipline: try to kill the gap before you promote it.
4. **Building a product from the shortlist** = new repo under the SVX
  family, MIT license, green-branded README, cross-linked to this repo
   as its evidence base. Gap #1 → `svx-evalgate` is the template.
5. Versioning across the family is deliberately conservative: products
   stay in 0.x/2.x and mature before any major. Do not bump versions to
   look busy.

## Related

- **Product:** [svx-evalgate](https://github.com/srivtx/svx-evalgate) —
  gap #1, shipped. Its `AGENTS.md` documents the product-side invariants.
- License: MIT. Research corpus and report reusable with attribution.
