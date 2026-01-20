---
id: IDEA-163
collection: concepts
directory: crackdown-radar
title: Crackdown Radar
type: App
status: concept
confidence: Med
one_liner: Near real-time arrest tracker that detects enforcement surges to identify when cities are cracking down on specific crimes
primary_user: Journalists, community advocates, and civil rights organizations
buyer: News organizations, advocacy groups, research institutions
distribution_wedge: Criminal justice reform communities, journalist networks, public data APIs
revenue_model: Freemium API with paid tiers for alerts and advanced analytics
time_to_signal_days: '14'
domain_tags:
- civic-data
- criminal-justice
- public-records
- surveillance
user_tags:
- journalists
- advocates
- researchers
- community-organizers
capability_tags:
- data-aggregation
- pattern-detection
- real-time-monitoring
distribution_tags:
- public-api
- community-driven
risk_tags:
- privacy
- surveillance
provenance:
- field: title
  tag: NEW
  source: User request
  quote: "track arrests in a city like san francisco in near real time with the specific goal of knowing when they are cracking down on crime"
related: []
---

## Core
- Problem (JTBD): Hard to detect when law enforcement is ramping up enforcement on specific crimes, areas, or populations without manually tracking arrest records
- Primary user: Investigative journalists covering criminal justice, community advocates monitoring policing patterns, civil rights organizations
- Buyer / budget owner: News organizations (investigative desks), advocacy nonprofits, academic research institutions
- Why now: Public arrest records increasingly available via open data portals; growing scrutiny of policing patterns post-2020
- Trigger event: User notices anecdotal increase in arrests (e.g., "sweeps" of homeless encampments, drug arrests, protest arrests) and wants to quantify it
- Frequency: Continuous monitoring with weekly/monthly pattern analysis

## Solution
- What it is (2–6 bullets):
  - Real-time ingestion of arrest records from police department APIs and public records portals
  - Time-series analysis to detect statistical anomalies (sudden spikes in arrest rates by crime type, location, demographics)
  - Dashboard showing enforcement trends: which crimes are being prioritized, where, and when
  - Alert system for significant changes (e.g., "DUI arrests up 300% in Mission District this week")
  - Historical comparison: "This month's vagrancy arrests vs. same month last year"
  - Geographic heatmaps showing enforcement concentration

- Key workflow (5–9 steps):
  1. Connect to city police department open data API (or scrape booking logs)
  2. Normalize arrest records: extract charge type, location, timestamp, demographics
  3. Store in time-series database for historical analysis
  4. Run statistical analysis to detect outliers: Z-scores, rate-of-change, moving averages
  5. Flag anomalies: "Disorderly conduct arrests 5σ above baseline"
  6. Generate alerts and publish to dashboard
  7. Provide drill-down: which precincts, which charges, which times of day
  8. Export reports for journalists/advocates with evidence

- Inputs needed:
  - Police department arrest/booking APIs (San Francisco, NYC, Chicago, LA, etc.)
  - Crime category taxonomies (map charges to categories like "drug possession," "quality of life," "violent crime")
  - Geographic boundaries (neighborhoods, precincts, supervisor districts)

- Outputs produced:
  - Real-time dashboard showing enforcement trends
  - Alert notifications when patterns change significantly
  - CSV/JSON exports for analysis
  - Shareable reports: "SF drug arrests doubled in Tenderloin in March 2026"

## Value + Differentiation
- Measurable value created:
  - Journalists can substantiate "crackdown" stories with data instead of anecdotes
  - Advocates can challenge enforcement priorities with evidence
  - Researchers get longitudinal enforcement data for studying policing patterns
  - Community members understand what's actually being enforced vs. rhetoric

- Status quo / substitutes:
  - Manually requesting arrest records via public records requests (slow, incomplete)
  - Spotty news coverage based on anecdotes
  - Academic studies published years after the fact
  - Police department press releases (selective, PR-driven)

- Differentiation:
  - Only tool focused on *change detection* rather than raw arrest counts
  - Real-time (daily/hourly updates) vs. quarterly/annual reports
  - Multi-city comparison: "How does SF's enforcement compare to Oakland, LA, Seattle?"
  - Open API for community tools and apps

- Moat hypothesis:
  - Data aggregation moat: Building 50+ city integrations takes time
  - Statistical methodology: Proprietary algorithms for detecting meaningful patterns vs. noise
  - Historical dataset becomes more valuable over time (3+ years of data)

## Distribution
- Distribution wedge:
  - Criminal justice reform networks (Twitter/X, Substack)
  - Journalist communities (IRE, Investigative Reporters & Editors)
  - Public API with docs → developer ecosystem builds on top
  - Prove it with high-profile examples: "We detected SF's Tenderloin crackdown 3 weeks before media coverage"

- Activation moment:
  - Journalist sees alert about arrest surge, publishes story attributing data to Crackdown Radar
  - Advocate uses data in city council testimony: "Arrests are up 400%, here's the proof"

- Retention hook:
  - Historical data gets richer over time (seasonal patterns, election cycles)
  - API integrations make it infrastructure for newsrooms/nonprofits

