const inputSearch = $('#input_search')
const listSearch = $('.list_search_objects')
const formSearch = $('#form_search')
const csrfToken = $('[name = csrfmiddlewaretoken]')[0].value
// let getSidebar = $('.sidebar');
// var mymap = L.map('Mapa')

function sendSearchData(znajdka){
    $.ajax({
        type: 'POST',
        url: '/en/search/',
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'znajdka': znajdka,
        },
        success: (list) => {
            listSearch.append(`<div id="light">
                                    <table style="width:100%">
                                         <tr>
                                            <td  class="td">Obverse</td>
                                            <td  class="td">Reverse</td>
                                            <td  class="td">Name</td>
                                            <td class="td">Publish</td>
                                         </tr></table></div> `)
            items = list.data
            if(Array.isArray(items)) {
                jQuery.each(items, function (i, item){
                    var color = ''
                    if(i % 2 === 0) color = 'light';
                    else color = 'dark'
                    listSearch.append(`<a href="`+ item.url +`"  class='item'>
                                            <div class="row " id="`+ color +`">
                                                 <table style="width:100%">
                          <tr>
                            <td class="td"><img src="`+ item.image_obverse +`" class="item-image"></td>
                            <td class="td"><img src="`+ item.image_reverse +`" class="item-image"></td>
                                              <td  class="td">  `+ item.name +`</td>
                                               <td class="td">`+ item.publish +`</td>
                                                 </tr>
                        </table>
                                            </div>
                                        </a>`)})

                }
            },
        error: (err) => {
            console.log(err)
        }
    })
}
    inputSearch.keyup(w => {
    const words = w.target.value
    if(words.length > 0){
        listSearch.removeClass('not-visible')
    }
     listSearch.html('')
    sendSearchData(words)

})

$(window).click(function (){
    listSearch.addClass('not-visible')
})
let getSidebar = document.querySelector('.sidebar');
let spaceFunction = document.querySelector('.space_function')
let getSidebar1 = $('.sidebar')
let sidebarStatus = false
var colFunction = $('#colFunction')

var latestObject = $('#latest_objects')
function sidebar(){
     getSidebar.style.width = colFunction.width().toString() + 'px';
     spaceFunction.style.height = latestObject.height().toString()-50 + 'px';
    if (sidebarStatus === false){
        // getSidebar.style.visibility = 'visible';
        getSidebar.style.opacity = '1';
        sidebarStatus = true
        }
    else{
        getSidebar.style.width = '0';
        // getSidebar.style.visibility = 'hidden';
        getSidebar.style.opacity = '0';
        sidebarStatus = false
    }
}
function styleFunction (style){
    $.ajax({
        type: 'POST',
        url: '/en/style/',
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'type': style
        },
        success: (list) => {
            window.location.reload()
        },
        error: (err) => {
            console.log(err)
            }
    })
}
// function maps_type(type){
//     if(type === 'satelite'){
//         L.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}').addTo(map)
//     }
//     else{
//         L.TileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}').addTo(map)
//     }
// }