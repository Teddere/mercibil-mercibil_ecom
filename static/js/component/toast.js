function generateToast(message,status='info',icon='fa-circle-check') {
    status === 'info' ? status='primary' : ''
    let content = `
            <div id="toast-message" class="toast fade show mb-2" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-body">
                    <div class="d-flex gap-4">
                    <span class="text-${status}"><i class="fa-solid ${icon}  fa-lg"></i></span>
                    <div class="d-flex flex-grow-1 align-items-center">
                        <span class="fw-semibold">${message}</span>
                        <button type="button" class="btn-close btn-close-sm btn-close-black ms-auto" data-bs-dismiss="toast"
                          aria-label="Close"></button>
                    </div>
            </div>
        </div>
    </div>`
    let toast = $(content);
    $('.toast-container').fadeIn(300,function (){
        $('.toast-container').append(toast)
    });

    setTimeout(()=>{
        toast.fadeOut('slow',function() {
            toast.remove()
        })
    },5000)

}