const NomencladorEdit = (btn, nomenclador, edit_nombre, edit_correo, url_edit) => {
    d.addEventListener("click", ev => {
                let fn;
                if (ev.target.matches(btn)) {
                    fn = new FormData;
                    fn.append('ccsrfmiddlewaretoken', getCookie("csrftoken"));
                    fn.append('pk', nomenclador.value);
                    fn.append('nombre', nomenclador.attributes.getNamedItem('name').textContent);
                    conectar_api_editar(url_edit,fn,edit_nombre,edit_correo)
                }
            });
        };




