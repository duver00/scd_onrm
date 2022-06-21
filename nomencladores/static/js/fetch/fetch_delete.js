async function api_delete(url,form) {
    const request = new Request(
        url,
        {
            headers: {'X-CSRFToken': getCookie("csrftoken")},
            'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
            'Content-Type': 'x-www-form-urlencoded'
        }
    );
    await fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        cache: 'no-cache',
        body: form,
    })
    .then(response => response.json())
        .then(data => {
            console.log(data);
            Swal.fire({
               icon: 'success',
               title: 'Eliminado exitosamente',
               showConfirmButton: true,
                }).then(function () {
                 location.reload()
                });
        })
        .catch((error) => {
            console.log(error);
        });
}