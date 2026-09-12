# R2 — Gaps in Integration, Data Layer & System Interconnection (2025–2026)

**Research task R2:** where is the broken plumbing between business systems? Missing migration/exit tooling, SMB data layers, identity/permission sync, legacy modernization, spreadsheet-as-database, and B2B interconnection.

**Method note:** z-ai web_search was quota-saturated by sibling agents (persistent HTTP 429 across ~25 retry cycles / 8 distinct queries). Evidence below was harvested and verified from cached sibling search-result files in this workspace (`research/tmp/s03–s17`, `tmp-a4`, `tmp-b1`) — every URL, date, and claim was read directly from those stored results. All numbers were actually seen in the cited sources; none are invented. Zapier, Fivetran, Workato, Airbyte, Okta etc. exist and are acknowledged — the focus is what remains **uncovered**.

---

## Gap 1 — Integration debt: unowned, unobserved pairwise wiring that breaks silently

**One-liner:** Companies run on point-to-point integrations built under deadline pressure, and nobody — vendor, iPaaS, or customer — is paid to detect when they silently break.

**Evidence:**
- "Integration debt is the accumulation of technical compromises in how systems communicate — point-to-point connections built under time pressure" — Bluepes, *Cost of poor integration* (Apr 2, 2025), https://bluepes.com/blog/the-hidden-costs-of-poor-integration
- "Enterprise Integration Crisis: Why IT Teams Are Rebuilding" — deferred integration architecture decisions and outdated iPaaS (ezintegrations.ai, Jun 11, 2026), https://ezintegrations.ai/integration-debt-enterprise
- "40% of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% in 2025" — i.e., agent integrations are about to multiply the fragility (LinkedIn/Gabe Veach, Apr 20, 2026), https://www.linkedin.com/pulse/fragility-point-to-point-integration-why-matters-your-gabe-veach-dt23c
- API deprecation is handled manually: "reading deprecation notices, updating code, testing, deploying" (davidpoll.com, Oct 19, 2025), https://www.davidpoll.com; an ACM study found **2.30% of dependency updates carry behavioral (invisible) breaking changes** (https://dl.acm.org, Jul 2024)
- Webhooks fail in production with "duplicates, out-of-order events, failed retries… debugging at 2 AM" (salable.app, Feb 4, 2026, https://salable.app; stork.ai, Jul 17, 2026)

**What exists & why it falls short:** Zapier/Make (per-task pricing that punishes volume — Cybernews Zapier review, May 18, 2026, https://cybernews.com); Workato/Boomi/MuleSoft ($50k+, expert-operated); Fivetran/Airbyte (ELT to warehouses, not operational write-back); Merge/Apideck (unified APIs = lowest common denominator). None of them *watch* the pipeline after setup: no drift alerts, no replay, no failure ownership.

**Why nobody built it:** detecting someone else's breakage is blame-heavy, unglamorous; incumbents monetize task volume, not reliability.

**Why now:** agent integrations (<5% → 40% of apps in one year, per Veach) are about to multiply the number of brittle pairwise links; LLMs can read changelogs/diffs and propose mapping repairs.

**2–4 person angle:** an **integration observability proxy** — sits between customer and existing Zapier/webhooks/exports, alerts on schema drift, empty payloads, dropped events; offers one-click replay and diff reports. Read-only, no migration, sells to whoever's paged when sync dies.

---

## Gap 2 — The SMB data layer: the modern data stack ends at ~employee #100

**One-liner:** Fivetran→Snowflake→dbt→BI presumes an analytics engineer; companies below that get CSV email attachments and "ductaped spreadsheet" stacks.

**Evidence:**
- "The Current Data Stack Is Too Complex — 70 Data Leaders & Practitioners Agree" (Medium, Mar 13, 2025), https://medium.com/@community_md101/the-current-data-stack-is-too-complex-70-data-leaders-practitioners-agree-b460821b07dd
- 63% of data practitioners spend >20% of their time just coping with data-stack complexity (The Modern Data Company, Aug 21, 2025), https://www.themoderndatacompany.com/blog/new-report-reveals-how-data-architecture-complexity-is-undermining-decision-making-and-ai-innovation
- DTC operators "gather, clean up, and reconcile" fragmented data by hand (moselle.io, Mar 11, 2025), https://moselle.io/blog/why-data-fragmentation-is-stifling-your-growth
- "You have enterprise data stack held by ductaped spreadsheet" (LinkedIn/Ali Šifrar, Oct 13, 2025); "The Modern Data Stack Is Broken" (TimeXtender, Jul 24, 2026), https://www.timextender.com/blog/data-empowered-leadership/the-modern-data-stack-is-broken

**What exists & why it falls short:** enterprise stack (too complex, per the 70-leaders piece); Fivetran's own SMB playbook presumes hiring a data consultant (fivetran.com blog, May 2023); 2025–26 "AI analysts" sit on the same fragmented connectors and inherit the same stale, permission-wrong data.

**Why nobody built it:** SMBs won't pay much for invisible plumbing; each SaaS ships its own dashboard, so the cross-system layer falls between every vendor's responsibility.

**Why now:** fully-managed $50–500/mo stacks are viable; LLMs can write and self-heal SQL/models.

**Angle:** an opinionated **data layer for one vertical** (e.g., 20-person e-commerce brands): normalize Shopify + ads + ERP + shipping into one owned schema, exposed as metrics *and* an API their agents can query.

---

## Gap 3 — Exit & migration tooling: regulators killed egress fees, but leaving is still archaeology

**One-liner:** Switching systems remains hand-built CSV migration where history, attachments, custom fields, and workflow logic are quietly lost — the exit side of the market has no tooling.

**Evidence:**
- Vendor lock-in costs enterprises an average **$315K per migration** (Kong, Jun 30, 2026), https://konghq.com/blog/learning-center/vendor-lock-in
- "Regulators are intensifying their scrutiny of cloud pricing, focusing on egress fees and switching friction that keep customers locked in" (Sep 18, 2025), https://www.youtube.com/watch?v=2jPdPuegE9I
- ERP migrations are the extreme case: 73% of discrete-manufacturing ERP projects miss objectives with **215% average cost overruns** (godlan.com, 2026); **62% of organizations cite data migration as a failure driver**; mid-size ERP averages **$7.1M and 17.4 months** (companieshistory.com, Jun 12, 2026); Panorama 2025 puts overall failure at 68% (kreativecoretech.com, Jul 11, 2026)
- Even trivial exits are scrambles: Notion Mail's sunset gave users until Sept 21, 2026 to export, while connected database syncs broke (TechCrunch, Jun 25, 2026, https://techcrunch.com; quicktion.io, Aug 20, 2026)

**What exists & why it falls short:** destination vendors build *import* wizards (biased, shallow — contacts but not history/audit/workflows); egress-fee removal solves the *cost* of leaving, not the *mechanics*; nothing exports workflow logic (the 200 zaps, automations, permission model) — the real lock-in.

**Why nobody built it:** exit buyers are customers already leaving (one-time, awkward revenue); vendors resist neutral portability.

**Why now:** EU Data Act portability obligations (applicable Sept 2025) create first-ever compliance demand; LLMs can translate schema *and* workflow definitions between systems.

**Angle:** **migration-as-a-service for one fleeing path** (a dying/hated platform → its rival): data + workflow translation, fixed project fee, recurring revenue via destination-vendor referrals.

---

## Gap 4 — Identity syncs accounts, not permissions: "who can do what" is unanswerable

**One-liner:** SCIM provisions login accounts, but each app's internal permission graph drifts silently — offboarding removes the login, not the access.

**Evidence:**
- SCIM "only if you stuck to its rigid schemas and limited provider support" (yeshid.com, Sep 11, 2025), https://www.yeshid.com
- The old "90% of SaaS apps don't support SCIM" stat is misleading — most support it "but there's a catch: you can't [use it] without an enterprise plan" (stitchflow.com, Jan 28, 2026), https://www.stitchflow.com
- IT managers struggle with the SSO/SCIM tax and apps lacking SAML/SCIM (accessowl.com, 2026, https://www.accessowl.com; zluri.com); ssotax.org documents workarounds that "sync user lists, assign roles, and remove access… bypassing SCIM"
- Per R4's search findings: Glean merely *mirrors* per-app permissions — permission chaos propagates into every new layer (enterprise search, and soon agents)

**What exists & why it falls short:** Okta/Entra SSO+SCIM (user objects only); SailPoint-class IGA (six figures, assumes an IT department). Nothing reads the *role/permission graph* inside each app — many have no API for it at all.

**Why nobody built it:** permissions APIs are uniformly bad or absent; no single vendor benefits from exposing cross-app access truth.

**Why now:** SOC 2/insurance pressure now reaches SMBs; browser automation + LLMs can read admin-console permission screens even with no API.

**Angle:** a **permission census scanner** — headless-browser crawls each admin console, diffs permission state over time, alerts on drift/orphaned access, emits the audit table. Read-only, per-app pricing.

---

## Gap 5 — Legacy modernization stuck: COBOL's crisis is knowledge, not code

**One-liner:** 220–800B lines of COBOL still settle 80% of financial transactions, the experts are retiring, and AI code translation doesn't fix it because the bottleneck is recovered business rules, not syntax.

**Evidence:**
- "220 billion to 800 billion lines of COBOL still power 80% of the world's financial transactions — built by a generation now walking toward [retirement]" (phasechange.ai, Oct 15, 2025), https://phasechange.ai
- A single blog post about AI COBOL translation wiped ~13% ($30B) off IBM's market cap; "AI-assisted code analysis isn't new — and translating code isn't the same as modernizing" (devops.com, Feb 25, 2026), https://devops.com
- COBOL developers average $125,525/yr with demand projected to grow 15% over the next decade (metaintro.com, Mar 17, 2026), https://www.metaintro.com

**What exists & why it falls short:** consultancy programs, AWS Mainframe Modernization, IBM watsonx Code Assistant for Z — aimed at Fortune-500 mainframes and code translation. The long tail of mid-market AS/400, Delphi, Access, VB6 line-of-business apps has no tooling and no staff to validate translations.

**Why nobody built it:** mid-market legacy is individually unglamorous, collectively enormous; the artifact that's missing (executable behavior spec) isn't what code-translation vendors sell.

**Why now:** the workforce that could validate a rewrite is literally leaving; LLMs can interview domain experts and emit testable characterization specs.

**Angle:** **legacy behavior extraction** for one platform (e.g., AS/400 or Delphi): deliver an executable spec + characterization test suite any modernizer can build against. Sell the spec, not the rewrite.

---

## Gap 6 — Spreadsheet-as-database: the world's actual data layer has no guarantees

**One-liner:** Estimating, healthcare PHI, freight, HR tracking run on Excel files serving as database + integration bus + UI at once — unversioned, unpermissioned, unaudited.

**Evidence:**
- 85% of construction professionals still use Excel for estimating and costing (premiercs.com, 2026), https://premiercs.com; 27% of global AECO professionals still rely on Excel/PDFs (PR Newswire, Jul 28, 2025), https://www.prnewswire.com
- Unmanaged PHI in spreadsheets adds an average **$670,000 to healthcare data breach costs** (blueBriX, 2026), https://bluebrix.health/blogs/shadow-it-in-healthcare-the-risks-of-excel-reporting
- "Shadow IT never dies — why spreadsheets are still running your business" (Diginomica, Mar 17, 2023), https://diginomica.com/shadow-it-never-dies-why-spreadsheets-are-still-running-your-business; academic work finds low end-user awareness of spreadsheet risk ("Spreadsheets: risk from the shadow," RePEc/IDEAS)

**What exists & why it falls short:** Airtable/Notion/Smartsheet ask for greenfield rebuilds — migrations lose 15 years of formulas/macros, so users keep shadow copies and the "system" bifurcates. Crucially, the Excel file *is* the integration layer (manually pasted between systems); replacements don't speak to the surrounding stack either.

**Why nobody built it:** "Excel killers" compete on features; Excel wins on zero cost + infinite flexibility. The missing product *absorbs* the workbook instead of replacing it.

**Why now:** LLMs can finally read a gnarly workbook — formulas, structure, VBA — and infer schema and invariants.

**Angle:** **Excel ingestion, not replacement**: point at the operational workbook, auto-generate schema + change-tracking + audit log + API around the same (or mirrored) file; humans keep Excel as UI. Sell the audit trail.

---

## Gap 7 — Real-time plumbing is enterprise-only by construction

**One-liner:** Kafka-class event streaming is architecturally "correct" but operationally absurd for small teams, so they get hours-stale batch or nothing — the reliable middle is empty.

**Evidence:**
- "Kafka is overkill for simple task queues" (inteca.com, May 6, 2025), https://inteca.com
- "Most teams evaluating Kafka alternatives don't need event streaming" — they need delivery guarantees (redisson.pro, Jul 22, 2026), https://redisson.pro
- Teams flee Kafka over "broker cost, storage growth, rebalancing delays, scaling limits" (automq.com, Jun 1, 2026), https://www.automq.com; a whole 2025–26 product category (Inngest et al.) exists just to simplify it, https://www.inngest.com

**What exists & why it falls short:** Kafka/Pulsar (ops burden), Confluent Cloud (assumes schema-governance discipline), managed CDC (enterprise ELT). Small firms need an *outcome*: "record changed → downstream apps see it now, idempotently, with retries."

**Why nobody built it:** the neediest buyers can't operate the platform; vendors earn more from complexity; "real-time" has been over-marketed into distrust.

**Why now:** durable-execution / queue-as-a-service primitives (Temporal-class, Cloudflare Queues) make guaranteed fan-out a product, not a platform team.

**Angle:** **webhooks with guarantees** for one ecosystem (e.g., commerce): exact-once fan-out, replay, dead-letter dashboard, schema versioning — the 10% of Kafka 90% of small integrators need.

---

## Gap 8 — Inter-company integration still runs on batch files over SFTP/EDI

**One-liner:** The actual B2B integration layer is nightly SFTP drops and EDI batches; every B2B SaaS hand-rolls per-client file ingestion with no tooling.

**Evidence:**
- B2B SaaS must "ingest, validate, map, and deliver client files automatically, without custom scripts for every [client]" — the pitch itself confirms today's norm is custom scripts (filefeed.io, Feb 28, 2026), https://www.filefeed.io
- SFTP "lacks native checkpoint[s]" for large EDI batches (focused-ec.com, Jul 21, 2026), https://www.focused-ec.com; batch file processing creates latency "between EDI receipt and ERP update" (boldvan.com); even 2026 "modern EDI" guides are enterprise-suite framing (cleo.com)

**What exists & why it falls short:** enterprise EDI/B2B gateways (Cleo, IBM-class — priced and staffed for the Fortune 500); iPaaS connectors target APIs, not your clients' arbitrary CSV/XLSX/EDI drops. SMB SaaS vendors build bespoke parsers per client and reconcile via email.

**Why nobody built it:** every client's file is a bespoke contract; the work hides inside "professional services" line items, so no standalone product forms.

**Why now:** LLMs make arbitrary-file schema inference cheap — the per-client custom-script tax is newly automatable.

**Angle:** **"drop-box to database" ingestion for one vertical's SaaS vendors**: monitored SFTP in → auto-detected schema → validated/mapped rows out via API/webhook, with per-client exception dashboards. Sell per-client-per-month, to the SaaS vendor, not the end user.

---

## Cross-cutting synthesis

1. **Connectivity exists; ownership doesn't.** The failure mode moved from "can't connect systems" to "nobody is paid to notice the connection broke" (Gaps 1, 7, 8).
2. **Every layer presumes an operator.** dbt presumes an analytics engineer, Kafka a platform team, SailPoint an IT department, mainframe modernization a consultancy (Gaps 2, 4, 5). Below ~100 employees there is no such person, so the layer silently reverts to spreadsheets (Gap 6) and email attachments.
3. **Entry is funded, exit is not.** Vendors build generous import tooling; exits are $315K-average, 62%-migration-driven failures (Gap 3) — until the Data Act forces a market.
4. **AI raises the stakes on plumbing.** Agent integrations are projected to grow from <5% to 40% of enterprise apps within 2026 (Veach) while AI analysts inherit fragmented connectors and mirrored permission chaos — the AI era's bottleneck is precisely this boring, unglamorous integration layer.

*(File complete; sources verified against stored search results. Own z-ai searches were blocked by shared-quota 429s — noted in worklog.)*
