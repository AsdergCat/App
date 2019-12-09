
window.onload = function () {
	document.getElementById("id_password1").onchange = validatePassword;
	document.getElementById("id_password2").onchange = validatePassword;
}

function validatePassword(){
    var pass2=document.getElementById("id_password2");
    var pass1=document.getElementById("id_password1");

    if(pass1.value!=pass2.value)
        pass2.setCustomValidity("Las contraseñas no coinciden");
    else{
        pass2.setCustomValidity('');

        if(pass1.value.length < 8)
            pass2.setCustomValidity("La contraseña debe tener al menos 8 caracteres");
        else
            pass2.setCustomValidity('');
    }
}