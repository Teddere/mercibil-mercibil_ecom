$(document).ready(function() {
    let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    // Create and update
    let categoryItem = $('.category-item');
    let btnModal = $('.btn-modal-submitted');
    let bodyModal = $('#modal-body');
    // Delete
    let categoryElement = $('.category');
    let btnPopup = $('#popup-btn');

    let itemName = '';

    categoryItem.each(function () {
        $(this).on('click',()=>{
            document.querySelector('#modal-body .alert') ? $('#modal-body').children().first().remove() : '';

            let item = $(this).data('filter');

            itemName = item.split('$');

            let file = '';

            itemName[0] ? file= 'Changez l\'image' : file = 'Ajoutez une image'

            let inputField = [
                {'title': itemName[0],'label': 'Catégorie','name': 'category','field': 'text'},
                {'title': '' ,'label': file,'name': 'image','field': 'file'}
            ]
            modalTitleContent(itemName[0])
            modalBodyContent(inputField,'field-content')
        });
    });

    btnModal.on('click',(e)=>{
        e.preventDefault();
        e.stopPropagation()
        let dataForm = new FormData();
        dataForm.append('csrfmiddlewaretoken',csrf);
        dataForm.append('id',itemName[1]);

        dataForm.append('name',$('.input-name').val());
        dataForm.append('image',document.getElementById('image').files[0])
        $.ajax({
                type: 'POST',
                url: `/dashboard/article/category/`,
                data: dataForm,
                contentType: false,
                processData: false,
                success: (res) => {
                    location.reload()
                },
                error: (err) => {
                  bodyModal.prepend(alertBoxContent(err.responseJSON.status,err.responseJSON.message))
                }
            })
    })

    categoryElement.each(function () {
        $(this).on('click',()=>{
            let item = $(this).data('filter');
            itemName = item.split('$');
            let msg = `La catégorie ${itemName[0]} va être définitivement supprimer.`
            modalPopupContent('danger','Êtes-vous de vouloir supprimer ?',msg);
        })
    });

    btnPopup.on('click',()=>{
        let dataForm = new FormData();
        dataForm.append('csrfmiddlewaretoken',csrf);
        dataForm.append('id',itemName[1]);

        $.ajax({
            type: 'POST',
            url: '/dashboard/article/category/delete/',
            data: dataForm,
            contentType: false,
            processData: false,
            complete: ()=> {
                location.reload();
            }
        })

    });
});