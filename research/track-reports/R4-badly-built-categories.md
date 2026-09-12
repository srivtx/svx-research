# R4 — Badly-Built Categories: Why Hated Software Stays Bad (2025–2026)

Research task R4: which software categories have existed 10–20 years, are used by everyone, are widely hated — and *why do they stay bad*? What would a genuine fix look like, and does AI change the economics now? Method: 24 web searches via z-ai; evidence prioritized from 2024–2026. All numbers below were actually seen in cited sources; older stats are flagged.

---

## 1. The cross-cutting structural pattern

Before categories: the *same four mechanisms* keep almost all of these categories bad, and they compound each other.

1. **Buyer ≠ user.** The person who selects the software (IT, procurement, VP, CFO) is not the person who suffers daily. Reddit r/sysadmin (Dec 2025): "Because a bad UI doesn't impact sales, because the people who do the purchase don't use the application." A Medium essay (Jul 2026, "The Enterprise Software Delusion") argues enterprise software is bloated "because the economic incentives are entirely misaligned" — the same observation HN was making in 2010, still true in 2025.
2. **Process-encoded pain.** Much of the hatred isn't UX hatred — it's the software faithfully automating a process employees already resent. Ministry of Testing forum (Feb 2025): "My biggest problem is not Jira itself, but how people are using it. Using it for command & control sucks." Breeze.pm (Oct 2025): PM tools "fail because of resistance, not because of missing features."
3. **"Good enough" + switching costs + integration moats.** Legacy tools sit on SSO, workflows, exports, and 10 years of muscle memory. MIT Sloan Review's classic "The Trouble with Enterprise Software" (2007) noted enterprise systems can carry 50%+ data error rates — and survived anyway, because replacing them is riskier than hating them.
4. **No UX feedback loop in procurement.** Buying is checklist-driven, so vendors invest in the demo-to-checkout path, not the daily-use path. UX Matters (Feb 2025): poor user adoption causes ~70% of digital-transformation initiatives to fail.

**The AI twist (2025–2026):** for the first time, the marginal cost of *manual entry, summarization, and retrieval* is collapsing (BCG, Oct 2025: ServiceNow-style agents report up to 60% reduction in manual workloads in IT/HR/ops). That attacks mechanism #2 and the data-quality half of #3 — but NOT the buyer≠user mismatch, which is organizational, not technical.

---

## 2. Category: Project management tools (Jira et al.)

- **Who suffers:** developers/users daily; buyers are engineering managers/CTOs who purchase governance.
- **Evidence of hatred:** dev.to (Nov 14, 2025), "Why Developers Hate Jira": teams "contorted their behavior to make the tickets look good. They gamed velocity metrics. They spent hours feeding the beast instead of shipping." Atlassian's own community forum documents heavy criticism of the May 2025 Jira navigation redesign (chaotic, more clicks, less efficient), and HN jokes that hating Jira is "passed down from each generation of programmers to the next."
- **Why it stays bad:** Jira's buyer is the org, not the dev; configurability *is* the product (every stakeholder gets their field, so every ticket becomes a form). The tool also encodes a control process (velocity, reports) that devs resent but managers buy. HN comment on enterprise software generally: "writing complex, highly configurable software is hard and very few companies have the billions" to do it well.
- **Tried & failed:** dozens of "Jira killers" (Monday, Asana, Trello, ClickUp). Even Linear, the most loved alternative, gets this critique — ClickUp (2026): "Linear stripped out the complexity that made Jira unpopular. But it also stripped out the reporting that would have made the switch work." I.e., the moment a tool is good enough for management reporting, admins reconfigure it into Jira. Everhour (Sep 2025): Linear's lack of custom fields limits non-developer teams, pushing them back to Jira.
- **Genuine fix:** not another board UI, but (a) *zero-touch issue capture* — the system of record assembles itself from commits, PRs, deploys, chat; humans never fill fields; (b) reporting computed from reality rather than from hand-entered ticket hygiene, removing the incentive to game it.
- **AI economics:** yes — commit/PR/chat → structured issue inference is newly cheap. But distribution must be bottom-up per-team, because top-down purchases re-create Jira.

---

## 3. Category: CRM data entry (the strongest, cleanest gap)

