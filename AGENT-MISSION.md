# AGENT-MISSION.md — The Whole Story & the Continuous Research Loop

**This is the operating document for SVX Research as a living system,
not a dated artifact.** Any agent (research or product) starting work
in this project family should read this file first, then
[`AGENTS.md`](AGENTS.md) for repo mechanics, then
[`docs/gap-registry.md`](docs/gap-registry.md) for the current state of
play. Humans are welcome to read it too — it is the story of why this
organization exists and how it runs.

## The whole story

**September 2026.** A single question was asked at the level of the
whole industry: *what is the software industry missing?* Not "what
product could be incrementally better" — what has never been built,
what connects things that exist but was never connected, and what was
built so badly it functions as an open wound.

**The method.** Five research agents (R1 developer tooling, R2
integration & data, R3 missing links, R4 badly-built categories, R5
AI-era frontier) ran ~60 web searches, harvested evidence
predominantly from 2024–2026, and — critically — applied a **kill-list
discipline**: every candidate gap was attacked on the assumption that
someone had already solved it, and only survivors were promoted.
Thirty-two validated deep-dives distilled into **twelve ranked
opportunities**. No statistic in the corpus was invented or
extrapolated; every claim traces to a dated source in the raw-search
evidence layer.

**The findings.** Three conclusions carried the whole report:
(1) the industry has a *translation problem* and AI just collapsed the
economics of translating between representations, making decades-old
gaps suddenly buildable; (2) the deepest gaps are *ownership vacuums*,
not technology vacuums — nobody is paid to watch the wiring;
(3) *buyer-user mismatch* is the one pattern AI does not fix, and the
viable wedge is bottom-up.

**The report.** `report/SVX-Industry-Gap-Analysis-2025-2026.pdf` —
Edition 2, 27 pages, SVX green, reproducible from `build/`.

