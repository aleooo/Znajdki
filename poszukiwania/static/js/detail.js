let fimage = $('.image_detail')

fimage.click(function (){
    if(fimage.hasClass('enlarged')){
        fimage.removeClass('enlarged');
        fimage.stop().animate({width: '20rem', height: '20rem'}, 200 );
    }else{
        fimage.addClass('enlarged')
        fimage.stop().animate({width: 800, height: 800}, 200 );
    }
});

