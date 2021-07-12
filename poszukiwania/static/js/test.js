$(document).ready(function (){
$('#id_text').setAttribute('width', '400')
})

let json = $('.json_form')
var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar'});
var m = L.map('map',   {center: [52.012, 21.922],
                            zoom: 13,
                            layers: [satellite]});
var baseMaps = {
    "Grayscale": satellite,
    "Streets": street}
var myIcon = L.icon({
    iconUrl:  "https://unpkg.com/leaflet@1.0.3/dist/images/marker-icon.png",
    iconSize: [20, 30],
      iconAnchor: [18, 18],
      popupAnchor: [0, -10],
      shadowSize: [0, 0],
      shadowAnchor: [10, 10]
});
L.control.groupedLayers(baseMaps).addTo(m);
var popup = L.popup();
function onMapClick(e) {
L.marker(e.latlng, {icon: myIcon}).addTo(m);
json.val(JSON.stringify(e.latlng))
}
m.on('click', onMapClick);

