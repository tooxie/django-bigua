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
        return main(request)
    else:
        return login(request)

def main(request):
    return 'index.html', tablas(request)

def login(request):
    from forms import LoginForm

    login = LoginForm(auto_id=True)
    return 'login.html', { 'form': login }

def do_login(request):
    from forms import LoginForm
    if request.method == 'POST':
        login_form = LoginForm(request.POST, auto_id=True)
        if not login_form.errors:
            username = request.POST['usuario']
            password = request.POST['password']
            usuario = auth.authenticate(username=username, password=password)
            if usuario is not None:
                if usuario.get_profile().en_regla():
                    auth.login(request, usuario)
                    if 'next' in request.POST:
                        return HttpResponseRedirect(request.POST['next'])
        else:
            return auth.login(request)

    return HttpResponseRedirect('/')

def do_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# Forgive me Guido for I have sin...
@login_required
def tablas(request):
    from models import Cancha

    if not request.user.get_profile().puede_reservar():
        try:
            r=request.user.reservas.get(desde__gt=datetime.now())
            mes = { 1: _(u'Enero'), 2: _(u'Febrero'), 3: _(u'Marzo'), 4: _(u'Abril'), 5: _(u'Mayo'), 6: _(u'Junio'), 7: _(u'Julio'), 8: _(u'Agosto'), 9: _(u'Setiembre'), 10: _(u'Octubre'), 11: _(u'Noviembre'), 12: _(u'Diciembre') }
            return { 'puede_reservar': False, 'mes': mes[datetime.today().month], 'dia': r.desde.day, 'hora': r.desde.hour, 'cancha': r.cancha.nombre, 'id': r.id, 'invitado': r.invitado }
        except Reserva.DoesNotExist:
            pass
    canchas = Cancha.objects.filter(desactivada=False)
    #Solo se puede reservar a las horas en punto.
    club = Club.objects.get(id=1)
    horas = club.get_horas()
    html_hoy, html_man = '', ''
    #FIXME: Un FIXME grande como una casa!!!
    # HTML para reservar hoy
    for hora in horas:
        html_hoy += '<tr>'
        html_hoy += '<td>%i:00 hs</td>' % hora
        for cancha in canchas:
            if cancha.esta_libre(hora, 'hoy'):
                html_hoy += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="%(reservar)s" class="reserva_link"><span class="escondido">%(reservar)s</span>&nbsp;</a></td>' % { 'reservar': u_(u'Reservar'), 'cancha': cancha.id, 'dia': datetime.today().day, 'hora': hora }
            else:
                html_hoy += '<td class="ocupada" title="%(ocupada)s"><span class="escondido">%(ocupada)s</span>&nbsp;</td>' % { 'ocupada': u_(u'Ocupada') }
        html_hoy += '</tr>'
    # HTML para reservar mañana
    for hora in horas:
        html_man += '<tr>'
        html_man += '<td>%i:00 hs</td>' % hora
        for cancha in canchas:
            if cancha.esta_libre(hora, 'maniana'):
                html_man += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="%(reservar)s" class="reserva_link"><span class="escondido">%(reservar)s</span>&nbsp;</a></td>' % { 'reservar': u_(u'Reservar'),'cancha': cancha.id, 'dia': datetime.today().day + 1, 'hora': hora }
            else:
                html_man += '<td class="ocupada" title="%(ocupada)s"><span class="escondido">%(ocupada)s</span>&nbsp;</td>' % { 'ocupada': u_(u'Ocupada') }
        html_man += '</tr>'
    # - - - - - - - - - - - - - - - #
    hoy, maniana = {}, {}
    for hora in horas:
        for cancha in canchas:
            hoy[hora] = cancha.esta_libre(hora, 'hoy')
            # maniana[hora] = cancha.esta_libre(hora, 'maniana')

    maniana = "%(dia)i-%(mes)i-%(anio)i" % { 'dia': datetime.today().day + 1, 'mes': datetime.today().month, 'anio': datetime.today().year }
    return { 'canchas': canchas, 'hoy': hoy, 'maniana': maniana, 'tabla_hoy': html_hoy, 'tabla_man': html_man, 'puede_reservar': request.user.get_profile().puede_reservar() }

def reservas(request):
    from models import Reserva
    reservas = Reserva.filter(socio=request.user, hasta__gt=datetime.now())

@login_required
@to_response
def reservar(request, **kwargs):
    from django.shortcuts import get_object_or_404
    from forms import ReservaSocioForm, ReservaInvitadoForm

    hora = kwargs['hora']
    dia = kwargs['dia']
    cancha_id = kwargs['cancha']
    """
    if datetime.today().day == int(dia):
        dia = "hoy (%s)" % dia
    else:
        dia = "ma&ntilde;ana (%s)" % dia
    """
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
        if post['socio'] != '':
            socio_form = ReservaSocioForm(post)
            if socio_form.is_valid():
                s=User.objects.get(id=post['socio'])
                if post['admin_cancela'] == 'on':
                    admin_cancela = True
                else:
                    admin_cancela = False
                r=Reserva(socio=request.user, cancha=Cancha.objects.get(id=post['cancha']), invitado=s, desde=datetime(datetime.today().year, datetime.today().month, int(post['dia']), int(post['hora'])), permitir_admin_cancelar=admin_cancela)
                r.save();
                return HttpResponseRedirect('/')
        else:
            if post['nombre'] != '' and post['cedula'] != '':
                i=Invitado(nombre=post['nombre'], documento=post['cedula'])
                i.save()
                r=Reserva(socio=request.user, cancha=Cancha.objects.get(id=post['cancha']), invitado=i, desde=datetime(datetime.today().year, datetime.today().month, int(post['dia']), int(post['hora'])))
                r.save();
                return HttpResponseRedirect('/')

    return reservar(request, dia=post['dia'], hora=post['hora'], cancha=post['cancha'])

def cancelar(request):
    if request.method == 'POST':
        try:
            reserva = Reserva.objects.get(id=request.POST['reserva'])
            reserva.delete()
            return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')

