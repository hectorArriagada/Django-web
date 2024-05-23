$(document).ready(function(){
    $("#btn-ingresar").click(function() {
        let user = $("#username").val();
        let pass = $("#pass").val();

        let resultado = validar(user,pass);
    });

    function validar(user, pass) {
        if (String(user).length < 9 && String(user).length > 10) {
            $(".resultado").html("<div class='alert alert-danger w-50 mx-auto text-center'>Email debe tener largo entre 9 y 10 caracteres</div>");
        } else if (String(pass).length < 9 && String(pass).length > 20) {
            $(".resultado").html("<div class='alert alert-danger w-50 mx-auto text-center'>Clave debe tener largo entre 9 y 20 caracteres</div>");
        }else{
            $(".resultado").html("<div class='alert alert-success w-50 mx-auto text-center'>Acceso concedido</div>");
        }
    }
});