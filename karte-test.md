---
layout: default
title: Interaktive Gedenkkarte (Entwurf)
permalink: /karte-test/
nav_exclude: true
---

# 📍 Interaktive Gedenkkarte (Entwurf)
### Die Sterbe- und Vermisstenorte der Neuwittenbeker Gefallenen

<p>Klicke auf eine Zahl oder einen Marker, um die Details und den Link zur jeweiligen Biografie anzuzeigen.</p>

<!-- Leaflet CSS & MarkerCluster CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.Default.css" />

<style>
  #map {
    width: 100%;
    height: 600px;
    border-radius: 12px;
    border: 1px solid #ccc;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin: 20px 0;
    z-index: 1;
  }
  .leaflet-popup-content-wrapper {
    border-radius: 8px;
    padding: 4px;
  }
  .map-popup {
    font-family: sans-serif;
    line-height: 1.4;
  }
  .map-popup h4 {
    margin: 0 0 4px 0;
    font-size: 1.1em;
    color: #cf222e;
  }
  .map-popup p {
    margin: 0 0 8px 0;
    font-size: 0.9em;
    color: #555;
  }
  .map-popup a {
    display: inline-block;
    background: #24292f;
    color: #fff !important;
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.85em;
    font-weight: bold;
  }
  .map-popup a:hover {
    background: #cf222e;
  }
</style>

<!-- Karten-Container -->
<div id="map"></div>

