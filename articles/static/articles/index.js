$(document).ready(function () {
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
});