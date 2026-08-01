import os
import re

try:
    import docx
except ImportError:
    print("Fehler: Bitte installiere zuerst 'python-docx' via: pip install python-docx")
    exit(1)

# Konfiguration
source_dir = "import_text"
repo_dir = "."
target_file_name = "index.md"

# Manuelle Ausnahmen für Schreibweisen und Abkürzungen
MANUAL_MAPPING = {
    "goerke-erich": ["goercke-erich"],
    "grotkopp-hans": ["grotkopp-h"],
    "popp-johann-hinrich": ["popp-h"],
    # Sammel-Biografien werden hier direkt auf beide Zielordner aufgeteilt:
    "petersen-fritz-und-heinz": ["petersen-fritz", "petersen-heinz"],
    "hass-helmut-und-johannes": ["hass-helmut", "hass-johannes"],
    "bast-walter-und-friedrich": ["bast-walter", "bast-friedrich"]
}

def name_to_slug(filename):
    name, _ = os.path.splitext(filename)
    name = name.lower().strip()
    
    # Störende Unterstriche und doppelte Leerzeichen entfernen
    name = name.replace("_", "").replace("  ", " ")
    name = name.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    
    if "," in name:
        parts = [p.strip() for p in name.split(",")]
        if len(parts) == 2:
            return f"{parts[0]}-{parts[1].replace(' ', '-')}"
            
    parts = name.split()
    if len(parts) >= 2:
        nachname = parts[-1]
        vorname = "-".join(parts[:-1])
        return f"{nachname}-{vorname}"
        
    return re.sub(r'[^a-z0-9-]', '', name)

if not os.path.exists(source_dir):
    print(f"Fehler: Der Ordner '{source_dir}' existiert nicht.")
    exit(1)

print("Starte optimierten Word-Text-Import (inkl. Multicopy für Geschwister)...\n")
success_count = 0
skipped_count = 0

for filename in sorted(os.listdir(source_dir)):
    if filename.startswith("~$") or not filename.endswith(".docx"):
        continue
        
    raw_slug = name_to_slug(filename)
    
    # Bestimme die Zielordner (entweder aus dem Mapping oder den Standard-Slug)
    target_slugs = MANUAL_MAPPING.get(raw_slug, [raw_slug])
    
    source_path = os.path.join(source_dir, filename)
    
    try:
        # Word-Dokument einmalig einlesen
        doc = docx.Document(source_path)
        content = "\n".join([para.text for para in doc.paragraphs])
        
        file_saved = False
        for slug in target_slugs:
            target_folder = os.path.join(repo_dir, slug)
            
            if os.path.isdir(target_folder):
                target_path = os.path.join(target_folder, target_file_name)
                with open(target_path, "w", encoding="utf-8") as dest:
                    dest.write(content)
                print(f"✓ {filename} -> {target_folder}/{target_file_name}")
                success_count += 1
                file_saved = True
            else:
                print(f"⚠ Ordner existiert nicht: {target_folder} (aus Slug: {slug})")
                
        if not file_saved:
            skipped_count += 1
            
    except Exception as e:
        print(f"✗ Fehler bei Datei {filename}: {e}")
        skipped_count += 1

print(f"\nFertig! {success_count} Zieldateien geschrieben. {skipped_count} Dateien komplett übersprungen.")
