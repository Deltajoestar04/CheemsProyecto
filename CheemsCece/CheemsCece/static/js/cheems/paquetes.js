function registrar(id) {
    var url = "/paquete-registro";  // Ruta para mostrar el formulario de registro de paquete
    $.get(url, function(data) {
        $('#modal_info').html(data);
        $('#modal_info').modal({ backdrop: 'static', keyboard: false });
        $('#modal_info').modal('show');
    });
}

function save() {
    const id_cliente = document.getElementById('form-id_cliente').value;  // Obtiene el ID del cliente
    const fecha_envio = document.getElementById('form-fecha_envio').value;  // Obtiene la fecha de envío
    const fecha_llegada = document.getElementById('form-fecha_llegada').value;  // Obtiene la fecha de llegada
    const tamano = document.getElementById('form-tamano').value;  // Obtiene el tamaño del paquete
    const codigo_paquete = document.getElementById('form-codigo_paquete').value;  // Obtiene el código del paquete
    const estado = document.getElementById('form-estado').value;  // Obtiene el estado del paquete

    // Datos del paquete a enviar al backend
    const data = { id_cliente, fecha_envio, fecha_llegada, tamano, codigo_paquete, estado };

    // Realiza una petición POST para guardar el paquete
    fetch('/paquete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 201) {
            alert('El paquete se guardó correctamente');
            location.reload();  // Recarga la página para mostrar el paquete registrado
        } else {
            alert(`Ocurrió un error al guardar: ${response.status}`);
        }
    })
    .catch(error => console.error('Error:', error));
}
