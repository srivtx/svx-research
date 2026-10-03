# R14 — Security & Supply-Chain Tooling Below the Enterprise Tier (2024–2026)

Research task R14 (first researcher in this never-searched lens): SBOM/dependency management for small teams, vulnerability-response workflows, secrets sprawl, permission/audit tooling for SaaS stacks, supply-chain attestation for non-enterprises. Known context honored (not re-searched): enterprise SBOM/SCA is served (Snyk/Dependabot/Trivy class = crowded); CMMC compliance killed as a services-play (R6). Kill-list discipline applied to every candidate gap.

**Method:** z-ai web_search; 15 queries (q01–q15), zero rephrasing retries needed, raw JSON immutable in `research/raw-search-results/r14/`. Evidence prioritized 2024–2026; host+date for every claim; single-source flagged; unsearched = UNVERIFIED, never invented.
**Evidence window:** search snapshot 2026-10-03/04.
**Search count:** 15 calls, 15 files saved, all usable to some degree; no hard 429 failures, no junk-artifact sets (OSRS/Scribd pattern absent this run); three thin-volume sets (q05: 5 results, q12: 5, q15: 6) counted as low-volume, not junk. The empty-title result-format quirk noted by V4 persisted throughout (URLs+snippets+dates intact).

## Query log

| # | Query | File | Yield |
|---|---|---|---|
| q01 | SBOM management tool small team pricing 2026 | q01.json | usable — FOSSA down-market tier, pricing color |
| q02 | vulnerability remediation workflow tool small business SaaS 2026 | q02.json | usable — SMB vuln-mgmt listicle, TPRM compare |
| q03 | secrets sprawl audit tool small company SaaS 2026 | q03.json | strong — GitGuardian 2026 report ×3, SaaS secrets class |
| q04 | SaaS permission audit tool small company 2026 | q04.json | usable — access-review + SMP categories, no pricing depth |
| q05 | supply chain security compliance software SMB cost 2026 | q05.json | thin (5) — SOC 2 budget content |
| q06 | open source vulnerability response understaffed security team survey 2026 | q06.json | usable — demand-side stats |
| q07 | software supply chain attestation SLSA small vendor cost 2026 | q07.json | usable — standards content, DoD pressure, OpenSSF/CRA |
| q08 | security tooling too expensive small teams reddit complaint Snyk pricing | q08.json | thin — review pages, no complaint voice |
| q09 | SOC 2 compliance automation pricing small startup 2026 | q09.json | usable — crowding + pricing confirmed |
| q10 | vendor security questionnaire automation tool small business pricing 2026 | q10.json | usable — crowded specialist tier + pricing-model note |
| q11 | EU Cyber Resilience Act small software vendors obligations SBOM 2026 | q11.json | strong — 24h/72h reporting duty live Sept 11 2026 ×6 |
| q12 | Cyber Resilience Act compliance software startup tooling for vendors 2026 | q12.json | thin (5) — hardware-vendor focus, no small-vendor tool |
| q13 | customers demanding SBOM from small software vendors how to respond 2026 | q13.json | strong — escrow+SBOM combo, vendor-visibility gap |
| q14 | "Cyber Resilience Act" compliance platform software companies readiness tool pricing | q14.json | strong — FOSSA free CRA assessment, Attestra AI, category listicle |
| q15 | GitGuardian pricing free tier small teams secrets detection 2026 | q15.json | usable — free ≤25-dev tier corroborated |

---

## 1. Headline findings

