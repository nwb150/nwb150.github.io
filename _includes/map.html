document.addEventListener("DOMContentLoaded", function() {
  var container = document.getElementById('leaflet-map');
  if (!container || container.dataset.mapLoaded) return;
  container.dataset.mapLoaded = "true";

  var lat = parseFloat(container.getAttribute('data-lat'));
  var lng = parseFloat(container.getAttribute('data-lng'));
  var zoom = parseInt(container.getAttribute('data-zoom')) || 12;
  var location = container.getAttribute('data-location');
  var country = container.getAttribute('data-country');
  var title = container.getAttribute('data-title');

  var map;

  // MODUS 1: Exakte Koordinaten vorhanden (z. B. Neuwittenbek / Friedhof)
  if (!isNaN(lat) && !isNaN(lng)) {
    map = L.map(container).setView([lat, lng], zoom);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var marker = L.marker([lat, lng]).addTo(map);
    if (title) {
      marker.bindPopup('<b>' + title + '</b>').openPopup();
    }
  } 
  // MODUS 2: Landesansicht (z. B. Russland) mit detaillierten Beschriftungen
  else if (location === 'Russland' || country === 'RUS' || country === 'Russland') {
    map = L.map(container).setView([58, 60], 3);

    // Detaillierte Basis-Karte ohne Text (CARTO Voyager)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      subdomains: 'abcd',
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> © <a href="https://carto.com/">CARTO</a>'
    }).addTo(map);

    // GeoJSON-Landesfläche (Lila Füllung)
    fetch('https://raw.githubusercontent.com/johan/world.geo.json/master/countries/RUS.geo.json')
      .then(function(res) { return res.json(); })
      .then(function(data) {
        L.geoJSON(data, {
          style: {
            color: '#8b5cf6',       // Lila Rahmen
            weight: 2,
            fillColor: '#8b5cf6',   // Lila Füllung
            fillOpacity: 0.22
          }
        }).addTo(map);
      })
      .catch(function(err) {
        console.error("GeoJSON-Fehler:", err);
      });

    // Beschriftungs-Ebene (liegt OBERHALB der lila Füllung, damit alle Ländernamen lesbar bleiben)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      subdomains: 'abcd',
      pane: 'markerPane' // Platzierung über dem GeoJSON
    }).addTo(map);
  } 
  // MODUS 3: Fallback (Europa/Welt)
  else {
    map = L.map(container).setView([50, 30], 3);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
  }
});
