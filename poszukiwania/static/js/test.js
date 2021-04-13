$(document).ready(function (){
             var map = L.map('map', {minZoom: 14,
    }).setView([52.011217, 21.921226], 0);
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    }).addTo(map);
    var popup = L.popup();
    function onMapClick(e) {
    popup.setLatLng(e.latlng).setContent( e.latlng.toString()).openOn(map);
    var json = {'type': 'Point', 'coordinates': [e.latlng.lng, e.latlng.lat]};
    console.log(json)
        var txt = document.getElementById('id_geolokalizacja');
    txt.innerHTML = JSON.stringify(json)
    // $('#id_geolokalizacja').innerHTML = JSON.stringify(json)

}

map.on('click', onMapClick);
})