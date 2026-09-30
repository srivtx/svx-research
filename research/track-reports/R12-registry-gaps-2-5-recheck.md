# R12 — Registry Re-Verification: Gaps #2–#5 (2026-09-30)

**Task ID:** R12 · **Agent:** general-purpose · **Mission:** try to KILL registry gaps #2–#5 with fresh kill-searches; issue a verdict per row.
**Method:** 23 `z-ai function web_search` executions (20 raw files saved + 3 hard 429 failures), staggered 120s behind sibling R11, `sleep 20–30` between queries, one rephrased retry per thin/failed result, hard stop on new searches enforced at ~minute 14 of the search phase. Raw evidence (immutable): `research/raw-search-results/r12/q01–q16*.json`. Service quality this session was poor — 8 of 20 saved files returned junk/garbage (recurring rfp.wiki/Scribd noise, same degradation pattern R7/R9 logged); verdicts below state their confidence honestly.
**Evidence window:** fresh searches run 2026-09-30; sources span Mar 2025 – Sep 2026 (bulk Jun–Sep 2026). Prior verification: 2026-09 (R1 dev-tooling, R2 integration-data, R3 missing-links, R5 frontier track reports).
**Prior basis being re-tested:** R3 §3/§4, R5 A3 (gap #2); R2 Gap 1 (gap #3); R1 Gap 3 + R3 §3 (gap #4); R1 Gap 1 (gap #5).

---

## Gap #2 — AI-code verification ledger (Lens: Links)

**Original claim (registry):** "No attestation standard for code authorship; regulation creating demand." First ship: OSS CLI + PR badge. Status at last verification (2026-09): OPEN. Prior basis: Sonar 96%-distrust / 48%-always-verify; C2PA covers media not code diffs; SLSA covers build provenance not authorship (R3 §4, R5 A3).

**Fresh evidence (2026-09-30 searches):**

- **The regulation tailwind is now LIVE and confirmed.** EU AI Act Article 50 transparency duties **applied from 2 August 2026** — "The Article 50 transparency duties have applied since 2 August 2026" (govarna.com, Jul 17 2026); "What changed on 2 August 2026 under Article 50 of Regulation (EU) 2024/1689: who must disclose AI interaction, mark synthetic content" (dryrights.com, 2026); draft Article 50 transparency guidelines published May 2026 (devthrottle.com, May 8 2026); labelling obligations for generative-AI providers in force (provenancelens.com, Aug 12 2026). Caveat for the wedge: Article 50's scope as described is **chatbot-interaction disclosure and synthetic-content marking** — none of the four sources extends it to source-code authorship, so the "regulation creates demand" premise holds for adjacent provenance demand, not yet for code per se.
- **Attribution measurement is emerging at the metrics layer — not attestation.** Typo's engineering-intelligence platform detects AI PRs via `Co-authored-by` commit trailers ("If any PR commit has a tool as a co-author, that PR is considered [AI]" — typo.gitbook.io docs, Aug 19 2026). larridin.com measures "What Percentage of Your Code Is AI-Generated?" using "the GitHub Copilot Metrics API, Cursor analytics" and commit metadata. Port ships a "Track AI-driven pull requests" blueprint so portals can "ensure AI-generated code meets your team's standards and review processes" (docs.port.io, 2026). All three are **telemetry dashboards** — detection after the fact, not signed attestations attached to artifacts.
- **A nascent human-written badge movement exists.** "Badge repository promotes human-written code over AI… The badge allows AI use only for specific purposes" (hellomarvisaitoday.com, Jul 30 2026) — same article circulates the claim that "code written with AI assistance shows 40% more bugs than human-written code" (unverified press claim, flagged). This is a convention/badge play on GitHub repos, not a verification ledger.
- **GitHub's own AI labeling is about alerts, not code.** "Code scanning shows AI security detections on pull requests… Alerts generated using AI will be labeled with AI so you can easily distinguish them from CodeQL results" (github.blog, Jul 14 2026). No GitHub/GitLab feature surfaced that labels AI-*authored* commits or PRs.
- **C2PA momentum in 2026 remains media-only.** OpenAI's European provenance work centers C2PA metadata for content ("helps content carry information about where it came from" — openai.com, Sep 7 2026); a CA began issuing production-ready C2PA-conformant certificates for media credentials (finance.yahoo.com, 2026); 2026 explainers cover images/text watermarking (datanorth.ai; pragma-code.de, Jun 14 2026; adaptlypost.com, Sep 15 2026). **Nothing extends C2PA to source code or diffs** — R5 A3's "C2PA-for-code is empty" premise survives.
- **SLSA still proves builds, not authorship.** "Your Software Supply Chain Only Proves Where Code [came from]" (hackernoon.com, Jun 28 2026 — SLSA provenance + Sigstore attestations exist but don't attest authorship/verification); NVIDIA's `aicr` repo ships SLSA Build L3 for container images (github.com/NVIDIA/aicr, 2026) — build provenance hygiene. Adjacent research exists — an open, model-agnostic "interaction card" for verifiable model-interaction records (discuss.huggingface.co, Aug 12 2026) — but it is a discussion-stage proposal, not a shipped code-authorship standard. Supply-chain attackers exploiting autonomous coding are now a named threat class (crashoverride.com, 2026).

**Attempted kill (queries):** q01 "AI generated code attribution attestation product 2026" (junk) → q01b "how to prove how much code was written by AI versus human pull request badge" (4 results, 2 usable); q02 "C2PA content credentials for source code provenance standard 2026"; q03 "SLSA attestation AI generated code authorship provenance git commit"; q04 "EU AI Act Article 50 transparency obligations August 2026 deadline synthetic content"; q05 (429 death) → q05b "GitHub Copilot pull requests show percent AI generated code label".

**VERDICT: OPEN** — high confidence. The edges are being nibbled (attribution telemetry: Typo/Port/larridin; a human-written badge repo; AI-labeled *alerts* at GitHub), but **no attestation standard, no OSS CLI, no PR badge proving AI/human authorship ratios shipped**. The "why now" actually strengthened: Article 50 duties live since 2026-08-02 and the 40%-more-bugs claim is circulating in press. This row's wedge (attestation format + GitHub App) remains unclaimed.

**Recommended registry update:** `| 2 | AI-code verification ledger | Links | No attestation standard for code authorship; regulation creating demand — EU AI Act Art. 50 duties live since 2026-08-02; attribution *telemetry* emerging (Typo/Port) but no attestations | OSS CLI + PR badge | OPEN | 2026-09-30 |` — justification: five kill-searches found measurement dashboards and a badge convention, no attestation product; regulation tailwind now in force.

---

## Gap #3 — Integration observability proxy (Lens: Plumbing)

**Original claim (registry):** "iPaaS monetizes volume, not reliability; nobody watches post-setup." First ship: read-only proxy with replay. Status 2026-09: OPEN. Prior basis (R2 Gap 1): Zapier/Make per-task pricing, Workato/Boomi $50k+, none watch the pipeline after setup — no drift alerts, no replay, no failure ownership.

**Fresh evidence (2026-09-30 searches):**

- **Watchdog demand is live and unresolved.** "How do you monitor n8n workflows in production" — practitioner thread still open (community.n8n.io, Jun 23 2026). The default answer is still DIY: "Monitor n8n Like a Pro — Healthchecks, Queues & Error [triggers]… to catch silent failures" (vps.us, Mar 2 2026).
- **Early movers exist — the strongest being-closed signal of all four gaps.** **Notilens** publishes "How to Detect n8n, Make, and Zapier Workflow Failures… how automation workflows fail, what to monitor, and execution history" (notilens.com, Apr 30 2026) — a product-domain content play covering exactly the cross-platform automation-failure-detection space. **Watchflow** appears as an n8n node/template that "transforms your n8n workspace into a self-monitoring powerhouse… automatically audits all [workflows]" (n8n.io, 2026) — ecosystem-internal self-monitoring, not a standalone cross-platform watchdog.
- **The vendor-side webhook layer is crowded — but it serves webhook *senders*, not automation *consumers*.** 2026 comparison: "HookSniff vs Svix vs Hookdeck vs Hook0" (hooksniff.vercel.app, May 10 2026); WebhookVault "Transforming Webhook Payloads at the Gateway" (webhookvault.com, Sep 8 2026); Hooksbase as "Svix alternative for webhook delivery" (hooksbase.com, 2026); Convoy vs Hooksbase (sourceforge.net, 2026); Webhook Relay vs webhook.co (itechguides.com, Sep 17 2026). These give retry/replay/DLQ infrastructure to SaaS vendors sending webhooks — the consumer-side "watch my Zapier/Make/iPaaS sync" proxy remains unclaimed by them.
- **The economics of why nobody watches, from a founder:** "Our startup was losing users silently for 6 hours — no alert fired… monitoring spend is judged against the cost of last quarter's silence, not next quarter's avoided disaster. Buyers don't have a budget [line]" (indiehackers.com, 2026) — confirms R2's structural claim (nobody is paid to watch).
- **Negative evidence with caveats:** direct watchdog queries returned junk or generic automation listicles ("Enterprise Workflow Automation Software: 10 Best (2026)" — teamwork.com, Apr 30 2026; n8n jobs board — community.n8n.io, Dec 13 2025; agency automation roundups — simular.ai, synkrai.com Apr 15 2026) — no monitoring/watchdog product surfaced in the generic lists, i.e., it is not yet a category with a default answer. A follow-up query to corroborate Notilens as a shipping product (q15) did **not** surface it again — its footprint rests on one content-marketing page.

**Attempted kill (queries):** q06 "Zapier workflow error monitoring alerting tool 2026" (junk) → q06b "how to monitor failed Zapier zaps get alerts when automation breaks" (junk); q07 "integration monitoring observability startup sync errors API data pipeline 2026" (junk) → q07b "tool that alerts me when my Zapier Make integration sync stops working silently" (8 generic); q08 "webhook monitoring retry replay dead letter queue tool Hookdeck Svix 2026"; q14 "monitoring dashboard for n8n Zapier workflow errors and healthcheck"; q15 "Notilens automation monitoring product pricing" (no direct hit).

**VERDICT: BEING-CLOSED (early, weakly evidenced).** Closers so far: **Notilens** (n8n/Make/Zapier failure detection; single-source footprint, product depth unverified) and **Watchflow** (n8n self-monitoring template — solves only inside one platform), with the Hookdeck/Svix/Hook0/Convoy crowd owning the vendor-side webhook replay slice. What's left: a verified cross-platform, read-only watchdog with replay for *consumed* automations is still not confirmed shipped; community demand threads remain open. If Notilens turns out to be vapor/thin, this row reverts cleanly to OPEN.

**Recommended registry update:** `| 3 | Integration observability proxy | Plumbing | iPaaS monetizes volume, not reliability; nobody watches post-setup — early movers appearing (Notilens, Watchflow for n8n); vendor-side webhook replay crowded | Read-only proxy with replay | OPEN (being-closed at edges — verify Notilens depth before build) | 2026-09-30 |` — justification: first real claimants surfaced Apr–Jun 2026 but none verified as a shipping cross-platform watchdog; demand threads and DIY default persist.

---

## Gap #4 — Self-verifying docs / doc tests (Lens: Tooling/Links)

**Original claim (registry):** "Freshness tools measure age, not truth; RAG made rot worse." First ship: README checker, OSS-first. Status 2026-09: OPEN. Prior basis (R1 Gap 3, R3 §3): stale-page notifications are age heuristics; RAG bots answer from stale pages; doctests only cover code-embedded docs; guides recommend discipline, not verification.

**Fresh evidence (2026-09-30 searches):**

- **The 2026 documentation-tool market is generator-dominated — verification tooling did not surface.** The "best documentation tools" results are all AI *generators*: "AI document generator: Create workplace guides effortlessly" (scribe.com, 2026); "AI Code Documentation Generator" (codegpt.co, 2026); "10 Best AI Tools for Software Documentation" (geeksforgeeks.org, Mar 10 2026); "I Tried 15 of the Best Documentation Tools" (dev.to, Jul 1 2025); "10 Best Document Generation Software Reviewed in 2026" (thedigitalprojectmanager.com, Sep 20 2026); documentation-tool list (apidog.com, 2026). **No doc-testing, docs-as-tests, snippet-verification, or doc-drift tool appears in any 2026 listicle** — consistent with R1/R3's finding that the category's answer to rot is still "write better docs," not "verify docs."
- This is also the mechanism that makes the gap *worse*, per the row's own thesis: generator volume increases the stock of prose that can silently go false while the verification layer stays empty.

**Attempted kill (queries):** q09 "Doc Detective docs as tests documentation testing framework 2026" (hard 429 death) → q09b "docs as tests verify code examples in documentation CI 2026" (7 junk results — unrelated); q13 "test documentation examples automatically tool keeps docs up to date with code" (7 results — all generator tools, used as negative evidence). **The kill attempt was search-degraded: only one of three executions produced usable results.** Doc Detective's current state specifically remains unverified — this is the #1 follow-up query for the next agent.

**VERDICT: OPEN** — medium confidence (search-degraded). The one clean look at the 2026 market (q13) shows generator tools everywhere and no verification tool anywhere in the lists; nothing new shipped to close the gap since 2026-09. Because Doc Detective / docs-as-tests momentum could not be directly checked, a residual risk of an OSS-community closer being missed is explicitly flagged.

**Recommended registry update:** `| 4 | Self-verifying docs (doc tests) | Tooling/Links | Freshness tools measure age, not truth; 2026 doc-tool market is generator-dominated, no verification tool in any listicle; RAG made rot worse | README checker, OSS-first | OPEN (kill attempt search-degraded; re-check Doc Detective/docs-as-tests momentum) | 2026-09-30 |` — justification: fresh 2026 tool lists contain zero docs-as-tests/verification entries; gap thesis (generation up, verification empty) reinforced.

---

## Gap #5 — Flaky-test root-cause repair (Lens: Tooling)

**Original claim (registry):** "Everyone detects and retries; nobody diagnoses or fixes." First ship: CI plugin filing diagnosis PRs. Status 2026-09: OPEN. Prior basis (R1 Gap 1): retries/quarantine/dashboards (Currents, BuildPulse, Launchable) manage symptoms; reproduction semi-manual; no tool links a flake to its causal trace and proposes a fix.

**Fresh evidence (2026-09-30 searches):**

- **The category's own September 2026 vocabulary is still "detection."** "9 Best Flaky Test **Detection** Tools for QA Teams in 2026" (testdino.com, Sep 7 2026) — the freshest category roundup (23 days old at search time) frames the space as detection, and its pitch is "identify and resolve flaky tests," with resolution via identification, not automated diagnosis.
- **The dashboard incumbents are dashboards still.** "Best Currents Alternatives in 2026 (Free & Paid)": "Currents is a polished, purpose-built Playwright dashboard — but it's Playwright-primary with Cypress support frozen at pre-v13 and no other framework supported" (qualflare.com, 2026) — i.e., a maturing *visibility* tier, not diagnosis.
- **ML in the adjacent tools is auto-healing/reliability, not root-cause.** "mabl focuses on improving test reliability using machine learning. It helps reduce flaky tests and integrates well into CI/CD" (getscandium.com, Mar 24 2026); 2026 AI-testing comparisons cover mabl, Katalon, Tricentis Testim, Applitools, Functionize (ones.com, Sep 25 2026) — all test-automation platforms with reliability features, none positioned as flake *diagnosis+fix*.
- **Negative evidence:** five attempts at diagnosis-tool queries returned junk or generic listicles — no product surfaced that files a diagnosis or a fix PR for a flaky test.

**Attempted kill (queries):** q10 "flaky test root cause analysis diagnosis tool CI 2026" (junk) → q10b "tool that finds why a Playwright test is flaky automatically diagnosis" (junk); q11 "Trunk Flaky Tests management tool" (junk — SVN-mail garbage); q12 "flaky test detection quarantine tools BuildPulse Currents Launchable 2026" (hard 429 death) → q12b "best tools for managing flaky tests in CI 2026" (2 listicles, usable); q16 "Currents flaky test management Playwright dashboard 2026" (2 results, both usable). **Search-degraded here too: 4 of 6 attempts junk/failed.**

**VERDICT: OPEN** — medium-high confidence. The two clean hits (Sep 2026) both describe the market as detection + dashboards; the AI-testing incumbents apply ML to auto-healing; nothing surfaced that diagnoses *why* a test flakes or files the fix. Registry's premise ("detect and retry, not diagnose and fix") is still an accurate description of the September 2026 market per available sources; caveat that Trunk's and Launchable's 2026 feature sets specifically could not be re-checked due to junk returns.

**Recommended registry update:** `| 5 | Flaky-test root-cause repair | Tooling | Everyone detects and retries; nobody diagnoses or fixes — Sep 2026 roundups still categorize the space as "flaky test detection"; ML effort goes to auto-heal | CI plugin filing diagnosis PRs | OPEN | 2026-09-30 |` — justification: testdino.com (Sep 7 2026) and qualflare.com (2026) confirm detection/dashboard framing persists; no diagnosis+fix product surfaced.

---

## Summary table — R12 verdicts

| # | Gap | Verdict | Closer / who's closing | Confidence | What would change it |
|---|-----|---------|------------------------|------------|----------------------|
| 2 | AI-code verification ledger | **OPEN** | Nobody; edges nibbled by Typo/Port (telemetry), human-written badge repo, GitHub AI-*alert* labels | High | A shipped attestation format/standard (C2PA-for-code, SLSA authorship extension, GitHub AI-authorship labels) |
| 3 | Integration observability proxy | **BEING-CLOSED (early)** | Notilens (n8n/Make/Zapier failure detection, Apr 2026, unverified depth) + Watchflow (n8n self-monitoring template); Hookdeck/Svix/Hook0/Convoy own vendor-side webhook replay | Medium-low (single-source) | One verification pass on Notilens product/pricing/traction → flips to CLOSED or back to OPEN |
| 4 | Self-verifying docs (doc tests) | **OPEN** | Nobody; 2026 doc-tool lists are all AI generators, zero verification tools | Medium (search-degraded) | Doc Detective/docs-as-tests momentum check (died on 429/junk this pass) |
| 5 | Flaky-test root-cause repair | **OPEN** | Nobody; mabl-class ML = auto-heal; Currents = dashboard; Sep 2026 category still named "detection" | Medium-high (partially search-degraded) | Trunk/Launchable/BuildPulse shipping diagnosis+fix features (uncheckable this pass — junk returns) |

**Bottom line:** none of the four rows died. Gap #2 and #5 are unchanged OPEN with strengthened evidence; gap #4 is OPEN with a degraded kill attempt that must be re-run; gap #3 is the only row with a real (early, unverified) closer signal and carries the most urgent follow-up.

## Quota / deadline notes

- **Search executions:** 23 (20 saved: q01, q01b, q02, q03, q04, q05b, q06, q06b, q07, q07b, q08, q09b, q10, q10b, q11, q12b, q13, q14, q15, q16; 3 hard 429 failures unsaved: q05, q09, q12). ~12 files carried usable signal; 8 returned junk/garbage (recurring rfp.wiki comparison spam and Scribd/OSRS-class noise — the same late-run degradation R7 and R9 logged).
- **Distribution vs plan:** gap #2 got 6 executions (good coverage); gap #3 got 6 (2 junk, 1 partial); gap #4 got 3 (1 usable-negative, 1 junk, 1 hard-fail — weakest coverage); gap #5 got 6 (2 clean, 4 junk/fail).
- **Deadline discipline:** hard stop on new searches enforced at ~minute 14 (05:52:31–06:06:27 search phase); skeleton was live before the first query; this report written immediately after.
- **Follow-up queries for the next agent (priority order):** (1) Notilens — product page, pricing, traction, funding; (2) Doc Detective 2026 status + docs-as-tests adoption; (3) Trunk Flaky Tests + Launchable 2026 feature sets (diagnosis?); (4) Watchflow scope beyond n8n; (5) whether EU AI Act Art. 50 guidance or pending code-specific rules touch source-code authorship disclosure.
- No git commands run; only this track report, the r12 raw dir, and the worklog were touched. `gap-registry.md` NOT edited (main agent owns it — recommended update text above is the deliverable).
