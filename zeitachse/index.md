---
layout: default
title: Zeitachse
permalink: /zeitachse/
nav_exclude: true
---

# Chronologische Zeitachse (Entwurf)

<style>
.density-chart {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  height: 140px;
  margin: 20px 0 30px 0;
  padding: 15px;
  background: #f6f8fa;
  border-radius: 8px;
  border: 1px solid #d0d7de;
}
.density-bar-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  justify-content: flex-end;
}
.density-bar {
  width: 100%;
  max-width: 32px;
  background: linear-gradient(180deg, #cf222e 0%, #8c1d18 100%);
  border-radius: 4px 4px 0 0;
  min-height: 4px;
}
.density-label {
  font-size: 0.8em;
  color: #57606a;
  margin-top: 6px;
  font-weight: 600;
}
.density-val {
  font-size: 0.8em;
  font-weight: bold;
  color: #cf222e;
  margin-bottom: 3px;
}
.timeline-container {
  position: relative;
  padding-left: 22px;
  border-left: 3px solid #d0d7de;
  margin: 20px 0 40px 10px;
}
.timeline-year-header {
  font-size: 1.2em;
  font-weight: bold;
  color: #1f2328;
  margin: 25px 0 15px -31px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.timeline-year-badge {
  background: #24292f;
  color: #ffffff;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8em;
}
.timeline-month-cluster {
  background: #fff8f0;
  border-left: 4px solid #d97706;
  padding: 6px 10px;
  margin: 12px 0 12px -10px;
  border-radius: 0 6px 6px 0;
  font-size: 0.85em;
  font-weight: bold;
  color: #92400e;
}
.timeline-item {
  position: relative;
  margin-bottom: 16px;
  padding-left: 8px;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -29px;
  top: 6px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #cf222e;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 2px #d0d7de;
}
.timeline-date {
  font-size: 0.85em;
  font-weight: bold;
  color: #57606a;
}
.timeline-title {
  font-size: 1.05em;
  font-weight: 600;
}
.timeline-location {
  font-size: 0.9em;
  color: #24292f;
}
</style>

## Häufigkeits-Übersicht nach Jahren

<div class="density-chart">
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1893</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1894</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1895</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1896</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1897</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1898</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1899</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1900</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1901</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1902</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1903</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1904</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1905</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1906</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1907</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1908</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1909</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1910</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1911</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1912</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1913</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1914</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1915</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1916</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1917</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1918</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1919</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1920</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1921</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1922</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1923</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1924</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1925</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1926</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1927</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1928</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1929</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1930</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1931</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1932</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1933</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1934</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1935</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1936</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1937</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1938</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1939</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">3</div>
    <div class="density-bar" style="height: 60%;"></div>
    <div class="density-label">1940</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">3</div>
    <div class="density-bar" style="height: 60%;"></div>
    <div class="density-label">1941</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">4</div>
    <div class="density-bar" style="height: 80%;"></div>
    <div class="density-label">1942</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1943</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">5</div>
    <div class="density-bar" style="height: 100%;"></div>
    <div class="density-label">1944</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">4</div>
    <div class="density-bar" style="height: 80%;"></div>
    <div class="density-label">1945</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1946</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1947</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1948</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1949</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val"></div>
    <div class="density-bar" style="height: 0%;"></div>
    <div class="density-label">1950</div>
  </div>
  <div class="density-bar-container">
    <div class="density-val">1</div>
    <div class="density-bar" style="height: 20%;"></div>
    <div class="density-label">1951</div>
  </div>
</div>

## Vertikaler Zeitstrahl

<div class="timeline-container">

<div class="timeline-year-header">
  <span class="timeline-year-badge">1893</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">18.07.1893</div>
  <div class="timeline-title"><a href="../popp-hinrich/">Hinrich Popp</a></div>
  <div class="timeline-location">Ort: <em>Gettorf</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1903</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">08.06.1903</div>
  <div class="timeline-title"><a href="../qualen-willi/">Willi Qualen</a></div>
  <div class="timeline-location">Ort: <em>Neuwittenbek geboren</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1909</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">06.03.1909</div>
  <div class="timeline-title"><a href="../hoelk-hans-detlef/">Hans Detlef Hölk</a></div>
  <div class="timeline-location">Ort: <em>Neuwittenbek geboren und stammte vom Hof Neuwittenbek</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1940</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(3 Schicksale)</span>
</div>

<div class="timeline-month-cluster">
  ⚡ Häufung: 2 Schicksale im Mai 1940
</div>

<div class="timeline-item">
  <div class="timeline-date">13.05.1940</div>
  <div class="timeline-title"><a href="../bast-walter/">Walter Bast</a></div>
  <div class="timeline-location">Ort: <em>Frankreich gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">24.05.1940</div>
  <div class="timeline-title"><a href="../johst-wilhelm/">Wilhelm Johst</a></div>
  <div class="timeline-location">Ort: <em>Belgien</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">12.10.1940</div>
  <div class="timeline-title"><a href="../schloesser-heinz/">Heinz Schlösser</a></div>
  <div class="timeline-location">Ort: <em>See</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1941</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(3 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">11.05.1941</div>
  <div class="timeline-title"><a href="../schoenfeld-walter/">Walter Schönfeld</a></div>
  <div class="timeline-location">Ort: <em>Hannover</em></div>
</div>

<div class="timeline-month-cluster">
  ⚡ Häufung: 2 Schicksale im Dezember 1941
</div>

<div class="timeline-item">
  <div class="timeline-date">22.12.1941</div>
  <div class="timeline-title"><a href="../joehnk-robert/">Robert Jöhnk</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">23.12.1941</div>
  <div class="timeline-title"><a href="../bast-friedrich/">Friedrich Bast</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1942</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(4 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">06.01.1942</div>
  <div class="timeline-title"><a href="../hoelk-hans-detlef/">Hans Detlef Hölk</a></div>
  <div class="timeline-location">Ort: <em>den Kämpfen vor Sewastopol auf der Krim</em></div>
</div>

<div class="timeline-month-cluster">
  ⚡ Häufung: 2 Schicksale im Februar 1942
</div>

<div class="timeline-item">
  <div class="timeline-date">08.02.1942</div>
  <div class="timeline-title"><a href="../staude-bruno/">Bruno Staude</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">13.02.1942</div>
  <div class="timeline-title"><a href="../huelle-erich/">Erich Hülle</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">14.09.1942</div>
  <div class="timeline-title"><a href="../marxen-johannes/">Johannes Marxen</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1943</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">23.12.1943</div>
  <div class="timeline-title"><a href="../jensen-alfred/">Alfred Jensen</a></div>
  <div class="timeline-location">Ort: <em>Italien gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1944</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(5 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">14.01.1944</div>
  <div class="timeline-title"><a href="../joehnk-otto/">Otto Jöhnk</a></div>
  <div class="timeline-location">Ort: <em>Nikopol in Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">02.07.1944</div>
  <div class="timeline-title"><a href="../marxen-friedrich/">Friedrich Marxen</a></div>
  <div class="timeline-location">Ort: <em>Italien gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">23.08.1944</div>
  <div class="timeline-title"><a href="../hass-helmut/">Helmut Hass</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">22.11.1944</div>
  <div class="timeline-title"><a href="../schneider-walter/">Walter Schneider</a></div>
  <div class="timeline-location">Ort: <em>Russland gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">24.12.1944</div>
  <div class="timeline-title"><a href="../behrend-erwin/">Erwin Behrend</a></div>
  <div class="timeline-location">Ort: <em>Frankreich gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1945</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(4 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">18.02.1945</div>
  <div class="timeline-title"><a href="../radbruch-otto/">Otto Radbruch</a></div>
  <div class="timeline-location">Ort: <em>Russland verhungert</em></div>
</div>

<div class="timeline-month-cluster">
  ⚡ Häufung: 2 Schicksale im April 1945
</div>

<div class="timeline-item">
  <div class="timeline-date">11.04.1945</div>
  <div class="timeline-title"><a href="../goercke-erich/">Erich Görcke</a></div>
  <div class="timeline-location">Ort: <em>Russland gestorben</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">25.04.1945</div>
  <div class="timeline-title"><a href="../kuest-fritz/">Fritz Küst</a></div>
  <div class="timeline-location">Ort: <em>Bayern gefallen</em></div>
</div>

<div class="timeline-item">
  <div class="timeline-date">21.12.1945</div>
  <div class="timeline-title"><a href="../frohreich-arthur/">Arthur Frohreich</a></div>
  <div class="timeline-location">Ort: <em>Italien gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1947</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">10.02.1947</div>
  <div class="timeline-title"><a href="../pohl-heinz/">Heinz Pohl</a></div>
  <div class="timeline-location">Ort: <em>Rußland gefallen</em></div>
</div>

<div class="timeline-year-header">
  <span class="timeline-year-badge">1951</span>
  <span style="font-size: 0.75em; color: #57606a; font-weight: normal;">(1 Schicksale)</span>
</div>

<div class="timeline-item">
  <div class="timeline-date">16.11.1951</div>
  <div class="timeline-title"><a href="../stroeh-heinrich/">Heinrich Ströh</a></div>
  <div class="timeline-location">Ort: <em>den Kriegsfolgen</em></div>
</div>

</div>
