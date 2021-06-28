const inputSearch = $('#input_search')
const listSearch = $('.list_search_objects')
const formSearch = $('#form_search')
const csrfToken = $('[name = csrfmiddlewaretoken]')[0].value
// var mymap = L.map('Mapa')

function sendSearchData(znajdka){
    $.ajax({
        type: 'POST',
        url: '/search/',
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
$('#category_selected').click(function (){
    category = window.location.href.split('/')[3]
    if(category != 'catalog'){
        // $('#'+category).attr('selected','selected')
    }
    console.log()
})
$(window).click(function (){
    listSearch.addClass('not-visible')
})

// $('#select_style').