1. **The single biggest fact in this lens is regulatory and it went live three weeks before this search: the EU Cyber Resilience Act's vulnerability- and incident-reporting duties started Sept 11, 2026.** "Manufacturers of products with digital elements" sold into the EU must file an early warning within 24 hours of learning of an actively exploited vulnerability or severe incident, with follow-up notification (hornetsecurity.com Sep 10 2026; corroborated by labs.cloudsecurityalliance.org Sep 10 2026, sciencedirect.com Sep 11 2026, aras.com Sep 11 2026, manageengine.com Aug 20 2026, venvera.com Jul 20 2026, digital-strategy.ec.europa.eu Sep 7 2026). There is no small-business exemption; remaining obligations (incl. CE marking pathway) hit 2027 (openlogic.com Jun 18 2026). This lands a monitoring + report-drafting workflow on every small software vendor selling into the EU.
2. **The generic layers below enterprise are crowded and getting more crowded downward.** Enterprise SCA/SBOM incumbents are packaging down: FOSSA introduced "a new business tier tailored for smaller teams, offering flexible pricing" for SBOM/vulnerability work (fossa.com Aug 19 2025) plus a "Free EU Cyber Resilience Act readiness assessment" lead-gen funnel (fossa.com, undated); a business plan around "$20 per project per month billed annually" is attributed (rfp.wiki — junk-tier host, flagged, single-source). Secrets detection is free at small-team scale: GitGuardian's free tier covers teams up to 25 contributing developers (rfp.wiki; corroborated capterra + g2.com Aug 16 2026 comparison showing GitGuardian Free and Snyk Free).
3. **The buyer≠user structure in this lens is confirmed and sharper than expected: small software vendors are now compliance producers, not just consumers.** Enterprise clients ask small vendors for escrow + SBOM together (codekeeper.co Jul 13 2026 — "Enterprise clients are asking for both escrow and an SBOM. Here's how to satisfy both with a single verified deposit"); vendors "were expected to share SBOMs with customers, but vendors themselves often had little visibility into their own upstream dependencies" (labradorlabs.ai Jan 26 2026). The buyer (enterprise procurement, EU regulator) demands; the small vendor's founding engineer does the work.
4. **The CRA-compliance-tool category is forming fast — a listicle ranking "the best Cyber Resilience Act compliance software for 2026" was published *before* the Sept 11 deadline** (venvera.com Jul 20 2026, "published pricing" promised). Named entrants: Attestra AI by CyberCert Labs ("Manage vulnerability reporting, product security, CE Mark documentation, and CRA compliance in one…" — cybercertlabs.com, undated, no pricing) and FOSSA's assessment funnel. Hardware/device makers are served by a separate visible wave (onekey.com program for connected-device manufacturers; mouser.com CRA-Annex-I product family, Sep 29 2026; festo.com CycloneDX SBOMs).
5. **SOC 2 automation is a fully crowded category aimed exactly at the small-team segment** — Vanta, Drata, Secureframe, Sprinto compared for startups (stackfyi.com May 4 2026; vizajobs.com Jul 6 2026; finextra.com Oct 13 2025 top-15 list); platform pricing ~$6K–$30K/yr quoted through sales (poliwriter.com, undated, single-source), first-year total $25K–$125K with audit fees $15K–$75K (strac.io, undated); "from about $8,000 per year" (techfundingnews.com Nov 26 2025). No gap.

## 2. SBOM & dependency management below enterprise

