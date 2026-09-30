# R11 — Model Portability Across LLM Vendors (2025–2026)

Task ID: **R11** | Agent: general-purpose | Date: 2026-09-30
Vertical: "Model portability across LLM vendors" — the last AI-infrastructure item on the never-searched backlog (all prior attempts died on rate limits, per R5 §Verticals-not-covered). This is both a first entry and a fresh-eyes verification: the AI-infra rows move fastest, so every "gap" candidate was kill-listed against the 2026 field.

**Method:** 22 `web_search` executions → 20 raw files saved to `research/raw-search-results/r11/` (q01–q15 incl. 7 b-retries; 2 hard-429 failures at q05/q07 — each retried once per protocol; 5 thin-return retries q01b/q04b/q09b/q12b/q13b, of which 4 recovered signal). `sleep 20–35` between queries; one concurrent sibling agent sharing quota. ~13 of 20 sets carried usable evidence. Evidence window Jan 2025–Sep 2026; a few undated hosts flagged. No statistic invented; pre-2024 numbers would be flagged (none used).

---

## Headline findings

1. **The gateway/unified-API layer is a CLOSED, crowded category — and it never promised behavior portability in the first place.** "Top 5 AI Gateways in 2026" already lists Bifrost, Cloudflare, Kong, Helicone, LiteLLM (getmaxim.ai, Jan 5, 2026), with Portkey/OpenRouter/Odock/Vercel AI Gateway on the same field (odock.ai comparison, Jul 2, 2026; Vercel AI Gateway pricing tracked at $0.042/M input, jevaiguide.com, Sep 25, 2026). The category normalizes the *request envelope*; the review field itself concedes behavior doesn't transfer: **OpenRouter "scores lowest on portability"** in a pros/cons review despite scoring highest on integrations and routing/fallbacks (faun.dev, undated in results), and "Assuming 'OpenAI-compatible' means interchangeable — **It doesn't.** Test the actual failure modes per provider — refusals, malformed tool calls" (aiwisdom.dev, Jul 29, 2026).

2. **The API "standard" is fragmenting at its own source.** OpenAI's Responses API forked its own de-facto standard: the *same model behaves differently* across Responses vs Chat Completions (lesswrong.com, Apr 11, 2025); parallel tool-calling behavior differs between the two APIs on identical requests, consistent across Azure too (community.openai.com, Dec 18, 2025); strict-by-default vs non-strict function schemas diverge (dev.to, Mar 18, 2026); OpenAI began deprecating chat/completions in Codex (github.com issue #7782, Sep 20, 2026); and the sharpest take: "The whole point of OpenAI's Responses API is to help them [lock you in] — there is nothing inherent about a stateful inference API that's better than a normal chat/completions stateless one" (seangoedecke.com, Sep 9, 2025). Vendors themselves now speak of **"The Five Layers of AI Vendor Lock-In"**, naming prompt portability (Layer 2: same prompt → different results) and fine-tune portability (Layer 3: custom models don't transfer) as distinct lock-in strata (theagilemonkeys.com, undated).

3. **Agent performance is scaffold-shaped, not model-shaped — which is why "swap the model" can't be tested at the benchmark layer.** "LLM agent benchmark scores are shaped not only by the model but also by the agent harness, environment, evaluator, and inference budget" (searcharxiv.com, Aug 6, 2026); traditional MMLU/HumanEval-style benchmarks "fall short in capturing operational behaviors of agents that call tools" (uixstore.com, undated); a survey formalizes agent eval as its own two-dimensional taxonomy (alphaxiv.org, Jul 29, 2025). Tool schemas still diverge at the wire level — OpenAI `tools` array with `type: function` vs Anthropic's distinct format (digitalapplied.com, Apr 1, 2026) — and models without tool support "will ignore the tools entirely" (lists.nongnu.org `llm` library changelog, undated). MCP is emerging as the *tool-side* portability layer: "An MCP server works with any MCP client regardless of which LLM powers it. Your tools aren't locked to OpenAI's format or Anthropic's format" (prefect.io, Apr 14, 2026; same framing at descope.com, Nov 3, 2025; nango.dev, Jul 14, 2026) — but MCP normalizes the tool boundary, not the model's calling behavior.

4. **Cross-model regression testing is half-served: the eval platforms own the matrix, promptfoo owns the CLI, and the CI gate is being monetized — which is exactly evalgate's ground.** Promptfoo is "an open-source CLI tool that runs your test cases against one or more LLM providers at once" (botmonster.com, May 12, 2026); Braintrust/LangSmith/Phoenix are compared explicitly on "evaluations, CI gates" (cipherprojects.com, Jul 17, 2026) with per-score pricing — "Braintrust bills $1.50 per 1000 scores… Don't Pay for the Gate" (beri.net, Aug 26, 2026); the 2026 eval-tool field is a ranked list of 8–9 platforms (dupple.com, Jun 16, 2026; confident-ai.com, Sep 21, 2026). Nobody in evidence ships a deterministic, per-provider-baselined, interval-statistics **swap check** as a CI artifact.

