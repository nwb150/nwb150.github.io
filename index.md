# Die sprechenden Steine von Neuwittenbek
### 150 Jahre Geschichte • Erinnerung lebendig halten

Hinter den Mauern und Wegen unseres Dorfes verbergen sich die Lebenswege und Schicksale vieler Generationen. Dieses Projekt bringt die Gedenksteine Neuwittenbeks zum Sprechen. Es lädt dich ein, innezuhalten und etwas mehr über das Leben, das Wirken und die Schicksale unserer ehemaligen Nachbarn, Väter, Brüder, Söhne und Ehemänner zu erfahren, die durch die Kriege aus unserer Mitte gerissen wurden.

### Digitale Gesamtübersicht der Biografien:

<!-- SOLDIER_LIST_START -->
* [Friedrich Bast](./bast-friedrich/)
* [Walter Bast](./bast-walter/)
* [Erwin Behrend](./behrend-erwin/)
* [Arthur Frohreich](./frohreich-arthur/)
* [Alfred Galinsky](./galinsky-alfred/)
* [Max Galinsky](./galinsky-max/)
* [Erich Goercke](./goercke-erich/)
* [Max Gosch](./gosch-max/)
* [Hans Grotkopp](./grotkopp-hans/)
* [Kurt Hansen](./hansen-kurt/)
* [Helmut Hass](./hass-helmut/)
* [Johannes Hass](./hass-johannes/)
* [Hans Detlef Hoelk](./hoelk-hans-detlef/)
* [Erich Huelle](./huelle-erich/)
* [Alfred Jensen](./jensen-alfred/)
* [Otto Joehnk](./joehnk-otto/)
* [Robert Joehnk](./joehnk-robert/)
* [Willy Joehnk](./joehnk-willy/)
* [Wilhelm Johst](./johst-wilhelm/)
* [Kurt Klein](./klein-kurt/)
* [Fritz Kuest](./kuest-fritz/)
* [Friedrich Marxen](./marxen-friedrich/)
* [Johannes Marxen](./marxen-johannes/)
* [Hans Paetow](./paetow-hans/)
* [Fritz Petersen](./petersen-fritz/)
* [Heinz Petersen](./petersen-heinz/)
* [Bernhard Pfahl](./pfahl-bernhard/)
* [Heinz Pohl](./pohl-heinz/)
* [Hinrich Popp](./popp-hinrich/)
* [Willi Qualen](./qualen-willi/)
* [Otto Radbruch](./radbruch-otto/)
* [Peter Radbruch](./radbruch-peter/)
* [Heinz Schloesser](./schloesser-heinz/)
* [Walter Schneider](./schneider-walter/)
* [Walter Schoenfeld](./schoenfeld-walter/)
* [Bruno Staude](./staude-bruno/)
* [Heinrich Stroeh](./stroeh-heinrich/)
<!-- SOLDIER_LIST_END -->

## Interaktive Karte

Diese Karte visualisiert die bekannten Sterbe- und Vermisstenorte der Neuwittenbeker Gefallenen. Nutze die Suche zum Filtern nach Namen oder Orten und klicke auf einen Marker, um direkt zur Biografie zu gelangen.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.Default.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet-gesture-handling/dist/leaflet-gesture-handling.min.css" type="text/css" />

<style>
  .map-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 15px;
    align-items: center;
    background: #f6f8fa;
    padding: 12px 16px;
    border-radius: 8px;
    border: 1px solid #e1e4e8;
  }
  .map-controls input {
    padding: 9px 14px;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    font-size: 0.95em;
    outline: none;
    flex-grow: 1;
    max-width: 420px;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  .map-controls input:focus {
    border-color: #0969da;
    box-shadow: 0 0 0 3px rgba(9, 105, 218, 0.15);
  }
  .map-stats {
    font-size: 0.88em;
    color: #57606a;
    font-weight: 500;
    margin-left: auto;
  }

  #map {
    width: 100%;
    height: 600px;
    border-radius: 12px;
    border: 1px solid #d0d7de;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    margin: 10px 0 25px 0;
    z-index: 1;
  }

  .custom-pin-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .custom-pin {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background-color: #cf222e;
    border: 2px solid #ffffff;
    box-shadow: 0 2px 6px rgba(0,0,0,0.35);
    transition: transform 0.15s ease-in-out;
  }
  .custom-pin:hover {
    transform: scale(1.35);
  }

  .map-popup {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.45;
    padding: 4px;
  }
  .map-popup h4 {
    margin: 0 0 6px 0;
    font-size: 1.05em;
    color: #1f2328;
    border-bottom: 1px solid #eaeef2;
    padding-bottom: 4px;
  }
  .map-popup p {
    margin: 6px 0 12px 0;
    font-size: 0.88em;
    color: #57606a;
  }
  .map-popup a {
    display: inline-block;
    background: #24292f;
    color: #ffffff !important;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 0.85em;
    font-weight: 600;
    transition: background 0.2s;
  }
  .map-popup a:hover {
    background: #cf222e;
  }
