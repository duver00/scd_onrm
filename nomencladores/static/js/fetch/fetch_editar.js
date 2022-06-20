function conectar_api_editar(url,form,edit_nombre,edit_correo) {
    const request = new Request(
        url,
        {
            headers: {'X-CSRFToken': getCookie("csrftoken")},
            'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
            'Content-Type': 'x-www-form-urlencoded'
        }
    );
    fetch(request, {
        method: 'post',
        cache: 'no-cache',
        mode: 'same-origin',
        body: form,

    })
        .then(response => response.json())
        .then(data => {
            if (Object.keys(data).length === 3) {
                edit_nombre.value = data['nombre'];
                edit_correo.value = data['correo'];
            } else if (Object.keys(data).length  === 2) {
                edit_nombre.value = data['nombre'];
            }

        })
        .catch((error) => {
            console.log(error);
        });
    
}