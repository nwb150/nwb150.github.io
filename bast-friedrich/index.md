---
nav_exclude: true
---

# Friedrich Bast 

Friedrich und Walter Bast waren die Brüder des schwerbehinderten Albert Bast. Auf dem Hof von Hans und Lena Jöhnk (heute Peter und Annette Jöhnk) war er gut versorgt und hat dort mitgearbeitet.[cite: 6]

Friedrich Bast ist am 23.12.1941 in Russland gefallen.[cite: 6]

<!-- Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-russia" style="height: 420px; width: 100%; border-radius: 8px; margin: 25px 0; border: 1px solid #d0d7de; box-shadow: 0 3px 8px rgba(0,0,0,0.05);"></div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    // Map-Instanz mit deaktiviertem Scroll-Zoom (verhindert Versehentliches Feststecken beim Scrollen)
    var map = L.map('map-russia', {
      scrollWheelZoom: false
    }).setView([61.5, 95.0], 2);

    // Kartendesign im reduzierten, historischen Archiv-Look (CartoDB Positron)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: 'abcd',
      maxZoom: 10
    }).addTo(map);

    // GeoJSON der russischen Landesgrenzen dynamisch laden & stylen
    fetch('https://raw.githubusercontent.com/johan/world-geojson/master/countries/RUS.geo.json')
      .then(response => response.json())
      .then(data => {
        var russiaLayer = L.geoJSON(data, {
          style: {
            color: '#8b0000',       // Dunkelrote Grenzlinie
            weight: 1.5,
            fillColor: '#b22222',   // Flächiges Rot
            fillOpacity: 0.35       // Transparent, damit Geografie lesbar bleibt
          }
        }).addTo(map);

        // Automatische Kameraausrichtung auf die vollen Ausmaße Russlands
        map.fitBounds(russiaLayer.getBounds(), { padding: [15, 15] });
      })
      .catch(err => console.error('Fehler beim Laden der GeoJSON-Daten:', err));
  });
</script>
