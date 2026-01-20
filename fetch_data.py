#!/usr/bin/env python3
"""
Fetch San Francisco Police incident data and detect enforcement patterns.
Focuses on daily arrest-related incidents by category.
"""

import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict
import statistics

# SF Police Department Incident Reports API
API_ENDPOINT = "https://data.sfgov.org/resource/wg3w-h783.json"

# Arrest-related incident categories (typically involve custody)
ARREST_CATEGORIES = [
    "Drug Offense",
    "Warrant",
    "Assault",
    "Robbery",
    "Burglary",
    "Motor Vehicle Theft",
    "Weapons Offense",
    "Disorderly Conduct",
    "Prostitution",
    "Suspicious Occ"
]

def fetch_incidents(days_back=365):
    """Fetch incident data for the last N days."""
    start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%dT00:00:00")

    print(f"Fetching incidents since {start_date}...")

    # Fetch data with pagination
    limit = 50000
    params = {
        "$where": f"incident_date >= '{start_date}'",
        "$limit": limit,
        "$order": "incident_date ASC"
    }

    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    incidents = response.json()
    print(f"Fetched {len(incidents)} incidents")

    return incidents

def aggregate_daily(incidents):
    """Aggregate incidents by date and category."""
    daily_counts = defaultdict(lambda: defaultdict(int))

    for incident in incidents:
        date = incident.get('incident_date', '').split('T')[0]
        category = incident.get('incident_category', 'Unknown')

        if date and category:
            daily_counts[date][category] += 1
            daily_counts[date]['TOTAL'] += 1

    return daily_counts

def calculate_baseline(daily_counts, category, days=90):
    """Calculate baseline (mean) for a category over last N days."""
    recent_dates = sorted(daily_counts.keys())[-days:]
    counts = [daily_counts[date].get(category, 0) for date in recent_dates]

    if not counts:
        return 0, 0

    mean = statistics.mean(counts)
    stdev = statistics.stdev(counts) if len(counts) > 1 else 0

    return mean, stdev

def detect_anomalies(daily_counts, threshold_sigma=2.0):
    """Detect days where categories spike above baseline."""
    anomalies = []

    dates = sorted(daily_counts.keys())
    if len(dates) < 100:
        print("Not enough data for anomaly detection")
        return anomalies

    # Check last 7 days for anomalies
    recent_dates = dates[-7:]

    for date in recent_dates:
        day_data = daily_counts[date]

        for category in ARREST_CATEGORIES:
            count = day_data.get(category, 0)
            if count == 0:
                continue

            mean, stdev = calculate_baseline(daily_counts, category, days=90)

            if stdev > 0:
                z_score = (count - mean) / stdev

                if z_score > threshold_sigma:
                    anomalies.append({
                        'date': date,
                        'category': category,
                        'count': count,
                        'baseline_mean': round(mean, 1),
                        'z_score': round(z_score, 2),
                        'percent_above': round(((count - mean) / mean * 100), 1)
                    })

    return sorted(anomalies, key=lambda x: -x['z_score'])

def generate_summary(daily_counts, anomalies):
    """Generate human-readable summary."""
    dates = sorted(daily_counts.keys())
    latest_date = dates[-1] if dates else "Unknown"

    summary = {
        'last_updated': datetime.now().isoformat(),
        'data_range': {
            'start': dates[0] if dates else None,
            'end': latest_date,
            'total_days': len(dates)
        },
        'latest_day': {
            'date': latest_date,
            'total_incidents': daily_counts[latest_date].get('TOTAL', 0),
            'by_category': dict(daily_counts[latest_date])
        },
        'current_anomalies': anomalies[:10],  # Top 10
        'alert_status': 'SURGE DETECTED' if len(anomalies) > 0 else 'NORMAL'
    }

    return summary

def main():
    print("SF Crackdown Radar - Data Fetcher")
    print("=" * 50)

    # Fetch data
    incidents = fetch_incidents(days_back=365)

    # Aggregate by day and category
    daily_counts = aggregate_daily(incidents)

    # Detect anomalies
    anomalies = detect_anomalies(daily_counts, threshold_sigma=2.0)

    # Generate summary
    summary = generate_summary(daily_counts, anomalies)

    # Save raw daily data
    with open('data/daily_counts.json', 'w') as f:
        json.dump(dict(daily_counts), f, indent=2)

    # Save summary
    with open('data/summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Data saved to data/ directory")
    print(f"  - Total days: {len(daily_counts)}")
    print(f"  - Latest date: {summary['data_range']['end']}")
    print(f"  - Anomalies detected: {len(anomalies)}")

    if anomalies:
        print(f"\n⚠️  RECENT SURGES:")
        for anom in anomalies[:5]:
            print(f"  {anom['date']}: {anom['category']}")
            print(f"    {anom['count']} incidents ({anom['percent_above']}% above baseline, {anom['z_score']}σ)")

if __name__ == "__main__":
    main()
