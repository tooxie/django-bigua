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
@to_response
def index(request):
    if request.user.is_authenticated():
        if request.user.is_staff == 1:
            return 'admin.html'
        else:
            return HttpResponseRedirect('/')
    return login(request)

def login(request):
    from forms import AdminLoginForm

    if request.method == 'POST':
        post = request.POST.copy()
        admin_form = AdminLoginForm(post)
        if admin_form.is_valid():
            usuario = auth.authenticate(username=post['usuario'], password=post['password'])
            if usuario is not None:
                if usuario.is_staff():
                    auth.login(request, usuario)
    else:
        admin_form = AdminLoginForm()

    return 'admin.html', { 'admin': admin_form }

@to_response
def socio_nuevo(request):
    from forms import NuevoSocioForm

    if request.user.is_staff == 1:
        socio_form=NuevoSocioForm()
        if request.method == "POST":
            post=request.POST.copy()
            socio_form=NuevoSocioForm(post)
            if socio_form.is_valid():
                usuario=User(
                    username=post['numero_de_socio'],
                    email=post['email'],
                    first_name="%s %s" % (post['primer_nombre'], post['segundo_nombre']),
                    last_name="%s %s" % (post['primer_apellido'], post['segundo_apellido']),
                )
                usuario.set_password(post['password2'])
                usuario.save()
                cuota=Cuota.objects.get(id=post['ultima_cuota_paga'])
                print "\"", post['fecha_de_nacimiento'], "\""
                socio=Socio(
                    user=usuario,
                    cedula=post['cedula'],
                    domicilio=post['domicilio'],
                    numero_de_socio=post['numero_de_socio'],
                    fecha_de_nacimiento=post['fecha_de_nacimiento'],
                    sexo=post['sexo'],
                    vencimiento_ficha_medica=post['vencimiento_ficha_medica'],
                    ultima_cuota_paga=cuota
                )
                socio.save()
                return HttpResponseRedirect('/administrador/socios/')
        return 'admin_socio.html', { 'socio_form': socio_form }
    else:
         return do_logout(request)

@login_required
@to_response
def reservar(request):
    from forms import AdminReservarForm
    from exceptions import CanchaNoDisponibleError, ReservaSuperpuestaError

    if request.user.is_staff == 1:
        reservar=AdminReservarForm()
        error=''
        if request.method == "POST":
            post=request.POST.copy()
            reservar=AdminReservarForm(post)
            if reservar.is_valid():
                if post['junto_a_socio'] != "":
                    invitado=User.objects.get(id=post['junto_a_socio'])
                else:
                    invitado=Invitado(nombre=post['junto_a_invitado_nombre'], documento=post['junto_a_invitado_documento'])
                if post['cuando_dia'] == date.today().day:
                    cuando=datetime(date.today().year, date.today().month, post['cuando_dia'], post['cuando_hora'])
                else:
                    maniana=date.today()+timedelta(1)
                    dia=datetime(maniana.year, maniana.month, maniana.day, int(post['cuando_hora']))
                    cuando=datetime(dia.year, dia.month, dia.day, dia.hour)
                reserva=Reserva(socio=User.objects.get(id=post['socio']), cancha=Cancha.objects.get(id=post['cancha']), invitado=invitado, desde=cuando, permitir_admin_cancelar=True)
                try:
                    reserva.save()
                    return HttpResponseRedirect('/administrador/reservas/')
                except (CanchaNoDisponibleError, ReservaSuperpuestaError), e:
                    error=e.message

        return 'admin_reservar.html', { 'admin_reservar': reservar, 'error': error }
    else:
        return do_logout(request)

def do_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

