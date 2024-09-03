$(document).ready(function() {


    // Product + / -
    $('.cart-btn-down').on('click',function (){
        let inputField = $(this).next();
        let item = $(this).data('filter');
        let num_art = Number(inputField.val());
        let dataForm = new FormData();
            dataForm.append('csrfmiddlewaretoken',csrf);
            dataForm.append('article_id',item);
            dataForm.append('action','post')
        if(num_art > 1) {
            inputField.val(num_art - 1);
            // Ajax
            $.ajax({
                type: 'POST',
                url: '/cart/update/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: function (res){
                    //document.getElementById('cart_num_total').textContent = res.quantity
                    location.reload();
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })
        }
        else if (num_art <= 1) {
            $.ajax({
                type: 'POST',
                url: '/cart/delete/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: function (res){
                    //document.getElementById('cart_num_total').textContent = res.quantity
                    location.reload();
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })
        }
    });

    $('.cart-btn-up').on('click',function (){
        let inputField = $(this).prev();
        let item = $(this).data('filter');
        let num_art = Number(inputField.val())
        let maxStock = Number(inputField.attr('max'));
        if (num_art < maxStock) {
            inputField.val(num_art + 1);

            let dataForm = new FormData();
            dataForm.append('csrfmiddlewaretoken',csrf);
            dataForm.append('article_id',item);
            dataForm.append('action','post')
            // Ajax
            $.ajax({
                type: 'POST',
                url: '/cart/add/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: function (res){
                    //document.getElementById('cart_num_total').textContent = res.quantity
                    location.reload();
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })

        }else {
            generateToast('Stock maximum atteint pour cet article','warning','fa-triangle-exclamation')
        }

    });

    // Remove item
    $('.cart-image').on('click',function () {
       let item = $(this).data('filter');
       let dataForm = new FormData();
       dataForm.append('csrfmiddlewaretoken',csrf);
       dataForm.append('article_id',item);
       dataForm.append('action','post')
        $.ajax({
                type: 'POST',
                url: '/cart/delete/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: function (res){
                    //document.getElementById('cart_num_total').textContent = res.quantity
                    location.reload();
                },
                error: function (xhr,errmsg,err){
                    console.log(err)
                }
            })

    })


});
