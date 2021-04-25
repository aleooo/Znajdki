const inputSearch = $('#input_search')
const listSearch = $('.list_search_objects')
const formSearch = $('#form_search')
const csrfToken = $('[name = csrfmiddlewaretoken]')[0].value

function sendSearchData(znajdka){
    $.ajax({
        type: 'POST',
        url: '/search/',
        data: {
            'csrfmiddlewaretoken': csrfToken,
            'znajdka': znajdka,
        },
        success: (list) => {
            items = list.data
            console.log(items)
            if(Array.isArray(items)) {
                jQuery.each(items, function (i, item){
                    listSearch.append(`<a href='' class='item'>
                                            <div class="row mt-2 mb-2">
                                                <div class="col-3">
                                                    <img src="`+ item.image +`" class="item-image">
                                                </div>
                                                <div class="col-2">
                                                    <h5>`+ item.title +`</h5>
                                                </div>
                                                <div class="col-5">
                                                    <h5>`+ item.publish +`</h5>
                                                </div>
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