function validar(form){
    var telefono=form.telefono.value;
    var password=form.password.value;
    var mensaje=validarTelefono(telefono);
    mensaje+=validarLongitudPassword(password);
    mensaje+=passwordRobusto(password);
    var div=document.getElementById("notificaciones");
    var ban=false;
    if(mensaje!=""){
        div.innerHTML=mensaje;
        ban=false;
    }
    else{
        div.innerHTML="";
        ban=true;
    }
    return ban;
}
function validarTelefono(cadena){
    var patron=/[0-9]{3}-[0-9]{3}-[0-9]{4}/
    var ban=patron.test(cadena);
    var salida="";
    if(ban==false){
        salida='Debes informar un numero telefonico con el siguiente patron ###-###-#### <br>';
    }
    return salida;
}
function validarLongitudPassword(cadena){
    var salida="";
    if(cadena.length<8){
        salida='Debes informar un password de al menos 8 caracteres <br>'
    }
    return salida;
}
function tieneDigito(cadena){
    var ban=false;
    for(i=0;i<cadena.length;i++){
        var cod=cadena.charCodeAt(i);
        if(cod>=48 && cod<=57){
            ban=true;
            break;
        }
    }
    return ban;
}
function passwordRobusto(cadena){
    var salida="";
    if(!tieneDigito(cadena)){
        salida='El password debe incluir al menos un digito <br>';
    }
    return salida;
}