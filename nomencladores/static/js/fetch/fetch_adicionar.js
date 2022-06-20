 async function conectar_api(url,form) {
    const request = new Request(url, {
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        Accept:
          "application/json, application/xml, text/plain, text/html, *.*",
        "Content-Type": "x-www-form-urlencoded",
      });
      await fetch(request, {
        method: "post",
        mode: "same-origin",
        body: form,
      })
        .then((response) => response.json())
        .then((data) => {
          Swal.fire({
            icon: "success",
            title: "Documento guardado exitosamente",
            showConfirmButton: true,
          }).then(function () {
            location.reload();
          });
        })
        .catch((error) => {
          console.log(error);
          Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Algo salió mal!",
            footer: error,
          });
        });
    
}