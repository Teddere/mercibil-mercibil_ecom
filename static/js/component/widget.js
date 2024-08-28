// title modal
function modalTitleContent(title = ''){
    let titleModal = $('.modal-title');
    title === '' ? titleModal.html('Nouveau') : titleModal.html('Modification');
}
// modal items modal
function modalBodyContent(items,element) {
    let itemBox = $(`#${element}`);
    itemBox.empty();
    for (let i = 0; i < items.length; i++) {
        let box = $(`
                    <div class="form-group mb-3">
                        <label for="${items[i].name}" class="form-label">${items[i].label}</label>
                        <input type="${items[i].field}" name="${items[i].name}" id="${items[i].name}" class="form-control input-name" value="${items[i].title}">
                    </div>
        `);
        itemBox.append(box)
    }
}
// modal popup

function modalPopupContent (status,title,msg) {
    let button= $('#popup-btn');
    let body = $('#popup-body');

    document.querySelector('#popup-body svg') ? body.children().first().remove() :''
    if (status === 'success') {
        $('#popup-status').addClass('bg-success');
        button.addClass('btn-success');
        button.html('Valider')
        body.prepend(
            `<svg xmlns="http://www.w3.org/2000/svg" class="icon mb-2 text-green icon-lg" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
                <path d="M9 12l2 2l4 -4" />
            </svg>`
        )
    } else {
        $('#popup-status').addClass('bg-danger');
        button.addClass('btn-danger');
        button.html('Supprimer')
        body.prepend(
            `<svg xmlns="http://www.w3.org/2000/svg" class="icon mb-2 text-danger icon-lg" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M10.24 3.957l-8.422 14.06a1.989 1.989 0 0 0 1.7 2.983h16.845a1.989 1.989 0 0 0 1.7 -2.983l-8.423 -14.06a1.989 1.989 0 0 0 -3.4 0z"></path>
                <path d="M12 9v4"></path>
                <path d="M12 17h.01"></path>
            </svg>`
        )
    }
    $('#popup-msg').html(msg)
    $('#popup-title').html(title);
}

// Alert box

function alertBoxContent (status,msg) {
    let statusIcon ='';
    if (status === 'success') {
        statusIcon= `<svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M5 12l5 5l10 -10"></path>
                    </svg>`
    }else if (status === 'warning') {
        statusIcon = `<svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M10.24 3.957l-8.422 14.06a1.989 1.989 0 0 0 1.7 2.983h16.845a1.989 1.989 0 0 0 1.7 -2.983l-8.423 -14.06a1.989 1.989 0 0 0 -3.4 0z"></path>
                        <path d="M12 9v4"></path>
                        <path d="M12 17h.01"></path>
                    </svg>`
    }else {
        status= 'danger'
        statusIcon = `<svg xmlns="http://www.w3.org/2000/svg" class="icon alert-icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"></path>
                        <path d="M12 8v4"></path>
                        <path d="M12 16h.01"></path>
                    </svg>`
    }

    return `
        <div class="alert alert-important alert-${status} alert-dismissible" role="alert">
            <div class="d-flex">
                <div>${statusIcon}</div>
                <div>${msg}</div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="close"></button>
            </div>
        </div>
    `
}

