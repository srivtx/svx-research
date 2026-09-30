# R13b — Verification Pass: R8 (COBOL) + R9 (Elder Care) + R10 (SMB Supply Chain) Owed Kill-Searches

**Task:** R13b — run the kill-searches R8, R9, and R10 could not complete before their deadlines; convert provisional SURVIVED/UNVERIFIED candidates into firm verdicts. Run date 2026-09-30.

**Method:** z-ai `web_search` CLI (10-result pages), staggered 120s behind sibling R13a, `sleep 20` between queries, `timeout 90` per call; <3 results or junk → one rephrased retry after `sleep 30`. Raw JSON saved incrementally to `research/raw-search-results/r13b/` (14 files: q01–q10 incl. b-retries; every file kept, never edited). Report skeleton created before searching and filled incrementally. Priority order enforced per work order: R8 equivalence-harness kill-search → R9 platform-API openness → R10 SourceDay kill-search first; remaining leads queued behind.

**Evidence window:** search snapshot 2026-09-30; sources 2024–2026 except where flagged.

**Search count:** 14 web_search calls / 14 files saved / ~10 usable sets (q01–q10 incl. b-retries). Four queries needed rephrase-retries (q01→q01b parallel-run noise; q02→q02b thin; q03→q03b OSRS-Scribd junk; q08→q08b listicle noise — the q08b rephrase recovered fully). Search window ran ~15 minutes wall-clock including the mandated 120s stagger and 20–30s inter-query sleeps; hard stop on new searches enforced at minute 15. Work-order items that got NO query before the stop: family-communication solvers, caregiver documentation-time stat, Amazon Q Transform validation; the tariff landed-cost item got one query that returned a single junk result (Indian SaaS pricing listicle) with no retry budget left. All are marked STILL-UNVERIFIED with the quota failure stated, per rules.

---

## Verdict summary table

