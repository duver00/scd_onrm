function validacionesOtros(nombre) {
    if (nombre.value === "" ) {
        Swal.fire({
          icon: "error",
          title: "<h4 style='color:red'>" + "Error..." +"</h4>",
          text: "Debe escribir un nombre",                   
        });
        return false
    }
    return true
}