---
nav_exclude: true
---

# Friedrich Bast 

Friedrich und Walter Bast waren die Brüder des schwerbehinderten Albert Bast. Auf dem Hof von Hans und Lena Jöhnk (heute Peter und Annette Jöhnk) war er gut versorgt und hat dort mitgearbeitet.

Friedrich Bast ist am 23.12.1941 in Russland gefallen.

<!-- Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-russia" style="height: 380px; width: 100%; border-radius: 8px; margin: 20px 0; border: 1px solid #d0d7de; box-shadow: 0 2px 6px rgba(0,0,0,0.05);"></div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map-russia', { scrollWheelZoom: false }).setView([60, 90], 3);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: 'abcd',
      maxZoom: 10
    }).addTo(map);

    // CORS-freundliche CDN-URL von jsDelivr
    fetch('https://cdn.jsdelivr.net/gh/johan/world-geojson@master/countries/RUS.geo.json')
      .then(function(res) { return res.json(); })
      .then(function(data) {
        var russiaLayer = L.geoJSON(data, {
          style: {
            color: '#8b0000',
            weight: 1.5,
            fillColor: '#b22222',
            fillOpacity: 0.35
          }
        }).addTo(map);
        map.fitBounds(russiaLayer.getBounds(), { padding: [15, 15] });
      })
      .catch(function(err) {
        console.error('Fehler beim Laden der Grenzen:', err);
      });
  });
</script>
