$(document).ready(function() {
    let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let customerItem = $('.customer-item');
    let inputName = '';
    let btnModal = $('.btn-modal-submitted');
    let bodyModal = $('#modal-body');
    let baseField = [
        {'label':'Nom utilisateur','name':'username','field':'text'},
        {'label':'Adresse email','name':'email','field':'email'},
        {'label':'Numéro de téléphone','name':'phone','field':'tel'},
    ]

    customerItem.each(function() {
        $(this).on('click',()=>{
            let item = $(this).data('filter');
            inputName = item.split('$');
            let inputField = [];

            for (let i=1; i < inputName.length; i++) {
                inputName[i] === 'None' ? inputName[i]='' : '';
                field = {'title':`${inputName[i]}`,'label':`${baseField[i-1].label}`,'name':`${baseField[i-1].name}`,'field':`${baseField[i-1].field}`}
                inputField.push(field)
            }
            modalTitleContent(inputField[0])
            modalBodyContent(inputField,'field-content')
        })
    });


    btnModal.on('click',(e)=>{
            e.preventDefault();
            e.stopPropagation();

            let dataForm = new FormData();
            dataForm.append('csrfmiddlewaretoken',csrf);
            dataForm.append('id',inputName[0]);
            for (let i = 0; i < baseField.length; i++) {
                dataForm.append(baseField[i].name, $(`#${baseField[i].name}`).val())
            }

            $.ajax({
                type: 'POST',
                url: '/dashboard/customer/',
                data: dataForm,
                contentType: false,
                processData: false,
                success: (res)=> {
                    console.log(res)
                },
                error: (err) => {
                    console.log(err)
                }
            })

    })

});