- **Who suffers:** salespeople (users); buyer is sales leadership/RevOps, who buy the CRM *for* the data — extracted from the people who hate entering it.
- **Evidence:** Attention (Feb 2025, citing Salesforce's own numbers): sellers spend ~40% of the week selling and 60% on everything else. DevRev (2026, citing Salesso): **79% of opportunity data reps collect never makes it into the CRM.** BusinessWire (Aug 2026) survey of 1,000 US sales/marketing professionals: nearly 4× as many respondents focused on logging calls/emails — "The Modern Salesperson Is Becoming a Data-Entry Clerk." Older but consistent: manual data entry is the #1 reason CRM adoption fails and 32% of salespeople spend over an hour/day on it (Dakota, 2022); heydan.ai (Dec 2025) cites CRM project failure rates of 20–70%, primarily poor user adoption.
- **Why it stays bad:** perfect buyer≠user case — the rep's labor is the input; the manager's dashboard is the output; the rep gets zero personal ROI (askelephant.ai, Feb 2026, lists "no personal ROI, misaligned incentives" as the real reasons reps avoid CRM). Salesforce's moat is integrations + 20 years of customization, not love.
- **Tried & failed:** mobile CRMs, "CRM adoption" training, gamification, mandatory-field policies — all treat the symptom. AI logging startups now attack it directly (auto-capture from calls/email/calendar).
- **Genuine fix:** CRM as an *observation* system, not an entry system: capture calls→transcripts→structured fields with the rep reviewing, never typing; sell to the rep first (saved prep time before calls) so adoption is voluntary.
- **AI economics:** strongly yes — speech→structured-fields is exactly what LLMs newly do well. This is the category where AI most changes the build.

---

## 4. Category: Enterprise internal search

- **Who suffers:** every knowledge worker; buyers are IT, who buy for permissions/compliance, not answer quality.
- **Evidence:** Slite's Enterprise Search Survey Report (Jan 2026): search failures cause customer delays (15% of respondents) and missed deadlines (9%) — "nearly a quarter of search failures affect external" outcomes. A 2026 YouTube talk titled "Why Enterprise Search Still Sucks in 2026" captures the mainstream sentiment; a practitioner piece (mydigitalworkplace) explains why it's not Google: "showing up in search results = putting in effort to be found," and different teams use different vocabularies for the same thing.
- **Why it stays bad:** fragmentation (answers live in 40 SaaS tools), ACL hell, and stale/ungoverned content. Critically, search quality depends on *writing quality upstream* — which nobody owns.
- **Tried & failed / what succeeded partially:** Neeva's consumer-search talent went enterprise (Snowflake); Glean became the category leader — a $4.6B valuation built on a permissions-aware index (Turing Post). But even Glean's alternatives pages (Slite, 2026) admit: "Glean mirrors the permissions in your connected tools" — so it can *amplify* existing permission chaos; garbage docs rank as well as good ones.
- **Genuine fix:** search is now an *answer/agent* problem, not a ranking problem — but the durable moat is data hygiene + permissions reconciliation, i.e., plumbing, not AI polish.
- **AI economics:** yes for answers (RAG everywhere), but the bottleneck moved to permissions, connectors, and content freshness — which is integration work AI doesn't remove.

---

## 5. Category: Meetings software & notes

- **Who suffers:** everyone; there is effectively no buyer — meetings tools are bundled (Zoom/Teams), so nobody is paid to fix the *work* around meetings.
- **Evidence of pain:** Fellow.ai (May 2025): unproductive meetings cost businesses upwards of $375B annually; Flowtrace (2025): meeting time costs ~$29,000 per employee per year; Asana data via SpeakWise (2026): individual contributors lose 3.7 hrs/week to unproductive meetings, a 118% jump since 2019.
- **Why notes stayed manual (until recently):** transcription quality, but mostly *accountability* — notes are trusted only if a human takes responsibility for them; summaries rot in silos.
- **Tried & failed / partial:** AI notetakers finally crossed the adoption line — Saner.ai (Jul 2026): ~75% of professionals now use an AI note-taker in work meetings. Yet Tana (Jul 2026): "Why AI notetakers fail to drive action... the action items they extract stay yours to carry out, and each meeting becomes its own silo." Plus a new risk layer: Mayer Brown (Jun 2026) on legal exposure; Nudge Security (Jan 2026) on shadow-AI OAuth grants; Careful Industries (Nov 2025) lists nine organizational risks; Smith Law (Oct 2025): transcripts "miss nuance or context... sarcasm or tone."
- **Genuine fix:** meeting→action loop: notes must flow into the ticket/CRM/doc systems automatically (the missing link), with consent tooling built in. The wedge is *execution follow-through*, not better transcripts.
- **AI economics:** yes — but the unsolved part (cross-system write-back + trust) is exactly what's unbuilt.

---

## 6. Category: Expense reports, timesheets, approvals — "the beige dead zone"

- **Who suffers:** every employee + finance teams; buyer is CFO/procurement, buying for control, not for the employee's Saturday-night receipt session.
- **Evidence:** New York Times (Nov 3, 2024): "Nobody Likes Doing Expense Reports. Why Isn't It Easier?... We hate them. The companies that build expense management software know that we hate them." WalkMe survey (Dec 2023): **half of workers don't file** some expense reports at all, leaving an average of $26.25 per person in unreimbursed expenses; 48% say work expenses create job stress. Corpay (Mar 2026): an expense report costs $58 to process and 19% contain errors. Mesh Payments: employees find the process too time-consuming and confusing to stay within policy.
- **Why it stays bad:** the buyer purchases *policy enforcement and audit*; the user wants money back with zero effort. Vendors optimized receipts-OCR long ago, but the pain is policy, out-of-pocket float, and multi-step approvals — org-process pain that software mirrors faithfully. This is the purest case of "the software is the process, the process is the hatred."
- **Tried & failed:** corporate cards + OCR + auto-categorization (Ramp, Brex, Navan, Expensify, Sage all market this heavily in 2025–2026) — and the NYT piece shows the hatred persists anyway, because personal-card spend, per diems, and approvals remain manual.
- **Genuine fix:** kill the report, not improve it: card-first everywhere + LLM agents that assemble evidence (receipt matching, policy explanation in chat, auto-approval for in-policy spend), with finance buying *exception-handling* rather than review of everything.
- **AI economics:** yes — document understanding + policy-as-conversation newly make 90%-auto-approval credible.

---

## 7. Category: Intranets / internal comms

- **Who suffers:** employees; buyer is internal comms/IT.
- **Evidence:** Firstup (Jun 2024): **57% of employees see no purpose in their company intranet**, yet 75% of internal comms professionals use one for communication. Nexinite (Aug 2025, citing Coveo): up to 90% of intranets fail to deliver clear value. Blink (Jun 2025) on why employees hate them: "too hard to find anything," "only updated once a quarter," "all corporate." Interact Software (Nov 2025) documents SharePoint intranet failure signs.
- **Why it stays bad:** two masters — execs want a billboard, employees want a tool; it's neither. Content freshness is nobody's job. SharePoint's moat is the M365 bundle.
- **Genuine fix / AI economics:** an *answer + action layer* over existing systems (people, PTO, expenses, forms) instead of a page tree — 90% generated and auto-updated per person, which fixes staleness for the first time.

---

## 8. Category: Email clients (a graveyard of "fixes")

- **Evidence of failed attempts:** Notion Mail shut down on September 22, 2026, roughly a year after launch (TechCrunch, Jun 25, 2026; Notion's own notice). TechCrunch: discontinued "in favor of its AI agent offering," with users "increasingly handing over the inbox" to agents; Enterprisedna (Jun 2026): **more than half of Notion Mail users never actually opened their inbox.** Superhuman — the celebrated UX play — ended up acquired by Grammarly and now sells "save 4+ hours per person every week" (its own marketing).
- **Why it stays bad:** Gmail/Outlook are free, default, and API-locked-enough; clients add a layer without owning the data. And the honest 2026 lesson: people don't want a *faster inbox*, they want *less inbox* — which a client can't sell without cannibalizing engagement (the very metric email monetizes).
- **Genuine fix:** agents that drain the inbox (draft, schedule, extract tasks into systems, unsubscribe/purge) — Notion's own pivot is the tell. The wedge is outcome-per-email, not UX.

---

## 9. Category: Knowledge management / documentation (Confluence–Notion–Obsidian era)

- **Evidence:** Atlassian community (Feb 2026): "Your Confluence wiki is confidently giving people wrong answers... Documentation goes stale silently. Unlike code, there's no test suite that goes red when your runbook references a deprecated service." Dev.to (2020): "Confluence Is Where Documentation Goes To Die" — outdated docs are worse than no docs. Fabric.so: this is "a problem with any documentation system that depends on humans writing and maintaining docs manually. Notion..." Despite Notion's scale (100M users, ~$600M ARR per Taskade, Mar 2026), reviews still note it "struggles with true project execution at scale" (Taskrhino, 2025) and locks meaningful AI behind a $20/user/month tier (Taskade, Mar 2026).
- **Why it stays bad:** docs are an unpaid externality — the writer pays, future readers benefit, so nobody maintains them; every tool assumes voluntary upkeep.
- **Genuine fix:** docs generated from the work itself (PRs, incidents, decisions-in-chat) with staleness detection — "a test suite for documentation" is the single best product phrase found in this research.
- **AI economics:** yes — generation + staleness detection + Q&A over docs are newly cheap; the moat is wiring into where work actually happens.

---

## 10. Category: Time tracking & billing (professional services)

- **Evidence:** LeanLaw: poor timekeeping costs a law firm $25,000–$100,000/year in unbilled time; LawBillity (Aug 2025) invokes "the psychology of time tracking" to explain lawyer resistance; the ABA itself (Mar 2025) now pushes AI time capture; Memtime sells passive capture as recovering lost billables.
- **Why it stays bad:** the tracker punishes its user (interruption, self-surveillance) while the benefit goes to the firm's billing; incumbents sell to firm partners, not associates.
- **Genuine fix / AI economics:** passive reconstruction of the day from calendar/email/docs, presented as a *draft timesheet* to edit; unbuilt is tight matter-mapping and trust-accounting write-back — reconstruction quality crossed the usability threshold ~2024–2025.

---

## 11. Weaker / adjacent findings (kept short)

- **Internal tools/admin panels:** Retool's 2025 Builder Report (Oct 2025) notes "something fundamental is changing about who builds software" — ops managers now ship tools — confirming the demand was always there; what remains unbuilt is *governed*, end-user-grade internals.
- **Spreadsheets-as-database:** Diginomica (2023): "Shadow IT never dies — spreadsheets are still running" companies; ResearchGate: BI tools had little impact on spreadsheet use; Securys (2026) flags rogue Excel/CSVs as the compliance black swan of the agentic-AI era. Root cause: databases demand schema and permissions nobody wants to administer.
- **Employee onboarding / PDF & e-sign:** evidence is real but mostly HR-vendor flavored (BambooHR 2024 on first-day paperwork; NetSuite 2025 on info overload); e-sign search results skewed to vendor comparisons. Both gaps look like cross-system orchestration, not another app.

---

## 12. Synthesis: the five mechanisms ranked by fixability

| Mechanism | Categories locked by it | Does AI (2025–26) unlock it? |
|---|---|---|
| Buyer ≠ user | CRM, PM tools, intranets, expense | No — needs bottom-up distribution |
| Software encodes a hated process | PM tools, expense/approvals, timesheets | Partially — agents can bypass process steps |
| Manual entry / summarization cost | CRM, notes, timesheets, docs, search | **Yes — this is the big unlock** |
| Integration/permission moats | search, email, intranets, PM | Partially — connector+agent layer is the new moat |
| "Good enough" trap + free defaults | email, spreadsheets | Yes, via outcome-pricing instead of seat-pricing |

**Bottom line:** the categories that stay bad are those where the person feeling the pain has no purchasing power and the vendor's revenue depends on the pain's *byproduct* (data, control, compliance), not on the pain being removed. AI does not fix buyer≠user — but it collapses the manual-entry layer that made these tools painful, enabling a new wedge: sell the suffering user a tool that *removes* their work (auto-capture, auto-fill, auto-file), then sell the resulting clean data to the buyer. Notion Mail's shutdown and Notion's pivot to agents is the 2026 proof that "a better version of the hated thing" loses to "the hated thing, deleted."

## Key sources
- dev.to (Nov 2025) Jira; Atlassian community (May 2025 nav; Feb 2026 Confluence); deviniti.com; Breeze.pm (Oct 2025); ClickUp; Everhour (Sep 2025); productlane (Aug 2024).
- Attention (Feb 2025); DevRev (2026); Everready (2023); Dakota (2022); BusinessWire (Aug 2026); heydan.ai (Dec 2025); askelephant.ai (Feb 2026).
- Slite Enterprise Search Survey (Jan 2026); Turing Post (Glean $4.6B); slite/flur.ee/gosearch.ai (Glean alternatives, permission mirroring).
- Fellow.ai (May 2025); Flowtrace (2025); Asana via SpeakWise (2026); Tana (Jul 2026); Saner.ai (Jul 2026); Mayer Brown (Jun 2026); Nudge Security (Jan 2026); Careful Industries (Nov 2025); Smith Law (Oct 2025).
- NYT (Nov 3, 2024); WalkMe (Dec 2023); Corpay (Mar 2026); Mesh Payments; Deem (2020).
- Firstup (Jun 2024); Nexinite/Coveo (Aug 2025); Blink (Jun 2025); Interact (Nov 2025).
- TechCrunch (Jun 25, 2026); Notion.com; Enterprisedna (Jun 2026); Superhuman blog (Nov 2025); usecarly.com (Jul 2026).
- LeanLaw (2022); LawBillity (Aug 2025); ABA Law Technology (Mar 2025); Memtime; hourlytime.com (Nov 2025).
- Retool 2025 Builder Report (Oct 2025); Diginomica (2023); ResearchGate; M365Princess (May 2025); Securys (2026).
- BambooHR (2024); hwny.org; NetSuite (May 2025) — onboarding. Pandadoc/Qwilr/Oneflow — e-sign comparisons.
- Reddit r/sysadmin (Dec 2025); Medium "Enterprise Software Delusion" (Jul 2026); MIT Sloan Review (2007, historical); UX Matters (Feb 2025); LinkedIn Smith (2018); BCG (Oct 2025).
