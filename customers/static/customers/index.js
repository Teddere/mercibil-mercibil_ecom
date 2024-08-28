$(document).ready(function() {

    let customerItem = $('.customer-item');
    let inputName = '';
    let inputField = []
    let btnModal = $('.btn-modal-submitted');
    let bodyModal = $('#modal-body');
    let baseField = [
        {'username':'Nom utilisateur','field':'text'},
        {'email':'Adresse email','field':'email'},
        {'tel':'Numéro de téléphone','field':'tel'}
    ]

    customerItem.each(function() {
        $(this).on('click',()=>{
            let item = $(this).data('filter');
            inputName = item.split('$');

            let fileField = {'title': '' ,'label': ' ','name': 'image','field': 'file'}
            for (let i=0; i < inputName.length - 1; i++) {
                field = {'title':`${inputName[i]}`,'label':``,'name':`${Object.keys(baseField[i][0])}`,'field':`${baseField[ Object.keys(baseField[i][1]) ]}`}
                inputField.push(field)
            }
            inputField.push(fileField);
            modalTitleContent(inputName[0])
            modalBodyContent(inputField,'field-content')
        })
    });
});