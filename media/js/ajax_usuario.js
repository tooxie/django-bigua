/* JavaScript functions */

var req;
var fields = new Array()
fields['id_documento'] = ''
fields['id_numero_de_socio'] = ''
fields['id_primer_nombre'] = ''
fields['id_segundo_nombre'] = ''
fields['id_primer_apellido'] = ''
fields['id_segundo_apellido'] = ''
fields['id_fecha_de_nacimiento'] = ''
fields['id_sexo_'] = ''
fields['id_domicilio'] = ''
fields['id_email'] = ''
fields['id_vencimiento_ficha_medica'] = ''
fields['id_ultima_cuota_paga'] = ''

function validate( idQueLlama, element) {
    numeroCaracteres = element.value.length;
    if( (numeroCaracteres%10) == 0 & numeroCaracteres>0){
        guardarTmp( idQueLlama, element);
    }
}

function guardarTmp( idQueLlama, element) {
    var url = "SrvltAjx?accion=guardardatos&campo="+idQueLlama+"&dato=" + encodeURIComponent(element.value);
    if (typeof XMLHttpRequest != "undefined") {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open("GET", url, true);
    req.onreadystatechange = callback;
    req.send(null);
}

function requestStateChange() {
    if(req.readyState==4) {
        if(req.status==200) {
            $('#loading').hide("slow");
            // obj=eval(req.responseText)
            alert(req.responseText);
            populateForm(obj);
        }
    } else if(req.readyState==1) {
        $('#loading').show("slow");
    }
}

function populateForm(jsonObject) {
    alert(jsonObject);
}

function guardarUltimaPagina( ppagina) {
    var url = "SrvltAjx?accion=guardarpag&pagina="+ppagina;
    if (typeof XMLHttpRequest != "undefined") {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open("GET", url, true);
    req.onreadystatechange = requestStateChange;
    req.send(null);
}

function initForm() {
    var url = "/administrador/socio/formulario/";
    if (typeof XMLHttpRequest != "undefined") {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open("GET", url, true);
    req.onreadystatechange = requestStateChange;
    req.send(null);
}

$(document).ready(function(){
    $('#loading').hide();
    initForm();
});
