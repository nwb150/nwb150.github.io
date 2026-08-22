---
nav_exclude: true
---

# Friedrich Bast 

Friedrich und Walter Bast waren die Brüder des schwerbehinderten Albert Bast. Auf dem Hof von Hans und Lena Jöhnk (heute Peter und Annette Jöhnk) war er gut versorgt und hat dort mitgearbeitet.[cite: 6]

Friedrich Bast ist am 23.12.1941 in Russland gefallen.[cite: 6]

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-russia" style="height: 380px; width: 100%; border-radius: 8px; margin: 20px 0; border: 1px solid #d0d7de;"></div>

<script>
  (function initMap() {
    if (typeof L === 'undefined') {
      setTimeout(initMap, 100);
      return;
    }
    var map = L.map('map-russia', { scrollWheelZoom: false }).setView([60, 90], 3);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap &copy; CARTO',
      subdomains: 'abcd',
      maxZoom: 10
    }).addTo(map);

    fetch('https://cdn.jsdelivr.net/gh/johan/world-geojson@master/countries/RUS.geo.json')
      .then(function(res) { return res.json(); })
      .then(function(data) {
        var russiaLayer = L.geoJSON(data, {
          style: { color: '#8b0000', weight: 1.5, fillColor: '#b22222', fillOpacity: 0.35 }
        }).addTo(map);
        map.fitBounds(russiaLayer.getBounds(), { padding: [15, 15] });
      })
      .catch(function(err) { console.error('GeoJSON Fehler:', err); });
  })();
</script>