5. **Models are being recognized as external dependencies with EOL clocks — and no Renovate-for-models surfaced.** "The Model EOL Clock: Treating Provider LLMs as External Dependencies… OpenAI's deprecations page lists dozens of retired models since 2023, with notice periods ranging from 14 days (for ChatGPT-only models) to…" (tianpan.co, Apr 16, 2026). The dev-workflow skill ecosystem is already emerging around it ("openrouter-upgrade-migration" skill covering "migrating from direct APIs, switching between models, upgrading SDK versions, and running comparison tests," lobehub.com, undated). Gateway concentration also creates a security surface: malicious LiteLLM-proxy packages were published to PyPI in a CI/CD credential harvest (think-ahead.tech, Apr 3, 2026) and Langflow/LiteLLM CVE-2026-5027 patch-lag was still being exploited later (linkedin.com, undated).

---

## 1. The gateway/unified-API layer in 2026 — what normalizes, what breaks

**Evidence.** The field is thick and consolidating: Bifrost/Cloudflare/Kong/Helicone/LiteLLM named as top 5 (getmaxim.ai, Jan 5, 2026); LiteLLM vs Kong vs Cloudflare vs Portkey vs Odock compared with the framing "the meaningful difference is not whether a product can proxy an OpenAI-style request. The difference is where each product starts from" (odock.ai, Jul 2, 2026). Cloudflare AI Gateway pricing/models/limits are tracked as a catalog (llmgatewayhub.com, Aug 22, 2026); Vercel AI Gateway sells unified pricing ($0.042/M input tokens, 32,000-token limits, jevaiguide.com, Sep 25, 2026) — and even third-party guides must "separat[e] what Vercel confirms from the model contract documented by Cloudflare" (jev-ai-guide.com, Sep 20, 2026), a telling detail about contract drift between the two. OpenRouter keeps expanding surface (audio transcription API with unified billing behind one compatible endpoint, remio.ai, undated).

**What still breaks (dated):** provider-specific multimodal constraints survive the unified layer — e.g., URL-delivered images are "not supported by Amazon Bedrock (hard requirement: base64 or S3)" (therouter.ai, undated); behavior divergence (parallel tool calls, strictness defaults, refusal patterns, malformed tool calls) is explicitly called out as something you must "test per provider" (aiwisdom.dev, Jul 29, 2026; community.openai.com, Dec 18, 2025). Prompt-caching economics also don't port: "Prompt caching cuts LLM API costs up to 90%… Claude vs OpenAI vs Gemini pricing, real cost math" — each vendor's caching rules differ (solutiongigs.in, Aug 7, 2026), so a cost-optimized architecture on one vendor is not cost-portable to another.

**Why open / why not:** as a *product category* this is closed — KILLED. As a *behavioral* problem it's open but it lives above the gateway, in testing.

## 2. The agent question — does my agent survive a model swap?

**Evidence.** Wire-format divergence persists (digitalapplied.com, Apr 1, 2026) even as concepts converge ("OpenAI calls it 'function calling' while Anthropic calls it 'tool use,' but the implementation is nearly identical," blog.stackademic.com, May 7, 2026). Migration produces real bug classes: "I migrated a LangChain Agent to Function Calling and hit 4 bugs: wrong tool calls, repeat calls, and missing safety checks" (pub.towardsai.net, Aug 25, 2026). The deeper problem is confounding: agent scores are harness/env/evaluator/budget-shaped (searcharxiv.com, Aug 6, 2026), so a model-swap eval must hold the scaffold constant and vary only the model — the opposite of public leaderboards, which vary both. MCP is the partial solver at the tool boundary (prefect.io, Apr 14, 2026) but sits below the model's *calling* behavior.

**Tried & failed / existing solvers:** promptfoo (multi-provider test runs, OSS CLI — botmonster.com, May 12, 2026); eval platforms with cross-model matrices and CI gates (cipherprojects.com, Jul 17, 2026; lyzr.ai 2026 list: "Run the identical test…"). **What's missing:** deterministic green/red semantics for *swap decisions* — per-provider baselines with interval statistics and a portability diff, i.e., precisely the statistics+gate layer svx-evalgate already owns, extended along a provider axis. This is an **evalgate extension**, not a new repo (reasoning in §Registry).

## 3. Migration stories 2024–2026

