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
});