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
});