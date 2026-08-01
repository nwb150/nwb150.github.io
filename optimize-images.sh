#!/bin/bash

echo "=== Starte Bildoptimierung ==="
echo "Ignoriere: ./Bilder, ./_site, ./vendor, ./.bundle, ./.git, ./.venv, ./qrcodes"

find . \( -path "./Bilder" -o -path "./_site" -o -path "./vendor" -o -path "./.bundle" -o -path "./.git" -o -path "./.venv" -o -path "./qrcodes" \) -prune -o -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -exec mogrify -resize "1600x1600>" -quality 85 -strip {} +

echo "=== Fertig! Alle Bilder in den Personen-Ordnern wurden optimiert. ==="
