function validacionesDirecciones(nombre,correo) {
  let r_correo = /\S+@\S+\.\S+/;
    if (nombre.value === "" ) {
        Swal.fire({
          icon: "error",
          title: "<h4 style='color:red'>" + "Error..." +"</h4>",
          text: "Nombre o Correo inválido",                   
        });
        return false
      } else if (nombre.value === "" || !r_correo.test(correo.value)) {
        Swal.fire({
          icon: "error",
          title: "<h4 style='color:red'>" + "Error..." +"</h4>",
          text: "Nombre o Correo inválido",          
        });
        return false
    }else {
      return true
    }
   }