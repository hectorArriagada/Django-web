$(document).ready(function(){

    $("#btn-registrar").click(function() {

        // JSON para guardar el usuario
        let usuario = {
            "Rut": "",
            "Nombre": "",
            "Appaterno": "",
            "Apmaterno": "",
            "Clave": "",
            "Fecnac": "",
            "Edad": "",
            "Genero": "",
            "Correo": "",
            "Telefono": ""
        }

        let rut = $("#rut").val();
        let nombre = $("#nombre").val();
        let appaterno = $("#appaterno").val();
        let apmaterno = $("#apmaterno").val();
        let clave = $("#clave").val();
        let fecnac = $("#fechanac").val();
        let edad = $("#edad").val();
        let genero = $("#genero").val();
        let correo = $("#correo").val();
        let telefono = $("#telefono").val();

        // Se validan los datos
        let resultado = validarUsuario(rut, nombre, appaterno, apmaterno, clave, edad, telefono);
        if (resultado) {
            $("#check").html("<div class='alert alert-success w-50 mx-auto text-center'>Registro completo</div>");
        }      

        // Se valida el correo
        if (validarCorreo(correo)) {

        } else {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>El correo debe ser Gmail.com, Hotmail.com o Duoc.cl</div>");
        }


        // Se guardan los datos
        usuario.Rut = rut;
        usuario.Nombre = nombre;
        usuario.Appaterno = appaterno;
        usuario.Apmaterno = apmaterno;
        usuario.Clave = clave;
        usuario.Fecnac = fecnac;
        usuario.Edad = edad;
        usuario.Genero = genero;
        usuario.Correo = correo;
        usuario.Telefono = telefono;

    });


    function validarUsuario(rut, nombre, appaterno, apmaterno, clave, edad, telefono) {
        // Se valida el rut
        if (String(rut).length < 9 || String(rut).length > 10) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>Rut minimo 9 y máximo 10 caracteres</div>");

        // Se valida el nombre
        } else if (String(nombre).length < 3 || String(nombre).length > 25) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>El nombre debe contener entre 3 y 25 caracteres</div>");
        
        // Se valida el Apellido paterno
        } else if (String(appaterno).length < 3 || String(appaterno).length > 25) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>El Apellido paterno debe contener entre 3 y 25 caracteres</div>");
        
        // Se valida el Apellido materno
        } else if (String(apmaterno).length < 3 || String(apmaterno).length > 25) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>El Apellido materno debe contener entre 3 y 25 caracteres</div>");
        
        // Se valida la clave
        } else if (String(clave).length < 3 || String(clave).length > 25) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>La clave debe contener al menos 9 caracteres</div>");

        // Se valida la edad
        } else if (Number(edad) < 18) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>Debes ser mayor de edad para registrarte</div>");
        
        // Se valida el telefono
        } else if (Number(telefono).length < 9 || Number(telefono).length > 12) {
            $("#check").html("<div class= 'alert alert-danger w-50 mx-auto text-center'>Debes ingresar un teléfono de 9 digitos</div>");
        
        // Acceso correcto    
        } else {
            return true;
        }
    }


    // funcion para validar el correo con una expresion regular
    function validarCorreo(correo) {
        let regex = /^[a-zA-Z0-9._-]+@(gmail\.com|hotmail\.com|duoc\.cl)$/;
        return regex.test(correo);
    }



});