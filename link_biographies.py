#!/usr/bin/env python3
from pathlib import Path

# Zuordnung von Dateipfaden zu Textersetzungen (Alt, Neu)
replacements = {
    "index.md": [
        ("Frau Tams", "[Frau Tams](./stroeh-heinrich/)")
    ],
    "goercke-erich/index.md": [
        ("Hans Detlef Hölk", "[Hans Detlef Hölk](../hoelk-hans-detlef/)")
    ],
    "pfahl-bernhard/index.md": [
        ("Familie Schneider/Stein", "[Familie Schneider/Stein](../schneider-walter/)")
    ],
    "bast-friedrich/index.md": [
        ("Walter Bast", "[Walter Bast](../bast-walter/)")
    ],
    "bast-walter/index.md": [
        ("Friedrich Bast", "[Friedrich Bast](../bast-friedrich/)")
    ],
    "hass-helmut/index.md": [
        ("Johannes Hass", "[Johannes Hass](../hass-johannes/)")
    ],
    "hass-johannes/index.md": [
        ("Helmut Hass", "[Helmut Hass](../hass-helmut/)")
    ],
    "galinsky-alfred/index.md": [
        ("Max Galinsky", "[Max Galinsky](../galinsky-max/)")
    ],
    "galinsky-max/index.md": [
        ("Alfred Galinsky", "[Alfred Galinsky](../galinsky-alfred/)")
    ],
    "petersen-fritz/index.md": [
        ("sein Bruder Heinz", "sein Bruder [Heinz](../petersen-heinz/)")
    ],
    "petersen-heinz/index.md": [
        ("Bruder Fritz", "Bruder [Fritz](../petersen-fritz/)")
    ],
    "joehnk-robert/index.md": [
        ("Otto Jöhnk", "[Otto Jöhnk](../joehnk-otto/)")
    ]
}

for rel_path, pairs in replacements.items():
    file_path = Path(rel_path)
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
        for old, new in pairs:
            if new not in content and old in content:
                content = content.replace(old, new)
                file_path.write_text(content, encoding="utf-8")
                print(f"✔ Aktualisiert: {rel_path}")
    else:
        print(f"✖ Datei nicht gefunden: {rel_path}")
