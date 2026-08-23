---
nav_exclude: true
title: "Friedrich Bast"
death_date: "23.12.1941"
location: "Russland"
---

# Friedrich Bast 

Friedrich und [Walter Bast](../bast-walter/) waren die Brüder des schwerbehinderten Albert Bast. Auf dem Hof von Hans und Lena Jöhnk (heute Peter und Annette Jöhnk) war er gut versorgt und hat dort mitgearbeitet.

Friedrich Bast ist am 23.12.1941 in Russland gefallen.

[📍 Russland auf Google Maps öffnen](https://www.google.com/maps/search/?api=1&query=Russland)

<div id="map" style="width: 100%; height: 300px; border-radius: 8px; margin-top: 10px;"></div>

<!-- Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<script>
  // 1. Karte auf Russland ausrichten
  const map = L.map('map').setView([60, 90], 2);

  // 2. OpenStreetMap Hintergrund-Tiles laden
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap'
  }).addTo(map);

  // 3. Landesgrenzen (GeoJSON) laden und dezent einfärben
  fetch('https://raw.githubusercontent.com/johan/world.geo.json/master/countries/RUS.geo.json')
    .then(response => response.json())
    .then(data => {
      L.geoJSON(data, {
        style: {
          color: '#a855f7',       // Rahmenfarbe (z. B. passend zu deinen lila Links)
          weight: 1.5,           // Linienstärke
          fillColor: '#a855f7',   // Füllfarbe
          fillOpacity: 0.15       // Transparenz (0.15 = sehr dezent)
        }
      }).addTo(map);
    });
</script>
