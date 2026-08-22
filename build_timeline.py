import os
import re
from pathlib import Path
from datetime import datetime
from collections import Counter

MONTHS = {
    'januar': 1, 'februar': 2, 'märz': 3, 'april': 4, 'mai': 5, 'juni': 6,
    'juli': 7, 'august': 8, 'september': 9, 'oktober': 10, 'november': 11, 'dezember': 12
}

MONTH_NAMES = ["", "Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]

events = []

pattern = re.compile(
    r'(?:ist\s+)?am\s+(\d{1,2})\.\s*([A-Za-zäöüÄÖÜ]+|\d{1,2})\.\s*(\d{4})\s+(?:in|bei|an|auf)\s+([^.\n]+)',
    re.IGNORECASE
)

for md_file in Path('.').rglob('*.md'):
    if md_file.name in ['index.md', 'README.md'] and md_file.parent in [Path('.'), Path('zeitachse')]:
        continue
        
    content = md_file.read_text(encoding='utf-8')
    
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    name = title_match.group(1).strip() if title_match else md_file.parent.name
    
    rel_link = f"../{md_file.parent.name}/"
    
    for match in pattern.finditer(content):
        day = int(match.group(1))
        month_raw = match.group(2).lower()
        year = int(match.group(3))
        location = match.group(4).strip()
        
        month = int(month_raw) if month_raw.isdigit() else MONTHS.get(month_raw, 1)
            
        try:
            dt = datetime(year, month, day)
            events.append({
                'date': dt,
                'year': year,
                'month': month,
                'date_str': f"{day:02d}.{month:02d}.{year}",
                'name': name,
                'location': location,
                'link': rel_link
            })
        except ValueError:
            continue

events.sort(key=lambda x: x['date'])

year_counts = Counter(ev['year'] for ev in events)
max_year_count = max(year_counts.values()) if year_counts else 1
month_counts = Counter((ev['year'], ev['month']) for ev in events)

md_output = """---
layout: default
title: Zeitachse
permalink: /zeitachse/
nav_exclude: true
---

# Chronologische Zeitachse (Entwurf)

<style>
.density-chart {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  height: 140px;
  margin: 20px 0 30px 0;
  padding: 15px;
  background: #f6f8fa;
  border-radius: 8px;
  border: 1px solid #d0d7de;
}
.density-bar-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  justify-content: flex-end;
}
.density-bar {
  width: 100%;
  max-width: 32px;
  background: linear-gradient(180deg, #cf222e 0%, #8c1d18 100%);
  border-radius: 4px 4px 0 0;
  min-height: 4px;
}
.density-label {
  font-size: 0.8em;
  color: #57606a;
  margin-top: 6px;
  font-weight: 600;
}
.density-val {
  font-size: 0.8em;
  font-weight: bold;
  color: #cf222e;
  margin-bottom: 3px;
}
.timeline-container {
  position: relative;
  padding-left: 22px;
  border-left: 3px solid #d0d7de;
  margin: 20px 0 40px 10px;
}
.timeline-year-header {
  font-size: 1.2em;
  font-weight: bold;
  color: #1f2328;
  margin: 25px 0 15px -31px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.timeline-year-badge {
  background: #24292f;
  color: #ffffff;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8em;
}
.timeline-month-cluster {
  background: #fff8f0;
  border-left: 4px solid #d97706;
  padding: 6px 10px;
  margin: 12px 0 12px -10px;
  border-radius: 0 6px 6px 0;
  font-size: 0.85em;
  font-weight: bold;
  color: #92400e;
}
.timeline-item {
  position: relative;
  margin-bottom: 16px;
  padding-left: 8px;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -29px;
  top: 6px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #cf222e;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 2px #d0d7de;
}
.timeline-date {
  font-size: 0.85em;
  font-weight: bold;
  color: #57606a;
}
.timeline-title {
  font-size: 1.05em;
  font-weight: 600;
}
.timeline-location {
  font-size: 0.9em;
  color: #24292f;
}
</style>

## Häufigkeits-Übersicht nach Jahren

<div class="density-chart">
"""

years = sorted(list(set(ev['year'] for ev in events))) if events else [1939, 1940, 1941, 1942, 1943, 1944, 1945]
min_yr = min(years, default=1939)
max_yr = max(years, default=1945)

for yr in range(min_yr, max_yr + 1):
    cnt = year_counts[yr]
    pct = int((cnt / max_year_count) * 100) if max_year_count > 0 else 0
    md_output += f"""  <div class="density-bar-container">
    <div class="density-val">{cnt if cnt > 0 else ''}</div>
    <div class="density-bar" style="height: {pct}%;"></div>
    <div class="density-label">{yr}</div>
  </div>
"""

md_output += """</div>

## Vertikaler Zeitstrahl

<div class="timeline-container">
"""

current_year = None
current_month = None

for ev in events:
    if ev['year'] != current_year:
        current_year = ev['year']
        current_month = None
        yr_cnt = year_counts[current_year]
        md_output += f"""
<div class="timeline-year-header">
  <span class="timeline-year-badge">{current_year}</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">({yr_cnt} Schicksale)</span>
</div>
"""
    
    if ev['month'] != current_month:
        current_month = ev['month']
        m_cnt = month_counts[(current_year, current_month)]
        if m_cnt > 1:
            m_name = MONTH_NAMES[current_month]
            md_output += f"""
<div class="timeline-month-cluster">
  ⚡ Häufung: {m_cnt} Schicksale im {m_name} {current_year}
</div>
"""

    md_output += f"""
<div class="timeline-item">
  <div class="timeline-date">{ev['date_str']}</div>
  <div class="timeline-title"><a href="{ev['link']}">{ev['name']}</a></div>
  <div class="timeline-location">Ort: <em>{ev['location']}</em></div>
</div>
"""

md_output += "\n</div>\n"

out_dir = Path('zeitachse')
out_dir.mkdir(exist_ok=True)
(out_dir / 'index.md').write_text(md_output, encoding='utf-8')

print(f"Zeitachse mit Visualisierung unter zeitachse/index.md ({len(events)} Einträge) aktualisiert.")
