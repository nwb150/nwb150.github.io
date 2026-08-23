import os
import re
from pathlib import Path

# Ordner, die nicht als Biografie-Ordner behandelt werden sollen
EXCLUDE_DIRS = {'.git', '_layouts', '_includes', '_site', 'zeitachse'}

def parse_biography_details(content):
    """Extrahiert bekannte Metadaten aus dem Fliesstext und den Links."""
    
    # 1. Titel finden (# Name)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # 2. Sterbedatum finden (Format DD.MM.YYYY)
    date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', content)
    death_date = date_match.group(1) if date_match else ""

    # 3. Ortsbezeichnung aus Google-Maps-Link ermitteln
    location = ""
    loc_match = re.search(r'\[📍\s*(.*?)\s*auf Google Maps', content)
    if loc_match:
        location = loc_match.group(1).strip()

    # 4. Koordinaten (lat, lng) aus Iframe oder Maps-URL extrahieren (falls numerisch vorhanden)
    lat, lng = "", ""
    coords_match = re.search(r'(?:q=|query=)(-?\d+\.\d+),\s*(-?\d+\.\d+)', content)
    if coords_match:
        lat = coords_match.group(1)
        lng = coords_match.group(2)

    return {
        "title": title,
        "death_date": death_date,
        "location": location,
        "lat": lat,
        "lng": lng
    }

def process_markdown_files():
    root_dir = Path(".")
    updated_count = 0

    for file_path in root_dir.glob("**/index.md"):
        # Hauptseite (root index.md) und ausgeschlossene Ordner überspringen
        if file_path.parent == root_dir or file_path.parent.name in EXCLUDE_DIRS:
            continue

        content = file_path.read_text(encoding="utf-8")

        # Bestehendes Frontmatter entfernen, um den reinen Body zu haben
        body = re.sub(r'^---[\s\S]*?---\n*', '', content).strip()

        # Metadaten aus dem Dateiinhalt auslesen
        data = parse_biography_details(body)

        # Neues YAML-Frontmatter aufbauen
        fm_lines = ["---", "nav_exclude: true"]
        if data["title"]:
            fm_lines.append(f'title: "{data["title"]}"')
        if data["lat"]:
            fm_lines.append(f'lat: {data["lat"]}')
        if data["lng"]:
            fm_lines.append(f'lng: {data["lng"]}')
        if data["death_date"]:
            fm_lines.append(f'death_date: "{data["death_date"]}"')
        if data["location"]:
            fm_lines.append(f'location: "{data["location"]}"')
        fm_lines.append("---\n")

        new_frontmatter = "\n".join(fm_lines)
        
        # Datei neu zusammensetzen und speichern (Inhalt bleibt 1:1 unverändert)
        new_content = f"{new_frontmatter}\n{body}\n"
        file_path.write_text(new_content, encoding="utf-8")
        
        print(f"✓ Frontmatter erweitert: {file_path}")
        updated_count += 1

    print(f"\nFertig! {updated_count} Biografie-Dateien wurden aktualisiert.")

if __name__ == "__main__":
    process_markdown_files()
