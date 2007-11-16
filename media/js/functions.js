/* JavaScript functions */
var socio_tpl;
var invitado_tpl;

function _(element_id) {
    return document.getElementById(element_id);
}

function atLoadTime() {
    $("#hoy").toggle();
    $("#maniana").toggle();
    if(_('hoy_link')) {
        _('hoy_link').innerHTML = '<a href="#" id="hoy_switch">' + _('hoy_link').innerHTML + '</td>';
    }
    if(_('maniana_link')) {
        _('maniana_link').innerHTML = '<a href="#" id="maniana_switch">' + _('maniana_link').innerHTML + '</td>';
    }
    if(_('cancelarform')) {
        Behaviour.register(bigua_cancelar_rules);
    }
    // FIXME: Esto anda 'pal culo.
    // El sistema no funciona en IE y anda buggy en Konqueror.
    if(_('partnerholder')) {
        // Hermoso hack: esto me permite hacer que el contenido dinamico sea traducible.
        socio_tpl = _('socio_tpl').innerHTML;
        invitado_tpl = _('invitado_tpl').innerHTML;

        _('partnerholder').innerHTML = '';
    }
    if(_('hoy_switch')) {
        Behaviour.register(bigua_reserva_rules);
        Behaviour.register(bigua_partner_rules);
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
    }
}

var bigua_cancelar_rules = {
    'form#cancelarform' : function(element) {
        element.onsubmit = function() {
            if(confirm('Realmente desea eliminar su reserva?')) {
                $('#confirmada').value = 'true';
                return true;
            } else {
                return false;
            }
        }
    }
}

var bigua_partner_rules = {
    '#socio' : function(element) {
        element.onclick = function() {
            if(element.checked) {
                _("partnerholder").innerHTML = '<p>' + socio_tpl + '</p>';
                _("invitado").checked = false;
            }
        }
    },
    '#invitado' : function(element) {
        element.onclick = function() {
            if(element.checked) {
                _("partnerholder").innerHTML = '<p>' + invitado_tpl + '</p>';
                _("socio").checked = false;
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