Honest note: this run surfaced **consumer/individual switching stories** (tinkeringwithideas.io, Jan 14, 2026; ai.plainenglish.io 60-day switch, Jun 11, 2026; HN "GPT-5 for Developers," Aug 7, 2025 — sentiment: "OpenAI's reasoning models write better code… but Claude Code is a much more useful product") but **no dated company-level infra migration post-mortem** (what broke, what it cost). The HN/engineering-blog migration-war-story query died to junk (q13/q13b). This sub-topic stays UNVERIFIED — flagged for a follow-up pass (see §Quota).

## 4. "The OpenAI API is the standard" — 2026 status: **forking from within**

Same-model behavior differs across OpenAI's own two APIs (lesswrong.com, Apr 11, 2025); identical requests diverge on parallel tool calls across Responses vs Chat Completions, on Azure too (community.openai.com, Dec 18, 2025); strict-by-default vs non-strict function schemas (dev.to, Mar 18, 2026); chat/completions being deprecated in Codex tooling (github.com, Sep 20, 2026); the lock-in thesis stated outright (seangoedecke.com, Sep 9, 2025). Add "OpenAI-compatible ≠ interchangeable" (aiwisdom.dev, Jul 29, 2026) and OpenRouter's own low portability score (faun.dev), and the standard's 2026 status is: *the request format* is near-universal, *the behavior contract* is not — not even within one vendor.

## 5. Prompt portability

User-level evidence of breakage: "a prompt that works perfectly in ChatGPT fails miserably in Claude or Gemini. Why is there such a discrepancy?" (icertglobal.com, Mar 2, 2025); "the same prompt produces different results on different models" as lock-in Layer 2 (theagilemonkeys.com, undated); "prompt portability between models is limited because different models and architectures respond differently to the same prompts" (zenml.io, undated). Counterpoint: "prompts are portable. A prompt is just text… the core of a good prompt" transfers (keepprompt.net, Sep 3, 2026) — and side-by-side arena tooling exists for individuals (makeuseof.com, Aug 12, 2026). **Verdict:** generic prompt-regression testing is served (promptfoo, §2); the remaining unserved slice is *agent-level* portability (system prompt + tool schemas + scaffold), which folds into §2's extension.

## 6. Cost/latency routing — closed as a category

Active research + shipping products: RouteLLM "over 2x cost saving" (ResearchGate/LinkedIn summaries in q12b; paper is pre-2025, flagged), robust batch-level routing under cost/GPU/concurrency constraints (arxiv.org, Mar 25, 2026), unified routing formulations (papers.ssrn.com, undated), dynamic routing/cascading (openreview.net, undated), and productized claims — "Route each AI request to the cheapest capable model… slash agent costs by over 60% in 2026" (o-mega.ai, undated). The honest caveat survives: "Model routing and cascades trade some quality risk for speed and cost, which is a real trade-off, not a free lever" (frenchydigital.com, undated). **KILLED for a small team** — the wedge there is measurement, not routing (and measurement is §2/§registry).

---

## Kill-list table

| Candidate gap | Attack (what I searched for as the existing solver) | Verdict |
|---|---|---|
| Build a unified LLM gateway / OpenAI-compatible abstraction | Top-5 gateway lists, LiteLLM/Kong/Cloudflare/Portkey/Odock/OpenRouter/Vercel comparisons (getmaxim Jan 2026; odock Jul 2026; faun.dev; llmgatewayhub Aug 2026) — the field is crowded and consolidating | **KILLED** (category closed; behavior-portability residue moves to testing layer) |
| Generic multi-provider prompt regression testing | promptfoo explicitly "runs your test cases against one or more LLM providers at once" (botmonster, May 2026); Braintrust/Langfuse matrices (cipherprojects Jul 2026; lyzr 2026) | **KILLED** at prompt granularity |
| Cross-model **agent** regression gating in CI (swap check with per-provider baselines) | promptfoo (prompt-granularity, no interval-statistics swap semantics); eval platforms monetize the gate ($1.50/1000 scores, beri.net Aug 2026); no deterministic per-provider-baseline diff artifact surfaced | **SURVIVED** — but as an **evalgate extension**, not a new repo (see below) |
| Cost/latency routing as a product | RouteLLM, SSRN/openreview routing literature, OpenRouter/LiteLLM/Portkey built-in routing, o-mega "cut agent costs 60%" | **KILLED** (competitive/closed; quality-risk caveat is research, not a product gap) |
| Model EOL / dependency management ("Renovate for models": deprecation clock + version-pin canary evals) | Only the thesis piece surfaced (tianpan.co, Apr 16, 2026) + skill-level workarounds (lobehub "openrouter-upgrade-migration"); **dedicated kill search NOT executed before deadline** | **UNVERIFIED** — follow-up kill pass required before any registry promotion |
| Company migration war-stories corpus (2024–2026 switch costs) | HN/Ask-HN + engineering-blog queries returned consumer-switch pieces only (q03/q13/q13b) | **UNVERIFIED** (evidence thin; likely exists but not captured in this window) |
| Tool-schema portability layer | MCP explicitly solves the tool boundary: "Your tools aren't locked to OpenAI's format or Anthropic's format" (prefect Apr 2026; descope Nov 2025; nango Jul 2026) | **KILLED** at the tool-boundary layer (model-calling behavior remains §2 territory) |
| Gateway security monitoring (supply-chain, CVE patch-lag on LiteLLM-class proxies) | Real incidents found (PyPI malicious LiteLLM-proxy packages, think-ahead.tech Apr 3, 2026; CVE-2026-5027 exploitation lag, linkedin.com) but **no dedicated kill search** performed | **UNVERIFIED** (recorded as observation; adjacent to security/supply-chain lens candidate) |

