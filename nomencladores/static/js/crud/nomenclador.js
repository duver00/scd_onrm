const NomencladorAdd = (btn, nomenclador_add, nombre, otro, url_add) => {
  d.addEventListener("click", (ev) => {
    let fd_add;   
    if (ev.target.matches(btn)) {
      fd_add = new FormData();
      if (nomenclador_add.attributes.getNamedItem("name").textContent ==="direcciones") {
        fd_add.append("ccsrfmiddlewaretoken", getCookie("csrftoken"));
        fd_add.append("nombre", nombre.value);
        fd_add.append("correo", otro.value);
        fd_add.append("action", nomenclador_add.value);
        if(validacionesDirecciones(nombre,otro)){
          conectar_api(url_add,fd_add)
        }       
      } else {
        fd_add.append("ccsrfmiddlewaretoken", getCookie("csrftoken"));
        fd_add.append("nombre", nombre.value);
        fd_add.append("action", nomenclador_add.value);
        if(validacionesOtros(nombre)){
          conectar_api(url_add,fd_add)
        }        
      }
    }
  });
};

