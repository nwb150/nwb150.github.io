import os
import qrcode
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage

# Konfiguration für das Plakat
output_dir = "qrcodes"
output_file = os.path.join(output_dir, "qr_code_plakat_hauptseite.png")
target_url = "https://nwb150.github.io"

# Ordner erstellen, falls nicht existiert
os.makedirs(output_dir, exist_ok=True)

print(f"Generiere abgerundeten Plakat-QR-Code für: {target_url}")

# QR-Code-Konfiguration identisch zu den Stein-Plaketten
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Level M garantiert das saubere 29x29 Raster
    box_size=30,  # Größere Boxen für extrem hohe Auflösung im Druck
    border=4,     # Sauberer weißer Sicherheitsrand
)

qr.add_data(target_url)
qr.make(fit=True)

# Bild mit den exakt gleichen runden Modulen erzeugen
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer()
)

# Speichern
img.save(output_file)

print(f"✅ Erfolg! Dein Plakat-QR-Code wurde gespeichert unter: {output_file}")