- Sales motion:
  - Freemium: Public dashboard free, API free for low volume
  - Paid: Advanced alerts, historical exports, multi-city access, white-label dashboards
  - Enterprise: Custom integrations for newsrooms/research institutions

## Monetization + Unit Economics
- Revenue model:
  - Freemium API:
    - Free tier: 100 API calls/day, access to last 90 days of data
    - Pro tier: $99/mo for unlimited calls, full historical data, custom alerts
    - Enterprise: $999/mo for white-label, multi-city bundles, SLA
  - Grant funding from criminal justice reform foundations
  - Sponsored research reports

- Pricing anchor:
  - Comparable to data APIs like Socrata, Census API, PACER access: $99-999/mo for institutions

- Main cost drivers:
  - Server costs for ingestion/storage (~$200/mo for 10 cities)
  - Alert infrastructure (email/SMS) (~$50/mo)
  - Engineering time to add new cities (~8 hours per city)

- Margin risks:
  - Cities could shut down public APIs or add rate limits
  - Some cities charge fees for bulk records access
  - Legal challenges from police departments

## Feasibility + Dependencies
- Build complexity:
  - Medium: API integration layer + time-series DB + anomaly detection + dashboard
  - MVP: Single city (SF) with basic spike detection - 2 weeks
  - Production: 10 cities with full analytics - 6 weeks

- Key dependencies:
  - San Francisco Police Department arrest data API
  - Open data portals: Socrata, ArcGIS, custom city APIs
  - Time-series database (InfluxDB or TimescaleDB)
  - Statistical libraries for anomaly detection (Python scipy, statsmodels)
  - Front-end dashboard (React, Chart.js or D3.js)

- How to run/demo:
  - Connect to SF open data API, ingest last 12 months of arrests
  - Run anomaly detection: "Drug arrests spiked 250% week of March 15-22"
  - Show dashboard with heatmap and timeline
  - Publish example report: "SF Quality of Life Arrests Analysis Q1 2026"

- Critical path milestones:
  - Phase 1 (2 weeks): Single-city MVP with SF arrest data + basic anomaly detection
  - Phase 2 (4 weeks): Multi-city support (add LA, NYC, Chicago, Seattle)
  - Phase 3 (8 weeks): Public API + alert system + historical exports
  - Phase 4 (12 weeks): Advanced analytics: demographic breakdowns, geographic clustering, predictive patterns

## Risk / Compliance / Trust
- Trust/fraud/dispute risks:
  - Data accuracy: Arrest records may have errors, duplicates, or lag
  - Statistical false positives: Random variation flagged as "crackdown"
  - Must clearly communicate confidence levels and limitations

- Regulatory/compliance risks:
  - Some states restrict publishing arrest records (expungement laws, juvenile records)
  - FOIA exemptions may apply to certain records
  - Must respect privacy: no PII beyond what's in public records

- Platform risks:
  - Cities could shut down or restrict public data APIs
  - Police departments could pressure cities to limit access
  - Political backlash: "This tool helps criminals avoid enforcement"

- Kill criteria:
  - Major city (SF, LA, NYC) shuts down arrest data APIs
  - Legal action from police unions/departments
  - Statistical methodology proven unreliable (too many false positives)
  - No media/advocacy uptake after 6 months

## Fastest path to truth
- Riskiest assumption:
  - Journalists/advocates actually need real-time data vs. quarterly reports
  - Anomaly detection algorithm can separate signal (crackdowns) from noise (random variance)

- MVP test (<=14 days):
  1. Build SF-only prototype with 12 months of historical arrest data
  2. Implement basic spike detection (moving average + Z-score)
  3. Identify 3-5 "crackdown" events in last year
  4. Cross-reference with news coverage: did media report these as enforcement surges?
  5. Share prototype with 5 investigative journalists → ask: "Is this useful?"

- 3 experiments with success metrics:
  1. **Data quality test**: Ingest 12 months of SF arrests, verify against manual review of 100 random records (target: 95%+ accuracy)
  2. **Anomaly detection validation**: Identify historical "crackdowns" and cross-check with news archives (target: 80%+ match with reported enforcement surges)
  3. **User validation**: Demo to 10 journalists/advocates (target: 5+ say "I would use this weekly")

- time_to_signal_days: 14 (Two weeks to validate data quality + anomaly detection + user interest)

## Open questions
1. Which cities have the best open data APIs for arrest records? (SF, NYC, Chicago, Seattle?)
2. What statistical threshold for "crackdown" minimizes false positives? (2σ, 3σ, 5σ?)
3. Should demographic breakdowns be included? (Race, age, gender - sensitive but important for civil rights monitoring)
4. How to handle cities without APIs? (Web scraping booking logs, FOIA requests?)
5. What's the right update frequency? (Hourly, daily, weekly?)
6. Should we track *stops* and *citations* in addition to arrests? (Broader enforcement picture)
7. How to communicate uncertainty and limitations to non-technical users?
8. Is there commercial demand beyond journalism/advocacy? (Insurance, real estate, legal services?)
