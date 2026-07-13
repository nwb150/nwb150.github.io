import os

# Konfiguration
target_file = "index.md"
ignored_folders = {".git", ".venv", "qrcodes", "import_text", "__pycache__", "Bilder", "_includes", ".github"}

# Marker für den dynamischen Bereich
start_marker = "<!-- SOLDIER_LIST_START -->"
end_marker = "<!-- SOLDIER_LIST_END -->"

# 1. Existierenden Text einlesen und manuelle Texte schützen
header_text = ""
footer_text = ""

if os.path.exists(target_file) and os.path.getsize(target_file) > 0:
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if start_marker in content and end_marker in content:
        # Perfekt: Marker existieren bereits. Wir isolieren Kopf und Fuß.
        header_text = content.split(start_marker)[0].strip() + "\n\n" + start_marker + "\n"
        footer_text = "\n\n" + end_marker + "\n\n" + content.split(end_marker)[1].strip() + "\n"
    else:
        # Erster Durchlauf: Wir trennen den Text vor dem ersten Bullet-Point
        lines = content.splitlines()
        header_lines = []
        for line in lines:
            if line.strip().startswith("*"):
                break
            header_lines.append(line)
        
        header_text = "\n".join(header_lines).strip() + "\n\n" + start_marker + "\n"
        footer_text = "\n\n" + end_marker + "\n\n"
else:
    # Absoluter Notfall-Fallback mit dem aktuellen Plakat-Text
    header_text = f"""# Die sprechenden Steine von Neuwittenbek
### 150 Jahre Geschichte • Erinnerung lebendig halten

Hinter den Mauern und Wegen unseres Dorfes verbergen sich die Lebenswege und Schicksale vieler Generationen. Dieses Projekt bringt die Gedenksteine Neuwittenbeks zum Sprechen. Es lädt dich dazu ein, innezuhalten und etwas mehr über das Leben, das Wirken und die Schicksale unserer ehemaligen Nachbarn, Väter, Brüder, Söhne und Ehemänner zu erfahren, die durch die Kriege aus unserer Mitte gerissen wurden.

### Digitale Gesamtübersicht der Biografien:

{start_marker}
"""
    footer_text = f"""\n\n{end_marker}

## Erinnerungen lebendig halten – Macht mit!
Manche der Erinnerungen rund um diese Gedenksteine leben heute nur noch in den Köpfen derer, die sie miterlebt haben oder denen sie weitererzählt wurden. Wir möchten verhindern, dass diese wertvollen, aber langsam verblassenden Erinnerungen im Laufe der Zeit verloren gehen. Ein Anfang ist gemacht, mit der großen Hilfe von Frau Tams. Habt ihr noch persönliche Anekdoten, historische Details, alte Dokumente oder Fotos? Wer Erinnerungen teilen kann und möchte, meldet sich bitte direkt bei uns.
"""

print("Lese bestehende index.md ein und schütze manuelle Texte...")

# --- NEU: Impressum-Link und Open-Source Hinweis mit kugelsicherem HTML-Trennstrich ---
impressum_text = "\n\n<hr>\n\n<p>Ein rein ehrenamtliches, nicht-kommerzielles Open-Source-Projekt der Gemeinde Neuwittenbek.</p>\n<p><a href=\"impressum.html\">Impressum & Datenschutz</a></p>\n"
if "Ein rein ehrenamtliches" not in footer_text:
    footer_text = footer_text.rstrip() + impressum_text
# -----------------------------------------------------------

# 2. Alle Verzeichnisse auflisten und sortieren
folders = sorted(os.listdir("."))
markdown_links = []

for folder in folders:
    if os.path.isdir(folder) and folder not in ignored_folders:
        parts = folder.split("-")
        if len(parts) >= 2:
            nachname = parts[0].capitalize()
            vorname_parts = [p.capitalize() for p in parts[1:]]
            vorname = " ".join(vorname_parts)
            
            if len(vorname) == 1:
                vorname += "."
                
            display_name = f"{vorname} {nachname}"
        else:
            display_name = folder.capitalize()
            
        markdown_links.append(f"* [{display_name}](./{folder}/)")

# 3. Datei sauber zusammenbauen und schreiben
with open(target_file, "w", encoding="utf-8") as f:
    f.write(header_text)
    f.write("\n".join(markdown_links))
    f.write(footer_text)

print(f"✓ {target_file} wurde erfolgreich aktualisiert! Die Liste umfasst jetzt {len(markdown_links)} Einträge.")
