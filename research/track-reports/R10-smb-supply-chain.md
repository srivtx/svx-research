# R10 — SMB Supply Chain Software (20–500 employees): First Entry into a Never-Searched Vertical

Research task R10, run 2026-09-30. Scope: who serves 20–500-employee companies for demand planning / inventory / supplier communication / inbound freight; what SMBs actually run (Excel evidence); pain pockets (forecasting, supplier side, inbound freight, multichannel inventory, customs/tariffs); 2024–2026 landscape shifts (tariffs, AI entrants, funding); failed plays; buyer≠user test. Kill-list discipline applied; no verdict invented — candidates I could not attack properly are marked UNVERIFIED.

**Method & evidence window.** Web searches via z-ai `web_search`, staggered behind sibling agent R9 (120s) with 20–30s between queries. 15 query attempts (q01–q10 including 5 b-retries plus one 429-retry), producing 15 saved result files, ~10 with usable content; 1 attempt died on an upstream 429 rate-limit and was retried (shared quota with sibling), 3 returned garbage/noise (documented below), several returned 1–4 results only. Raw evidence: `research/raw-search-results/r10/*.json`. This is the first search ever completed against the SMB supply-chain backlog item (all prior attempts died on rate limits per R5 track report). Evidence prioritized 2024–2026; older material flagged.

---

## Headline findings

1. **Enterprise planning is confirmed priced out of SMB, with a hard number.** A buyer's-guide analysis of SAP IBP / o9 / Kinaxis (zuloma.com, Jan 19, 2026) puts software alone at **$380,000–$520,000/year** for a mid-market manufacturer with just 5,000–15,000 SKUs and 10–15 planners — before implementation. A true 20–500-employee SMB sits far below that tier. TrustRadius (2026) lists no public pricing for SAP IBP at all (quote-only — itself a signal of enterprise-only sales motion). This confirms the mission's hypothesis: Kinaxis/Blue Yonder/o9/SAP IBP are structurally absent from SMB.

2. **The SMB inventory/planning mid-tier is real, cheap, and crowded — the generic gap is closed.** SMB-accessible pricing exists everywhere below the enterprise tier: inventory software at ~$31–47/user/month (ZDNet, Apr 24, 2026), plans from $161/month ($436+/month for multi-location small business) (SoftwareConnect, Jul 15, 2026), $200–500/month per warehouse with implementation add-ons of 10–30% of annual plan (TheRetailExec, Jul 8, 2026). Katana, Orderhive, Zoho, Cin7, Linnworks and others saturate the listicle layer (Stackby Dec 2023; Linnworks Dec 7, 2025; saastoolboxus Aug 28, 2026). "SMB inventory app" is not an open gap.

3. **Excel is the acknowledged default planning layer for small companies — and the SMB planning vendors themselves concede it.** Deskera (undated): "When you're just starting your business, Excel can be your go-to inventory management system." BuyPlanr (undated, SMB demand-planning vendor): "Most Shopify merchants start forecasting in a spreadsheet — and Excel is genuinely good for it, up to a point." Databrush (Apr 29, 2026): with larger portfolios and more suppliers, Excel "becomes a risk." Adexin (Dec 9, 2024), citing McKinsey: "too many companies still rely on manual forecasting" and AI can reduce forecast errors (range truncated in snippet — exact figure not verified). This mirrors gap #11's construction pattern (85% estimating in Excel) almost exactly.

4. **2025 tariffs hit SMB importers hardest and made their manual planning worse — a live, dated demand driver.** QIMA 2025 Supply Chain Signals Report (Aug 14, 2025): global toy supply chains facing significant disruption from U.S. tariffs, "with small and medium businesses especially strongly affected." Armstrong (Apr 17, 2025): tariff uncertainty "can introduce significant volatility into demand forecasting and inventory management." McKinsey's 2025 Supply Chain Risk Survey (via esgthereport.com, Jan 30, 2026): 39% of respondents reported supplier and material cost increases from tariffs. BusinessJournalDaily (Mar 25, 2026): 2025 tariff disruptions triggered a "major supply chain reset" among U.S. importers.

