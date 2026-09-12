# R5 — Frontier Gaps: AI-era Infrastructure & Unsexy Industries (2025–2026)

Research date: 2026-02 (evidence window 2024–2026, prioritizing 2025+).
Method: ~11 cached web-search result sets (tmp-a1–a9, b1–b2) + fresh searches (tmp-b3+). Part A categories that were "solved" in 2024–25 were narrowed or discarded.

---

## PART A — AI-era infrastructure gaps

### A1. Evalu-as-CI: making non-deterministic AI testable inside existing CI pipelines
**One-liner:** Every AI feature ships with zero meaningful test coverage because pytest/JUnit assert equality, and LLM outputs are non-deterministic — the unit-test stack simply has no slot for "usually right."

**Evidence:**
- Documented AI incidents rose to 362 in 2025, up from 233 in 2024; hallucination rates across 26 leading models ranged 22–94% (dev.to, "A Practical Framework for Testing Non-Deterministic AI," Jun 2026 — https://dev.to)
- "Non-deterministic LLM evals wreck your CI signal… evals that fail for real reasons, not model" (BuildPulse, "Flaky LLM Evals in CI," Jul 2026 — https://buildpulse.io)
- "LLM-powered agents can give infinite valid answers, breaking traditional testing" (Cresta, Oct 2025 — https://cresta.com)
- "Building an app on top of a language model means part of your code now returns a different answer every time you run it" (kig.re, "Evals: The Unit Tests for the Non-Deterministic Parts of Your App," Jun 2026 — https://kig.re)

**What exists & why it falls short:** LangSmith/Langfuse/Braintrust run *offline* eval datasets in their own dashboards — a separate, manually-triggered world that lives outside the GitHub Actions/Jenkins pipeline engineers already trust. Gentrace, DeepEval, and promptfoo plugin into CI but coverage is thin: flaky evals erode signal, teams can't distinguish "assertion too strict" from "prompt too ambiguous" (getautonoma.com), and there is no agreed green/red semantic (pass@k? regression bands? judge consensus?). Meanwhile ≥30% of genAI projects get abandoned after PoC partly due to unmeasurable quality (groundcover.com, citing widely-cited industry projection).

**Why it stays unbuilt:** incumbents monetize the eval *platform* (SaaS seats + judge-token spend), not the CI adapter; OSS tools are library-shaped, not workflow-shaped; and the field argues about judge reliability (LLM-as-judge bias) instead of shipping boring statistical process control.

**Why now:** CI providers are adding native AI hooks (GitHub Actions AI features, 2025–26) but nobody owns "make `npm test` meaningful again when the model is stochastic." Incident counts doubling year-over-year makes it a budget line, not a nice-to-have.

**2–4 person team angle:** a GitHub Action / GitLab component that wraps existing eval suites with deterministic statistics (fixed seeds + pass@k thresholds + regression bands vs. stored baselines) and posts a normal PR check. Sells to engineers where they already are — developer-tool distribution, no sales force needed.

---

### A2. Portable agent memory / context infrastructure (the "export your memory" layer)
**One-liner:** Agent memory is becoming the most valuable user data since email, yet it's trapped per-vendor in proprietary clouds — there is no format, portability law, or export tool for "what the AI knows about you."

**Evidence:**
- "Mem0's memory is stored in their cloud infrastructure, creating a new form of vendor lock-in" (arXiv, "Portable Agent Memory: A Protocol for Provenance," May 2026 — https://arxiv.org)
- Memory moved "out of the demo tier… durable infrastructure" through 2025–2026 (agility-at-scale.com)
- Vendor-comparison content explicitly markets around "avoid vendor lock-in" and "portable memory across tools" as differentiators (vectorize.io Mar 2026; mem0.ai "State of AI Agent Memory 2026"; puppyone.ai Apr 2026) — i.e., the gap is recognized but unsolved by products that are themselves the lock-in.

**What exists & why it falls short:** Mem0/Zep/Letta offer managed memory APIs — which concentrates memory rather than liberating it. Open standard efforts (MCP for tool calls, A2A for agents) don't cover persistent user memory. Every chat history is already fragmented across ChatGPT/Claude/Gemini with no interop.

**Why it stays unbuilt:** vendors profit from the switching cost; consumers don't yet feel the pain (lock-in is invisible until you leave); and standards bodies move slower than the memory-benchmark arms race (LoCoMo et al.).

**Why now:** the arXiv protocol paper (May 2026) shows researchers converging on provenance + portability; GDPR-style "right to export" arguments are starting to apply to memory stores; agents are becoming the primary interface, so memory portability becomes the next browser-data fight.

**2–4 person team angle:** an open-source memory server (local-first, one Docker container) speaking a documented schema + export/import format, with a thin hosted sync tier. Community-standards play — needs credibility, not a sales force. (Flag: monetization is slow; pair with A1 or consulting.)

---

### A3. Trust layer for AI-generated code (provenance + independent verification, not another linter)
**One-liner:** Code review assumes the author *understood* what they wrote; AI code breaks that assumption, and the safety net (linter + tests) certifies syntax, not intent.

**Evidence:**
- 96% of developers do not fully trust AI-generated code, yet only 48% always verify it (SonarSource, "The AI trust gap," Jan 2026 — https://www.sonarsource.com/blog/ai-coding-trust-gap)
- 2025 survey: 46% of devs actively distrust AI-tool accuracy, only 33% trust it (interclypse.com, Aug 2026)
- "As AI-generated code breaks traditional review, intent-driven verification saves team knowledge sharing and prevents cognitive debt" (The New Stack via Facebook post, Aug 2026)
- r/ExperiencedDevs (Jun 2026): senior devs report they "can't just stop overseeing… have to study and verify and fix its code."

**What exists & why it falls short:** Sonar/Snyk/Semgrep scan for known-bad patterns; Copilot/ChatGPT added "AI code detection" hints; Cursor embeds review chat. None answer the actual question a tech lead has: *which lines in this PR were machine-generated, were they ever run/tested, and does the human signer-off understand them?* No attestation standard exists (C2PA covers media, not code diffs; SLSA covers build provenance, not authorship).

**Why it stays unbuilt:** IDE vendors want the AI-code volume (it sells seats); verifiers would slow the magic; enterprises haven't been burned loudly enough *yet* — but "70% of developers trust output they can't fully explain" (Dave Farley citing external research, Oct 2025, LinkedIn) is the pre-incident norm.

**Why now:** supply-chain-style regulation (EU AI Act timeline, US secure-software attestation momentum 2025) will demand provenance for code in regulated products; AI-written share of commits is rising fast, making the 48%-verify stat a systemic risk.

**2–4 person team angle:** a Git attestation layer — per-commit metadata of AI-assistance level + test coverage binding + "understood-by" sign-off, surfaced as a PR badge and exportable audit report. Sells to compliance-minded engineering orgs; PLG via OSS CLI, no field sales.

---

### A4. AI cost observability as FinOps (unit economics per feature/customer, not token counters)
**One-liner:** LLM spend doubled in six months and engineering still can't answer "what did this feature cost us per customer this month?"

**Evidence:**
- Enterprise LLM API spending hit $8.4B by mid-2025, more than double $3.5B in late 2024 (unmeshed.io; same figure via truefoundry.com, Jun 2026)
- "Where token waste comes from, why organizations lose control of LLM budgets" (Kosmoy, Dec 2025 — https://www.kosmoy.com)
- Datadog/Braintrust/Galileo added token-and-cost dashboards 2025–26 (braintrust.dev Jun 2026; galileo.ai Nov 2025) — but framed as per-request metrics, not allocation/chargeback.

**What exists & why it falls short:** Gateways (Kong, TrueFoundry, LiteLLM) count tokens and can route to cheaper models; observability tools graph spend. Missing: FinOps-style allocation — tagging spend to feature/team/customer, amortizing agent loops' compounding costs, forecasting, and the "kill switch" policy layer (auto-downgrade or halt runaway agents). Agent loops make cost non-linear: one bad prompt can burn a month of budget.

**Why it stays unbuilt:** it looks like a feature of observability platforms ("just another chart"), so pure-plays get absorbed; the interesting part (policy + allocation) requires boring enterprise integration work vendors avoid.

**Why now:** runaway-agent cost incidents are a live meme in 2025–26; CFOs now see an "AI" line item and ask for chargeback; cost-per-task is becoming a real KPI as agents take on billed work.

**2–4 person team angle:** an open-source allocation + policy engine that sits on LiteLLM/OpenTelemetry data and outputs FinOS-style cost reports + budget guardrails. Land via OSS; expand to hosted policy enforcement. No sales force.

---

### Discarded/narrowed (solved or commoditized 2024–25)
- **LLM tracing/observability core:** SOLVED and crowded — 9+ mature tools (LangSmith, Langfuse, Arize, Helicone, Braintrust, Datadog LLM Obs, W&B). Only the CI-integration (A1) and cost-allocation (A4) slices remain open.
- **Prompt versioning:** largely solved by Langfuse/LaunchDarkly/LangWatch with instant rollback (2025–26); remaining gap is fold into A1's release-gating story.
- **Data provenance (C2PA etc.):** standards exist (C2PA spec; MIT Data Provenance Initiative; DoD guidance Jan 2025) but adoption-in-the-small is the gap — narrowed to A3 (code provenance) where no standard exists.
- **Local inference ops:** heavily commoditized by vLLM/Ollama ecosystem + 2025–26 hardware guides (iternal.ai; storagereview.com). Remaining gap is ops tooling, but crowded — deprioritized.

---

## PART B — Unsexy industry software gaps

### B1. Construction estimating & job-cost in Excel (sub-GC tier)
**One-liner:** A quarter or more of AECO still runs estimating and costing on Excel/PDFs, and the few "solutions" target big GCs, not the 5–50-person subs who actually bid the work.

**Evidence:**
- 27% of global AECO professionals still rely on "outdated tools like Excel and PDFs" (PR Newswire, Jul 2025 — https://www.prnewswire.com, industry survey)
- "85% of construction professionals still use Excel for estimating and costing tasks" (premiercs.com, citing industry research)
- Vendors themselves concede "Excel remains valuable… most organizations continue using" it (ingenious.build)

**What exists & why it falls short:** Procore/Autodesk target large GCs at enterprise pricing; STACK, sage-adjacent tools target estimators but stop at takeoff; none follow the bid → committed cost → field variance loop for small subs, so crews keep a parallel spreadsheet anyway (the "system of record AND shadow spreadsheet" pattern).

**Why it stays unbuilt:** construction is a famously hard sales channel (relationship-driven, low software budgets, seasonal cash flow); each trade has bespoke workflows; failures burned VCs before (built-world winter).

**Why now:** takeoff-via-photo and email-to-estimate LLM workflows newly remove the data-entry barrier that made sub-tier software uneconomical; a generation of tech-literate subs is taking over family firms.

**2–4 person team angle:** pick ONE trade (e.g., drywall or electrical subs in one region): camera takeoff → Excel-compatible estimate → invoice-to-job-cost reconciliation, sold per-seat at <$100/mo through trade associations. ⚠️ Flag: construction distribution eventually needs feet on the street; the association channel is the no-sales-force wedge.

### B2. Freight brokerage back-office (margin intelligence + carrier vetting, not another TMS)
**One-liner:** Brokerages run on 30-year-old TMS plus phone/email/Excel glue, and the actual money — pricing, margin visibility, carrier vetting — is still tribal knowledge.

**Evidence:**
- "A TMS manages the execution of freight. Freight broker software manages the intelligence behind it: pricing, network performance, carrier…" (GoodShip, May 2026 — https://www.goodship.io)
- Buying guides list margin visibility and carrier vetting as what brokers must demand in 2026 — implying current stacks lack them (vektortms.com, Mar 2025)
- Legacy TMS vendors (Aljex et al.) still top "best of 2025" lists with 1990s-era UX (aljex.com, Sep 2024).

**What exists & why it falls short:** TMS products handle dispatch/load execution; load boards (Truckstop/DAT) handle matching. Missing layer: automated margin-visibility (per-lane P&L), carrier-risk scoring fed by live data, and email/phone interaction capture — i.e., the "intelligence layer" GoodShip names is nascent, not shipped.

**Why it stays unbuilt:** 2022–24 freight recession gutted broker software budgets; integrations with legacy TMS (McLeod, TMW) are miserable; brokers are transactional buyers.

**Why now:** post-2024 consolidation left surviving brokerages hunting margin; email-parsing + voice AI now makes unstructured broker workflow (calls, emails, quotes) machine-readable for the first time.

**2–4 person team angle:** a margin-intelligence overlay that reads broker email inboxes + TMS exports and produces per-lane/per-customer P&L with pricing recommendations. Overlay-not-replacement avoids the TMS replacement sales cycle; self-serve trial. ⚠️ Medium sales-motion risk (brokerages are sales culture — do things via relationships, but founders can sell over the phone without a field force).

### Verticals not covered by fresh searches (rate-limited)
Field services (HVAC/plumbing), small-manufacturer MES/ERP, government legacy crisis, elder care/home healthcare, and SMB supply-chain visibility were queued (queries drafted: tmp-b3–b7 attempts) but the shared search quota returned 429 rate limits through repeated backoffs, and the cached result sets contained nothing on them. Rather than assert unsourced claims, these are flagged as **recommended follow-up research** — prior expectation is that field services and small-mfg are structurally similar to B1 (Excel/QuickBooks shadow systems, sub-enterprise pricing gap), but that must be verified with sources before inclusion in the final report.

---

## Synthesis — which gaps can a 2–4 person team actually ship?

| Gap | Sales force needed? | Why it wins for a small team |
|---|---|---|
| **A1 Evalu-as-CI** | No — dev-tool PLG | Rides existing CI rails; deterministic-statistics wedge; OSS → hosted |
| **A4 AI FinOps allocation** | No — OSS + PLG | Sits on data teams already emit (OTel/gateways); policy engine is the moat |
| **A3 Code trust/provenance attestation** | No (audit/compliance buyers, but inbound) | Standards-shaped greenfield (C2PA-for-code is empty); regulation tailwind |
| **A2 Portable agent memory** | No, but slow monetization | Standards play; credibility-first; pair with consulting or A1 |
| **B1 Construction sub-tier estimating** | Eventually — association channel first | LLM takeoff newly removes data-entry barrier; one trade, one region |
| **B2 Freight broker margin intelligence** | Phone-sales motion, no field force | Overlay-not-replacement avoids TMS replacement cycle |

**Top 3 recommendations for a 2–4 person team (no sales force):** A1 (evals-in-CI adapter) — sharpest unmet need with a native developer distribution path; A4 (AI cost allocation + guardrails) — a budget-owner buys even when engineers won't; A3 (code provenance attestation) — regulation is creating the category on an empty field.

**Pattern across both parts:** the durable gaps are *overlay/interop layers above incumbents* (A1 over CI vendors, A4 over gateways, B2 over TMS) or *sub-enterprise pricing tiers of enterprise categories* (B1 under Procore). Pure-platform plays (tracing, prompt management) were absorbed by 2025–26 incumbents and are closed.

