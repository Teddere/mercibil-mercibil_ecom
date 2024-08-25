$(document).ready(function() {


    // Product + / -
    $('.cart-btn-down').on('click',function (){
        let numProduct=Number($(this).next().val());
        if(numProduct > 0)$(this).next().val(numProduct - 1)
    });
    $('.cart-btn-up').on('click',function (){
        let numProduct=Number($(this).prev().val());
        $(this).prev().val(numProduct + 1)
    });
});