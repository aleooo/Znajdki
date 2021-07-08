$(document).ready(function (){
$('#id_text').setAttribute('width', '400')

})

// id_geolocation_div_map
// id_geolocation_map
// ol-unselectable
// var m = L.map('id_geolocation_map');
//
// L.map.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
// ).addTo(m);


// var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/' +
//                                         'World_Imagery/MapServer/tile/{z}/{y}/{x}');
//                                 var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar'});
//                                    var m = L.map('id_geolocation_map',   {center: [52.012, 21.922],
//                                                             zoom: 13,
//                                                             layers: [satellite]});
//                                 var baseMaps = {
//                                     "Grayscale": satellite,
//                                     "Streets": street}
//
//                                 L.control.groupedLayers(baseMaps).addTo(m);
//                                 var popup = L.popup();
//                                 function onMapClick(e) {
//     popup.setLatLng(e.latlng).setContent("You clicked the map at " + e.latlng.toString()).openOn(m);
// }
//
// m.on('click', onMapClick);
//
