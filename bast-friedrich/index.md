---
nav_exclude: true
---

# Friedrich Bast 

Friedrich und Walter Bast waren die Brüder des schwerbehinderten Albert Bast. Auf dem Hof von Hans und Lena Jöhnk (heute Peter und Annette Jöhnk) war er gut versorgt und hat dort mitgearbeitet.

Friedrich Bast ist am 23.12.1941 in Russland gefallen.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-russia" style="height: 420px; width: 100%; border-radius: 8px; margin: 20px 0; border: 1px solid #d0d7de; box-shadow: 0 2px 6px rgba(0,0,0,0.05);"></div>

<script>
  (function initMap() {
    if (typeof L === 'undefined') {
      setTimeout(initMap, 100);
      return;
    }

    // Zentrierung zwischen Deutschland und Russland bei Zoomstufe 3
    var map = L.map('map-russia', { scrollWheelZoom: false }).setView([56, 50], 3);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: 'abcd',
      maxZoom: 10
    }).addTo(map);

    // Direkt eingebettetes Polygon für das russische Staatsgebiet (Ausfall- und CORS-sicher)
    var russiaPolygon = [
      [69.7, 31.0], [65.0, 29.5], [60.5, 27.8], [59.5, 28.0], [57.5, 27.3],
      [55.9, 28.1], [53.2, 30.8], [52.1, 31.8], [50.5, 34.5], [49.6, 39.8],
      [43.5, 40.0], [41.2, 47.7], [46.0, 49.0], [51.0, 54.0], [51.0, 78.0],
      [49.1, 87.3], [49.9, 116.8], [53.5, 124.0], [42.3, 130.6], [46.0, 138.0],
      [59.0, 150.0], [60.0, 165.0], [66.0, 170.0], [72.0, 130.0], [73.0, 80.0],
      [69.0, 60.0], [68.0, 44.0]
    ];

    // Rote Flächenmarkierung für Russland
    L.polygon(russiaPolygon, {
      color: '#8b0000',
      weight: 2,
      fillColor: '#b22222',
      fillOpacity: 0.35
    }).addTo(map);

    // Blauer Orientierungspunkt für Deutschland / Neuwittenbek
    L.circleMarker([54.33, 9.96], {
      color: '#0055ff',
      fillColor: '#3388ff',
      fillOpacity: 0.9,
      radius: 6
    }).addTo(map).bindPopup("Neuwittenbek (Deutschland)");
  })();
</script>
