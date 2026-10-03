# V5 — Verification Pass: Field-Service + SMB Vertical Stragglers (2026-10-03)

**Task:** V5. Clear the field-service and SMB stragglers from the registry's still-unverified list — the items R13a/R13b could not reach due to quota and search-service degradation. Nine targets in priority order: per-job margin overlay, Ply pricing/traction, Numa/Avoca/Sameday AI answering, Carrier/Trane OEM warranty claims, commissions/spiff tracking, Workiz/ServiceTitan small-shop tier, Paperless Parts pricing, Katana/MRPeasy/Fishbowl sentiment, tariff landed-cost cockpit.

**Method:** 15 web-search executions via z-ai `web_search`, 15 raw JSON files saved immutable to `research/raw-search-results/v5/` (q01.json–q15.json; every query logged below). Staggered 240s behind sibling V4; 20–30s sleeps between queries; hard stop on new searches honored (~minute 13 of the window). **Notable: a clean run** — zero 429s, zero hard failures, and the recurring OSRS/Scribd "zoberetimifid" artifact that poisoned R13a/V3's windows did not appear once; no rephrase retries were needed. Every claim traces to a named qNN.json file; host+date for every claim; single-source and undated items flagged; unsearched = UNVERIFIED, never invented.

**Evidence window:** searches run 2026-10-03, 22:56–~23:09 UTC; cited sources span 2022–Sep 2026, load-bearing evidence 2025–2026 (older flagged).

---

## T1 — Per-job margin overlay on shelfware ERP + Excel (R6's last weak survivor; V3's query went unspent)

**Question (registry):** does a solver exist for per-job/per-job-order margin visibility over shelfware ERP + Excel scheduling in small job shops, or is the evidence too weak to row at all?

**Queries:** q01 `job shop per job profit margin tracking software`; q02 `manufacturing margin visibility small shop Excel ERP`.

**Evidence (q01):**
- **mie-solutions.com (undated):** MIE Trak Pro "helps manufacturers, job shops, and fabricators connect quoting, scheduling, inventory, purchasing, production, quality, reporting, and accounting" — full job-shop ERP with costing inside.
- **jobpack.com (Jul 17, 2026):** "Production Reporting System for Shop Floor Intelligence… Live facts help custom job shops protect their profit margins. Integrate ERP for Full Reporting. Isolated data limits your ability to scale" — shop-floor reporting/data-capture layer for job shops, explicitly marketing margin protection and ERP integration. The nearest adjacent product found.
- **lynexus.com (undated):** JobBOSS² ERP setup content — "real-time costing" via proper configuration of the incumbent shelfware.
- **geniuserp.com (May 29, 2026):** "An ERP tracks all of the costs associated with a manufactured item including material, labor, equipment, outsourced operations" — ERP-vendor content marketing owning the margin-visibility question.
- **myquoteiq.com (undated, competitor SEO):** QuoteIQ markets "CRM with job costing for contractors who want to see their actual margin per job — not just their total revenue" — the per-job-margin job-costing pitch exists at the cheap-contractor tier.
- **getapp.com (undated):** "Job Cost Pro… Snap or speak a receipt; it files the cost to the right job and shows the real margin" — receipt-to-job-cost mobile apps for small contractors.
- **emergent.sh (Jul 24, 2026):** a general contractor "built a job cost tracking app on Emergent [no-code AI builder] to track materials and labour in real time and know their margin before the job ends" — DIY workaround demand signal.
- **scoopanalytics.com (undated):** margin-calculator listicle conceding "calculators miss the real question: which product, which location, and why margins drop."
- **proshoperp.com (Feb 23, 2022 — old):** CNC-shop profit checklist content.

**Evidence (q02):** ERP-replacement content marketing only. **cdhcpa.com (Dec 9, 2025):** "Stuck between Excel and a costly ERP? CDH helps small manufacturers adopt cloud inventory tools" — the Excel-to-ERP gap is acknowledged vendor terrain (consultancy, not margin overlay). **arribatec.com (Jun 18, 2025):** "Without a comprehensive overview, it's harder to monitor margins, value creation, and alignment between purchase orders, goods receipt…" — pain framing from an ERP vendor. Plus axolt.com, 2isolutions.com (Feb 18, 2026), erpsoftwareblog.com (Sep 9, 2025), paystand.com (Jun 10, 2025), gloriumtech.com (Jun 23, 2026) — generic manufacturing-ERP visibility content.

