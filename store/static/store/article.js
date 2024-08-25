$(document).ready(function () {
    let sw_small = new Swiper('.detail-article',{
        spaceBetween: 10,
        slidesPerView: 4,
        freeMode: true,
        watchSlidesProgress: true,
    })

    let sw_large = new Swiper('.detail-slide',{
        loop:true,
        spaceBetween: 30,
        effect: "fade",
        crossFade: true,
        navigation:{
            nextEl:'.sw-next',
            prevEl:'.sw-prev',
        },
        thumbs: {
            swiper: sw_small,
        },
    })

    // Open modal image
    $('.detail-slide').magnificPopup({
        delegate:'a',
        type:'image',
        gallery: {
          enabled: true
        },
        mainClass:'mfp-fade'
    });
    // Product + / -
    $('.btn-num-down').on('click',function (){
        let numProduct=Number($(this).next().val());
        if(numProduct > 0)$(this).next().val(numProduct - 1)
    });
    $('.btn-num-up').on('click',function (){
        let numProduct=Number($(this).prev().val());
        $(this).prev().val(numProduct + 1)
    });
});