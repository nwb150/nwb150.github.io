import os
import qrcode
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage

# Konfiguration
base_dir = "."  # Aktuelles Verzeichnis
output_dir = "qrcodes"

# Ordner, für die KEIN QR-Code erzeugt werden soll
ignored_folders = {".git", ".venv", output_dir, "__pycache__"}

os.makedirs(output_dir, exist_ok=True)

print("Scanne Verzeichnis nach Personen-Ordnern...")

# Alle Einträge im aktuellen Verzeichnis auflisten und sortieren
try:
    items = sorted(os.listdir(base_dir))
except Exception as e:
    print(f"Fehler beim Lesen des Verzeichnisses: {e}")
    items = []

count = 0

for folder in items:
    folder_path = os.path.join(base_dir, folder)
    
    # Nur echte Ordner verarbeiten, die nicht auf der Ignorierliste stehen
    if os.path.isdir(folder_path) and folder not in ignored_folders:
        
        # Schönere Namensdarstellung fürs Terminal aus dem Ordnernamen basteln
        # Beispiel: "marxen-johannes" -> "Johannes Marxen" (Umlaute fehlen im Ordnernamen)
        parts = folder.split("-")
        if len(parts) >= 2:
            display_name = f"{parts[-1].capitalize()} {' '.join(parts[:-1]).capitalize()}"
        else:
            display_name = folder.capitalize()
            
        print(f"Generiere wetterfesten QR-Code für: {display_name} (Ordner: {folder})")
        
        # Die kurze Basis-URL mit dem dynamischen Ordnernamen
        url = f"https://stramon.github.io/dssvn/{folder}/"
        
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Level M für 29x29 Layout
            box_size=20,  # Fette Pixel für den Druck
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        img.save(f"{output_dir}/qr-{folder}.png")
        count += 1

print(f"\nFertig! Es wurden {count} QR-Codes automatisch im 29x29-Raster erzeugt.")