**Verdict: STILL-UNVERIFIED** — leaning open on the supply side, too weak to row on the demand side. **No dedicated per-job margin overlay on shelfware ERP + Excel surfaced** in two fresh phrasings (making 31 total searches across R6's 29 + these 2 with no direct hit). But the adjacent space is crowded on three sides: (a) shop-floor production reporting that integrates ERP and markets margin protection (**JobPack**, jobpack.com Jul 17 2026 — the closest neighbor, though it is a data-capture system, not a read-only overlay over ERP+Excel); (b) incumbent-ERP content claiming the margin-visibility answer (Genius ERP, JobBOSS², MIE Trak); (c) cheap contractor-tier job-costing apps (QuoteIQ, Job Cost Pro) and DIY no-code builds (Emergent, Jul 24 2026). Crucially, **no user-voice pain evidence surfaced** — every demand signal is vendor SEO or an anecdote of someone building their own tool. Answer to the mission's question: no solver exists in evidence, but the evidence base remains too weak to row.

**Registry action:** no promotion (unchanged). Keep on the follow-up list with a sharpened next-pass note: query user forums (e.g., practicalmachinist "track profit per job") rather than product SEO — the phrasings used are now saturated with vendor content. Do not count JobPack as a closer (different shape), but name it the closest neighbor to beat.

---

## T2 — Ply pricing/traction (killed the truck-stock row as drafted; SMB-priced residual unresolved; 2 prior search passes blocked)

**Question (registry):** Ply is quote-priced; is there any pricing/traction signal, or does this go search-retired (3rd failure) and move to direct vendor-page reads?

**Queries:** q03 `Ply inventory trades pricing per month`; q04 `Ply app field service inventory cost`. Third pass after R13a (q10/q10b junk) and V3 (dead) — **this pass succeeded; not retired.**

**Evidence (q03):**
- **thesaasnews.com (Dec 4, 2025):** "Ply, a New York-based inventory and purchasing platform built for the trades, has raised $8.5 million in a strategic funding round." — **traction confirmed: $8.5M strategic round.**
- **mypowerhouse.group (undated):** "PCG Announces Ply as a CRP Partner — Ply is a game-changer in inventory management, helping contractors track materials in real-time, prevent costly delays, and automate reordering" — channel partnership with Powerhouse Consulting Group (contractor-groups channel).
- **sourceforge.net (undated, "Ply Reviews in 2026"):** live reviews page — "Read Ply reviews from real users, and view pricing and features of the Inventory Management software" (review presence = real user base; the adjacent "free e2-micro VM / no per-seat fees" text is SourceForge boilerplate, not Ply pricing).
- **webcatalog.io (undated):** "Ply Inventory — Desktop & Mobile App" — shipped product surface.

**Evidence (q04):**
- **help.housecallpro.com (Jan 20, 2026):** "Ply Inventory Management Integration Overview — Easily audit and manage inventory with one-click scanning, barcoding and seamless integration for importing price book and material list data" — **Ply is documented inside Housecall Pro's own help center as an integration: native distribution into HCP's install base.**
- **getply.com (Sep 14, 2026):** Ply's own site publishes "Free Inventory Management Software for Small Business — Compare the best free inventory management software for small businesses. Discover which free tools actually work, what they cost later" — **the vendor itself markets an SMB/free positioning.**
- **fieldservicesoftware.io (Jul 22, 2026):** FSM pricing context — "Field Service lists $105/user/month and $50/user/month for Contractor, paid annually; Salesforce lists $175/user/month for Dispatcher" (tier pricing, not Ply's).

**Verdict: CLOSED** — the SMB-priced residual is dead, not merely unpriced. Ply is a funded ($8.5M, Dec 2025), channel-partnered (PCG), HCP-natively-integrated (Jan 20 2026) incumbent whose own marketing targets small business with a free-software angle (getply.com Sep 14 2026). Exact list price remains unpublished across 4 attempts in 3 passes — but the question the registry actually cared about ("is the wedge unoccupied below Ply's price?") is answered: the occupier is marketing straight at the SMB end with free-tier positioning and has distribution advantages a newcomer cannot undercut with price alone.

**Registry action:** close the truck-stock residual permanently: "SMB-priced truck-stock reconciliation residual — CLOSED 2026-10-03: Ply traction confirmed ($8.5M strategic round, thesaasnews.com Dec 4 2025; Housecall Pro native integration, help.housecallpro.com Jan 20 2026; PCG channel partnership; SMB/free self-positioning, getply.com Sep 14 2026)." Ply's exact list price can stay a watchlist footnote only if a future product fights it head-on.

---

## T3 — Numa / Avoca / Sameday AI answering status (field-service AI receptionists)

**Question (registry):** do the named AI-answering players for trades exist/traction/price — i.e., is missed-call capture owned?

**Queries:** q05 `Numa AI phone answering trades 2026`; q06 `Avoca AI answering service contractors`; q07 `Sameday AI home service`.

**Evidence (q05 — Numa):** every usable result places Numa in **automotive dealerships, not trades**: numa.com (May 29, 2026) — "A multi-rooftop dealer group using Numa captured $1.5 million in incremental Fixed Ops and parts revenue in 2025"; skywork.ai (Oct 7, 2025) — "Numa AI transforms automotive dealerships with 24/7 customer service, missed call rescue, and seamless DMS integration"; appscribed.com (2026 review) — "Numa is the best AI receptionist for car dealerships"; reachall.ai (Feb 24, 2026) — listed in "Top 7 Voice AI Platforms for Car Dealerships in 2026"; cbtnews.com (Dec 11, 2024) — Numa's own 2024 insights report ($1.17M lost revenue framing). Alive, funded-seeming, **but verticalized to auto retail**.

**Evidence (q06 — Avoca):** avoca.ai (undated) — "Avoca integrates directly with Foundations so every call is answered, every job is booked, and every lead is followed up — automatically"; help.avoca.ai (undated) — live product docs ("Configure Responder… answers, books, transfers, and classifies calls"). Positioning: titanpipelines.com (undated, competitor, single-source) — "Avoca is enterprise home-services AI (gated pricing, call-center fit)." **Context (callacy.com, Aug 13, 2026):** "8 Best AI Answering Services for Contractors (2026) — Rosie, Smith.ai, and Goodcall are solid picks if all you want is the phone covered. Avoca, Housecall Pro, Jobber, and Podium fit larger shops" — a crowded 2026 comparison field. Plus whippy.ai (AI + live-agent contractor answering) and titanpipelines.com (done-for-you AI for owner-operators) as further entrants.

**Evidence (q07 — Sameday):** ycombinator.com (undated) — "Sameday: The leading AI workforce for the trades — outperforming humans at high-stakes, revenue-critical work, such as sales, dispatch, and more" (YC-backed); gosameday.com (undated, live product site) — "answering every call instantly, qualifying leads in real time, and booking jobs automatically, 24 hours a day"; voiceaispace.com (undated) — "an AI-powered phone answering system designed specifically for home service businesses such as plumbing, heating, cooling."

**Verdict: CLOSED** — the missed-call/AI-receptionist market for trades is served and crowded. All three named players verified live in 2025–2026 evidence: Numa (alive but automotive-vertical — not a trades closer), Avoca (enterprise home-services AI with live docs, integrations, gated pricing), Sameday (YC-backed, trades-native, sales+dispatch scope). Around them: Rosie, Smith.ai, Goodcall, Podium, Whippy, Titan Pipelines, and platform-embedded options from Housecall Pro and Jobber (callacy.com, Aug 13 2026). There is no ownership vacuum at any tier — the phone-answered end has $-commoditized options and the larger-shop end has Avoca/Sameday.

**Registry action:** mark the Numa/Avoca/Sameday straggler resolved-CLOSED with these traces; no registry row was ever proposed here and none should be.

---

## T4 — Carrier/Trane OEM warranty-claim workflows (contractor pain hypothesis)

**Question (registry):** is contractor-side OEM warranty-claim processing (dealer portals, labor reimbursement) digitized/owned?

**Query:** q08 `HVAC warranty claim processing software Carrier Trane`.

**Evidence (q08 — thin but usable, 5 results):**
- **aem-dev.mtechapis.com (undated, Trane login mirror):** "Complete Warranty requirements online. This is the login for Trane® Connect™ and other Trane® commercial applications" — **the OEM dealer portal (Trane Connect) exists and hosts warranty workflows.**
- **warranty.tranetechnologies.com (undated):** OEM warranty-registration pages including "Request for Extension… if the warranty registration for the inventory is initiated before…" — registration/extension workflows are online at the OEM.
- **talents.vaia.com (undated, job listing):** Trane Technologies is hiring a **Claims Specialist** — "Administer, review, and process claims as assigned… Review, analyze and process claims per policies" — claims adjudication at the OEM is human-administered.
- **claimspages.com (undated):** a local Trane contractor listed in an insurance-claims directory (noise-adjacent).
- start.connect.tis.trane.com — Trane Connect app login (portal confirmation).

**Verdict: STILL-UNVERIFIED** (third pass on this question family; partial progress, lean toward "portals exist, pain unmeasured"). New facts: Trane's OEM-side digitization is real (Trane Connect portal + warranty.tranetechnologies.com registration/extension pages), and the OEM processes claims with humans per policy. What remains unevidenced: the contractor-side experience (is filing labor-reimbursement claims a black hole of re-keying and denials?), any third-party warranty-claim software for contractors (none surfaced in 3 passes), and anything Carrier-specific (zero Carrier evidence). No contractor-pain user voice has ever surfaced — the hypothesis remains plausible but unmeasured.

**Registry action:** keep on the follow-up list at reduced priority; amend the next-pass note: this product-query phrasing is now 1-for-3 productive — the next pass should read contractor forums directly (HVAC-Talk threads on "warranty claim reimbursement paperwork") rather than run another product query.

---

## T5 — Commissions/spiff tracking for contractors

**Question (registry):** does dedicated commission/spiff tracking software for HVAC/trades contractors exist?

**Query:** q09 `sales commission tracking software HVAC contractors spiff`.

**Evidence (q09):**
- **launchadvisor.co (undated, single-source):** "ServiceTitan integrates with several payroll providers and tracks technician commission/spiff payments automatically" — native commission/spiff tracking at the enterprise-FSM tier.
- **slashdot.org (undated, 2026 comparison):** "ReliaServ vs. Salesforce Spiff in 2026 — … real-time portals for tracking commissions" — **Spiff is now Salesforce Spiff** (enterprise SPM).
- **sourceforge.net (undated):** QuotaPath — "the only commission tracking software built for all of Sales, Finance, and RevOps."
- **capterra.com / ventureradar.com (undated):** Spiff — "sales commission software… real-time visibility into earnings and statements"; "combines spreadsheet with automation at scale."

**Verdict: CLOSED** — as an evidenced gap. The workflow is covered at both ends that matter: natively inside ServiceTitan for the top tier (launchadvisor.co, single-source, flag) and by a mature general-purpose SPM category (Salesforce Spiff, QuotaPath) for everyone else. A dedicated small-contractor spiff tracker did not surface — but neither did any demand voice: in three reports' worth of field-service evidence (R7, R13a, this pass) not one user complaint about commission/spiff tracking has appeared. With supply-side coverage at both ends and zero demand evidence, this is a hypothesis with no evidenced gap, not a registry candidate.

**Registry action:** remove from the still-unverified follow-up list (mark closed-as-no-evidenced-gap in the backlog notes); any revival requires user-voice pain documentation first.

---

## T6 — Workiz / ServiceTitan small-shop tier

**Question (registry):** does Workiz serve the small shop at published prices, and does ServiceTitan have any entry tier / minimum contract?

**Queries:** q10 `Workiz pricing small shop 2026`; q11 `ServiceTitan minimum contract price small business`.

**Evidence (q10 — Workiz):**
- **revcorepro.com (Sep 24, 2026):** "Workiz does not publish prices. It sells 3 plans (Standard, Pro and Ultimate), quoted by its sales team, $499/mo Pro plan, quote required" — quote-sales motion, Pro ~$499/mo.
- **itqlick.com (Jun 29, 2026):** "Workiz starts at $49 per user/month."
- **itechguides.com (Sep 21, 2026):** "from $149/mo. $99 each. Prices re-checked Sep 2026. Prices as published by the vendor on workiz.com" — a published $149/mo + $99/user structure claimed.
- **cleanbiztools.com (May 20, 2026):** "Workiz uses custom pricing… depends on your team size."
- **g2.com (Jul 2, 2026):** small-business (≤50 employees) reviews at 4/5 — small shops do use it.
- **contractorplus.app (Sep 10, 2026, competitor comparison):** "Starts at $59/month; Max Plan pricing undisclosed. Workiz is tailored for small to medium-sized businesses" (attribution of the $59 start between HCP/Workiz ambiguous in snippet — flagged).

**Evidence (q11 — ServiceTitan):**
- **thetechyside.com.au (Mar 7, 2026):** "roughly $245 to $300 per technician per month at the Starter level, $300 to $400 for Essentials, $400 to…" — **a Starter tier exists, at $245–300/tech/mo.**
- **serviceagent.ai (Aug 3, 2026):** "ServiceTitan requires a 12-month minimum contract with early termination fees of $5,000 to $20,000 or more. $245 to $500 per technician per [month]."
- **baadigi.com (Sep 21, 2026):** implementation "$5,000–$15,000 for small companies, $15,000–$30,000 for mid-size and $30,000–$50,000 or more for large."
- **pineido.com (undated):** "Implementation fees range from $5,000–$15,000 for most small and mid-size shops to $50,000+ for enterprise… a 12-month minimum contract is standard."
- **leadduo.io (Mar 25, 2026):** "ServiceTitan costs $200+/mo with onboarding fees; Jobber starts at $39/mo with no setup cost."
- **roofingsoftwareguide.com (Sep 23, 2026):** "ServiceTitan's implementation fees ($5,000–$50,000+), per-technician monthly pricing, and 12-month contract create disproportionate financial [burden]."
- **myquoteiq.com (undated, competitor SEO, convergent):** "$245–$500 per technician per month, requires a 12+ month contract, and comes with $5,000–$50,000 in implementation fees."
- **velocityaipartners.co (Jun 22, 2026):** "$500+/month with long-term contracts, it's out of reach for many small [businesses]."

**Verdict: RESOLVED — the question is answered; no registry row follows.** ServiceTitan has **no small-shop tier**: even its Starter level runs $245–300/tech/mo on top of a 12-month minimum contract with $5K–$20K early-termination fees and $5K–$15K small-company implementation (five+ convergent 2026 hosts). Workiz **does** serve the small-to-medium shop with visible entry points ($49/user/mo per itqlick Jun 29 2026; $149/mo + $99/user per itechguides Sep 21 2026) but is drifting to quote-sales ($499/mo Pro, revcorepro Sep 24 2026; custom pricing, cleanbiztools May 20 2026). The "missing middle" ($39–79/mo cheap tier ↔ $245+/tech ST) is real and now precisely priced — but R7 already killed the mid-tier FSM row as a contested challenger war (Fieldy, Contractor+, QuoteIQ, Sera — plus Workiz itself occupying the lower-middle). This pass adds evidence density to a killed row, not a new one.

**Registry action:** mark the straggler resolved (numbers above recorded as evidence ammo for the field-service track); no row change.

---

## T7 — Paperless Parts pricing (bottom-of-market quoting question)

**Question (registry):** any public pricing signal for Paperless Parts — is the bottom of the job-shop quoting market priced out?

**Query:** q12 `Paperless Parts pricing per month job shop` (third pricing pass: R13a q04/q04b, V5 q12).

**Evidence (q12):**
- **paperlessparts.com (Sep 8, 2025):** vendor blog — "Our automated costing and pricing logic is customized to your shop" — quote-customization sales motion, no price.
- **softwarefinder.com / capterra.ca (undated):** "Pricing, Free Demo & Features" and review pages — no number in snippets.
- **practicalmachinist.com (Sep 18, 2024):** forum thread "What is the deal with Paperless Parts?" — user voice: "What paperless does for you is give you a baseline and speed things up. It's integrated with Thyssen for realtime material pricing" — real shop adoption, positive on baseline/speed (pre-2025, flagged).
- **slashdot.org (undated, alternatives list):** "Top Paperless Parts Alternatives in 2026… $99 per month See Software" — a $99/mo alternative visible in the list (attribution ambiguous — not Paperless Parts' own price).

**Verdict: STILL-UNVERIFIED — query family RETIRED from web search** (three consecutive pricing passes across two agents, zero numbers: R13a q04 off-target + q04b marginal; V5 q12 usable-but-numberless). The consistently unpublished price now itself functions as the finding: quote-only, sales-assisted motion — which filters for shops large enough to take a sales call, consistent with R13a's earlier read. The practicalmachinist thread confirms genuine shop adoption and value ("baseline… speeds things up"), and the alternatives list shows the surrounding market has a visible ~$99/mo bracket.

**Registry action:** retire the pricing query family per the 3-strike rule; next step is direct reads, not search: softwarefinder/capterra review pages for bill mentions and the practicalmachinist thread itself. No row change (bottom-of-market quoting stays un-promoted).

---

## T8 — Katana / MRPeasy / Fishbowl sentiment (small-mfg shelfware complaints)

**Question (registry):** complaint density on the modern SMB-mfg tier — is there a sentiment wedge (shelfware complaints) or is the tier liked?

**Queries:** q13 `Katana MRP review complaints 2026`; q14 `MRPeasy Fishbowl G2 comparison`.

**Evidence (q13 — Katana):**
- **capterra.com (Aug 13, 2026, verified user):** "From a financial point of view. It is expensive for micro companies."
- **rfp.wiki (undated):** "A recurring theme is aggressive pricing changes tied to usage metrics. Some customers report billing friction and difficult cancellation experiences."
- **eziil.com (undated, competitor — flagged):** "First-time MRP adopters repeatedly say Katana's visual dashboard shortened their learning curve. **Pricing has become a real complaint theme.**"
- **g2.com (undated):** "Users find the lack of features in Katana Cloud Inventory limits tracking options" (feature-gap complaints).
- **apps.shopify.com (undated, positive):** "Katana has saved my business!"
- **tecmausa.com (Aug 21, 2026):** "**Katana Alternatives in 2026: What to Switch To** — For most switchers, MRPeasy is the answer to both complaints at once. Entry costs $49 per user per month with a two-user minimum — $98/month" — a switching-guide market exists and MRPeasy is positioned as the escape hatch.

**Evidence (q14 — MRPeasy/Fishbowl):**
- **usersolutions.com (Apr 25, 2026):** "MRPeasy Professional ($99/user/month)… Fishbowl Manufacturing (~$4,395 one-time)" — real prices: MRPeasy $99/user/mo Professional tier; Fishbowl ~$4,395 perpetual.
- **aitoolshop.co (May 19, 2026):** "MRPeasy Review 2026 — Best value in class: $49/user/month delivers production planning depth that typically costs 3–5× more in comparable platforms."
- **supergood.ai (undated):** "MRPeasy API: Grade C… one of the most-recognized SMB cloud MRP brands, consistently named alongside Katana, Cin7, Fishbowl, Unleashed, and ERPAG."
- **rfp.wiki (undated, 2026):** "Fishbowl · Risk Notes: Red Flags & Mitigations (2026)" — documented failure modes for Fishbowl.
- **g2.com (Sep 21, 2026) / softwareadvice.com.au / slashdot.org / linkedin.com:** category listings confirm all three as recognized SMB inventory/MRP brands; MRPeasy self-positions for 10–200-employee manufacturers.

**Verdict: RESOLVED — sentiment evidenced; no ownership vacuum; no registry row.** The modern SMB-mfg tier is a real market with a real complaint axis — but the axis is **pricing** (Katana: "expensive for micro companies," aggressive usage-tied price changes, billing friction, hard cancellations), not missing margin visibility or shelfware passivity. And the escape hatch is already sold as such: MRPeasy at $49/user/mo (2-user min) is explicitly marketed as "the answer to both complaints" for Katana switchers (tecmausa.com Aug 21 2026). Fishbowl carries its own documented red flags at a ~$4,395 one-time price. Notably for T1: **no margin-visibility complaint theme surfaced anywhere** — the sentiment data does not support the margin-overlay residual's demand side.

**Registry action:** mark the straggler resolved (sentiment facts recorded for any future SMB-mfg work); no row. Cross-reference: this weakens T1's demand-side case (complaint axis is price, not per-job margin blindness).

---

## T9 — Tariff landed-cost cockpit for SMB importers (R10 straggler)

**Question (registry):** does an SMB-priced landed-cost/tariff calculator product exist for small importers?

**Query:** q15 `landed cost calculator tariff software SMB importers 2026`.

**Evidence (q15):**
- **paidnice.com (undated, 2026 page):** "Tariff Calculator: US Import Duty by Country (2026) — Work out US import duty, fees and total landed cost for a shipment, see what the tariff does to your margin, and compare countries of origin side by side" — free calculator with margin impact + origin comparison.
- **tariffstool.com (undated, 2026):** "True landed cost in 60 seconds: duty + 0.3464% MPF + 0.125% HMF + de minimis check. Free 2026 calculator. Paid duties in 2025? Refunds available" — free calculator + a duty-refund service angle.
- **zonos.com (undated):** "Duties and Taxes Calculator — Try free to get landed cost estimates."
- **borderlinegenius.com (undated):** "landed cost software by Borderline Genius Inc. — Calculate accurate landed costs using current tariffs, duties, taxes, and shipping data."
- **icustoms.ai (undated):** "iCustoms AI-driven landed cost calculator… simplify the calculation of customs charges."
- **ustariffrates.com (undated, updated June 2026):** "Best Landed Cost Calculators — US Tariff Rates 2026… Built for importer, broker" — a comparison listicle covering the category.
- **passportglobal.com (Jun 4, 2026):** landed-cost formula content.

**Verdict: CLOSED as drafted.** SMB-priced — indeed free — landed-cost/tariff calculators for importers exist in force in 2026 (paidnice, tariffstool, zonos free calculators; Borderline Genius and iCustoms as software vendors; a June 2026 comparison listicle covering the field). The one-shot calculator layer is commoditized. Residual, honestly stated: a **continuous** "cockpit" — tariff-change alerting wired into a small importer's live POs/inventory with margin re-computation — did not surface as an owned product, and stays unverified; but the free-calculator floor materially weakens that wedge's entry-point economics.

**Registry action:** mark the R10 tariff-cockpit straggler closed-as-drafted with these traces; note the unverified residual (continuous, ERP/PO-integrated tariff alerting for SMB importers) as a low-priority possible future lens, not a follow-up mission.

---

## Summary table

| # | Target (source, prior verdict) | FINAL VERDICT | Closer / basis |
|---|---|---|---|
| 1 | T1 Per-job margin overlay on shelfware ERP + Excel (R6 SURVIVED-weak; R13a/V3 quota-blocked) | **STILL-UNVERIFIED** (lean-open supply, weak demand) | No dedicated solver in 31 total searches (q01, q02 fresh); adjacent crowding: JobPack shop-floor reporting (jobpack.com Jul 17 2026), ERP-native costing content (geniuserp.com May 29 2026), contractor-tier job-cost apps (QuoteIQ, Job Cost Pro), DIY no-code (emergent.sh Jul 24 2026); demand signals all vendor-SEO — do not row |
| 2 | T2 Ply pricing/traction (R13a/V3 search-blocked ×2) | **CLOSED** (residual dead; traction CONFIRMED) | $8.5M strategic round (thesaasnews.com Dec 4 2025); Housecall Pro native integration (help.housecallpro.com Jan 20 2026); PCG channel partnership (mypowerhouse.group); SMB/free self-positioning (getply.com Sep 14 2026); exact list price still unpublished — moot |
| 3 | T3 Numa/Avoca/Sameday AI answering (R13a service-blocked ×4) | **CLOSED** | Avoca live enterprise home-services AI (avoca.ai + help.avoca.ai, gated pricing per titanpipelines.com); Sameday YC-backed trades AI workforce (ycombinator.com, gosameday.com); Numa alive but automotive-vertical (numa.com May 29 2026); crowded field Rosie/Smith.ai/Goodcall/Podium/Whippy + HCP/Jobber embedded (callacy.com Aug 13 2026) |
| 4 | T4 Carrier/Trane warranty claims (R13a junk ×2) | **STILL-UNVERIFIED** (3rd pass; lean: portals exist, pain unmeasured) | Trane Connect portal hosts warranty requirements (mtechapis.com mirror); warranty.tranetechnologies.com registration/extension pages; OEM processes claims via human Claims Specialists (talents.vaia.com); no third-party contractor software, no Carrier evidence, zero demand voice |
| 5 | T5 Commissions/spiff tracking (never reached) | **CLOSED** (no evidenced gap) | ServiceTitan native commission/spiff tracking (launchadvisor.co, single-source); Salesforce Spiff + QuotaPath SPM class (slashdot/capterra/sourceforge); zero contractor demand voice in 3 reports |
| 6 | T6 Workiz/ST small-shop tier (R13a 429 ×2) | **RESOLVED** (question answered; row stays killed) | ST: no small-shop tier — $245–300/tech/mo Starter + 12-mo min contract + $5–20K ETF + $5–15K implementation (thetechyside.com.au Mar 7 2026; serviceagent.ai Aug 3 2026; baadigi.com Sep 21 2026); Workiz: $49/user–$149/mo entry, quote-drift to ~$499/mo Pro (itqlick Jun 29 2026; itechguides Sep 21 2026; revcorepro Sep 24 2026); Jobber $39/mo floor (leadduo.io Mar 25 2026) |
| 7 | T7 Paperless Parts pricing (R13a thin ×2) | **STILL-UNVERIFIED — query family RETIRED** | 3rd numberless pass (q12); quote-only motion confirmed (paperlessparts.com Sep 8 2025); real adoption + positive user voice (practicalmachinist.com Sep 18 2024); ~$99/mo bracket visible among alternatives (slashdot, ambiguous) → next step direct reads, not search |
| 8 | T8 Katana/MRPeasy/Fishbowl sentiment (never reached) | **RESOLVED** (no row; weakens T1 demand side) | Katana complaint axis = pricing: "expensive for micro companies" (capterra Aug 13 2026), usage-tied price changes + billing friction + hard cancellations (rfp.wiki); MRPeasy sold as switch answer at $49/user/mo 2-user min (tecmausa Aug 21 2026); MRPeasy Pro $99/user/mo + Fishbowl ~$4,395 one-time (usersolutions Apr 25 2026); Fishbowl red-flags doc (rfp.wiki); no margin-visibility complaint theme anywhere |
| 9 | T9 Tariff landed-cost cockpit (R10/R13b straggler) | **CLOSED as drafted** | Free/crowded 2026 calculator layer: paidnice.com, tariffstool.com ("free 2026 calculator"), zonos.com; software vendors Borderline Genius + iCustoms AI; June 2026 comparison listicle (ustariffrates.com); residual continuous PO-integrated tariff-alerting cockpit unverified — low-priority future lens |

**Net effect on the registry:** 4 stragglers cleared CLOSED/resolved (Ply residual; AI answering; commissions; tariff calculator layer), 2 questions answered without rows (Workiz/ST tier; Katana sentiment — the latter actively weakens the margin-overlay residual's demand case), 3 remain STILL-UNVERIFIED (margin overlay — still no solver but still no user-voice demand; Carrier/Trane contractor-side warranty pain; Paperless Parts pricing — retired from search, moved to direct reads). No new rows recommended from this pass; the registry's field-service and SMB-vertical straggler list is now substantially cleared.

## Quota / deadline notes

- **Executions:** 15 web_search calls / 15 raw files saved (q01–q15) / **zero hard 429 failures / zero retries needed** — the cleanest verification window in the wave-3/4 sequence (vs. R13a: 429s + 11 junk files; V3: 4×429 + 5 junk). The recurring OSRS/Scribd "zoberetimifid" artifact did not appear once, and no rfp.wiki-style junk clusters (rfp.wiki appears in q13/q14 but with substantive review-content snippets, used with the host flagged). One call over the "~14" guideline (15th call to cover the ninth target, T9) — deliberate, taken with ~1 minute of window margin left; time budget honored (~13 min of search window, hard stop at minute ~13).
- **Thin sets:** q08 (5 results, 3 usable, 2 noise) and q07 (3 results, all usable) were the thinnest; q03/q04 returned 5 results each with the load-bearing facts present. Nothing required the junk-artifact escalation path.
- **Attribution flags:** contractorplus.app's "$59/month start" (q10) is ambiguous between HCP and Workiz in the snippet — not used in the verdict; slashdot's "$99 per month" (q12) is an alternative's price, not Paperless Parts' — not used; sourceforge's "no per-seat fees" (q03) is SourceForge boilerplate — not used; launchadvisor.co's ServiceTitan commission claim is single-source and undated; titanpipelines.com's "Avoca gated pricing" is competitor SEO, single-source; rfp.wiki used for Katana/Fishbowl complaint aggregation with the host's junk-tier reputation noted (substantive review-aggregate snippets, cross-confirmed by capterra + eziil + tecmausa on the pricing-complaint axis). Pre-2025 items flagged: practicalmachinist (Sep 18 2024), paperlessparts.com blog (Sep 8 2025), cbtnews (Dec 11 2024).
- **Epistemics:** all pricing figures are host-reported (none verified against vendor checkout); thes are comparison/SEO hosts with known inflation risk — reported as brackets with host+date, per house style. The $8.5M Ply round is single-source (thesaasnews.com) but corroborated contextually by HCP's own help-center integration doc and the PCG partnership announcement.
- **No edits** were made to `docs/gap-registry.md` (main agent owns it), to prior track reports, or to any prior raw-search dirs. This report + the v5 raw dir + the worklog append are the only writes.

## Query log

| File | Query | Outcome |
|---|---|---|
| q01.json | job shop per job profit margin tracking software | usable (9 results: JobPack, MIE, JobBOSS², QuoteIQ, Job Cost Pro, Emergent, Genius ERP) |
| q02.json | manufacturing margin visibility small shop Excel ERP | usable-thin (7 results, all ERP content marketing; cdhcpa Excel-gap) |
| q03.json | Ply inventory trades pricing per month | usable (5: $8.5M round, PCG partner, sourceforge reviews, webcatalog; 1 powersports noise) |
| q04.json | Ply app field service inventory cost | usable (5: getply.com SMB/free, HCP help-center integration, FSM pricing context) |
| q05.json | Numa AI phone answering trades 2026 | usable (6: all automotive — numa.com, skywork, appscribed, reachall, cbtnews) |
| q06.json | Avoca AI answering service contractors | usable (6: avoca.ai, help.avoca.ai, callacy listicle, whippy, titanpipelines) |
| q07.json | Sameday AI home service | usable (3: ycombinator, gosameday, voiceaispace) |
| q08.json | HVAC warranty claim processing software Carrier Trane | usable-thin (5: Trane Connect, warranty.tranetechnologies, claims-specialist job; 2 noise) |
| q09.json | sales commission tracking software HVAC contractors spiff | usable (5: ServiceTitan native, Salesforce Spiff, QuotaPath, capterra, ventureradar) |
| q10.json | Workiz pricing small shop 2026 | usable (6: revcorepro $499 quote-only, itqlick $49/u, itechguides $149+$99, cleanbiztools, g2, contractorplus) |
| q11.json | ServiceTitan minimum contract price small business | usable (8: Starter $245–300/tech, 12-mo min + $5–20K ETF, $5–50K implementation ×5 hosts) |
| q12.json | Paperless Parts pricing per month job shop | usable-numberless (6: vendor blog, softwarefinder, capterra, practicalmachinist forum, slashdot $99 alt) |
| q13.json | Katana MRP review complaints 2026 | usable (8: capterra micro-co complaint, rfp.wiki billing friction, eziil, tecmausa switch guide, g2, shopify positive) |
| q14.json | MRPeasy Fishbowl G2 comparison | usable (9: usersolutions prices, aitoolshop review, supergood API grade C, rfp.wiki Fishbowl red flags, listings) |
| q15.json | landed cost calculator tariff software SMB importers 2026 | usable (7: paidnice, borderlinegenius, tariffstool, ustariffrates, icustoms, passportglobal, zonos) |