**The products.** Gap #1 (the evals-in-CI adapter) was productized
immediately as **[svx-evalgate](https://github.com/srivtx/svx-evalgate)**
— deterministic statistics gate for AI evals, now at v2.1.0 with 264
tests, zero dependencies, and green CI. Wave 3 (2026-09-30) added two
more, each born from a verified-open registry row with a self-contained
task brief so any agent can pick them up cold:
**[svx-careops](https://github.com/srivtx/svx-careops)** (row 14 — the
home-care back-office agent layer; read-only, human-approves-everything)
and **[svx-parityrun](https://github.com/srivtx/svx-parityrun)**
(row 13 — the legacy differential-validation harness). Each product
repo follows the evalgate template: `AGENTS.md` mechanics,
`AGENT-GOALS.md` work orders with build gates and evidence-traced
necessity cases, MIT, CI from the first commit. That is how a gap goes
from a ranked row to a product a stranger can build without asking
anyone for context.

**The agent layer.** Every repo in the family carries `AGENTS.md`
onboarding files and `AGENT-GOALS.md` (work orders for open goals,
with build gates where verification is still narrowing); this file
plus `docs/gap-registry.md` make the research side a *continuously
operating* system rather than a one-time report.

## The operating model: two loops

```
   LOOP 1 — RESEARCH (this repo)                LOOP 2 — PRODUCTS (new repos)
   ─────────────────────────────                ──────────────────────────────
   find   → search new evidence                 pick   → choose a registry gap
   verify → try to kill it (kill-list)          verify → re-verify field TODAY
   record → track report + raw JSON             build  → separate repo, SVX family
   rank   → update gap-registry.md              ship   → CI green, docs, AGENTS.md
              │                                              ▲
              └────────── gap survives & is ready ───────────┘
```

Research agents push findings **into this repo**; product agents read
the registry and **create separate repos** per gap. The registry is
the only handshake point — it is how loop 1 tells loop 2 what to
build, and how loop 2 reports back what it shipped.

## Loop 1 protocol — research agents

1. **Find.** Sources of new work: (a) the never-searched backlog
   below; (b) re-verification of existing claims as they age; (c)
   entirely new lenses (an R6+ track) — candidate lenses that did not
   exist as tracks: security/supply-chain, accessibility, climate
   tech software, education tooling, developer economics.
2. **Verify.** Kill-list discipline is mandatory: before promoting
   any finding, search specifically for an existing strong solution
   and document why it does not close the gap. A gap closed by the
   market is a *finding* — record it in the registry as CLOSED, with
   the closing product named. That is the system working.
3. **Record.** Follow the three-layer rule from
   [`AGENTS.md`](AGENTS.md): raw search JSON goes into
   `research/raw-search-results/` as *new files only* (never edit
   existing evidence); analysis goes into a track report
   (`research/track-reports/R6-....md`); the report PDF is only
   regenerated as a deliberate new edition.
4. **Rank.** Update `docs/gap-registry.md`: status, last-verified
   date, and any reordering with a one-line justification. New gaps
   enter at a provisional rank with an OPEN-NEW status until
   independently re-verified.
5. **Hand off.** When a gap is validated and unowned, write a
   handoff note in the registry row (why now, first ship, distribution
   model). Product agents pick from these rows.

Rules that never bend: every claim traces to a dated source; no
invented statistics; if search quota blocks verification, say so
explicitly instead of asserting; the raw-evidence layer is immutable.

### The never-searched backlog (first missions)

These verticals were identified during the original research but
never searched — every attempt died on rate limits (documented in the
R5 track report). They are the highest-value unexplored territory:

- Small-manufacturing ERP/MES
- Field service (HVAC/plumbing) operations software
- Government legacy (COBOL) modernization tooling
- Elder care / home healthcare operations
- SMB supply chain
- Model portability across LLM vendors

## Loop 2 protocol — product agents

1. **Pick** a registry row marked OPEN (never one marked CLOSED or
   BUILT). Read its track report for the full evidence base.
2. **Re-verify the field today** — the report is a September 2026
   snapshot and the AI-infrastructure rows move fastest. Fresh
   searches at build time are mandatory; the registry's
   last-verified column tells you how stale the row is.
3. **Create a separate repo** under the SVX family
   (github.com/srivtx/*), following the svx-evalgate template: MIT
   license, green-branded README, `AGENTS.md` onboarding from day one,
   CI from the first commit, cross-linked to this repo as the
   evidence base, zero-dependency bias where the domain allows.
4. **Prefer the overlay shape.** The pattern across all tracks: small
   teams win by *watching, verifying, or connecting* systems that
   incumbents built and neglected — not by asking anyone to rip
   anything out.
5. **Version conservatively** (explicit owner instruction): products
   stay at their current minor and mature. Docs-only changes get no
   bump. A major version must be earned in production, never
   announced by ambition. See svx-evalgate's `AGENT-GOALS.md` for how
   maturation criteria are documented in practice.
6. **Report back**: update the registry row to BUILT with the repo
   link, and add a `docs/research-worklog.md` entry.

## Registry status conventions

| Status | Meaning |
|---|---|
| `OPEN` | Validated, unowned, re-verified reasonably recently — safe to consider |
| `OPEN-NEW` | Newly promoted, awaiting independent re-verification |
| `STALE` | Older than ~6 months since last verification — re-verify before building |
| `BUILT` | Productized under the SVX family — link in row; maintenance happens in the product repo |
| `CLOSED` | The market closed the gap — closing product named; this is a successful finding |

## Family standards (apply everywhere)

- **Over-production bar:** beyond production-grade — guarantees
  proven by tests, statistics correct, docs explain the why, CI green
  on real runners.
- **SVX brand:** green only (emerald `#1d9459`, deep header `#2f5140`,
  light sage surfaces; hue ~150°). No blue. Geometric sans covers,
  never serif.
- **Security:** tokens supplied in chat are never committed to any
  file; one-shot usage only.
- **Worklog discipline:** every session appends to
  `docs/research-worklog.md` (or the product repo's changelog). The
  story must stay reconstructible.
