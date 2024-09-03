$(document).ready(function (){
    $('#btn-toggle').on('click',()=>{
        $("#nav-menu").slideToggle(700);
    });
     // Set background image
  $(".set-bg").each(function () {
    let bg = $(this).data("bg");
    $(this).css("background-image", `url('${bg}')`);
  });
  // Fixed header
    let headContainer = $('.header-section');
    let navTopMenu = $('.nav-top');
    let sizeHeader = navTopMenu.height() + $('.nav-main').height();

    $(window).on('scroll',function (){
      if((this).scrollY > sizeHeader) {
        headContainer.addClass('fixed-header');
        navTopMenu.hide('slow')
      }else{
        headContainer.removeClass('fixed-header')
        navTopMenu.show('slow')
      }
    });

    // Footer
  document.querySelector('#copyright-date').innerHTML=new Date().getFullYear();
    // Button add cart
  if(document.querySelectorAll('.addCart')){
    let btnCart = $('.addCart');
    btnCart.each(function() {
        $(this).on('click',(e)=>{
            e.preventDefault();
            let item = $(this).data('article');
            let dataForm = new FormData();
            dataForm.append('csrfmiddlewaretoken',csrf);
            dataForm.append('article_id',item);
            dataForm.append('action','post')
            $.ajax({
                type: 'POST',
                url: '/cart/add/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: function (res){
                    document.getElementById('cart_num_total').textContent = res.quantity
                    generateToast("Article ajouté au panier",)
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })


        });
    });
  }
});