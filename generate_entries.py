import os
import re

# Gesamtliste aus beiden Dokumenten inklusive der gewünschten Varianten
entries = [
    # --- Dokument 11 ---
    ("Friedrich Asmussen", "vermisst in Pommern"),
    ("Friedrich Bast", "gefallen am 13.05.1940 in Frankreich"),
    ("Walter Bast", "gefallen am 23.12.1941 in Russland"),
    ("Erwin Behrendt", "gefallen am 24.12.1944"),
    ("Ernst Dinse", "gefallen am 04.05.1944 in Russland"),
    ("Heinrich Dose", "gefallen am 26.02.1942"),
    ("Heinrich Doose", "gefallen am 26.02.1942"),  # Variante Doose
    ("Arthur Frohreich", "gefallen am 21.12.1945 in Italien"),
    ("Alfred Galinsky", "vermisst seit 1943 in Russland"),
    ("Max Galinsky", "vermisst seit 1945"),
    ("Erich Görcke", "gefallen am 11.04.1945 in Russland"),
    ("Kurt Götsch", "gefallen am 08.04.1945 auf Hela"),
    ("Max Gosch", "nach Verwundung in Ostpreußen am 19.02.1945 im Lazarett Halberstadt verstorben"),
    ("Kurt Hansen", "vermisst seit 1944 in Russland"),
    ("Helmut Hass", "gefallen am 23.08.1944 in Russland"),
    ("Johannes Hass", "vermisst seit 1945 in Ostpreußen"),
    ("Rudolf Hass", "vermisst seit 1942 in Stalingrad"),
    ("Walter Heckt", "vermisst seit 1945 im Rheinland"),
    ("Hans Detlef Hölk", "gefallen am 06.01.1942 in Russland (Krim)"),
    ("Erich Hülle", "nach Verwundung am 13.02.1942 im Lazarett Smolensk/Russland verstorben"),
    ("Alfred Jensen", "gefallen am 23.12.1943 in Italien"),
    ("Otto Jöhnk", "gefallen am 14.01.1944 in Nikopol/Russland"),
    ("Robert Jöhnk", "gefallen am 22.12.1941 in Russland"),
    ("Willy Jöhnk", "vermisst seit 21.01.1945 in Polen"),
    ("Wilhelm Johst", "gefallen am 24.05.1940 in Belgien"),
    ("Willy Kalipke", "vermisst seit 23.05.1944 in Russland"),
    ("Kurt Klein", "vermisst seit 27.02.1945 in Ostpreußen"),
    ("Hans Koch", "gefallen am 04.09.1942 in Russland"),
    ("Otto Koch", "vermisst in Russland"),
    ("Leo Krentz", "gefallen am 20.06.1944 in Russland"),
    ("Fritz Küst", "gefallen am 25.04.1945 in Bayern"),
    ("Hans Laß", "gefallen am 12.12.1945 in Pommern"),
    ("Willi Laß", "gefallen am 21.09.1942 in Italien"),
    ("Walter Neumann", "gefallen am 20.03.1942 in Sabolotje/Russland"),
    ("Friedrich Marxen", "gefallen am 02.07.1944 in Italien"),
    ("Friedrich Maryen", "gefallen am 02.07.1944 in Italien"),  # Variante Maryen
    ("Johannes Marxen", "gefallen am 14.09.1943 in Russland"),
    ("Johannes Maryen", "gefallen am 14.09.1943 in Russland"),  # Variante Maryen
    ("Erich Maske", "vermisst"),
    ("Hans Paetow", "vermisst seit 1944 in Russland"),
    ("Fritz Petersen", "gefallen im Oktober 1945 in Russland"),
    ("Heinz Petersen", "gefallen am 06.02.1945 in Ostpreußen"),
    ("Bernhard Pfahl", "vermisst seit 1945 in Pommern"),
    ("Heinz Pohl", "gefallen am 10.02.1947 in Russland"),
    ("Willi Qualen", "gefallen am 06.02.1943 in Russland"),

    # --- Dokument 12 ---
    ("Otto Radbruch", "gefallen am 18.02.1945 in Russland"),
    ("Peter Radbruch", "gefallen am 23.06.1945 in Westfalen"),
    ("Albert Reimer", "gefallen im Mai 1945 in Berlin"),
    ("Emil Reimer", "vermisst in Russland"),
    ("Paul Rückwardt", "vermisst in Russland"),
    ("Willi Rückwardt", "gefallen am 09.01.1943 in Russland"),
    ("Heinz Schlösser", "gefallen am 12.10.1940 auf See"),
    ("Walter Schneider", "gefallen am 23.12.1944"),
    ("Walter Schönfeld", "gefallen am 11.05.1941 in Hannover"),
    ("Helmut Schröder", "gefallen am 09.07.1941 in Russland"),
    ("Bruno Staude", "gefallen am 08.02.1942 in Russland"),
    ("Werner Stenzeleit", "vermisst seit 1945 in Russland"),
    ("Heinrich Ströh", "vermisst seit 1944 in Russland"),
    ("August Weber", "gefallen am 08.02.1943 in Russland"),
    ("Horst Wichert", "infolge Kriegsleidens 1951 verstorben"),
    ("Karl Heinz Wulff", "verstorben im heimatlichen Lazarett")
]

def generate_slug(name):
    name = name.lower()
    name = name.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    parts = name.split()
    if len(parts) >= 2:
        nachname = parts[-1]
        vornamen = "-".join(parts[:-1])
        slug = f"{nachname}-{vornamen}"
    else:
        slug = name
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    return slug

created_dirs = 0
existing_dirs = 0

for name, fate in entries:
    slug = generate_slug(name)
    if not slug:
        continue

    if not os.path.exists(slug):
        os.makedirs(slug)
        
        html_template = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{name} - Die sprechenden Steine von Neuwittenbek</title>
</head>
<body>
    <h1>{name}</h1>
    <p>Schicksal: {fate}</p>
</body>
</html>"""
        
        with open(os.path.join(slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_template)
        created_dirs += 1
    else:
        existing_dirs += 1

print(f"Verzeichnisse neu erstellt: {created_dirs}")
print(f"Bereits existiert (übersprungen): {existing_dirs}")