- Down-market absorption is the pattern: FOSSA business tier for smaller teams (fossa.com Aug 19 2025); ComplyJet "Free (unlimited developers, limited tests). Team from $25/developer/month (min. 5 dev…)" (complyjet.com May 29 2026 — note: complyjet's snippet reads compliance-testing; SCA-adjacent). SBOM practice splits into "three disciplines, each with its own tool class: generating documents, managing and moni[toring]" (everbright-it.de, undated — method content).
- Demand arrives from above: enterprises requiring SBOM contractually from vendors (nflo.tech Sep 23 2025 — buyer-side how-to); global regulation reshaping SBOM assurance (sonatype.com Jan 23 2026); US federal/executive-order momentum making SBOMs "essential" (lineaje.com Nov 21 2024).
- The escrow+SBOM combo for small vendors already has a named seller: CodeKeeper (codekeeper.co Jul 13 2026).
- **Verdict: generic small-team SBOM/SCA gap CLOSED (crowded + free tiers + down-market packaging).** The vendor-side "I must produce a trustworthy SBOM but can't see my own upstream" pain (labradorlabs.ai Jan 26 2026) is real but its tooling surface is being absorbed by the same SCA incumbents.

## 3. Vulnerability-response workflows for small teams

- Enterprise tier crowded: Tenable/Qualys/Rapid7/CrowdStrike/Wiz comparisons (safeguard.sh Jul 19 2026; guptadeepak.com May 8 2026); cloud platforms bundle scanning (Prisma Cloud — securityboulevard.com Dec 19 2025).
- An SMB tier exists as a category: "The best vulnerability management for small businesses in 2026 — affordable, easy-to-run picks" (spotsaas.com Jun 27 2026). ManageEngine Vulnerability Manager Plus positioned for scanning+remediation (expertinsights.com, undated). MDR services market "24/7 monitoring without hiring more analysts… for teams of 2, 5…" (underdefense.com Mar 20 2026) — a services workaround, the R6 CMMC pattern at smaller scale.
- Demand-side: understaffed security teams pay "$1.76 million more in breach damages than fully staffed teams" (testlify.com Sep 14 2026, single-source, provenance unverified — flag); "software security teams are often critically underfunded and understaffed" (dl.acm.org May 12 2026); 86% of survey respondents had ≥1 breach (technewsworld.com Oct 8 2025).
- **What changed the game: the CRA 24h/72h reporting duty (§1) turns dependency-vuln response into a deadline workflow for small vendors.** That slice — monitor exploited-vuln feeds against your SBOM, draft the ENISA submission — is new. Nearest closers: Attestra AI (cybercertlabs.com, undated, single-source — depth owed) and the venvera-ranked category (Jul 20 2026). **Verdict: generic tier CLOSED; CRA-reporting slice BEING-CLOSED at formation speed — category listicle predates the deadline.**

## 4. Secrets sprawl & SaaS audit

- Scale of problem, multi-sourced: 28.65M new secrets leaked to public GitHub in 2025, a 34% jump from 2024 (GitGuardian State of Secrets Sprawl 2026 via akeyless.io Sep 8 2026; aembit.io; passwork.pro Jun 4 2026). Eight of the ten fastest-growing leaked-secret types are tied to AI services (passwork.pro Jun 4 2026 citing GitGuardian). New sprawl frontier: "MCP sprawl is hitting every mid-sized business in 2026: 20 connectors, ballooning token costs" (cierra.ai Jun 5 2026).
- Detection is free at small scale (GitGuardian ≤25 devs, §1); vaulting/management is a crowded category going SaaS-native in 2026 — "Secrets Management Tools in 2026: arrives as SaaS. Provable audit, dynamic secrets, and policy…" (capy.sc May 29 2026); credential-management category writeups (envmanager.com Jun 11 2026).
- **Verdict: secrets DETECTION and VAULTING both closed (free tier + crowded SaaS class). Residual "secrets census across the SaaS estate" (beyond git) surfaced no dedicated small-team solver — but also no demand voice this run (q03 was vendor-side content) → UNVERIFIED, do not row.**

## 5. SaaS permission/audit tooling (overlap check vs registry gap #8)

- Categories that exist: access-review software (8-tool 2026 comparison "on automation, remediation, reviewer workflows" — guideflow.com Aug 25 2026); SaaS management platforms that "find hidden apps, cut license waste, tighten access" (smarttechatlas.com, undated); audit software for small businesses (krowdbase.com, undated); Netwrix Auditor for mid-size (slashdot, undated); ITSM-integrated audit (ones.com Jun 17 2026).
- None of these surfaced small-team pricing this run; the access-review/SMP classes are historically mid-market-plus (pricing UNVERIFIED this pass — do not assert).
- **Verdict: registry gap #8 (permission census scanner, headless-browser crawler) is NOT closed by anything found here — the surfaced categories are reviewer-workflow/SMP shapes, not census/scanning. Gap #8 stands; recommend a pricing-depth follow-up (direct product-page reads of the guideflow-compared access-review tools) rather than any new row, which would duplicate #8.**

## 6. Supply-chain attestation for non-enterprises (overlap check vs gap #2)

- Standards layer mature: SLSA L1–3+, in-toto (minimus.io, undated — method content). Free community layers forming: Docker Hardened Images "DHI Community costs $0 under Apache 2.0" (echo.ai, undated, single-source). OpenSSF discussing "voluntary attestation models under the Cyber Resilience Act" (openssf.org, undated).
- DoD-side pressure on small defense vendors persists (projectspectrum.io, undated) — but that is CMMC-adjacent territory already killed as a services-play (R6, honored — not re-searched).
- **Verdict: attestation GENERATION is ossifying into standards + free platform layers → CLOSED as a gap. Registry gap #2 (AI-code verification ledger) concerns code authorship, not artifact provenance — unaffected by this pass; no new row.**

## 7. SOC 2 / compliance automation crowding check

- Confirmed fully crowded and startup-focused: Vanta/Drata/Secureframe/Sprinto evidence-collection comparisons for startups (stackfyi.com May 4 2026; vizajobs.com Jul 6 2026; finextra.com Oct 13 2025); pricing bands $6K–$30K/yr (poliwriter.com, undated, single-source), $8K/yr entry (techfundingnews.com Nov 26 2025), first-year totals $25K–$125K incl. audits (strac.io, undated). Compliance-platform comparison content targets enterprise with framework breadth (getsecureslate.com May 4 2026); enterprise compliance pricing drivers analyzed (securitribe.com May 19 2025).
- **Verdict: CLOSED (crowded). Any "SOC 2 for tiny startups" candidate is dead — the category's core market IS startups.**

## 8. Vendor security questionnaires (small-vendor answerer side)

- Crowded specialist tier: Conveyor ("built for enterprise" — g2.com); Vendict AI-led GRC/questionnaires (vendict.com Dec 15 2025; guptadeepak.com); Loopio (auditive.io Nov 28 2025); Whistic and Vanta-TPRM ranked for "cutting questionnaire volum[e]" (ipwithease.com Sep 3 2026); Cyber Sierra "343x faster ev[idence]" self-ranked (cybersierra.co Sep 8 2026, vendor claim); new AI-agent entrant Iris/heyiris.ai (undated); TPRM platform comparisons with workflows/approvals (aravo.com Sep 15 2026).
- Pricing shape note: "Specialist response tools generally price per user or per seat for the people drafting answers" (scrutineer.ai, undated, single-source) — suggests seat pricing that punishes the tiny vendor, but this is one undated source.
- **Verdict: CROWDED above; small-vendor-priced slice UNVERIFIED (no pricing evidence, no complaint voice surfaced — q08 thin). Do not row; follow-up via forum reads (r/netsec, r/devops, Indie Hackers) not more product queries.**

---

## 9. Kill-list table

| Candidate gap | Attack (searched for the existing solver) | Verdict |
|---|---|---|
| SBOM/SCA management for small teams | FOSSA business tier for smaller teams (fossa.com Aug 19 2025) + free CRA assessment (fossa.com) + free tiers all around (GitGuardian/Snyk free per g2 Aug 16 2026); ComplyJet free/low ladder (May 29 2026) | **KILLED (crowded; down-market packaging already shipped)** |
| SBOM + escrow deliverable for small vendors | CodeKeeper sells exactly the combo (codekeeper.co Jul 13 2026) | **KILLED** |
| Vulnerability management for small business | SMB listicle category exists (spotsaas.com Jun 27 2026); ManageEngine tier (expertinsights); MDR services for 2–5-person teams (underdefense.com Mar 20 2026) | **KILLED (crowded + services workaround)** |
| CRA compliance / vulnerability-reporting workflow for small software vendors | Attestra AI exists (cybercertlabs.com, undated, no pricing); FOSSA free CRA readiness assessment (fossa.com); category listicle published pre-deadline (venvera.com Jul 20 2026); device-side wave separate (onekey, mouser, festo) | **BEING-CLOSED at formation** — demand live (24h duty since Sept 11 2026) but the race started before the deadline; watch-list, not a row; Attestra depth + pricing owed |
| Secrets sprawl detection/audit for small teams | GitGuardian free ≤25 devs (rfp.wiki/capterra/g2); SaaS secrets-management class arriving (capy.sc May 29 2026); problem sized 28.65M secrets/2025 (GitGuardian via akeyless Sep 8 2026) | **KILLED for detection/vaulting; "secrets census across SaaS estate" residual UNVERIFIED (no solver, no demand voice)** |
| SaaS permission audit for small companies | Access-review category (guideflow.com Aug 25 2026), SMPs (smarttechatlas) — all mid-market-shaped, no small-team pricing found; registry gap #8 already owns this | **SURVIVES as registry gap #8 (unchanged); no new row — would duplicate** |
| Supply-chain attestation for non-enterprises | SLSA/in-toto standards (minimus.io); Docker Hardened Images Community $0 (echo.ai, single-source); OpenSSF voluntary attestation under CRA (openssf.org) | **KILLED (ossifying into free platform layers)** |
| SOC 2 automation for startups | Vanta/Drata/Secureframe/Sprinto — category's core market IS startups (stackfyi May 4 2026 + 3 more) | **KILLED (crowded)** |
| Vendor security questionnaire answering (small-vendor side) | Conveyor/Vendict/Loopio/Whistic/Cyber Sierra/heyiris (q10, 8+ named); seat-pricing note (scrutineer.ai, single-source) | **UNVERIFIED lean-crowded** — no small-vendor pricing or pain voice evidenced; no row |
| Understaffed-team vuln response as a general product | Demand stats exist ($1.76M breach delta — testlify Sep 14 2026 single-source; ACM May 12 2026) but served by MDR services + SMB scanners | **KILLED (services + crowded scanners)** |

## 10. Registry recommendations

**No new rows.** The lens resolves as: **vertical closed at the generic layer** — every classic candidate (SBOM, SOC 2, vuln-mgmt, secrets, attestation) is either crowded, free-tiered, down-market-packaged, or services-served; and its one genuinely new opening (CRA-response for small software vendors) is **BEING-CLOSED at formation speed** — the category's comparison listicle shipped a month *before* the regulatory deadline. Per kill-list discipline, a forming category is recorded closed, not chased.

Recommended maintainer actions (no file edits made by me):
1. **Do not add a CRA-compliance row.** Record the lens as cleared in the backlog with this note: demand driver live (EU CRA 24h reporting since 2026-09-11, full effect 2027), category forming (closers: Attestra AI, FOSSA CRA funnel, venvera-ranked field), re-check trigger = 2 quarters or first verified sub-$100/mo small-vendor CRA product, whichever first.
2. **Gap #8 (permission census scanner): unchanged, mildly strengthened** — access-review/SMP categories exist but no small-team-priced census-shaped solver surfaced; append "R14 (2026-10-03): guideflow 8-tool access-review comparison + SMP class checked — none census-shaped or SMB-priced (pricing unverified)."
3. **Follow-up list additions (owed, with method):** Attestra AI depth + pricing (direct page read, not search); access-review small-team pricing (guideflow-compared vendors' pricing pages directly); small-vendor questionnaire pain (forum reads — query family weak on this search service).
4. **Watch-list (not a row):** "secrets census across SaaS estate" and "MCP-connector sprawl" (cierra.ai Jun 5 2026) — both demand-side signals with no evidenced small-team solver; revisit if a complaint voice surfaces.

## 11. Quota / deadline notes

- 15 search calls / 15 files / 0 hard failures / 0 retries / 0 junk-artifact sets — cleanest possible run profile; thin sets (q05, q12, q15 at 5–6 results) were low-volume, not the degraded-upstream pattern. Empty-title format quirk persisted (V4's flag to the search-tooling owner stands).
- Hard stop honored: new searches ended at call 15 (~minute 14–15); report written from what landed.
- Coverage gaps owned: no direct pricing pages read (Capterra/vendor) — all pricing claims above are search-snippet grade, flagged where single-source; Attestra AI depth not done; Reddit/forum demand voice for questionnaire pain not captured (q08 thin); hardware/device CRA wave only sketched (mouser/festo/onekey).

## Key sources (hosts + dates as seen in raw files)

- CRA deadline/duties: hornetsecurity.com (Sep 10 2026); labs.cloudsecurityalliance.org (Sep 10 2026); sciencedirect.com (Sep 11 2026); aras.com (Sep 11 2026); manageengine.com (Aug 20 2026); venvera.com (Jul 20 2026); digital-strategy.ec.europa.eu (Sep 7 2026); openlogic.com (Jun 18 2026); kusari.dev (undated); securitytoday.de (Apr 9 2026).
- CRA-tool entrants: cybercertlabs.com (undated — Attestra AI); fossa.com (undated free CRA assessment + Aug 19 2025 business tier); onekey.com, mouser.com (Sep 29 2026), festo.com (device side).
- SBOM demand-from-above: codekeeper.co (Jul 13 2026); nflo.tech (Sep 23 2025); sonatype.com (Jan 23 2026); labradorlabs.ai (Jan 26 2026); lineaje.com (Nov 21 2024); encryptionconsulting.com (Jul 3 2026).
- Secrets sprawl: akeyless.io (Sep 8 2026); passwork.pro (Jun 4 2026); aembit.io (undated); capy.sc (May 29 2026); envmanager.com (Jun 11 2026); cierra.ai (Jun 5 2026); gitguardian.com / capterra.com.sg / g2.com (Aug 16 2026) / rfp.wiki (pricing, junk-tier host flagged).
- SOC 2 / compliance: stackfyi.com (May 4 2026); vizajobs.com (Jul 6 2026); finextra.com (Oct 13 2025); techfundingnews.com (Nov 26 2025); poliwriter.com (undated, single-source); strac.io (undated); getsecureslate.com (May 4 2026); securitribe.com (May 19 2025); thesectorpost.com (Jan 29 2026).
- Questionnaires/TPRM: g2.com (Conveyor); vendict.com (Dec 15 2025); auditive.io (Nov 28 2025); ipwithease.com (Sep 3 2026); cybersierra.co (Sep 8 2026); aravo.com (Sep 15 2026); scrutineer.ai (undated, single-source); heyiris.ai (undated).
- Vuln-mgmt/SMB: spotsaas.com (Jun 27 2026); safeguard.sh (Jul 19 2026); guptadeepak.com (May 8 2026 + Vendict); securityboulevard.com (Dec 19 2025, Jun 30 2025); expertinsights.com (undated); underdefense.com (Mar 20 2026); testlify.com (Sep 14 2026, single-source); technewsworld.com (Oct 8 2025); dl.acm.org (May 12 2026); files.gao.gov (Apr 24 2026).
- Permissions/access: guideflow.com (Aug 25 2026); smarttechatlas.com (undated); krowdbase.com (undated); ones.com (Jun 17 2026); thectoclub.com (Sep 1 + Sep 3 2026); selecthub.com (Mar 16 2026); kryptoadvantage.com (Jul 18 2026).
- Attestation: minimus.io (undated); echo.ai (undated, single-source); openssf.org (undated); projectspectrum.io (undated).
