/* JavaScript functions */
function _(element_id) {
    return document.getElementById(element_id);
}

function switch_visibility(obj, dis) {
    if (obj.style != null) {
        if (obj.style.display == 'none') {
            obj.style.display = dis;
        } else {
            obj.style.display = 'none';
        }
    } else {
        obj.style.display = 'none';
    }
    return true;
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
}

var bigua_rules = {
    'body' : function(element) {
        element.onload = atLoadTime();
    },
    'a#hoy_switch' : function(element) {
        element.onclick = function() {
            $("#hoy").addClass("ohmy").toggle("slow");
            return false;
        }
    },
    'a#maniana_switch' : function(element) {
        element.onclick = function() {
            $("#maniana").addClass("ohmy").toggle("slow");
            return false;
        }
    },
    'form#cancelarform' : function(element) {
        element.onsubmit = function() {
            alert('hola');
            if(confirm('Realmente desea eliminar su reserva?')) {
                return true;
            } else {
                return false;
            }
        }
    }
};

Behaviour.register(bigua_rules);
