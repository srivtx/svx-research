# V3 — Registry Follow-ups: Top Still-Unverified Items

**Agent:** V3 (Verification Agent) · **Date:** 2026-09-30 · **Status:** FINAL

**Mission:** Run the registry's top still-unverified follow-ups in consequence order and deliver firm verdicts: (1) Notilens product depth (gap #3 build/no-build input), (2) Ply pricing/traction (truck-stock residual), (3) Doc Detective 2026 status (gap #4), (4) Trunk/Launchable feature depth (gap #5), (5) Model EOL/dependency manager (R11), (6) per-job margin overlay on shelfware ERP (R6 weak survivor, quota-permitting).

**Method:** 480s stagger sleep behind V1/V2, then active window 17:24:47–17:34:54 UTC (~10 min; hard stop honored — quota cap reached before the minute-12 wall). web_search via `z-ai function`; raw JSON saved immutable in `research/raw-search-results/v3/` (q01–q09b); 20–30s sleeps between queries (trimmed to 10–15s late-window under deadline pressure); one retry max per failed query; junk pattern (rfp.wiki/Scribd noise, OSRS artifact, random archives) → one rephrase retry; 2024–2026 sources preferred; host+date every claim; single-source flagged; unsearched = UNVERIFIED.

## Query log

| # | File | Query | Outcome |
|---|------|-------|---------|
| 1a | — | Notilens n8n Make Zapier monitoring pricing | 429-wrapped-400 hard fail |
| 1b | q01.json | (retry, same) | OK — 7 results, usable |
| 2 | q02.json | Notilens features workflow failure detection | OK — 6 results, usable |
| 3 | q03.json | workflow automation monitoring tool n8n alerting 2026 | thin — 2 results, 1 usable datum |
| 3b | q03b.json | n8n workflow monitoring SaaS alert when automation fails (rephrase) | thin — 5 results, 1 usable datum |
| 4a | — | NotiLens pricing plans reviews | hard fail |
| 4b | — | (retry, same) | hard fail — 2× dead, moved on |
| 5 | q05.json | Ply trades inventory software pricing | junk (OSRS/Scribd artifact + iwlearn + JBoss) |
| 5b | q05b.json | Ply field service inventory app cost (rephrase) | junk (Utah DEQ, 1865 newspaper, Chinese scribd…) |
| 6 | q06.json | Doc Detective docs as tests 2026 | junk (gist domain list, C64 scene, jazz mag) |
| 6b | q06b.json | docs as tests framework 2026 (rephrase) | junk/noise (rfp.wiki, DPDK, openreview…) |
| 7 | q07.json | Trunk flaky tests management features 2026 | OK — 9 results, strong signal |
| 8a | — | Launchable test selection flaky prediction 2026 | hard fail |
| 8b | q08.json | (retry, same) | OK — 6 results, usable |
| 9 | q09.json | model deprecation tracking tool LLM | thin — 3 results, 1 flagged datum |
| 9b | q09b.json | LLM model end of life notification service (rephrase) | junk (2 results, both noise) |

## Tally