No verdict above is invented: SURVIVED/UNVERIFIED both name the missing kill pass explicitly.

---

## Registry recommendation

**Primary call: this is an evalgate extension, not a new repo.**

Reasoning, traced to evidence:
- The surviving behavioral gap (§1, §2, §4) is *testing-shaped*: "test the actual failure modes per provider" (aiwisdom.dev, Jul 29, 2026). The gateway field is closed (KILLED), routing is closed (KILLED), MCP covers the tool boundary (KILLED at that layer), and prompt-granularity multi-provider testing is promptfoo's (KILLED at that granularity).
- What no one in evidence ships: a **deterministic model-swap check** — run the same agent/eval suite against N providers, keep per-provider baselines with confidence intervals, and emit a green/red + portability-diff as a CI artifact. The eval platforms monetize the gate itself ($1.50/1000 scores, beri.net, Aug 26, 2026) — the same structural opening (gap #1's "why open") that produced svx-evalgate, now along a *provider axis* instead of a time axis.
- evalgate v2.1.0 already has the load-bearing pieces: deterministic statistics (pass@k, Wilson intervals, seeded bootstrap), baselines, `evalgate diff`, JUnit/pytest ingestion, exit-code contract. The extension is a second baseline dimension (provider/model tag) + a swap-diff report + docs on "hold the scaffold constant, vary only the model" — the exact discipline the confounding evidence demands (searcharxiv.com, Aug 6, 2026).
- Distribution format: unchanged from gap #1 — GitHub Action / CLI, PLG, no sales force. AI-economics angle: routing claims 60% savings (o-mega.ai) but quality risk is real (frenchydigital.com) — a swap check is what makes the routing trade-off measurable, so it rides the routing wave rather than competing with it.

**Secondary (do NOT promote yet):** if a follow-up kill pass confirms no solver, a model-dependency/EOL manager (deprecation clock + version-pinned canary evals; tianpan.co, Apr 16, 2026 as thesis) would enter as a new OPEN-NEW row — proposal drafted, promotion gated on the kill search named in the kill-list table. **Do not** add rows for gateway, routing, prompt-regression, or tool-schema layers — those are successful kills (market-closed findings; record in registry change log as CLOSED-with-closing-product if the maintainer wants the audit trail).

**For the registry maintainer (gap-registry.md not edited by me, per rules):**
1. Tick the "Model portability across LLM vendors" backlog item — now searched (this report).
2. Consider a one-line note on gap #1 (evalgate): "R11 proposes provider-axis extension (swap check) — see R11 report" + status stays BUILT with the extension noted as an AGENT-GOALS candidate.
3. Optionally record the kills (gateway/routing/promptfoo/MCP) as CLOSED findings.

---

## Quota / deadline notes

- 22 executions / 20 saved files / 2 hard-429 failures (q05, q07 — each retried once, per protocol). Thin returns (≤4 results): q01 (1), q07b (1), q09 (1), q12 (1), q13 (1), q11 (2), q06 (3) — of these, q04→q04b, q09→q09b, q12→q12b, q13→q13b retries recovered usable signal; q11 (prompt caching) stayed thin and leans on a single source (solutiongigs.in, Aug 7, 2026).
- Usable sets: ~13 of 20. Search API degradation matched R7/R9 patterns (junk returns late in run). Hard stop enforced ~minute 15 of search phase; report written from saved evidence only.
- Follow-up queries specified for the next agent: (1) kill-search "model EOL tracker / LLM deprecation monitoring tool" (the UNVERIFIED row above); (2) company migration post-mortems ("migrated our LLM stack from X to Y" engineering-blog phrasing); (3) Bedrock/Vertex-specific divergence guides; (4) whether promptfoo/Braintrust ship per-provider baseline diffs natively (feature-page checks, not listicles); (5) LiteLLM/Portkey "provider support matrix" failure ledgers.

*Raw evidence: `research/raw-search-results/r11/` — 20 JSON files, q01–q15 incl. b-retries (immutable). Every dated claim above traces to a file in that set.*
