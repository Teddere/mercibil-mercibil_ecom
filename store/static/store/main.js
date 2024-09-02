$(document).ready(function () {
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
                    console.log(res)
                    document.getElementById('cart_num_total').textContent = res.quantity
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })
        });
    });
});