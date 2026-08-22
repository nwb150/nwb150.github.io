import os
import re
from pathlib import Path
from datetime import datetime

# Monate für die Datumsumwandlung
MONTHS = {
    'januar': 1, 'februar': 2, 'märz': 3, 'april': 4, 'mai': 5, 'juni': 6,
    'juli': 7, 'august': 8, 'september': 9, 'oktober': 10, 'november': 11, 'dezember': 12
}

events = []

# Regex sucht nach Mustersätzen wie: "ist am 23.12.1941 in Russland gefallen" oder "am 6. Februar 1945"
pattern = re.compile(
    r'(?:ist\s+)?am\s+(\d{1,2})\.\s*([A-Za-zäöüÄÖÜ]+|\d{1,2})\.\s*(\d{4})\s+(?:in|bei|an|auf)\s+([^.\n]+)',
    re.IGNORECASE
)

for md_file in Path('.').rglob('*.md'):
    if md_file.name in ['index.md', 'zeitachse.md', 'README.md'] and md_file.parent == Path('.'):
        continue
        
    content = md_file.read_text(encoding='utf-8')
    
    # Name aus der H1-Überschrift extrahieren
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    name = title_match.group(1).strip() if title_match else md_file.parent.name
    
    # Relative URL für GitHub Pages / Jekyll bestimmen
    rel_link = f"../{md_file.parent.name}/"
    
    # Datum und Ort finden
    for match in pattern.finditer(content):
        day = int(match.group(1))
        month_raw = match.group(2).lower()
        year = int(match.group(3))
        location = match.group(4).strip()
        
        if month_raw.isdigit():
            month = int(month_raw)
        else:
            month = MONTHS.get(month_raw, 1)
            
        try:
            dt = datetime(year, month, day)
            events.append({
                'date': dt,
                'date_str': f"{day:02d}.{month:02d}.{year}",
                'name': name,
                'location': location,
                'link': rel_link
            })
        except ValueError:
            continue

# Chronologisch sortieren
events.sort(key=lambda x: x['date'])

# Markdown-Inhalt für zeitachse.md generieren
md_output = """---
layout: default
title: Zeitachse
nav_order: 2
---

# Chronologische Zeitachse

Eine zeitliche Übersicht der Gefallenen und Vermissten aus Neuwittenbek.

<div style="border-left: 3px solid #d0d7de; padding-left: 20px; margin-top: 30px;">
"""

for ev in events:
    md_output += f"""
<div style="margin-bottom: 25px; position: relative;">
  <div style="font-weight: bold; color: #57606a; font-size: 0.9em;">{ev['date_str']}</div>
  <div style="font-size: 1.1em; font-weight: 600;">
    <a href="{ev['link']}">{ev['name']}</a>
  </div>
  <div style="color: #24292f;">Gefallen/Vermisst in: <em>{ev['location']}</em></div>
</div>
"""

md_output += "\n</div>\n"

Path('zeitachse.md').write_text(md_output, encoding='utf-8')
print(f"Zeitachse erfolgreich mit {len(events)} Einträgen generiert.")