5. **The two least-crowded pain pockets — the SUPPLIER side of SMB purchasing and tariff-era landed-cost re-planning — survived every search I could throw at them, but only barely: my kill-list attacks on them were weakened by thin/garbage search returns (429s, noise). They are candidates for re-verification, not validated gaps.** What did get killed: multichannel inventory (Cin7, Linnworks, Zoho, Webgility all sell exactly this — saastoolboxus Aug 28, 2026; Linnworks Dec 7, 2025; Webgility Sep 29, 2025) and generic SMB demand planning (Netstock/Slimstock/StockIQ/EazyStock tier plus new AI entrants like Datup — datup.ai, Sep 8, 2025, lists itself alongside Oracle/Blue Yonder/Kinaxis as "best software for supply chain planning").

---

## 1. Landscape: who serves SMB supply chain

- **Enterprise (absent from SMB):** SAP IBP, o9, Kinaxis, Blue Yonder — confirmed priced out (headline 1). Comparison content for these tools is entirely enterprise-framed (zglg.work, Jun 11, 2026: "Choose Blue Yonder when end-to-end supply chain execution and AI/ML at scale matter"). o9/OMP/SAP IBP buyer's guide (zuloma.com, Sep 4, 2026) discusses process-manufacturer finite-capacity scheduling — a large-enterprise concern.
- **SMB/mid-market planning tier:** Netstock, Slimstock, StockIQ, EazyStock are named in the mission brief; my searches surfaced the tier indirectly (vendor listicles and comparison sites) but **did not return Netstock/Slimstock-specific pricing pages** — their SMB pricing remains unverified in this run. Datup (datup.ai, Sep 8, 2025) positions AI supply-chain planning explicitly for the smaller tier ("7 Best Software for Supply Chain Planning: Datup, Oracle SCM Cloud, Blue Yonder, Kinaxis, Logility, e2Open, o9" — self-ranked first).
- **SMB inventory/ops tier (crowded):** Katana, Orderhive, Zoho Inventory, Cin7, Linnworks, Stackby, BoxHero, Lark, Deskera and more (q01: Stackby Dec 23, 2023; biz2credit Mar 6, 2026; hectorassetmanager Sep 4, 2025; technologyadvice Aug 12, 2026; softdecide Apr 22, 2026). Pricing has collapsed to $30–500/month bands (headline 2).
- **Fulfillment/3PL adjacency:** Stord raised an additional $120M ($325M total, $1.3B valuation) — engage.vc news page, undated (pre-2026 flag; capital goes to fulfillment infrastructure, not planning software).
- **Freight visibility:** Gnosis Freight sells "container lifecycle visibility and execution software for importers" (rfp.wiki comparison, 2026) — importer-focused, so the category exists; SMB affordability unverified.

## 2. What SMBs actually run: the Excel layer

Evidence that Excel is the default and persists well past its safe limit (all vendor-adjacent sources, dated where seen):

- BuyPlanr (undated): "Most Shopify merchants start forecasting in a spreadsheet — and Excel is genuinely good for it, up to a point."
- Deskera (undated): "When you're just starting your business, Excel can be your go-to inventory management system. It's cheap and easy to customize."
- BusinessSP (undated): claims small businesses are "ditching" Excel as cloud MRP became affordable — a vendor's hope, contradicted by every other source here and by gap #11's construction precedent.
- Databrush.cz (Apr 29, 2026): "Why Excel stops being enough for inventory management" — with larger portfolios, more suppliers, complex availability, "it becomes a risk."
- Varox (Jun 25, 2026): "Excel is useful at the beginning. It is flexible, familiar, and fast for early sales forecasts or inventory checks."
- Adexin (Dec 9, 2024), citing McKinsey: too many companies still rely on manual forecasting; AI-driven forecasting can reduce errors (figure truncated in snippet — not quoted here).
- Context from R4 (this repo): spreadsheets-as-database persists because "databases demand schema and permissions nobody wants to administer" (Diginomica 2023; ResearchGate: BI tools had little impact on spreadsheet use).

