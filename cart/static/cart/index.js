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
    // input
    function debounce(func,wait) {
        let timeout;
        return function(...args) {
            const context = this;
            clearTimeout(timeout);
            timeout = setTimeout(()=>{
                func.apply(context,args)
            },wait);
        }

    }
    $('.cart-qte-num').each(function() {
        $(this).on('input',debounce(function() {
            let qty = $(this).val();
            let stock = parseInt($(this).attr('max'));
            let item = $(this).next().data('filter');
            if ((qty >= 1 && qty <= stock) && qty !== '' ) {

                let dataForm = new FormData();
                dataForm.append('csrfmiddlewaretoken',csrf);
                dataForm.append('article_id',item);
                dataForm.append('article_qty',qty)
                dataForm.append('article_override',true);
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
            }
            else if(qty > stock) {
                generateToast(`Stock de cette article est inférieur à ${qty} article(s)`,'warning','fa-triangle-exclamation')
            }

        },500))
    });

});
