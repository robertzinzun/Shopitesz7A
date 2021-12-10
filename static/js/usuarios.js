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
        salida='Debes informar un numero telefonico con el siguiente patron: ###-###-####. <br>';
    }
    return salida;
}
function validarLongitudPassword(cadena){
    var salida="";
    if(cadena.length<8){
        salida='Debes informar un password de al menos 8 caracteres. <br>'
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
        salida='El password debe incluir al menos un digito. <br>';
    }
    if(!tieneMayuscula(cadena)){
        salida+='El password debe incluir al menos una letra en Mayuscula. <br>';
    }
    if(!tieneCaracterEspecial(cadena)){
        salida+='El password debe incluir al menos un caracter especial. <br>';
    }
    return salida;
}
function tieneMayuscula(cadena){
    var ban=false;
    for(i=0;i<cadena.length;i++){
        var cod=cadena.charCodeAt(i);
        if((cod>=65 && cod<=90) || cod==165 ){
            ban=true;
            break;
        }
    }
    return ban;
}
function tieneCaracterEspecial(cadena){
    var ban=false;
    for(i=0;i<cadena.length;i++){
        var cod=cadena.charCodeAt(i);
        if((cod>=32 && cod<=47) || (cod>=58 && cod<=64) || (cod>=91 && cod<=96)|| (cod>=123 && cod<=126)|| cod==168 || cod==173 || cod==239){
            ban=true;
            break;
        }
    }
    return ban;
}
function verPassword(){
    var check=document.getElementById("ver");
    if(check.checked){
        document.getElementById("password").setAttribute("type","text");
    }
    else{
        document.getElementById("password").setAttribute("type","password");
    }
} 
function consultarEmail(){
    var ajax=new XMLHttpRequest();
    var email=document.getElementById("email").value;
    var url="/usuarios/email/"+email;
    var div=document.getElementById("notificaciones");
    ajax.open("get",url,true);
    ajax.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var respuesta=JSON.parse(this.responseText);
            if(respuesta.estatus=='Error'){
                div.innerHTML=respuesta.mensaje;
                document.getElementById("registrar").setAttribute("disabled","true");
            }
            else{
                div.innerHTML="";
                document.getElementById("registrar").removeAttribute("disabled");
            }
        }
    };
    ajax.send();
}