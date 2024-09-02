$(document).ready(function() {
    let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let customerItem = $('.customer-item');
    let btnModal = $('.btn-modal-submitted');
    let bodyModal = $('#modal-body');
    let inputItem = '';
    let baseField = [
        {'label':'Nom utilisateur','name':'username','field':'text'},
        {'label':'Adresse email','name':'email','field':'email'},
        {'label':'Numéro de téléphone','name':'phone','field':'tel'},
    ]

    // Customer item click
    customerItem.each(function () {
        $(this).on('click', ()=>{
            let inputField = []
            let item = $(this).data('filter');
            inputItem = item.split('$');

            if (inputItem.length > 1) {
                for(let i= 1; i < inputItem.length; i++) {
                    inputItem[i] === 'None' ? inputItem[i] = '': ''
                    let field = {
                        'title': inputItem[i],
                        'label': `${baseField[i-1].label}`,
                        'name':`${baseField[i-1].name}`,
                        'field':`${baseField[i-1].field}`
                    }
                    inputField.push(field)
                }
            }
            else {
                for (let i = 0; i < baseField.length; i++) {
                    let field = {
                        'title':'','label':`${baseField[i].label}`,
                        'name':`${baseField[i].name}`,
                        'field':`${baseField[i].field}`
                    }
                    inputField.push(field)
                }
            }
            modalTitleContent(inputItem[0]);
            modalBodyContent(inputField,'field-content')
        });
    });

    // Create customer & update customer
    btnModal.on('click',(e)=>{
        e.preventDefault();
        e.stopPropagation();
        let dataForm = new FormData();
        // Update customer
        inputItem.length > 1 ? dataForm.append('id',inputItem[0]): ''
        // update & create customer
        dataForm.append('csrfmiddlewaretoken',csrf);
        for (let i=0; i < baseField.length; i++) {
            dataForm.append(baseField[i].name,$(`#${baseField[i].name}`).val())
        }
        $.ajax({
            type: 'POST',
            url: '/dashboard/customer/',
            data: dataForm,
            contentType: false,
            processData: false,
            success: (res)=>{
                location.reload()
            },
            error: (err)=>{
                bodyModal.prepend(alertBoxContent(err.responseJSON.status,err.responseJSON.message));
            }
        })
    });
});