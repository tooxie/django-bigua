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
        try:
            p=request.user.get_profile()
            return main(request)
        except Socio.DoesNotExist:
            return 'error.html', { 'error': _(u'No existe aún un socio para este usuario. Comunique este error a webmaster@bigua.com.uy') }
    else:
        return login(request)

def main(request):
    return 'index.html', tablas(request)

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

# Forgive me Guido for I have sin...
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
            return { 'puede_reservar': False, 'mes': mes_to_string(datetime.today().month), 'reserva': mi_reserva, 'reservas_canceladas': canceladas }

    # Interfaz de reserva
    canchas = Cancha.objects.filter(desactivada=False)
    # Solo se puede reservar a las horas en punto.
    club = Club.objects.get(id=1)
    horas = club.get_horas()
    html_hoy, html_man = '', ''
    # HTML para reservar hoy
    for hora in horas:
        html_hoy += '<tr>'
        html_hoy += '<td class="tdhora">%i:00 hs</td>' % hora
        for cancha in canchas:
            if cancha.esta_libre(hora, datetime.today().day):
                html_hoy += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="%(reservar)s" class="reserva_link"><span class="escondido">%(reservar)s</span>&nbsp;</a></td>' % { 'reservar': u_(u'Reservar'), 'cancha': cancha.id, 'dia': datetime.today().day, 'hora': hora }
            else:
                html_hoy += '<td class="ocupada" title="%(ocupada)s"><span class="escondido">%(ocupada)s</span>&nbsp;</td>' % { 'ocupada': u_(u'Ocupada') }
        html_hoy += '</tr>'
    # HTML para reservar mañana
    for hora in horas:
        html_man += '<tr>'
        html_man += '<td class="tdhora">%i:00 hs</td>' % hora
        for cancha in canchas:
            maniana=datetime.today()+timedelta(1)
            if cancha.esta_libre(hora, maniana.day):
                html_man += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="%(reservar)s" class="reserva_link"><span class="escondido">%(reservar)s</span>&nbsp;</a></td>' % { 'reservar': u_(u'Reservar'),'cancha': cancha.id, 'dia': datetime.today().day + 1, 'hora': hora }
            else:
                html_man += '<td class="ocupada" title="%(ocupada)s"><span class="escondido">%(ocupada)s</span>&nbsp;</td>' % { 'ocupada': u_(u'Ocupada') }
        html_man += '</tr>'
    # - - - - - - - - - - - - - - - #
    hoy, maniana = {}, {}
    for hora in horas:
        for cancha in canchas:
            hoy[hora] = cancha.esta_libre(hora, date.today().day)

    maniana = "%(dia)i-%(mes)i-%(anio)i" % { 'dia': datetime.today().day + 1, 'mes': datetime.today().month, 'anio': datetime.today().year }
    return { 'canchas': canchas, 'hoy': hoy, 'maniana': maniana, 'tabla_hoy': html_hoy, 'tabla_man': html_man, 'puede_reservar': request.user.get_profile().puede_reservar(), 'reservas_canceladas': canceladas }

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
            except Exception, e:
                return 'error.html', { 'error': e }
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