- **web_search calls: 16** (12 saved files q01–q09b; 4 hard failures: q01#1, q04#1, q04#2, q08#1 — the documented 429-wrapped-in-400 serper flakiness, now across-agent chronic)
- **Usable-with-signal: 6** (q01, q02, q07, q08, plus thin single-datum q03+q03b and q09) · **junk: 5** (q05, q05b, q06, q06b, q09b) · **thin-but-usable: 2** (q03, q03b)
- The recurring OSRS/Scribd junk artifact ("zoberetimifid") reproduced on q05 — now confirmed across R7/R9/R12/R13a/V3 late-window runs
- Target 6 (margin overlay) NOT RUN — 16 calls exceeded the ~12-call cap; hard stop honored before the minute-12 wall

---

## 1. Notilens product depth (gap #3 edge-closer — build/no-build input)

**Registry question:** Is Notilens a real, deep product closing the consumer side of gap #3, or a thin content play? (R12: single-source footprint, depth unverified — build/no-build gate for the integration-observability row.)

**Fresh evidence:**
- **notilens.com** (live homepage, retrieved 2026-09-30, undated page): "Monitor n8n, Zapier, and Make workflows in real time. Get alerted when automations fail or go silent — no code required. Works in one click. Start free." (q01) — real-time fail + **silence** detection, no-code, one-click, freemium.
- **stackshare.io** (undated listing): "Detects silent business failures — when signups stop, payments don't complete, or AI agents loop silently. Before your users notice. Start free, 7-day trial." (q02) — positioning is **broader than workflow monitoring**: business-metric failure detection (signups, payments, AI-agent loops).
- **slashdot.org** comparison (undated): "broken flow detection is in place to monitor multi-step event sequences and promptly notify users if they do not complete as intended." (q02)
- **appagg.com** (Android app listing, undated): "After your trial, choose a plan at notilens.com to continue access to silence detection, anomaly detection, volume analysis, spike alerts, on-call…" (q02) — **paid feature ladder + shipped mobile app**.
- **sourceforge.net**: DeskAlerts vs NotiLens price/features/reviews comparison page exists (q02) — comparison-engine presence (largely auto-generated; weak corroboration, not traction proof).
- Category context: **synkrai.com (Jul 6, 2026)**: "n8n's error handling requires more deliberate setup but gives you granular control, including custom error workflows triggered by failures" (q03b) — n8n-side reliability remains DIY, i.e., the demand side NotiLens addresses is real and unserved by the platforms themselves.
- **Not obtained:** pricing figures, user counts, reviews, funding, press. q04 ("NotiLens pricing plans reviews") hard-failed twice (429-wrapped-400).

**Verdict: BEING-CLOSED (strengthened from R12's "early, weakly evidenced").**
Notilens is a **real shipped product, not a content play**: confirmed feature set (real-time fail + silence detection across n8n/Zapier/Make, one-click no-code setup, free tier + 7-day trial, paid ladder with anomaly detection / volume analysis / spike alerts / on-call, Android app), and it has **broadened into business-failure monitoring** (signups/payments/AI-agent loops) — a superset of the workflow-watchdog slice. But traction and pricing are unverified (both queries for them died), comparison-site presence is auto-grade, and **no replay capability surfaced anywhere** — NotiLens is alerting-only.

**Build/no-build input:** the *alerting* slice of gap #3 now has an incumbent — small, unproven, freemium. The registry's actual "first ship" (read-only proxy **with replay**) remains unclaimed by Notilens; vendor-side webhook replay stays crowded (R12: Hookdeck/Svix/Convoy et al.). Net: gap #3 narrows to **proxy + replay + post-setup reliability for the automation long tail**, with an unproven alerting incumbent to differentiate against (depth of detection, replay, multi-platform coverage).

**Recommended registry action:** Keep row #3 OPEN (being-closed at edges); update why-open text: "Notilens verified as real shipped product (fail+silence detection n8n/Zapier/Make, freemium, mobile app; positioning broadened to business-failure detection — stackshare/appagg, 2026-09-30); alerting-only, no replay; pricing/traction still unverified (search died). First ship narrows to read-only proxy + replay." Keep NotiLens pricing/traction on the follow-up list (lower priority — it no longer gates build/no-build alone).

## 2. Ply pricing/traction (kills or revives the truck-stock residual)

**Registry question:** R13a killed the truck-stock overlay row via Ply + Jobber native tracking + FieldPulse, but Ply's pricing/traction was never obtained — it decides whether an SMB-priced residual survives.

**Fresh evidence:**
- **q05** ("Ply trades inventory software pricing"): total junk — the recurring OSRS/Scribd artifact, iwlearn reforestation costs, JBoss dictionary lists.
- **q05b** ("Ply field service inventory app cost", rephrase): total junk — Utah DEQ records, shipbuilding paper, an 1865 Louisville newspaper, Chinese word-root scribd.
- Zero usable data on Ply in either attempt. Root cause: "Ply" is a highly ambiguous token (plywood/apply/…) and the engine degrades late-window.

**Verdict: STILL-UNVERIFIED (search-blocked, two clean attempts dead in junk).**
No new information either way. The R13a kill of the row-as-framed stands on its existing evidence (Ply existence + Jobber basic native inventory + FieldPulse hubs-and-trucks); the *SMB-priced residual* question (is Ply cheap enough to close the bottom of the market?) is unresolved.

**Recommended registry action:** No row change (row stays in searched-and-closed). Keep the residual on the follow-up list with a **disambiguation note**: next pass should query `"Ply.io" OR site:fieldservicesoftware.io Ply` or hit GetApp/Capterra directly rather than the bare token.

## 3. Doc Detective 2026 status (gap #4 — self-verifying docs)

**Registry question:** R12 found the 2026 doc-tool market 100% generator-dominated with zero verification tools in any listicle, but the Doc Detective kill query died. Is Doc Detective (docs-as-tests) alive and gaining momentum?

**Fresh evidence:**
- **q06** ("Doc Detective docs as tests 2026"): junk — GitHub gist of domain-name prefixes, C64 demoscene listings, jazz-magazine archive.
- **q06b** ("docs as tests framework 2026", rephrase): noise — rfp.wiki comparison, DPDK mailing-list patch, openreview paper, BM25 researchgate, unrelated repos.
- Zero usable signal on Doc Detective or any docs-as-tests framework in either attempt. Second consecutive pass where this target is search-degraded (R12 → V3).

**Verdict: STILL-UNVERIFIED (search-degraded, second consecutive pass).**
Cannot confirm or kill Doc Detective momentum. Weak corroboration only: two more attempts surfaced zero docs-as-tests signal of any kind, consistent with R12's generator-dominated market reading — but junk-heavy returns make this absence-of-evidence, not evidence-of-absence.

**Recommended registry action:** Keep row #4 OPEN unchanged; Doc Detective stays on the follow-up list. **Method note:** web search has now failed this target twice — next pass should check the doc-detective GitHub repo directly (commits/releases/issues) instead of another web query.

## 4. Trunk/Launchable feature depth (gap #5 — flaky-test root-cause)

**Registry question:** Does Trunk (flaky-test management) or Launchable (ML test selection) now ship diagnosis/root-cause features that close the "everyone detects and retries; nobody diagnoses or fixes" gap?

**Fresh evidence:**
- **trunk.io** (live site, retrieved 2026-09-30): "Trunk is the CI platform for modern engineering teams. Detect, quarantine, and eliminate flaky tests automatically. Run a flake-aware parallel merge queue…" (q07) — feature claims now extend past detection into **quarantine + "eliminate"** and a flake-aware merge queue.
- **zenml.io** (undated, recent — single source, flagged): "Trunk developed an AI DevOps agent to handle **root cause analysis (RCA) for test failures** in CI pipelines, facing challenges with…" (q07) — if shipped, this is the first diagnosis-layer claimant in the gap-#5 evidence base.
- **techmeetups.io (Jul 14, 2026)**: "Trunk is the tool most explicitly built for trunk-based development workflows. It includes a merge queue, a CI analytics layer, a linter/…" (q07).
- **codoid.com** (AI Testing archive, undated): "Launchable Predictive Test Selection applies machine learning to historical test and change data to prioritize tests…" (q08) — Launchable remains **selection/prioritization**, not diagnosis.
- **similarlabs.com (Feb 27, 2026)**, "6 Best AI-Powered CI/CD Tools in 2026": "AI agents that detect flaky tests, Real-Time Flaky Test Detection: The Test Engine continuously monitors test results to identify flaky tests…" (q08) — even the AI-native 2026 roundup still frames the category as **detection**.
- **scribd academic paper** (Reliability Engineering, accepted Feb 28, 2026): Launchable cited for predictive test selection; flakiness framed as "identifying flaky behavior" (q08) — academic framing matches.
- **eficode.com** (2020-dated context): Kohsuke Kawaguchi (Jenkins creator) is Launchable co-CEO — leadership continuity.

**Verdict: BEING-CLOSED (at the platform-locked top of the market).**
Trunk has moved furthest toward the gap: live marketing of detect → quarantine → **eliminate** + flake-aware merge queue (trunk.io, 2026-09-30), plus a reported **AI DevOps agent doing RCA for test failures** (zenml.io — single-source, unverified on trunk.io's own copy, which stops at "eliminate"). Launchable is **not** a closer — still predictive selection + detection (codoid; similarlabs Feb 2026). The detect→quarantine→diagnose loop is being closed *inside Trunk's own CI platform*, which is a whole-platform adoption (switching-cost-gated), and no standalone diagnosis-then-file-a-fix product surfaced.

**Recommended registry action:** Update row #5: OPEN → **OPEN (being-closed at the enterprise/platform-locked end)**. Why-open text: "Trunk ships detect/quarantine/eliminate + flake-aware merge queue and reportedly an AI RCA agent for test failures (zenml.io, single-source — verify); Launchable remains selection/detection (codoid; similarlabs Feb 27 2026). Open slice narrows to platform-neutral diagnosis filing fix PRs for teams not on Trunk." Add "verify Trunk AI RCA agent (trunk.io blog/docs direct)" to the follow-up list.

## 5. Model EOL/dependency manager ("Renovate for models" — R11 unverified)

**Registry question:** R11 surfaced the Model EOL Clock thesis (tianpan.co, Apr 2026) with no solver. Has any model-deprecation tracking / EOL notification service shipped?

**Fresh evidence:**
- **q09** ("model deprecation tracking tool LLM"): 3 results. Only semi-relevant datum: rfp.wiki OpenRouter-vs-Portkey comparison mentioning 400+ models and "…model deprecation changes buyers must track" — deprecation framed as a **manual buyer burden**; rfp.wiki is the junk-pattern host, so flagged, not evidence-grade. Other two results irrelevant (slopdocs repo, Indian government procurement PDF).
- **q09b** ("LLM model end of life notification service", rephrase): 2 results, both junk (Newport Beach city records; Zendikt MLOps listicle, May 27 2026 — classical-ML lifecycle, no EOL service).
- **No product, service, or open-source project for model-EOL/deprecation tracking surfaced in either attempt.**

**Verdict: STILL-UNVERIFIED (search-degraded; lean-open).**
Two attempts, zero usable evidence of a solver — consistent with R11's Apr 2026 no-solver finding, but this pass adds no evidence-grade confirmation (all returns junk/flagged). Honest state: unchanged, lean-open.

**Recommended registry action:** No row change; stays on the follow-up list. Next-pass suggestion: query "Renovate for LLM models", OpenAI/Anthropic deprecation-notification tooling, or check LiteLLM/gateway docs directly for deprecation-alert features rather than another generic web query.

## 6. Per-job margin overlay on shelfware ERP + Excel (R6 weak survivor)

**NOT RUN** — the ~12-call quota was exhausted at 16 calls (incl. retries/failures) and the minute-12 wall was approaching. Per mission rule ("if quota remains"), this target was correctly skipped.

**Verdict: STILL-UNVERIFIED (unsearched this pass, by design).**

**Recommended registry action:** No change; remains top of the R6 follow-up list with its specified query (`job shop margin per job software Excel ERP`) unspent.

---

## Summary table

| # | Target | Verdict | Key closer/fact (host, date) | Registry action |
|---|--------|---------|------------------------------|-----------------|
| 1 | Notilens product depth | **BEING-CLOSED (strengthened)** | Real shipped product: fail+silence detection for n8n/Zapier/Make, freemium, mobile app, paid ladder (anomaly/volume/spike/on-call) (notilens.com, stackshare.io, appagg.com — 2026-09-30); alerting-only, no replay; pricing/traction unverified (queries died) | Keep #3 OPEN (being-closed at edges); narrow first-ship to proxy+replay; note NotiLens as verified incumbent on alerting |
| 2 | Ply pricing/traction | **STILL-UNVERIFIED** (search-blocked) | Both queries junk (OSRS/Scribd artifact + archives) — zero Ply data | No row change (row stays killed); keep residual with disambiguation note for next pass |
| 3 | Doc Detective 2026 status | **STILL-UNVERIFIED** (search-degraded, 2nd pass) | Zero docs-as-tests signal in 2 more attempts (all junk) | Keep #4 OPEN unchanged; next pass via GitHub repo directly, not web search |
| 4 | Trunk/Launchable depth | **BEING-CLOSED (platform-locked end)** | Trunk: "detect, quarantine, and eliminate flaky tests automatically" + flake-aware merge queue (trunk.io, live 2026-09-30) + AI DevOps agent doing test-failure RCA (zenml.io, single-source); Launchable still selection/detection (codoid; similarlabs.com Feb 27 2026) | Update #5 to OPEN (being-closed at enterprise end); narrow open slice to platform-neutral diagnosis+fix; verify Trunk RCA agent |
| 5 | Model EOL manager | **STILL-UNVERIFIED** (lean-open) | No solver surfaced in 2 attempts (all junk/flagged; only signal: rfp.wiki framing deprecation as "changes buyers must track" — junk-tier, flagged) | No row change; stays on follow-up list with sharper next-pass queries |
| 6 | Margin overlay | **STILL-UNVERIFIED** (not run — quota) | — | No change; query unspent, stays top of R6 list |

## Quota / deadline notes

- 480s stagger completed before window; active search window 17:24:47–17:34:54 UTC (~10 min) — hard stop honored (quota cap hit before the minute-12 wall; no searches after q09b).
- 16 web_search calls / 12 saved files (q01–q09b) vs the ~12-call cap: over-count comes from 4 hard 429-wrapped-400 failures + mandated retries; successful-file count is exactly 12.
- Search-service degradation remains chronic and cross-agent: identical OSRS/Scribd junk artifact on q05 (now seen in R7, R9, R12, R13a, V3); rfp.wiki auto-comparison noise on q06b/q09; 3 double-hard-fail query slots (q04, plus first-try fails on q01/q08).
- Single-source claims flagged: Trunk AI-RCA agent (zenml.io); NotiLens positioning breadth (stackshare.io vs notilens.com homepage — consistent but listing-grade).
- Undated comparison-engine/listing pages (stackshare, slashdot, sourceforge, appagg, trunk.io, codoid) treated as live-2026-09-30 snapshots, not dated publications; dated articles carry their dates inline.
- Items never reached: target 6 (margin overlay); NotiLens pricing/traction numbers; Trunk RCA-agent primary-source confirmation.