**Why open:** no shared "Excel share of SMB planning" statistic surfaced (searches q08/q08b returned noise) — the quantitative base for gap #11's "85% in Excel" equivalent does not exist yet for supply chain. Adjacency note: this is the same substrate as registry gap #12 (Excel absorption layer — schema + audit log around the live file) applied to a different vertical, and gap #11's pattern (tools priced above the small end; Excel fills the vacuum).

## 3. Pain pockets — what the evidence supports

- **Demand forecasting for SMB:** mid-tier exists (headline 2), generic gap closed. The open residue: forecasting *for importers under tariff volatility* (Armstrong Apr 2025 — uncertainty injects volatility into forecasting and inventory management) — no SMB tool surfaced for that specific problem.
- **Supplier communication / PO changes (email/phone):** my two dedicated searches (q05, q05b) failed — q05 returned ERP listicles and literal dictionary noise; q05b returned an unrelated "Anvil CRM" (queststack.io, Sep 15, 2026) and a Glassdoor employer page for Anvyl. Critically, **SourceDay did not surface at all** in an SMB context, and no SMB-priced supplier-portal/PO-change product appeared. Absence of evidence, not evidence of absence — UNVERIFIED, but nothing in the results contradicts the mission hypothesis that the supplier side is unserved at the SMB price point.
- **Inbound freight/container visibility for importers:** category exists (Gnosis Freight — importer-focused container lifecycle visibility; rfp.wiki 2026). Whether a 50-employee importer can afford/adopt it: unverified.
- **Multichannel inventory (wholesale + DTC + marketplaces):** KILLED — Cin7 Core explicitly "catering to brands that operate across both B2C ecommerce marketplaces and B2B wholesale" (saastoolboxus, Aug 28, 2026); Linnworks "Multichannel Inventory Management Software: 8 Top Picks" (Dec 7, 2025); Webgility keeps inventory updated "across Walmart, Amazon, Shopify" (Sep 29, 2025); Zoho Inventory for SMBs; plus 3PL alternatives (ShipCalm, Jul 20, 2026).
- **Port/customs chaos for small importers:** no direct search completed before the hard stop; tariff-pain evidence (QIMA Aug 2025; McKinsey 2025 survey via esgthereport Jan 2026) is the adjacent proxy. UNVERIFIED.

## 4. 2024–2026 landscape shifts

- **Tariffs → volatility (the big one):** QIMA (Aug 14, 2025) — SMBs "especially strongly affected"; McKinsey 2025 survey (via esgthereport, Jan 30, 2026) — 39% report supplier/material cost increases; BusinessJournalDaily (Mar 25, 2026) — "major supply chain reset" among U.S. importers; Grassi (Apr 4, 2025) — manufacturing/distribution disruptions and higher costs. Tariff volatility raises the value of re-planning speed exactly where SMBs are slowest (manual spreadsheets).
- **AI planning entrants at the low end:** Datup (Sep 8, 2025) self-positions as AI planning for the non-enterprise tier; impactive-ai.com (Jan 3, 2025) markets AI demand forecasting replacing Excel inventory management; BuyPlanr (undated) targets Shopify-merchant forecasting. AI entrants are attacking the Excel layer directly — which both validates the substrate and crowds the generic forecasting wedge.
- **Funding signal:** weak this run — funding searches (q06/q06b) returned only Stord's fulfillment raise ($325M total, $1.3B valuation, undated engage.vc) — capital flows to fulfillment infra, not SMB planning software, in what surfaced.

## 5. Tried & failed

