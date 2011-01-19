/* JavaScript functions */
var socio_tpl;
var invitado_tpl;
var vacio;
var socio_vacio;
var invitado_vacio;
var admin_cancela_ayuda;

function _(element_id) {
    return document.getElementById(element_id);
}

function setError(msg) {
    _('errorholder').innerHTML = msg;
    $("#errorholder").show("slow");
}

function atLoadTime() {
    $("#hoy").hide();
    $("#maniana").hide();

    if(_('hoy_link')) {
        _('hoy_link').innerHTML = '<a href="#" id="hoy_switch">' + _('hoy_link').innerHTML + '</td>';
    }
    if(_('maniana_link')) {
        _('maniana_link').innerHTML = '<a href="#" id="maniana_switch">' + _('maniana_link').innerHTML + '</td>';
    }
    if(_('canceladas_link')) {
        _('canceladas_link').innerHTML = '<a href="#" id="canceladas_switch">' + _('canceladas_link').innerHTML + '</td>';
        $("#canceladas").hide();
    }
    if(_('cancelarform')) {
        Behaviour.register(bigua_cancelar_rules);
    }
    if(_('canceladas')) {
        Behaviour.register(bigua_canceladas_rules);
    }
    // FIXME: Esto anda 'pal culo.
    // El sistema no funciona en IE y anda buggy en Konqueror.
    if(_('partnerholder')) {
        // Hermoso hack: esto permite que el contenido dinamico sea traducible.
        socio_tpl = _('socio_tpl').innerHTML;
        invitado_tpl = _('invitado_tpl').innerHTML;
        socio_vacio = _('socio_vacio').value;
        invitado_vacio = _('invitado_vacio').value;
        vacio = _('vacio').value;
        admin_cancela_ayuda = _('admin_cancela_texto').value;

        _('partnerholder').innerHTML = '';
    }
    if(_('hoy_switch')) {
        Behaviour.register(bigua_reserva_rules);
        Behaviour.register(bigua_partner_rules);
    }
    if(_('errorholder')) {
        $('#errorholder').hide();
    }
}

var bigua_reserva_rules = {
    'a#hoy_switch' : function(element) {
        element.onclick = function() {
            $("#hoy").toggle("slow");
            return false;
        }
    },
    'a#maniana_switch' : function(element) {
        element.onclick = function() {
            $("#maniana").toggle("slow");
            return false;
        }
    },
    '.reserva_link' : function(element) {
        element.onclick = function() {
            if(_('socio').checked) {
                if(_('numero').value == '') {
                    setError(socio_vacio);
                    return false;
                }
            } else if(_('invitado').checked) {
                if(_('nombre').value == '' || _('cedula').value == '') {
                    setError(invitado_vacio);
                    return false;
                }
            } else {
                setError(vacio);
                return false;
            }
            url = element.href.substring(element.href.indexOf('reservar/')+9, element.href.lastIndexOf('/'));
            var cancha = url.substring(0, url.indexOf('/'));
            var dia = url.substring(url.indexOf('/')+1, url.lastIndexOf('/'));
            var hora = url.substring(url.lastIndexOf('/')+1);
            _("cancha").value = cancha;
            _("dia").value = dia;
            _("hora").value = hora;
            pform = _('partnerform');
            pform.submit();
            return false;
        }
    },
    '#admin_cancela_ayuda' : function(element) {
        element.onclick = function() {
            if(_('admin_cancela_ayuda').innerHTML!=admin_cancela_ayuda) {
                $('#admin_cancela_ayuda').hide().html(admin_cancela_ayuda).show("slow");
            }
            return false;
        }
    }
}

var bigua_cancelar_rules = {
    'form#cancelarform' : function(element) {
        element.onsubmit = function() {
            if(confirm(_('confirmar_text').value)) {
                _('confirmada').value = 'true';
                _('cancelar').disabled = true;
                setTimeout(function() { _('cancelar').disabled = false; }, 5000);
                return true;
            } else {
                return false;
            }
        }
    },
    '#imprimir' : function(element) {
        element.onclick = function() {
            window.print();
            return false;
        }
    }
}

var bigua_canceladas_rules = {
    '#canceladas_link' : function(element) {
        element.onclick = function() {
            $("#canceladas").toggle("slow");
            return false;
        }
    }
}

var bigua_partner_rules = {
    '#socio' : function(element) {
        element.onclick = function() {
            if(element.checked) {
                _("partnerholder").innerHTML = '<p>' + socio_tpl + '</p>';
                _("invitado").checked = false;
                _("numero").focus();
            }
        }
    },
    '#invitado' : function(element) {
        element.onclick = function() {
            if(element.checked) {
                _("partnerholder").innerHTML = '<p>' + invitado_tpl + '</p>';
                _("socio").checked = false;
                _("nombre").focus();
            }
        }
    }
}

var bigua_rules = {
    'body' : function(element) {
        element.onload = atLoadTime();
    }
};

Behaviour.register(bigua_rules);