| Track | Candidate | Prior status | Fresh evidence (this run) | FINAL VERDICT |
|-------|-----------|--------------|---------------------------|---------------|
| R8 | Equivalence-validation harness (standalone parallel-run/differential product) | SURVIVED (thin; kill-queries had died) | AveriSource = analysis+transformation suite (averisource.com; prnewswire Jan 31 2024; rfp.wiki); TSRI still service-bundled (rfp.wiki, carried from R8); Mechanical Orchard's **Imogen** productizes behavior-capture + test-driven rewrite but as a delivered modernization platform (mechanical-orchard.com Jun 8 2026; Jul 8, 2026; carahsoft.com; thoughtworks.com Sep 7 2026) — not a licensable vendor-neutral harness | **CONFIRMED-OPEN (narrowed)** — nearest closer named: Mechanical Orchard Imogen (method owned, not sold as a tool); parallel-run product queries returned noise AGAIN |
| R8 | Mechanical Orchard product surface | Missing evidence (R8 §Deadline notes #4) | Imogen platform: "uses those tests, code, and a combination of LLMs to automatically implement a modern program that matches the behavior" (mechanical-orchard.com, Jul 8 2026); "captures real-time system behavior" (carahsoft.com); JCL batch→Python/AWS + 3 Db2 migrations (thoughtworks.com, Sep 7 2026) | **RESOLVED — evidence now in** (product exists; public-sector reach via Carahsoft reseller) |
| R8 | VSAM/DB2 data-migration reconciliation tooling | UNVERIFIED | One relevant hit: in-com.com "The Data-First Approach to Mainframe Modernization" (Apr 20 2026): "Data validation and reconciliation are essential for ensuring that migrated data accurately reflects the state of the source system" — content marketing from the SMART TS XL vendor; no named reconciliation product | **STILL-UNVERIFIED** (quota blocked — dedicated tooling queries not reached; single-source signal only) |
| R9 | Platform API openness (overlay feasibility gate) | UNVERIFIED (feasibility never examined) | AlayaCare "offers Restful APIs" (crozdesk.com); AlayaCare plans "from $1000/mo" (saaskart.co, third-party); AxisCare public API docs with admin-issued token flow (crm.coach); "AlayaCare, AxisCare, and WellSky Personal Care… maintain extensive public API documentation" (homecaregroup.com); Axxess: only CEHRT-mandated patient-access endpoints, "no signup, sandbox, or keys" (supergood.ai); HHAeXchange $325/mo pricing (Capterra, Sep 16 2026) but no API docs surfaced | **CONFIRMED-OPEN (feasibility gate PASSES on AlayaCare + AxisCare)** — Axxess closed; HHAeXchange/WellSky API depth unverified |
| R9 | Family-communication layer solver | UNVERIFIED | No dedicated query (quota); adjacent hit: a platform shipping "the Care Circle portal for friends & family" as bundled feature (sourceforge.net listing, undated) | **STILL-UNVERIFIED** (quota blocked; new signal leans toward bundled-portals-exist, weakening the standalone-layer hypothesis) |
| R9 | Caregiver unpaid documentation-time quantification | UNVERIFIED | No query reached | **STILL-UNVERIFIED** (quota blocked; no stat asserted) |
| R10 | Supplier-communication layer (SourceDay/Anvyl/PO-change solvers) | SURVIVED (provisional; "SourceDay never surfaced") | **SourceDay is alive and is exactly this product**: "supply chain performance software that bridges the gap between the ERP and the supplier network, making it easy to manage changes" (sourceday.com); "They're very, very focused on supplier communications. SourceDay is filling that gap between our customers and their suppliers" (sourceday.com customer quote); active support docs (support.sourceday.com, Nov 25 2025); marketed inside Medius's P2P suite: "SourceDay automates and de-risks the PO Lifecycle (where up to 70% of supply chain issues occur). Together with Medius, you'll have a powerful P2P solution" (medius.com). Plus **Anvyl absorbed by Sage** — "Sage Supply Chain Intelligence (formerly Anvyl)… connects your teams, systems, and suppliers" (sourceforge.net); "Anvyl is not trying to do everything under the sun like some of the big SRM platforms. It is far more focused, mostly on supply chain visibility" (zapro.ai, Jun 11 2026); "Supplier collaboration and production visibility portals give sourcing teams a shared workspace with their supplier base" (benroberts.ai) | **KILLED as drafted** (closers named: **SourceDay → Medius P2P**; **Anvyl → Sage Supply Chain Intelligence**) — the row's "no solver surfaced" premise is false on two independent legs; only the SMB-priced sub-$X slice remains open, unproven |
| R10 | Tariff landed-cost cockpit for SMB importers (Flexport/Freightos/Zonos class) | UNVERIFIED (watchlist) | No query reached | **STILL-UNVERIFIED** (quota blocked) |

---

## 1. R8 — Equivalence-validation harness (CRITICAL kill-search)

**Original claim (R8 §4, kill-list #1):** "nobody in this evidence base sells a standalone, vendor-neutral equivalence/parallel-run validation harness" — but the two dedicated kill-queries (q08/q08b) had returned pure noise, making this the least kill-tested survivor. R8's own follow-up list put "parallel run mainframe migration comparison testing tool" first.

**Fresh evidence.** The parallel-run product phrasing failed AGAIN exactly as it did for R8: q01 ("parallel run comparison tool mainframe migration equivalence testing") returned 3 junk results (android.googlesource.com, lists.apache.org, lists.jboss.org — the same JBoss-dictionary noise class R8 documented); the q01b rephrase returned 2 more of the same. This phrasing is now confirmed structurally unanswerable against this search service — noise on both runs, both years of attempts.

The named-vendor phrasings did land:

- **AveriSource** (q02/q02b): "AveriSource Platform is a legacy modernization product suite that combines application inventory, architecture discovery, execution-path analysis, and AI-[powered code transformation]" (rfp.wiki); own site: "AI-powered analysis, business rules extraction and code transformation capabilities" (averisource.com); PR: "AveriSource accelerates legacy modernization through application analysis, business rules extraction and AI-powered code transformation" (prnewswire.com, Jan 31, 2024). **Read: an analysis + transformation suite. Equivalence testing is not the product; it is at most a stage inside their transformation engagement** (consistent with R8's rfp.wiki quote on TSRI functional-equivalence testing being bundled in services). No standalone differential-comparison product surfaced.
- **Mechanical Orchard** (q03b/q04): see §2 — their **Imogen** platform productizes exactly the behavior-capture → test → behavior-matching method R8's proposed row describes, but as a delivered modernization, not a harness for sale.

**FINAL VERDICT: CONFIRMED-OPEN, narrowed.** No standalone, vendor-neutral, buyable parallel-run/differential-validation harness for third-party-run migrations surfaced. But the field is no longer empty in the way R8's report implied: the *method* is owned and productized by Mechanical Orchard (Imogen) inside an end-to-end modernization offering. The surviving open slice is precise: **the harness sold to the people who run their own migrations (mid-market SIs on fixed-price risk) rather than sold as a delivered rewrite.** If Imogen is ever licensable standalone, or if Medius-class P2P vendors absorb it, the slice closes.

**Registry action:** promote R8's rank-1 row OPEN-NEW with the "why open" rewritten to name the nearer closer: *"Equivalence-validation exists only inside delivered-modernization platforms (Mechanical Orchard Imogen — behavior-capture + test-driven rewrite, sold via Carahsoft for public sector) and transformation-service bundles (AveriSource, TSRI, Virtusa); no vendor-neutral harness sold to SIs running their own migrations."*

## 2. R8 — Mechanical Orchard's actual product

R8 flagged "Mechanical Orchard's actual product" as missing evidence entirely; the work order asked whether the vendor that called modernization "a verification problem" built the harness.

**Fresh evidence (q03/q03b/q04):**
- "The Imogen platform then uses those tests, code, and a combination of LLMs to automatically implement a modern program that matches the behavior [of the legacy system]" (mechanical-orchard.com, Jul 8, 2026).
- "At the core of this methodology is Imogen, our AI-powered platform purpose-built for mainframe modernization. Imogen captures real-time system behavior and…" (carahsoft.com — public-sector reseller page; "our" indicates a Mechanical Orchard-authored or co-authored partner listing, i.e., Imogen is being taken to government through the Carahsoft channel).
- Case study: "They moved four key batch jobs from mainframe JCL to Python running on AWS Batch, and migrated three Db2…" (thoughtworks.com, Sep 7, 2026 — a ThoughtWorks-published account referencing the Imogen platform).
- Additional footprint: startupintros.com (Jul 13, 2026) — "The Imogen platform generates maintainable software, significantly reducing migration risk"; mechanicalorchard.substack.com — case study of "a leading global manufacturing company" rewriting its extended warranty platform with Imogen; cdn.prod.website-files.com case study (Mar 31, 2025); builtin.com profile (Apr 4, 2026) — "behavior-first, incremental modernization of mainframe and other legacy [systems]"; gilzor.com company profile.

**Read:** Mechanical Orchard did build the verification-shaped thing — Imogen generates tests from captured behavior and proves the rewrite matches — but sells modernization outcomes (with case studies and a public-sector reseller), not the verification tool itself. R8's "sell to the SI" channel hypothesis is unaffected: Mechanical Orchard competes FOR migration engagements; it does not equip other migrators.

**FINAL VERDICT: RESOLVED** (missing-evidence item now evidenced). Implication for R8's row: method-validated, product-shape-validated, but the tool-for-SI slice remains unsold. This strengthens the row's realism while narrowing its claim.

## 3. R8 — VSAM/DB2 data-migration reconciliation tooling

**Fresh evidence (q05):** one relevant result — "The Data-First Approach to Mainframe Modernization" (in-com.com, Apr 20, 2026): "Data validation and reconciliation are essential for ensuring that migrated data accurately reflects the state of the source system." In-com is the vendor behind SMART TS XL (R8's kill-list #3 occupant). This is content marketing asserting the necessity of data validation, not a named reconciliation product. The query returned nothing else (1 result).

**FINAL VERDICT: STILL-UNVERIFIED (quota blocked).** The failure statistic (80% of core-banking migrations fail on data, openlegacy.com — vendor-claimed, carried from R8) remains strong, but no standalone reconciliation tool surfaced and the search budget ran out before a second phrasing. Do not promote. Next-pass query: "data migration reconciliation software Db2 VSAM compare source target tooling."

## 4. R9 — Platform API openness (CRITICAL feasibility gate)

R9's back-office overlay row is gated on whether the incumbent home-care platforms expose APIs an overlay could read/write. R9 ran zero API queries.

**Fresh evidence (q06/q07):**
- **AlayaCare:** "Does this service offer an API? Yes, AlayaCare offers Restful APIs" (crozdesk.com Q&A listing). Pricing signal: "AlayaCare is an end-to-end home care platform with care plans, scheduling, EVV, and billing plus a caregiver app. Plans from $1000/mo" (saaskart.co — third-party, vendor-unverified figure).
- **AxisCare:** "Public docs show a site-specific token flow, not an end-user OAuth flow. An admin signs into AxisCare, goes to Admin > API Token > Create New Token…" (crm.coach — an integration writeup documenting AxisCare's public API auth).
- **WellSky Personal Care:** "Platforms such as AlayaCare, AxisCare, and WellSky Personal Care, which maintain extensive public API documentation and adherence to modern interoper[ability standards]" (homecaregroup.com — agency-side source; single-source claim for WellSky).
- **Axxess:** "The only public API is the CEHRT-mandated patient-access endpoint set (C-CDA/CCDS) at engage.axxess.com, with no signup, sandbox, or keys" (supergood.ai) — Axxess is CLOSED to third-party overlays beyond the mandated patient-access endpoints.
- **HHAeXchange:** pricing surfaced — Capterra comparison page (Sep 16, 2026) lists HHAeXchange at "$325/month" (adjacent "$375/month" field is comparison-table ambiguity — two rows, exact tier mapping unclear); rating 3.64/100 reviews on that page. No API documentation surfaced for HHAeXchange; tadabase.io (Feb 9, 2026) lists HHAeXchange and WellSky Home Health in a no-code-integration context, implying integration paths exist but proving nothing about openness.

**FINAL VERDICT: CONFIRMED-OPEN — the feasibility gate passes.** AlayaCare (REST APIs) and AxisCare (public docs, admin-issued API tokens) are confirmed API-accessible; WellSky PC has one "extensive public API documentation" claim (single source — verify depth before building); Axxess is out (mandated endpoints only); HHAeXchange unproven. R9's overlay row should name AlayaCare and AxisCare as first-ship targets. Caveats: cost/limits of API access unverified; saaskart's $1000/mo AlayaCare figure is third-party.

## 5. R9 — Family-communication layer

No dedicated query reached the budget (R9's q09/q09b had returned garbage; my queue was consumed by the CRITICAL items). One adjacent signal landed in q07: a sourceforge.net platform listing describing "the Care Circle portal for friends & family" as a bundled feature alongside rostering, scheduling, ECM care monitoring, eMAR, payroll, invoicing (platform unnamed in the snippet; the feature set suggests a UK/EU-style rostering platform).

**FINAL VERDICT: STILL-UNVERIFIED (quota blocked).** The one new signal (a bundled friends-and-family portal existing on at least one platform) leans against the standalone-layer hypothesis but proves nothing about US home-care agencies. Do not promote. Next-pass query: "family portal home care agency software AlayaCare WellSky features."

## 6. R9 — Caregiver documentation-time quantification

No query reached. The stat R9 refused to invent remains unquantified. **FINAL VERDICT: STILL-UNVERIFIED (quota blocked; no stat asserted).** Next-pass query: "home care caregiver documentation time per visit study minutes."

## 7. R10 — Supplier-communication layer (CRITICAL kill-search)

**Original claim (R10 kill-list #4, proposed OPEN-NEW row):** "No SMB-priced solver surfaced in dedicated searches (q05/q05b — SourceDay absent from SMB context)" — the row's premise was the absence of a supplier-communication/PO-change product.

**Fresh evidence (q08/q08b):** the premise is now FALSE. SourceDay did not surface in R10's searches because those queries degraded — not because the product doesn't exist:

- "SourceDay is a supply chain performance software that bridges the gap between the ERP and the supplier network, making it easy to manage changes throughout the [PO lifecycle]" (sourceday.com homepage).
- Customer/partner voice on SourceDay's own site: "They're very, very focused on supplier communications. SourceDay is filling that gap between our customers and their suppliers… we can meet the supplier where [they are]" (sourceday.com).
- Product is alive and maintained: support.sourceday.com published a custom-workflow guide for supplier changes on Nov 25, 2025.
- Category consolidation: "SourceDay automates and de-risks the PO Lifecycle (where up to 70% of supply chain issues occur). Together with Medius, you'll have a powerful P2P solution" (medius.com) — SourceDay is now marketed as part of Medius's procure-to-pay suite. (Whether acquisition or deep partnership is not directly stated in the snippet; medius.com marketing it as "together with" indicates at minimum channel-level ownership by Medius. Vendor-claimed stat: the 70% figure is SourceDay/Medius marketing.)
- Ecosystem presence: SourceDay listed as an integration option in procure-to-pay software listings alongside Avalara and Sovos (sourceforge.net; slashdot.org).
- "Sourceday is a procurement management software that streamlines the purchasing process by automating purchase order (PO) tracking, supplier collaboration…" (howdy.com).

**FINAL VERDICT: KILLED as drafted — closers named: SourceDay (supplier-communication/PO-change software, now within Medius P2P) and Anvyl (supplier-collaboration/visibility platform, acquired and renamed Sage Supply Chain Intelligence).** The category R10 proposed as empty is occupied by TWO focused vendors, one of whose customer language ("filling that gap between our customers and their suppliers") is the exact gap text of R10's row — and both have now consolidated into larger P2P/ERP suites (Medius; Sage), the classic absorption pattern. Anvyl evidence (q09): "Sage Supply Chain Intelligence (formerly Anvyl) is a collaborative supply chain management platform that connects your teams, systems, and suppliers in one [place]" (sourceforge.net); "Anvyl is not trying to do everything under the sun like some of the big SRM platforms. It is far more focused, mostly on supply chain visibility" (zapro.ai, Jun 11, 2026); "Supplier collaboration and production visibility portals give sourcing teams a shared workspace with their supplier base for tracking production milestones" (benroberts.ai); SCRM positioning (spotsaas.com, May 18, 2026); "Anvyl connects global supply chain teams, systems and suppliers to improve collaboration and decision-making from PO issuance thro[ugh]" (flieber.com); $9.3M raise (pymnts.com, Jul 10, 2019 — pre-2024); vendor marketing from Anvyl's own CEO (inc.com, Jun 5, 2020 — pre-2024). No pricing surfaced for either closer (TrustRadius's Anvyl page is quote-gated). The only surviving slice is the one R10's row hedged on: **SMB (20–500-employee) price-point fit** — a pricing question, not an absence-of-solver question.

**Registry action: do NOT add R10's drafted row.** Either record the category CLOSED (closer: SourceDay/Medius) or replace with a narrowed watchlist item: "SMB-priced subset of the SourceDay/Medius PO-collaboration space — pricing evidence required before any build decision."

## 8. R10 — Tariff landed-cost calculators for SMB importers

One query ran before the hard stop and returned a single unusable result (an India-focused SaaS pricing listicle with no tariff/landed-cost relevance, appadvisor.in) — no retry budget remained. R10's watchlist framing stands unchanged: strong dated demand driver (QIMA Aug 2025; McKinsey-2025 via esgthereport Jan 2026), no completed kill-search against the Flexport/Freightos/Zonos class.

**FINAL VERDICT: STILL-UNVERIFIED (quota blocked — query returned junk, retry not reached).** Next-pass query: "landed cost calculator tariffs importer software Freightos Flexport Zonos pricing."

---

## Quota / deadline notes

- 14 web_search calls / 14 raw files / ~10 usable sets; 4 rephrase-retries; search window ~15 min wall-clock including the mandated 120s stagger and 20–30s inter-query sleeps; hard stop on new searches enforced at minute 15 with the family-communication, documentation-time, and Amazon-Q queries unspent and the tariff query un-retried. Items not reached are reported as STILL-UNVERIFIED rather than guessed.
- Recurring upstream degradation confirmed: "parallel run" phrasing → JBoss/Apache dictionary noise on both R8's and this run's attempts (4 queries total across both runs, all noise); OSRS-Scribd garbage reappeared once (q03); listicle noise on the first SourceDay phrasing (q08) — the rephrase (q08b) recovered fully.
- Third-party/vendor-claimed figures flagged in place: saaskart's "$1000/mo" AlayaCare plans; SourceDay/Medius "70% of supply chain issues" marketing stat; Capterra's $325–375/mo HHAeXchange table row; thoughtworks.com Imogen case-study account (co-marketing risk); homecaregroup.com's "extensive public API documentation" (single source for WellSky PC).
- No pre-2024 sources relied on for any verdict; prnewswire's Jan 31, 2024 AveriSource release is the oldest load-bearing citation (dated 2024).

## Recommended registry actions (for maintainer; gap-registry.md NOT edited by R13b per rules)

1. **PROMOTE (amended) — R8 rank-1 row, OPEN-NEW:** "Legacy differential-validation harness for SI-run mainframe migrations (behavior capture → replay → deterministic compare; JCL batch first)" | Lens: modernization verification | Why open: validation exists only inside delivered-modernization platforms (Mechanical Orchard Imogen, behavior-capture + test-driven rewrite, public sector via Carahsoft, Jul–Sep 2026 evidence) and transformation-service bundles (AveriSource analysis/rules/transformation suite, Jan 2024 PR; TSRI equivalence testing bundled in service; Virtusa); no vendor-neutral harness sold to SIs carrying fixed-price migration risk | First ship: COBOL batch capture-replay pack, "legacy system as test oracle," OSS core | Distribution: mid-market modernization SIs (Karsun-class); no FedRAMP needed (SI holds the contract).
2. **PROMOTE (amended) — R9 back-office overlay row, OPEN-NEW:** append feasibility evidence to the "why open": AlayaCare (REST APIs, crozdesk) and AxisCare (public API docs, admin-issued tokens, crm.coach) confirmed API-accessible; WellSky PC claimed "extensive public API documentation" (homecaregroup.com, single source); Axxess CLOSED (CEHRT patient-access endpoints only, supergood.ai). First-ship target: AlayaCare or AxisCare.
3. **DO NOT PROMOTE — R10 supplier-communication row as drafted.** Record: "SMB supplier-communication layer — KILLED as an unoccupied category (closers: SourceDay — supplier-communication/PO-change software, now marketed within Medius P2P (sourceday.com; support.sourceday.com Nov 25 2025; medius.com); Anvyl — acquired and renamed Sage Supply Chain Intelligence (sourceforge.net; zapro.ai Jun 11 2026)). Residual open question: SMB-priced subset — pricing evidence required."
4. **Record STILL-UNVERIFIED (quota-blocked, this pass):** VSAM/DB2 data-migration reconciliation; family-communication layer (lean-closed: bundled 'Care Circle' portals exist on ≥1 platform); caregiver documentation-time stat; tariff landed-cost cockpit for SMB importers (one junk query, unretried); Amazon Q Transform COBOL validation. Each has a ready next-pass query listed in its section.

**Bottom line:** 2 CONFIRMED-OPEN (R8 harness — narrowed, closer-adjacent; R9 overlay — feasibility gate passed), 1 KILLED (R10 supplier-communication as drafted — closers: SourceDay/Medius + Anvyl/Sage), 1 RESOLVED (Mechanical Orchard product = Imogen), 4 STILL-UNVERIFIED on quota. The SVX kill-list discipline did its job three times in both directions this pass: it kept R8's survivor alive with sharper boundaries, it passed R9's feasibility gate with named platforms, and it stopped R10's row from entering the registry on a false premise.