- **Direct evidence: none gathered this run** — searches for failed SMB supply-chain plays were not reached before the hard stop (candidate query cut). Hypothesis from adjacent repo findings (R4): mid-tier planning vendors succeed by selling to owners/ops managers but suffer the "good enough Excel + switching cost" trap (Diginomica 2023: BI barely dented spreadsheet use). Mark UNVERIFIED.
- **Cin7's own SMB-marketing post** ("How SMBs can mitigate supply chain disruptions," Jan 28, 2025) shows incumbents already packaging "supply chain visibility" messaging at SMB — a caution that generic visibility claims will be crowded even if the underlying tooling is thin.

## 6. Buyer ≠ user test

- SMB pattern hypothesis: owner/ops manager buys inventory software; planners/purchasing staff (often 1–3 people) and shop staff live in it daily. **No direct evidence gathered this run** (no Reddit/forum search completed before hard stop) — UNVERIFIED. The one adjacent signal: TheRetailExec (Jul 8, 2026) warns SMB buyers that "cheap" plans accrue per-order micro-fees and implementation runs 10–30% of annual plan cost — buyer-side pain, not user-side, consistent with procurement friction rather than daily-use hatred.

## 7. Kill-list table

| # | Candidate gap | Attack mounted (evidence) | Verdict |
|---|---------------|---------------------------|---------|
| 1 | Generic SMB demand-planning / inventory app | Mid-tier exists and is crowded: ZDNet Apr 2026 ($31–47/user/mo), SoftwareConnect Jul 2026 ($161–436/mo), TheRetailExec Jul 2026, Datup Sep 2025, plus Netstock/Slimstock/StockIQ/EazyStock tier (pricing unverified) | **KILLED** (as a generic play) |
| 2 | Multichannel inventory across wholesale+DTC+marketplaces | Cin7 (Aug 28, 2026), Linnworks (Dec 7, 2025), Zoho, Webgility (Sep 29, 2025), 3PL alternatives (Jul 20, 2026) | **KILLED** |
| 3 | Enterprise-grade planning for SMB (build it cheaper) | Confirmed priced out ($380–520k/yr, zuloma Jan 2026) — but building a cheap clone fights the crowded mid-tier of #1, not the vacuum | **KILLED** (as clone; the vacuum is real but adjacent to #1) |
| 4 | Supplier-side PO-change/communication layer for SMB importers | Attacks failed on service quality (q05 noise; q05b wrong product; SourceDay never surfaced in SMB context) — no SMB-priced solver surfaced | **SURVIVED (provisional) — UNVERIFIED, requires re-verification** |
| 5 | Inbound container/freight visibility for small importers | Gnosis Freight exists (importer-focused container lifecycle, rfp.wiki 2026); SMB pricing/fit unknown | **UNVERIFIED** (category exists; SMB affordability unproven) |
| 6 | Tariff-era landed-cost + re-planning cockpit for SMB importers | No solver surfaced in tariff searches (q07b: QIMA, Armstrong, McKinsey, Wipro — all enterprise or advisory framing); no dedicated kill search completed | **UNVERIFIED** (no counter-evidence, no confirmation — verification incomplete) |

## 8. Registry recommendation rows

**Recommendation: add ONE provisional row (OPEN-NEW) and a watchlist note; do not promote #4–#6 candidates without a re-verification pass.** Search-service flakiness (429s, 1-result returns, garbage) means only candidates 1–3 were properly killed; survivors were insufficiently attacked. Per the rules, this is stated rather than papered over.

| Opportunity | Lens | Why open (evidence trace) | First ship | Distribution model |
|-------------|------|---------------------------|------------|--------------------|
| SMB supplier-communication layer (PO changes/confirmations over email, for 20–500-employee importers/distributors) | Unsexy / ownership vacuum | No SMB-priced solver surfaced in dedicated searches (q05/q05b — SourceDay absent from SMB context); tariff volatility raises PO-change frequency (QIMA Aug 2025; McKinsey-2025-via-esgthereport Jan 2026: 39% cost increases); Excel/email is the documented default (BuyPlanr, Deskera; Databrush Apr 2026) | Overlay on the SMB user's existing email/Excel: read PO threads, extract changes, sync the workbook/ERP — never ask supplier or buyer to adopt a portal | Bottom-up: free single-user PO-tracker → paid sync; trade-association and freight-forwarder channels (mirrors gap #11's association channel) |

