$(document).ready(function () {

    if (location.pathname === '/dashboard/article/new/') {
        let sumittedButton = $('#btnForm');
        let formCreateArticle = $('#art-form')
        Dropzone.autoDiscover = false;
        let dropzone = new Dropzone('#dropzone-image',{
        url:'***************',
        paramName: "images",
        autoProcessQueue: false,
        uploadMultiple: true,
        parallelUploads: 2,
        maxFilesize: 2,
        maxFiles: 3,
        acceptedFiles: 'image/png,image/jpeg,image/jpg',
        addRemoveLinks: true,
        dictRemoveFile: "<i class='fa-regular fa-trash-can'></i>",
        dictDefaultMessage: 'Déposez vos images ici ou cliquez pour télécharger',
        init: function () {
            sumittedButton.on('click',(e)=>{
                e.preventDefault();
                e.stopPropagation();

                if (dropzone.getQueuedFiles().length > 0) {
                    dropzone.getQueuedFiles().forEach((file)=> {
                        let dataTransfer = new DataTransfer();
                        dataTransfer.items.add(file);
                        let inputFile = document.createElement('input');
                        inputFile.type = 'file';
                        inputFile.name = 'images';
                        inputFile.files = dataTransfer.files;
                        inputFile.style.display = 'none';
                        formCreateArticle.append(inputFile);
                    } );
                    formCreateArticle.submit();
                } else {
                    formCreateArticle.submit();
                }
            });
        }
    })
    }else {
        let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        let articleItem = $('.article-item');
        let btnPopup = $('#popup-btn');
        let articleName = '';

        articleItem.each(function (){
            $(this).on('click',()=>{
                let item = $(this).data('filter');
                articleName = item.split('$');
                console.log(articleName)
                msg = `Article ${articleName[0]} sera supprimé définitivement.`
                modalPopupContent('danger','Êtes-vous sûr de vouloir supprimer ?',msg)
            });
        });

        btnPopup.on('click',()=>{
            const dataForm = new FormData();
            dataForm.append('csrfmiddlewaretoken',csrf);
            dataForm.append('id',articleName[1]);
            $.ajax({
                url:'/dashboard/article/',
                type: 'POST',
                data: dataForm,
                contentType: false,
                processData: false,
                complete: ()=> {
                    location.reload();
                }
            })
        })
    }

});