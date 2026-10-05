# R16 — Consumer money-dates lens (wave-5 pivot)

**Lens (new, owner-directed 2026-10-05):** every previous SVX row is
business-software-shaped (dev tooling, vertical SIS overlays, SMB ops).
The owner's pivot directive: find a gap in **consumer software people
actually use daily/weekly** — one where the pain is visceral enough that
users "psychologically fall for" the fix, and the market is everyone,
not 10 people. No more deterministic-validation tooling that sits
unused.

**Hypothesis (to be tested, not assumed):** consumers bleed money on
*dates* — free trials that convert, renewals that fire, warranties that
lapse, gift cards that decay, 0% APR windows that cliff, IDs/passports
that expire at the worst moment. The subscription economy's business
model *depends* on forgetting (negative-option defaults). Existing
"fixes" (Rocket Money, Hiatus, Copilot) demand **bank linkage** — a
trust barrier — and often charge a subscription to fight subscriptions.
If the evidence shows (a) massive prevalence, (b) quantified money at
stake, (c) incumbent weakness = bank-link/fee/fragmentation, and (d) no
local-first unified "expiry radar" exists — then the wedge is a
**no-account, no-bank-link, local-first PWA** that weaponizes loss
aversion with a live "$ at risk" ticker.

**Candidate set under test:**

| # | Candidate | Class | Key risk |
|---|-----------|-------|----------|
| A | Unified expiry radar (trials, renewals, warranties, gift cards, APR cliffs, IDs, domains) | Consumer / loss-aversion | platform absorption (Apple/Google renewal alerts); fragmentation by single-purpose apps |
| B | Standalone warranty vault | Consumer / niche | receipt-capture UX burden; single decay class |
| C | Gift card value tracker | Consumer / niche | single decay class; retailer apps absorb |
| D | Freelancer late-payment chaser | Prosumer | email-infra dependency; crowded-ish (Bonsai etc.) |
| E | Family document/emergency vault | Consumer / trust-heavy | trust barrier for a new brand is worse than bank link |
| F | Meal planner + fridge inventory | Consumer / huge | brutally competitive, BigCorp-adjacent (negative check only) |
| G | Photo dedup/organizer | Consumer / huge | desktop-app territory, platform photos apps absorbing (negative check only) |

**Method:** 14 targeted queries via `tools/svxsearch.py` into
`research/raw-search-results/w5cp/` (append-only manifest, junk
screening, 25s pacing). Collision checks for the leading candidate run
inside the same pass. Verdict + scoring matrix appended after evidence
lands. Registry row proposed only if the bar (prevalence + money +
incumbent weakness + no unified local-first incumbent) is met.

**Status: COMPLETE — 2026-10-05. 17 search calls (q01–q17, one FAILED
retry q15b thin, one phrasing re-run q07b clean), all raw JSON immutable
in `../raw-search-results/w5cp/`. The empty-title format quirk (V4 flag)
persisted across the entire window; every set was graded from
snippet/URL content per playbook.**

## Findings

**1. Prevalence and money at stake (subscriptions) — VERIFIED, large.**
62% of consumers waste money on unwanted subscriptions; 70%+ keep
paying because they simply forget to cancel (Hiatus survey via
GlobeNewswire, Mar 2016 — dated but directional). 52% enter free
trials intending to cancel; only 38% actually do (Cerillion, May 2022).
Average subscription spend $90/mo = $1,080/yr (Ohio State Univ.
extension citing industry data, Sep 2025); ~23% of US subscribers
spend $100+/mo (Bango via fortunly.com, May 2026). Consumers
underestimate their spend by wide margins (West Monroe series via
substop.io — think-$133-vs-actual shape).

**2. Gift cards — VERIFIED, massive.** $21–23B in unspent gift cards;
47% of US adults hold at least one unused card; average $175–187 per
person (multiple independent hosts: uppermichiganssource Feb 2023,
Yahoo/WBKO Dec 2023, TheStreet Aug 2022). The single largest
quantified "free money decaying" pool found in this pass.

**3. Deferred interest (0% APR cliff) — VERIFIED, sharp.** 80% of
store cards with 0% APR offers carry deferred interest — retroactive
interest on the *original* balance if not paid in full by promo end
(WalletHub 2026 study via CNBC, Dec 2 2025). CFPB has formally
expressed concern about "surprise … high, retroactive interest
charges"; NCLC calls it "the hidden time bomb." This is the most
acute per-event dollar loss in the decay classes.

**4. Documents — qualitative.** Six-month passport validity rule
produces boarding denials at the gate (MSN, Jan 2026); "millions lost
each year by passengers denied boarding" (TripAdvisor air-travel
forum). No hard stat found; class kept as supported but unquantified.

**5. Domains — qualitative, vivid.** Renewal-loss horror genre (HN
"GoDaddy Stole My Domain" Jan 2024; UKBusinessForums "SO MAD. Lost my
.com"; squatters aggregate expiring-domain WHOIS lists; ransom
reports). SMB-side consumer-ish; class kept.

**6. Behavior proof — the strongest psychological evidence.**
Food-expiry tracking apps are a thriving consumer category: NoWaste
(barcode scan, expiry alerts), Fango (fridge/freezer/pantry filters),
Controle de Validade, Expiry Date Alert, multiple Play Store listings
(q10, q14). Consumers demonstrably install and use *expiry trackers
for food*. The money-dates equivalent (where the stakes are dollars,
not vegetables) is fragmented across single-purpose apps.

