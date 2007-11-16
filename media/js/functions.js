/* JavaScript functions */
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
    if(_('hoy_switch')) {
        Behaviour.register(bigua_reserva_rules);
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

var bigua_rules = {
    'body' : function(element) {
        element.onload = atLoadTime();
    }
};

Behaviour.register(bigua_rules);
