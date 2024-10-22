document.getElementById('logout-button').addEventListener('click', function () {
    Swal.fire({
        title: 'Are you sure?',
        text: 'You will lose your current ',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = '/logout/';  
        }
    });
});