**7. Incumbent weakness — VERIFIED.** Rocket Money (the category
leader, ex-Truebill) requires bank linkage (Reuters confirms the
account-linking model) and attracts complaints of "tricking users to
sign up for premium services or paying high bill negotiation fees"
(eonvpn summary of the state-complaint record, Jun 2026). The
no-bank-link niche validates the trust barrier: Subby markets "No
bank login. No account. Nothing to connect" (Play Store listing);
ReSubs markets "privacy-first … never connects to your bank" (Apr
2026). SubTracker's free plan "puts reminders behind Plus" (Jul
2026) — the category paywalls the core value. Unroll.me's data-sale
scandal legacy keeps the privacy story commercially resonant.

**8. Competitive field (the wedge is real).** All found trackers are
(a) **subscription-only** (Subby, ReSubs incl. "30+ step-by-step
cancel guides", Finny, Bobby, SubTracky, PocketSubs Jul 2026,
SubTracker) or (b) **single-class** (VoucherCue gift cards, iOS;
"Warranty Tracker & Receipt" iOS Aug 2026) — and (c) essentially all
**store-distributed mobile apps**. No product found that unifies
trials + renewals + warranties + gift cards + deferred-interest
windows + documents + domains, and none distributed as an
installable web PWA with local-first storage and a loss-aversion
("$ at risk") framing. A hobbyist-built offline bills-only due-date
tracker (technofino.in, Mar 28 2026) independently confirms the
demand signal. The 0-star "unlapse" GitHub repos (Go, Jun 2026;
Python, Jul 2026) are two more independent concept-validations —
hobby-scale, not products.

**9. Platform-absorption risk — PARTIALLY VERIFIED, bounded.**
Apple's OS-level subscription machinery (renewal receipts, Settings
subscription management) covers **App-Store-billed subscriptions
only** (q15b: Apple support page; the existence of thriving
third-party trackers incl. PocketSubs despite 15+ years of OS
features is itself the evidence). Direct-billed services (Netflix,
gym, newspapers, insurance), gift cards, warranties, APR windows,
IDs and domains are structurally outside it. Risk logged, bounded.

**10. Naming kills (documented for the record).** "ExpiryRadar" —
taken (Play Store "Expiry Radar" 倒计雷达, com.wilson.expradar).
"DueDay" — taken (Play Store Subscription Tracker: DueDay; App Store
Bill Reminder: DueDay Tracker). "Unlapse" — concept-claimed on
GitHub. "NeverDue" — 21 GitHub repos. "Vigilo" — 224 GitHub repos.
**"PocketVeto"** — clean: 0 GitHub name-collisions, no app-store or
web collision surfaced (q17).

## Scoring matrix

| # | Candidate | Prevalence | $ at stake | Use frequency | Incumbent weakness | Buildability | Psych hook | Publishability | Total /35 |
|---|-----------|-----------|-----------|---------------|--------------------|--------------|-----------|----------------|-----------|
| A | **Unified money-dates radar** | 5 | 5 | 4 | 4 | 5 | 5 | 5 | **33** |
| B | Warranty vault standalone | 3 | 3 | 2 | 4 | 4 | 3 | 4 | 23 |
| C | Gift-card value tracker | 4 | 3 | 2 | 4 | 4 | 4 | 4 | 25 |
| D | Freelancer late-payment chaser | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 19 |
| E | Family document/emergency vault | 3 | 2 | 1 | 3 | 3 | 2 | 3 | 17 |
| F | Meal planner + fridge inventory | 5 | 2 | 5 | 1 | 2 | 3 | 3 | 21 |
| G | Photo dedup/organizer | 4 | 2 | 3 | 1 | 1 | 3 | 2 | 16 |

## Verdict

**BUILD candidate A, named PocketVeto.** The hypothesis survived every
attack this pass could mount: prevalence is mass-market (47% of US
adults on gift cards alone; effectively all subscription-holders on
renewals), the money is quantified ($21–23B gift cards, $1,080/yr avg
sub spend, 80%-of-store-cards deferred-interest clawback), the
incumbent field is bank-linked-and-fee'd or fragmented single-class
mobile apps, the behavior precedent (food-expiry apps) proves
consumers adopt this exact psychological shape, and the platform
absorption is bounded to platform-billed subscriptions.

**Differentiators against every named competitor:**
1. *Unified*: trials, renewals, warranties, gift cards, deferred-APR
   windows, documents, domains, custom — one radar, one "$ at risk"
   ticker. Every incumbent is subscriptions-only or single-class.
2. *Local-first, no account, no bank link, works offline* — the trust
   story the incumbents' complaint records make resonant.
3. *Web PWA* — installable on any OS, no store gatekeeper, no 30% tax,
   OSS-inspectable (MIT) — vs a field of store-distributed closed
   apps.
4. *Loss-aversion-native UI*: live "$ at risk" sum + countdown radar;
   competitors market features, not the loss.
5. *Fully free* — vs SubTracker paywalling reminders behind Plus.

**Honest limits (stated up front in the product):** web notifications
fire while the PWA/service worker can run; no server push in v1 (an
optional self-hostable push service is the roadmap item). Receipt
photo capture is out of scope for v1. Warranty-unclaimed dollars:
NOT asserted (q06 drifted to unclaimed-funds noise; no stat verified).

**Status: PRODUCTIZED same day — [pocketveto](https://github.com/srivtx/pocketveto)
(v1.0.0, MIT, local-first PWA).**
