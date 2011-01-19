# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, ugettext as u_
from django.contrib.auth.decorators import login_required
from decorators import render_response
from django.http import HttpResponseRedirect, HttpResponse
from django import newforms as forms
from django.contrib import auth
from models import *
from datetime import date, datetime, timedelta
to_response = render_response('canchas/')

# Create your views here.
@to_response
def index(request):
    if request.user.is_authenticated():
        if request.user.is_staff == 1:
            return HttpResponseRedirect('/administrador/')
        try:
            p=request.user.get_profile()
            return main(request)
        except Socio.DoesNotExist:
            return 'error.html', { 'error': _(u'No existe aún un socio para este usuario. Comunique este error a webmaster@bigua.com.uy') }
    else:
        return login(request)

def main(request):
    return 'index.html', tablas(request)

def set_lang(request, lang):
    from django.utils.translation import check_for_language, activate, to_locale, get_language
    from settings import LANGUAGES
    from multilingual.languages import set_default_language

    if lang and check_for_language(lang):
        set_default_language(lang)
        if hasattr(request, 'session'):
            request.session['django_language'] = lang
        else:
            response.set_cookie('django_language', lang)
    return HttpResponseRedirect('/')

@to_response
def login(request):
    from forms import LoginForm
    from exceptions import FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError

    error=''
    if request.user.is_authenticated():
        HttpResponseRedirect('/')
    login_form = LoginForm(auto_id=True)
    if request.method == 'POST':
        login_form = LoginForm(request.POST, auto_id=True)
        if login_form.is_valid():
            username = request.POST['usuario']
            password = request.POST['password']
            usuario = auth.authenticate(username=username, password=password)
            if usuario is not None:
                try:
                    if usuario.get_profile().en_regla():
                        auth.login(request, usuario)
                        if 'next' in request.POST:
                            return HttpResponseRedirect(request.POST['next'])
                        else:
                            return HttpResponseRedirect('/')
                except (FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError), e:
                    error = e.message
                except Socio.DoesNotExist:
                    error = _(u'El socio especificado no existe. Si usted es socio del club entonces aún no lo ingresaron a la base del sistema. Si el problema persiste comuníquelo al club. Muchas gracias.')
                    pass

    return 'login.html', { 'form': login_form, 'error': error }

def do_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# Una ofrenda a Guido
#FIXME: Un FIXME grande como una casa!!!
@login_required
def tablas(request):
    from utils import mes_to_string

    # Reservas canceladas
    canceladas = []
    for reserva_cancelada in request.user.reservas.filter(cancelada=True):
        canceladas.append(reserva_cancelada)
    for reserva_cancelada in Reserva.objects.filter(invitado=request.user, cancelada=True).exclude(socio=request.user):
        canceladas.append(reserva_cancelada)
    # Reservas pendientes
    if not request.user.get_profile().puede_reservar():
        mi_reserva=None
        try:
            mi_reserva=request.user.reservas.get(desde__gt=datetime.now(), cancelada=False)
        except Reserva.DoesNotExist, e:
            try:
                mi_reserva=Reserva.objects.get(desde__gt=datetime.now(), cancelada=False, invitado=request.user)
            except Reserva.DoesNotExist, e:
                pass
        if mi_reserva is not None:
            # Si tiene reservas pendientes no puede realizar
            # otra, así que termino acá y le mando el html.
            return { 'puede_reservar': False, 'mes': mes_to_string(datetime.today().month), 'reserva': mi_reserva, 'reservas_canceladas': canceladas }

    # Interfaz de reserva
    canchas = Cancha.objects.filter(desactivada=False)
    # Solo se puede reservar a las horas en punto.
    club = Club.objects.get(id=1)
    horas = club.get_horas()

    maniana = "%(dia)i-%(mes)i-%(anio)i" % { 'dia': datetime.today().day + 1, 'mes': datetime.today().month, 'anio': datetime.today().year }
    return { 'canchas': canchas, 'maniana': maniana, 'puede_reservar': request.user.get_profile().puede_reservar(), 'reservas_canceladas': canceladas, 'horas': horas }

