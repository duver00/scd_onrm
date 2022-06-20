const NomencladorDelete = (btn, nomenclador_delete, url_delete) =>{
            d.addEventListener("click", ev => {
                let fd;
                if(ev.target.matches(btn)) {
                    Swal.fire({
                      title: 'Desea eliminar '+ nomenclador_delete.attributes.getNamedItem('name').textContent+'?',
                      text: "Si acepta no se podrá revertir el proceso",
                      icon: 'warning',
                      showCancelButton: true,
                      confirmButtonColor: '#3085d6',
                      cancelButtonColor: '#d33',
                      confirmButtonText: 'Si, elimínalo!',
                      cancelButtonText: "Cancelar",
                    }).then((result) => {
                      if (result.isConfirmed) {
                           fd = new FormData;
                           fd.append('ccsrfmiddlewaretoken', getCookie("csrftoken"));
                           fd.append('valor', nomenclador_delete.value);
                           fd.append('direccion',nomenclador_delete.attributes.getNamedItem('name').textContent);                           
                            api_delete(url_delete,fd)
                        }
                    })

                }
            })
        };