**Adjacency notes:** This row is the supply-chain sibling of **gap #12 (Excel absorption layer)** — same "absorb the workbook, don't kill it" shape — and can share its first-ship architecture (schema + audit log around the live file, here fed by email/PO parsing, which AI newly cheapens per R4's translation-problem thesis). It also rhymes with **gap #11 (construction sub-tier estimating)**: same vertical pattern (tools priced for the top of the market, Excel at the bottom, association-channel distribution). If gap #12 ships, this is its second vertical — worth a shared build decision.

**Watchlist (not registry rows):** (a) tariff landed-cost/re-planning cockpit — dated demand driver is strong (QIMA Aug 2025; BusinessJournalDaily Mar 2026) but no completed kill search; (b) SMB-priced container visibility — Gnosis Freight may already close it at SMB prices; (c) Excel-share quantification for SMB planning — needed as the evidence base for any future row (the #11-style "85% in Excel" stat does not exist here yet).

## 9. Quota / deadline notes

- 15 query attempts, 15 saved result files, ~10 usable; 1 hard 429 failure retried (shared quota with concurrent sibling R9), 3 garbage/noise returns (q05, q07, q08), several 1–4-result returns. Hard stop enforced at ~minute 15–18 of the run; queries cut before the stop: SourceDay-specific kill search, Anvyl SMB pricing, failed-startup history, buyer≠user forum evidence, customs brokers software. These are the first searches for the recommended re-verification pass.
- Pre-2024 numbers flagged in place: Stackby list (Dec 2023), Stord raise (undated engage.vc page), BusinessSP/Deskera/BuyPlanr (undated vendor pages).
- Raw evidence immutable at `research/raw-search-results/r10/` (q01–q10 incl. retries; every file saved, none edited).

## Key sources

- zuloma.com (Jan 19, 2026; Sep 4, 2026) — enterprise planning pricing $380–520k/yr, o9/OMP/SAP IBP buyer's guide
- ZDNet (Apr 24, 2026); SoftwareConnect (Jul 15, 2026; 2025 SAP IBP review); TheRetailExec (Jul 8, 2026) — SMB pricing tiers
- TrustRadius (2026) — SAP IBP no public pricing
- QIMA (Aug 14, 2025) — 2025 Supply Chain Signals, SMBs especially affected by tariffs
- Armstrong / goarmstrong.com (Apr 17, 2025) — tariff volatility in demand forecasting
- McKinsey 2025 Supply Chain Risk Survey via esgthereport.com (Jan 30, 2026) — 39% cost increases
- BusinessJournalDaily (Mar 25, 2026) — tariff supply-chain reset survey
- Grassi (Apr 4, 2025); ResearchGate (Feb 14, 2025) — tariff disruption framing
- Adexin (Dec 9, 2024, citing McKinsey); Databrush.cz (Apr 29, 2026); Varox (Jun 25, 2026); Deskera, BuyPlanr, BusinessSP (undated) — the Excel layer
- datup.ai (Sep 8, 2025) — AI planning tier; impactive-ai.com (Jan 3, 2025)
- saastoolboxus.com (Aug 28, 2026); Linnworks (Dec 7, 2025); Webgility (Sep 29, 2025); ShipCalm (Jul 20, 2026); Stackby (Dec 23, 2023) — multichannel inventory crowding
- rfp.wiki (2026) — Gnosis Freight container lifecycle visibility
- Cin7 (Jan 28, 2025) — SMB supply-chain marketing
- engage.vc (undated) — Stord $325M/$1.3B
- G2 / queststack.io (Sep 15, 2026) / Glassdoor — q05b false-positive noise (Anvil ≠ Anvyl), documented as failed attack