</style>

<div class="map-controls">
  <input type="text" id="searchInput" placeholder="🔍 Name oder Ort suchen..." />
  <div class="map-stats" id="markerCount">Zeige 0 Einträge</div>
</div>

<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>
<script src="https://unpkg.com/leaflet-gesture-handling/dist/leaflet-gesture-handling.min.js"></script>

{% raw %}
<script>
  document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map', {
      gestureHandling: true
    }).setView([52.0, 19.0], 4);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '© OpenStreetMap-Mitwirkende'
    }).addTo(map);

    var markersCluster = L.markerClusterGroup({
      spiderfyOnMaxZoom: true,
      showCoverageOnHover: false,
      zoomToBoundsOnClick: true,
      maxClusterRadius: 40
    });

    var soldiers = [
      { name: "Hans Detlef Hölk", lat: 44.470756, lng: 33.705583, date: "06.01.1942", loc: "Gontscharnoje (Krim)", link: "./hoelk-hans-detlef/" },
      { name: "Willi Qualen", lat: 50.080489, lng: 36.306031, date: "04.01.1943", loc: "Charkiw / Luhansk", link: "./qualen-willi/" },
      { name: "Wilhelm Johst", lat: 51.192, lng: 5.313, date: "24.05.1940", loc: "Lommel (Belgien)", link: "./johst-wilhelm/" },
      { name: "Heinz Schlösser", lat: 56.0, lng: 7.0, date: "12.10.1940", loc: "Seegebiet Nordsee / Dänemark", link: "./schloesser-heinz/" },
      { name: "Otto Jöhnk", lat: 47.567, lng: 34.394, date: "14.01.1944", loc: "Nikopol (Ukraine)", link: "./joehnk-otto/" },
      { name: "Walter Schönfeld", lat: 52.8878, lng: 8.0264, date: "11.05.1941", loc: "Varrelbusch (Cloppenburg)", link: "./schoenfeld-walter/" },
      { name: "Max Gosch", lat: 51.894, lng: 11.053, date: "09.02.1945", loc: "Halberstadt", link: "./gosch-max/" },
      { name: "Fritz Küst", lat: 48.79, lng: 11.42, date: "25.04.1945", loc: "Bayern", link: "./kuest-fritz/" },
      { name: "Peter Radbruch", lat: 51.6, lng: 7.8, date: "23.06.1945", loc: "Westfalen", link: "./radbruch-peter/" },
      { name: "Heinrich Ströh", lat: 54.368, lng: 9.967, date: "16.11.1951", loc: "Neuwittenbek", link: "./stroeh-heinrich/" },
      { name: "Johannes Hass", lat: 54.0, lng: 18.5, date: "1945", loc: "Westpreußen (Polen)", link: "./hass-johannes/" },
      { name: "Bernhard Pfahl", lat: 53.8, lng: 15.0, date: "1945", loc: "Pommern", link: "./pfahl-bernhard/" },
      { name: "Kurt Klein", lat: 54.71, lng: 20.51, date: "27.02.1945", loc: "Ostpreußen (Königsberg)", link: "./klein-kurt/" },
      { name: "Heinz Petersen", lat: 54.68, lng: 20.45, date: "06.02.1945", loc: "Ostpreußen", link: "./petersen-heinz/" },
      { name: "Willy Jöhnk", lat: 51.919, lng: 19.145, date: "21.01.1945", loc: "Polen", link: "./joehnk-willy/" },
      { name: "Helmut Hass", lat: 50.0647, lng: 19.9450, date: "23.08.1944", loc: "Krakau (Polen)", link: "./hass-helmut/" },
      { name: "Walter Bast", lat: 48.85, lng: 2.35, date: "13.05.1940", loc: "Frankreich", link: "./bast-walter/" },
      { name: "Erwin Behrend", lat: 47.0, lng: 2.5, date: "24.12.1944", loc: "Frankreich", link: "./behrend-erwin/" },
      { name: "Alfred Jensen", lat: 42.5, lng: 12.5, date: "23.12.1943", loc: "Italien", link: "./jensen-alfred/" },
      { name: "Friedrich Marxen", lat: 43.0, lng: 11.5, date: "02.07.1944", loc: "Italien", link: "./marxen-friedrich/" },
      { name: "Arthur Frohreich", lat: 42.0, lng: 13.0, date: "21.12.1945", loc: "Italien", link: "./frohreich-arthur/" },
      { name: "Friedrich Bast", lat: 55.75, lng: 37.61, date: "23.12.1941", loc: "Russland", link: "./bast-friedrich/" },
      { name: "Robert Jöhnk", lat: 55.80, lng: 37.50, date: "22.12.1941", loc: "Russland", link: "./joehnk-robert/" },
      { name: "Bruno Staude", lat: 57.9897, lng: 31.3572, date: "08.02.1942", loc: "Staraja Russa (Russland)", link: "./staude-bruno/" },
      { name: "Erich Hülle", lat: 54.782, lng: 32.045, date: "13.02.1942", loc: "Smolensk (Russland)", link: "./huelle-erich/" },
      { name: "Johannes Marxen", lat: 55.85, lng: 37.65, date: "14.09.1942", loc: "Russland", link: "./marxen-johannes/" },
      { name: "Alfred Galinsky", lat: 56.00, lng: 38.00, date: "1943", loc: "Russland", link: "./galinsky-alfred/" },
      { name: "Max Galinsky", lat: 56.10, lng: 38.10, date: "1945", loc: "Russland", link: "./galinsky-max/" },
      { name: "Hans Paetow", lat: 55.50, lng: 37.20, date: "1944", loc: "Russland", link: "./paetow-hans/" },
      { name: "Kurt Hansen", lat: 55.40, lng: 37.30, date: "1944", loc: "Russland", link: "./hansen-kurt/" },
      { name: "Hans Grotkopp", lat: 55.20, lng: 37.10, date: "12.07.1944", loc: "Russland", link: "./grotkopp-hans/" },
      { name: "Walter Schneider", lat: 55.10, lng: 37.00, date: "22.11.1944", loc: "Russland", link: "./schneider-walter/" },
      { name: "Otto Radbruch", lat: 56.3422, lng: 30.5239, date: "18.02.1945", loc: "Welikije Luki (Russland)", link: "./radbruch-otto/" },
      { name: "Erich Görcke", lat: 54.80, lng: 36.80, date: "11.04.1945", loc: "Russland", link: "./goercke-erich/" },
      { name: "Fritz Petersen", lat: 45.356, lng: 36.467, date: "Oktober 1945", loc: "Kertsch (Krim)", link: "./petersen-fritz/" },
      { name: "Heinz Pohl", lat: 54.60, lng: 36.60, date: "10.02.1947", loc: "Russland", link: "./pohl-heinz/" }
    ];

    var allMarkers = [];

    function getPinIcon() {
      return L.divIcon({
        className: 'custom-pin-wrapper',
        html: '<div class="custom-pin"></div>',
        iconSize: [14, 14],
        iconAnchor: [7, 7]
      });
    }

    function renderMap(filteredSoldiers) {
      markersCluster.clearLayers();
      allMarkers = [];

      filteredSoldiers.forEach(function(s) {
        var popupContent = 
          '<div class="map-popup">' +
            '<h4>' + s.name + '</h4>' +
            '<p><strong>Datum:</strong> ' + s.date + '<br><strong>Ort:</strong> ' + s.loc + '</p>' +
            '<a href="' + s.link + '">Zur Biografie →</a>' +
          '</div>';

        var marker = L.marker([s.lat, s.lng], { icon: getPinIcon() }).bindPopup(popupContent);
        markersCluster.addLayer(marker);
        allMarkers.push(marker);
      });

      map.addLayer(markersCluster);
      document.getElementById('markerCount').innerText = 'Zeige ' + filteredSoldiers.length + ' von ' + soldiers.length + ' Einträgen';

      if (allMarkers.length > 0) {
        var group = new L.featureGroup(allMarkers);
        map.fitBounds(group.getBounds().pad(0.1));
      }
    }

    function filterData() {
      var searchVal = document.getElementById('searchInput').value.toLowerCase().trim();

      var filtered = soldiers.filter(function(s) {
        return s.name.toLowerCase().includes(searchVal) || s.loc.toLowerCase().includes(searchVal);
      });

      renderMap(filtered);
    }

    document.getElementById('searchInput').addEventListener('input', filterData);

    renderMap(soldiers);
  });
</script>
{% endraw %}

## Erinnerungen lebendig halten – Macht mit!
Manche der Erinnerungen rund um diese Gedenksteine leben heute nur noch in den Köpfen derer, die sie miterlebt haben oder denen sie weitererzählt wurden. Wir möchten verhindern, dass diese wertvollen, aber langsam verblassenden Erinnerungen im Laufe der Zeit verloren gehen. Ein Anfang ist gemacht, mit der großen Hilfe von [Frau Tams](./stroeh-heinrich/). Habt ihr noch persönliche Anekdoten, historische Details, alte Dokumente oder Fotos? Wer Erinnerungen teilen kann und möchte, meldet sich bitte direkt bei uns.

<hr>

<p>Ein rein ehrenamtliches, nicht-kommerzielles Open-Source-Projekt der Gemeinde Neuwittenbek.</p>
<p><a href="impressum.html">Impressum & Datenschutz</a></p>
