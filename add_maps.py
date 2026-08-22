#!/usr/bin/env python3
from pathlib import Path
import urllib.parse

# Zuordnung der Unterordner zu Todesort, Suchbegriff für Google und Zoomstufe
LOCATION_MAP = {
    "bast-walter": ("Frankreich", "Frankreich", 5),
    "behrend-erwin": ("Frankreich", "Frankreich", 5),
    "frohreich-arthur": ("Italien", "Italien", 5),
    "galinsky-alfred": ("Russland", "Russland", 2),
    "galinsky-max": ("Russland", "Russland", 2),
    "goercke-erich": ("Russland", "Russland", 2),
    "gosch-max": ("Halberstadt", "Halberstadt, Deutschland", 7),
    "grotkopp-hans": ("Russland", "Russland", 2),
    "hansen-kurt": ("Russland", "Russland", 2),
    "hass-helmut": ("Russland", "Russland", 2),
    "hass-johannes": ("Westpreußen", "Westpreußen", 5),
    "huelle-erich": ("Russland", "Russland", 2),
    "jensen-alfred": ("Italien", "Italien", 5),
    "joehnk-otto": ("Nikopol", "Nikopol, Ukraine", 6),
    "joehnk-robert": ("Russland", "Russland", 2),
    "joehnk-willy": ("Polen", "Polen", 5),
    "johst-wilhelm": ("Lommel (Belgien)", "Lommel, Belgien", 6),
    "klein-kurt": ("Ostpreußen", "Ostpreußen", 5),
    "kuest-fritz": ("Bayern", "Bayern, Deutschland", 6),
    "marxen-friedrich": ("Italien", "Italien", 5),
    "marxen-johannes": ("Russland", "Russland", 2),
    "paetow-hans": ("Russland", "Russland", 2),
    "petersen-fritz": ("Russland", "Russland", 2),
    "petersen-heinz": ("Ostpreußen", "Ostpreußen", 5),
    "pfahl-bernhard": ("Pommern", "Pommern", 5),
    "pohl-heinz": ("Russland", "Russland", 2),
    "radbruch-otto": ("Russland", "Russland", 2),
    "radbruch-peter": ("Westfalen", "Westfalen, Deutschland", 6),
    "schloesser-heinz": ("auf See (Nordsee)", "Nordsee", 4),
    "schneider-walter": ("Ostpreußen", "Ostpreußen", 5),
    "schoenfeld-walter": ("Hannover", "Hannover, Deutschland", 7),
    "staude-bruno": ("Russland", "Russland", 2),
    "stroeh-heinrich": ("Neuwittenbek", "Neuwittenbek", 9),
}

def generate_map_markdown(display_name, query, zoom):
    encoded_query = urllib.parse.quote(query)
    return f"""

[📍 {display_name} auf Google Maps öffnen](https://www.google.com/maps/search/?api=1&query={encoded_query})

<iframe 
  width="100%" 
  height="300" 
  style="border:0; border-radius: 8px; margin-top: 10px;" 
  loading="lazy" 
  allowfullscreen 
  src="https://maps.google.com/maps?q={encoded_query}&t=&z={zoom}&ie=UTF8&iwloc=&output=embed">
</iframe>
"""

repo_dir = Path(".")

for folder, (display_name, query, zoom) in LOCATION_MAP.items():
    file_path = repo_dir / folder / "index.md"
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
        
        # Prüfen, ob bereits eine Karte vorhanden ist
        if "<iframe" in content or "maps.google.com" in content:
            print(f"⏭ Übersprungen (Karte existiert bereits): {folder}")
            continue
            
        # Karte ganz unten anhängen (unter allen Texten & Bildern)
        map_md = generate_map_markdown(display_name, query, zoom)
        new_content = content.rstrip() + map_md
        
        file_path.write_text(new_content, encoding="utf-8")
        print(f"✔ Karte hinzugefügt: {folder} ({display_name})")
    else:
        print(f"✖ Datei nicht gefunden: {file_path}")
