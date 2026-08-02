#!/usr/bin/env python3
import os

OUTPUT_FILE = "gesamte_biografien.txt"

# Ordner und Dateien, die ignoriert werden sollen
IGNORE_DIRS = {'_site', '_includes', 'vendor', '.git', '.github', 'Bilder', 'qrcodes'}
IGNORE_FILES = {'README.md', 'impressum.md'}

files_to_combine = []

# 1. Haupt-Index zuerst hinzufügen
if os.path.exists("index.md"):
    files_to_combine.append("index.md")

# 2. Unterordner nach Markdown-Dateien durchsuchen
for root, dirs, files in os.walk("."):
    # Ignorierte Ordner ausfiltern
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
    
    for file in sorted(files):
        if file.endswith(".md") and file not in IGNORE_FILES:
            filepath = os.path.normpath(os.path.join(root, file))
            if filepath != "index.md":
                files_to_combine.append(filepath)

# 3. Zusammenführen in eine Textdatei
with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for filepath in files_to_combine:
        outfile.write(f"{'='*60}\n")
        outfile.write(f"DATEI: {filepath}\n")
        outfile.write(f"{'='*60}\n\n")
        
        try:
            with open(filepath, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
            outfile.write("\n\n")
        except Exception as e:
            outfile.write(f"[Fehler beim Lesen der Datei: {e}]\n\n")

print(f"Fertig! {len(files_to_combine)} Dateien wurden in '{OUTPUT_FILE}' zusammengefasst.")
