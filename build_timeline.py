import os
import re
from pathlib import Path
from datetime import datetime

MONTHS = {
    'januar': 1, 'februar': 2, 'märz': 3, 'april': 4, 'mai': 5, 'juni': 6,
    'juli': 7, 'august': 8, 'september': 9, 'oktober': 10, 'november': 11, 'dezember': 12
}

events = []

pattern = re.compile(
    r'(?:ist\s+)?am\s+(\d{1,2})\.\s*([A-Za-zäöüÄÖÜ]+|\d{1,2})\.\s*(\d{4})\s+(?:in|bei|an|auf)\s+([^.\n]+)',
    re.IGNORECASE
)

for md_file in Path('.').rglob('*.md'):
    # Hauptseiten und Zeitachsen-Ordner auslassen
    if md_file.name in ['index.md', 'README.md'] and md_file.parent in [Path('.'), Path('zeitachse')]:
        continue
        
    content = md_file.read_text(encoding='utf-8')
    
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    name = title_match.group(1).strip() if title_match else md_file.parent.name
    
    # Relative Verlinkung aus dem Unterordner /zeitachse/ heraus
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
                'date_str': f"{day:02d}.{month:02d}.{year}",
                'name': name,
                'location': location,
                'link': rel_link
            })
        except ValueError:
            continue

events.sort(key=lambda x: x['date'])

md_output = """---
layout: default
title: Zeitachse
permalink: /zeitachse/
nav_exclude: true
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

# 1. Unterordner zeitachse/ anlegen und index.md schreiben
out_dir = Path('zeitachse')
out_dir.mkdir(exist_ok=True)
(out_dir / 'index.md').write_text(md_output, encoding='utf-8')
print(f"Zeitachse unter zeitachse/index.md mit {len(events)} Einträgen generiert.")

# 2. Alte zeitachse.md im Hauptverzeichnis aufräumen, falls vorhanden
old_file = Path('zeitachse.md')
if old_file.exists():
    old_file.unlink()

# 3. Link auf der Hauptseite (index.md) ergänzen
root_index = Path('index.md')
if root_index.exists():
    root_content = root_index.read_text(encoding='utf-8')
    link_markdown = "[⏱️ Chronologische Zeitachse aller Schicksale anzeigen](zeitachse/)"
    if 'zeitachse' not in root_content.lower():
        root_content += f"\n\n---\n\n{link_markdown}\n"
        root_index.write_text(root_content, encoding='utf-8')
        print("Link zur Zeitachse auf der Hauptseite (index.md) ergänzt.")
