# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext as u_
from django.contrib.auth.decorators import login_required
from decorators import render_response
from django.http import HttpResponseRedirect, HttpResponse
from django import newforms as forms
from django.contrib import auth
from models import *
to_response = render_response('canchas/')

# Create your views here.
def get_form_socio(request):
    try:
        datos={}
        usuario=request.user
        incompleto=usuario.incompleto
        datos['id_documento']=incompleto.documento
        datos['id_numero_de_socio']=incompleto.numero_de_socio
        datos['id_primer_nombre']=incompleto.primer_nombre
        datos['id_segundo_nombre']=incompleto.segundo_nombre
        datos['id_primer_apellido']=incompleto.primer_apellido
        datos['id_segundo_apellido']=incompleto.segundo_apellido
        datos['id_fecha_de_nacimiento']=incompleto.fecha_de_nacimiento
        datos['id_sexo_']=incompleto.sexo
        datos['id_domicilio']=incompleto.domicilio
        datos['id_email']=incompleto.email
        datos['id_vencimiento_ficha_medica']=incompleto.vencimiento_ficha_medica
        datos['id_ultima_cuota_paga']=incompleto.ultima_cuota_paga
    except Exception, e:
        datos=None
    return HttpResponse(datos)

