# The SVX Search Playbook — degradation map and counter-tactics

**Every lesson from research passes R1–R15 and V1–V5, encoded so the
next agent stops paying for them twice.** The search service degrades
in known, reproducible ways; this file is the map. Read it before any
search-heavy mission. The companion driver is
[`svxsearch.py`](svxsearch.py) (junk detection, query manifest, retry
discipline, pacing).

## 1. The degradation map (what fails, how to know, what to do)

| Pattern | Seen in | Signature | Counter-tactic |
|---|---|---|---|
| **Structural noise families** — some query phrasings *always* return dictionary/list/book junk, regardless of retry | R8/R13b/V1 ("parallel run"), R9/V2 ("family communication", "documentation time"), R12/V2 ("EVV exception", "Doc Detective") | same junk class across 2-3 passes | **3-strike rule**: after 3 failed runs of a phrasing family, retire it from search and switch to direct reads. Retired list lives in the registry's follow-up section |
| **The OSRS/Scribd artifact** — an identical junk doc ("zoberetimifid") recurs across unrelated agents and weeks | R7, R9, R12, R13a, V3 | exact-match title markers | auto-detected by `svxsearch.py`; never count as evidence |
| **Hard 429s wrapped around 400s** — concurrency-triggered rate limits, sometimes mislabeled | R5, R9, R11-R13, V2 | `serper 400-wrapped-in-429` | sleep 20-35s between calls; stagger sibling agents ≥240s; one retry max per query; **never run 3+ agents un-staggered** |
| **Empty-title result sets** — valid URLs/snippets, blank titles | V4, V5, R14, R15 | titles blank in JSON | treat as thin, not junk; extract from snippet/URL; flagged by the driver |
| **Junk rate 30-50% of saved files** in degraded windows | all waves | many JUNK grades in a run | budget accordingly: ~12-15 calls per pass yields ~7-10 usable sets |
| **Vendor-mill noise** — content farms around pricing/comparison queries | R13a, V5 | contradicting vendor claims (Jobber inventory "basic" vs "advanced") | prefer the vendor's own docs; cross-check two independent hosts before asserting |
| **SEO-farm fresh content** targeting research-shaped queries | V1 ("golden master characterization legacy migration") | days-old domains | check domain age signals; single-source = flagged |

## 2. Direct-read recipes (when search is the wrong tool)

Search answers "what exists in the index"; several load-bearing
questions need the actual page. Proven recipes from the 2026-10-04
gate session (`research/raw-search-results/w4-direct/`):

- **Vendor API docs** (ReadMe.io-style portals): `curl -sL <url>` then
  strip tags — the AlayaCare portal served its full 397-endpoint
  reference as server-rendered HTML. Grab `/reference` index pages and
  link-extract with a regex; check for `/docs/authentication` and
  `/docs/rate-limiting`.
- **GitHub repo vitality** (the Doc Detective recipe): use the
  **authenticated** API (`curl -H "Authorization: token $GH_TOKEN"
  https://api.github.com/repos/{org}/{repo}``) — unauthenticated hits
  IP rate limits almost immediately. Pull `pushed_at`,
  `archived`, latest releases, last 3 commits. Search API
  (`/search/repositories?q=`) has a separate quota when direct calls
  are exhausted.
- **JS-walled marketplaces** (AWS Marketplace): curl gets a shell;
  use the `agent-browser` headless browser — `open <search-url>`,
  `wait --load networkidle`, `get text "body"`, and
  `eval` to extract `a[href*="prodview"]` listing links, then open the
  listing detail page the same way. Delivery method / seller / pricing
  model are all in the rendered body text.
- **Cloudflare-walled vendor blogs**: curl returns a challenge page —
  fall back to press coverage in reputable secondaries (Toronto Star,
  Yahoo Finance) and flag single-sourcing honestly.
- **Press-release details**: search for the company + "announces" +
  month/year, then read the most reputable host that summarizes it;
  record host + date in the report.

## 3. Runtime discipline (the rules that came from deadline deaths)

1. **Skeleton first.** Write the report skeleton *before* the first
   query; fill incrementally. R6/R7/R8 died with 80 raw files and zero
   report lines — the salvage (S6-S8) cost more than the searches.
2. **Budget:** 12-15 calls per pass; hard stop on new searches at
   minute 14-16 of the run; write from what landed.
3. **Query log is sacred:** never argv-only (R8's lesson). Use
   `svxsearch.py` so the manifest captures text + timestamp + grade.
4. **Honest verdicts:** unsearched = UNVERIFIED. Junk = not evidence.
   Single-source = flagged. No invented numbers, ever.
5. **Stagger siblings ≥240s** and keep concurrency ≤3 search agents.
6. **Kill-list discipline:** a crowded category is a *finding* (record
   it closed with closers named) — the registry's searched-and-closed
   list is the system's trophy case, not its graveyard.

## 4. Known structurally-unsearchable phrasings (retired)

Do not re-run these through web_search; use direct reads instead:

- "parallel run" family (mainframe migration comparison) — 6+
  consecutive structural failures; resolved via agent-browser on AWS
  Marketplace + vendor sites
- family-communication layer (home care) — 3 failed runs; direct
  product-page reads
- caregiver documentation-time quantification — 3 failed runs;
  literature reads
- EVV-exception standalone solver — 3 failed runs; product-page reads
- Doc Detective momentum — 2 failed runs; **solved by the GitHub API
  recipe** (134 stars, v4.38.1, active 2026-10)
- Ply pricing — 2 failed runs; resolved by V5 via funding/integration
  evidence instead of list price

## 5. When you're done

Raw JSON is immutable — never edit a saved file. Reports go to
`research/track-reports/`, registry updates are recommended in-report
(the maintainer owns `docs/gap-registry.md`), worklog gets the
append-only entry. Search-degradation observations that reproduce
should be added to §1 of this file — that is how the map stays current.