<!-- Leaflet JS & MarkerCluster JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    // 1. Karte initialisieren (Zentriert auf Europa)
    var map = L.map('map').setView([52.0, 19.0], 4);

    // 2. OpenStreetMap Kacheln einbinden
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '© OpenStreetMap-Mitwirkende'
    }).addTo(map);

    // 3. MarkerCluster-Gruppe erstellen
    var markers = L.markerClusterGroup({
      spiderfyOnMaxZoom: true,
      showCoverageOnHover: false,
      zoomToBoundsOnClick: true
    });

    // 4. Datenbasis der Soldaten (Koordinaten, Namen, Datumsangaben, Links)
    var soldiers = [
      // Exakte Koordinaten
      { name: "Hans Detlef Hölk", lat: 44.470756, lng: 33.705583, date: "06.01.1942", loc: "Gontscharnoje (Krim)", link: "../hoelk-hans-detlef/" },
      { name: "Willi Qualen", lat: 50.080489, lng: 36.306031, date: "04.01.1943", loc: "Charkiw / Luhansk", link: "../qualen-willi/" },
      { name: "Wilhelm Johst", lat: 51.192, lng: 5.313, date: "24.05.1940", loc: "Lommel (Belgien)", link: "../johst-wilhelm/" },
      { name: "Heinz Schlösser", lat: 56.0, lng: 7.0, date: "12.10.1940", loc: "Seegebiet Nordsee / Dänemark", link: "../schloesser-heinz/" },
      { name: "Otto Jöhnk", lat: 47.567, lng: 34.394, date: "14.01.1944", loc: "Nikopol (Ukraine)", link: "../joehnk-otto/" },
      { name: "Walter Schönfeld", lat: 52.375, lng: 9.732, date: "11.05.1941", loc: "Hannover", link: "../schoenfeld-walter/" },
      { name: "Max Gosch", lat: 51.894, lng: 11.053, date: "09.02.1945", loc: "Halberstadt", link: "../gosch-max/" },
      { name: "Fritz Küst", lat: 48.79, lng: 11.42, date: "25.04.1945", loc: "Bayern", link: "../kuest-fritz/" },
      { name: "Peter Radbruch", lat: 51.6, lng: 7.8, date: "23.06.1945", loc: "Westfalen", link: "../radbruch-peter/" },
      { name: "Heinrich Ströh", lat: 54.368, lng: 9.967, date: "16.11.1951", loc: "Neuwittenbek", link: "../stroeh-heinrich/" },

      // Regionale Cluster (Pommern, Westpreußen, Ostpreußen)
      { name: "Johannes Hass", lat: 54.0, lng: 18.5, date: "1945", loc: "Westpreußen (Polen)", link: "../hass-johannes/" },
      { name: "Bernhard Pfahl", lat: 53.8, lng: 15.0, date: "1945", loc: "Pommern", link: "../pfahl-bernhard/" },
      { name: "Kurt Klein", lat: 54.71, lng: 20.51, date: "27.02.1945", loc: "Ostpreußen (Königsberg)", link: "../klein-kurt/" },
      { name: "Heinz Petersen", lat: 54.68, lng: 20.45, date: "06.02.1945", loc: "Ostpreußen", link: "../petersen-heinz/" },
      { name: "Willy Jöhnk", lat: 51.919, lng: 19.145, date: "21.01.1945", loc: "Polen", link: "../joehnk-willy/" },

      // Frankreich
      { name: "Walter Bast", lat: 48.85, lng: 2.35, date: "13.05.1940", loc: "Frankreich", link: "../bast-walter/" },
      { name: "Erwin Behrend", lat: 47.0, lng: 2.5, date: "24.12.1944", loc: "Frankreich", link: "../behrend-erwin/" },

      // Italien
      { name: "Alfred Jensen", lat: 42.5, lng: 12.5, date: "23.12.1943", loc: "Italien", link: "../jensen-alfred/" },
      { name: "Friedrich Marxen", lat: 43.0, lng: 11.5, date: "02.07.1944", loc: "Italien", link: "../marxen-friedrich/" },
      { name: "Arthur Frohreich", lat: 42.0, lng: 13.0, date: "21.12.1945", loc: "Italien", link: "../frohreich-arthur/" },

      // Russland / Ostfront Allgemein (Leicht gestreut, damit das Cluster sauber auffächert)
      { name: "Friedrich Bast", lat: 55.75, lng: 37.61, date: "23.12.1941", loc: "Russland", link: "../bast-friedrich/" },
      { name: "Robert Jöhnk", lat: 55.80, lng: 37.50, date: "22.12.1941", loc: "Russland", link: "../joehnk-robert/" },
      { name: "Bruno Staude", lat: 55.70, lng: 37.70, date: "08.02.1942", loc: "Russland", link: "../staude-bruno/" },
      { name: "Erich Hülle", lat: 55.65, lng: 37.55, date: "13.02.1942", loc: "Russland", link: "../huelle-erich/" },
      { name: "Johannes Marxen", lat: 55.85, lng: 37.65, date: "14.09.1942", loc: "Russland", link: "../marxen-johannes/" },
      { name: "Alfred Galinsky", lat: 56.00, lng: 38.00, date: "1943", loc: "Russland vermisst", link: "../galinsky-alfred/" },
      { name: "Max Galinsky", lat: 56.10, lng: 38.10, date: "1945", loc: "Russland vermisst", link: "../galinsky-max/" },
      { name: "Hans Paetow", lat: 55.50, lng: 37.20, date: "1944", loc: "Russland vermisst", link: "../paetow-hans/" },
      { name: "Kurt Hansen", lat: 55.40, lng: 37.30, date: "1944", loc: "Russland vermisst", link: "../hansen-kurt/" },
      { name: "Helmut Hass", lat: 55.30, lng: 37.40, date: "23.08.1944", loc: "Russland", link: "../hass-helmut/" },
      { name: "Hans Grotkopp", lat: 55.20, lng: 37.10, date: "12.07.1944", loc: "Russland vermisst", link: "../grotkopp-hans/" },
      { name: "Walter Schneider", lat: 55.10, lng: 37.00, date: "22.11.1944", loc: "Russland", link: "../schneider-walter/" },
      { name: "Otto Radbruch", lat: 54.90, lng: 36.90, date: "18.02.1945", loc: "Russland", link: "../radbruch-otto/" },
      { name: "Erich Görcke", lat: 54.80, lng: 36.80, date: "11.04.1945", loc: "Russland", link: "../goercke-erich/" },
      { name: "Fritz Petersen", lat: 54.70, lng: 36.70, date: "Oktober 1945", loc: "Russland", link: "../petersen-fritz/" },
      { name: "Heinz Pohl", lat: 54.60, lng: 36.60, date: "10.02.1947", loc: "Russland", link: "../pohl-heinz/" }
    ];

    // 5. Marker erzeugen und zum Cluster hinzufügen
    soldiers.forEach(function(s) {
      var popupContent = 
        '<div class="map-popup">' +
          '<h4>' + s.name + '</h4>' +
          '<p><strong>Datum:</strong> ' + s.date + '<br><strong>Ort:</strong> ' + s.loc + '</p>' +
          '<a href="' + s.link + '">Zur Biografie →</a>' +
        '</div>';

      var marker = L.marker([s.lat, s.lng]).bindPopup(popupContent);
      markers.addLayer(marker);
    });

    map.addLayer(markers);
  });
</script>

---

[← Zurück zur Hauptübersicht](../)