@login_required
@to_response
def reservar(request, **kwargs):
    from django.shortcuts import get_object_or_404
    from forms import ReservaSocioForm, ReservaInvitadoForm

    if 'numero' in request.POST:
        if request.POST['numero'] != '':
            return do_reservar(request)
    elif 'nombre' in request.POST and 'cedula' in request.POST:
        if request.POST['nombre'] != '' and request.POST['cedula']:
            return do_reservar(request)
    hora = kwargs['hora']
    dia = kwargs['dia']
    cancha_id = kwargs['cancha']
    # reserva = Reserva(socio=request.user, cancha=cancha_id, invitado)
    cancha = get_object_or_404(Cancha, id=cancha_id)
    if request.method == 'POST':
        socio = ReservaSocioForm(request.POST)
        invitado = ReservaInvitadoForm(request.POST)
    else:
        socio = ReservaSocioForm()
        invitado = ReservaInvitadoForm()
    return 'reservar.html', { 'dia': dia, 'hora': hora, 'cancha': cancha.nombre, 'cancha_id': cancha_id, 'costo': cancha.costo, 'socio_form': socio, 'invitado_form': invitado }

@login_required
@to_response
def do_reservar(request):
    from forms import ReservaSocioForm, ReservaInvitadoForm

    if request.user.is_staff == 0:
        if request.method == "POST":
            post = request.POST.copy()
            socio_form = ReservaSocioForm(post)
            if socio_form.is_valid():
                try:
                    if reservar_socio(request):
                        if 'next' in post:
                            return HttpResponseRedirect(post['next'])
                        else:
                            return HttpResponseRedirect('/')
                except User.DoesNotExist:
                    error=_(u'No existe ningun socio registrado con ese número, por favor verifique los datos antes de ingresarlos.')
                return 'error.html', { 'error': error }
            else:
                if post['nombre'] != '' and post['cedula'] != '':
                    i=Invitado(nombre=post['nombre'], documento=post['cedula'])
                    i.save()
                    r=Reserva(socio=request.user, cancha=Cancha.objects.get(id=post['cancha']), invitado=i, desde=datetime(datetime.today().year, datetime.today().month, int(post['dia']), int(post['hora'])))
                    r.save();
                    if 'next' in post:
                        return HttpResponseRedirect(post['next'])
                    else:
                        return HttpResponseRedirect('/')

            return reservar(request, dia=post['dia'], hora=post['hora'], cancha=post['cancha'])
        # Si no hay datos por post pasa algo raro... me voy al mazo.
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def reservar_socio(request):
    post=request.POST.copy()
    if post['admin_cancela'] == 'on':
        admin = True
    else:
        admin = False
    usuario=User.objects.get(id=post['numero'])
    if not usuario.get_profile().puede_reservar():
        return False
    r=Reserva(socio=request.user, cancha=Cancha.objects.get(id=post['cancha']), invitado=usuario, desde=datetime(datetime.today().year, datetime.today().month, int(post['dia']), int(post['hora'])), permitir_admin_cancelar=admin)
    r.save();
    return True

@to_response
def cancelar(request):
    if request.method == 'POST':
        post=request.POST.copy()
        try:
            reserva = Reserva.objects.get(id=post['reserva'])
            if post['confirmada'] == 'true':
                reserva.cancelar(request.user)
                if 'next' in post:
                    return HttpResponseRedirect(post['next'])
                else:
                    return HttpResponseRedirect('/')
            else:
                return 'confirmar.html', { 'reserva': reserva }
        except:
            if 'next' in post:
                return HttpResponseRedirect(post['next'])
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@to_response
def sancionar(request):
    if request.method == 'POST':
        post=request.POST.copy()
        sancionar_a=User.objects.get(id=post['usuario'])
        try:
            sancion=Sancion.objects.get(socio=sancionar_a)
            hasta_cuando=sancion.hasta+timedelta(7)
            sancion.save()
            if 'next' in post:
                return HttpResponseRedirect(post['next'])
            else:
                return HttpResponseRedirect('/')
        except:
            hasta_cuando=date.today()+timedelta(7)
            sancion=Sancion(socio=sancionar_a, hasta=hasta_cuando)
            sancion.save()
            if 'next' in post:
                return HttpResponseRedirect(post['next'])
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

