var $ = jQuery.noConflict();

let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


function registrar() {
    activarBoton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje)
            setTimeout(() => {
                redirigirCrear(response.url);
            }, 10)
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}

function consultar() {
    activarBoton();
    $.ajax({
        data: $('#form_consulta').serialize(),
        url: $('#form_consulta').attr('action'),
        type: $('#form_consulta').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje)
            setTimeout(() => {
                redirigirCrear(response.url);
            }, 10)
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}

function editar(){
    activarBoton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(() => {
                cerrar_modal_edicion();
                redirigirEditar();
            }, 10)
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        }
    });
}

// SweetAlerts

function notificacionError(mensaje){
	Swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}

function notificacionSuccess(mensaje) {

	Swal.fire({
		title: 'Buen Trabajo!',
		text: mensaje,
		icon: 'success'
	})
}

function redirigirCrear(url) {
    window.location.href = url;
}

function redirigirEditar() {
    location.reload();
}

function mostrarErroresCreacion(errores){
	$('#errores').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errores').append(error);
}

function mostrarErroresEdicion(errores) {
	$('#erroresEdicion').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#erroresEdicion').append(error);
}

function activarBoton(){
	if($('#boton_creacion').prop('disabled')){
		$('#boton_creacion').prop('disabled',true);
	}else{
		$('#boton_creacion').prop('disabled', false);
	}
}

function abrir_modal(url) {
	$('#modal').load(url, function () {
        $(this).modal('show');
	});
}

function abrir_modal_edicion(url) {
	$('#edicion').load(url, function () {
        $(this).modal('show');
	});
}

function cerrar_modal() {
	$('#modal').modal('hide');
}

function cerrar_modal_edicion() {
	$('#edicion').modal('hide');
}