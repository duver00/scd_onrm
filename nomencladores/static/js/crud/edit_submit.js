const NomencladorEditedSubmit = (btn, nomenclador_selector, selector_direccion, input_nombre, input_otro, url_edited) => {
            d.addEventListener("click", ev => {
                ev.stopPropagation();
               if (ev.target.matches(btn)) {
                    let fd_edit;
                    fd_edit = new FormData;
                    if( nomenclador_selector.attributes.getNamedItem('name').textContent ==='direccion'){
                         fd_edit.append('ccsrfmiddlewaretoken', getCookie("csrftoken"));
                         fd_edit.append('nombre', input_nombre.value);
                         fd_edit.append('correo', input_otro.value);
                         fd_edit.append('pk', selector_direccion.value);
                         fd_edit.append('action', 'edited_direccion')
                         if(validacionesDirecciones(input_nombre,input_otro)){
                            conectar_api(url_edited,fd_edit)
                          }       
                    }else{
                         fd_edit.append('ccsrfmiddlewaretoken', getCookie("csrftoken"));
                         fd_edit.append('nombre', input_nombre.value);
                         fd_edit.append('pk', selector_direccion.value);
                         fd_edit.append('post_action',nomenclador_selector.attributes.getNamedItem('name').textContent);
                         if(validacionesOtros(input_nombre)){
                            conectar_api(url_edited,fd_edit)
                        }                                
                    }               
                }
            });
        };
