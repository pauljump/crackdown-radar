# 🚨 SF Crackdown Radar

**IDEA-163** | Status: App | **MVP Live**

Near real-time arrest tracker that detects enforcement surges to identify when San Francisco is cracking down on specific crimes.

## Live Dashboard

View at: `https://pauljump.github.io/crackdown-radar/`

## What It Does

- **Tracks daily arrest-related incidents** from SF Police Department
- **Detects statistical anomalies** - days where specific crime categories spike above normal
- **Visualizes trends** - 90-day time series of enforcement patterns
- **Highlights surges** - alerts when crackdown patterns emerge

## Quick Start

**Update data and view dashboard:**

```bash
# Install dependencies
pip install -r requirements.txt

# Fetch latest data
python3 fetch_data.py

# View locally
python3 -m http.server 8000
# Open http://localhost:8000
```

## How It Works

**Data Source:** San Francisco Police Department Incident Reports via [DataSF](https://data.sfgov.org/)

**Anomaly Detection:**
- Calculates 90-day baseline (mean) for each crime category
- Detects days where count is >2σ above baseline
- Highlights as "surge" or "crackdown"

**Focus Categories:**
- Drug Offense
- Warrant
- Assault
- Robbery
- Burglary
- Motor Vehicle Theft
- Weapons Offense
- Disorderly Conduct

## Deploy to GitHub Pages

```bash
git add .
git commit -m "Update data"
git push

# Enable GitHub Pages:
# Settings → Pages → Source: main branch, root directory
```

## Project Files

- `fetch_data.py` - Data fetcher with anomaly detection
- `index.html` - Dashboard visualization
- `data/` - Generated data files (daily_counts.json, summary.json)

## Links

- [Full Idea Card](./IDEA-CARD.md)
- [Working Guide](./.idea-factory/working-guide.md)

---

🤖 Generated with [Idea Factory](https://github.com/pauljump/idea_factory)
