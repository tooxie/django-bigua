from django.contrib.auth.models import User
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
                auth.login(request, usuario)
                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST['next'])
        else:
            return auth.login(request)

    return HttpResponseRedirect('/')

def do_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def tablas(request):
    from models import Cancha

    canchas = Cancha.objects.filter(desactivada=False)
    #Solo se puede reservar a las horas en punto.
    club = Club.objects.get(nombre='Biguá')
    horas = club.get_horas()
    html_hoy, html_man = '', ''
    #FIXME: Un FIXME grande como una casa!!!
    # HTML para reservar hoy
    for hora in horas:
        html_hoy += '<tr>'
        html_hoy += '<td>%i:00 hs</td>' % hora
        for cancha in canchas:
            if cancha.esta_libre(hora, 'hoy'):
                html_hoy += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="Reservar"><span class="escondido">Reservar</span>&nbsp;</a></td>' % { 'cancha': cancha.id, 'dia': datetime.today().day, 'hora': hora }
            else:
                html_hoy += '<td class="ocupada" title="Ocupada"><span class="escondido">Ocupada</span>&nbsp;</td>'
        html_hoy += '</tr>'
    # HTML para reservar mañana
    for hora in horas:
        html_man += '<tr>'
        html_man += '<td>%i:00 hs</td>' % hora
        for cancha in canchas:
            if cancha.esta_libre(hora, 'maniana'):
                html_man += '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/"><span class="escondido">Reservar</span>&nbsp;</a></td>' % { 'cancha': cancha.id, 'dia': datetime.today().day + 1, 'hora': hora }
            else:
                html_man += '<td class="ocupada"><span class="escondido">Ocupada</span>&nbsp;</td>'
        html_man += '</tr>'
    # - - - - - - - - - - - - - - - #
    hoy, maniana = {}, {}
    for hora in horas:
        for cancha in canchas:
            hoy[hora] = cancha.esta_libre(hora, 'hoy')
            # maniana[hora] = cancha.esta_libre(hora, 'maniana')

    maniana = "%(dia)i-%(mes)i-%(anio)i" % { 'dia': datetime.today().day + 1, 'mes': datetime.today().month, 'anio': datetime.today().year }
    return { 'canchas': canchas, 'horarios': horas, 'hoy': hoy, 'maniana': maniana, 'tabla_hoy': html_hoy, 'tabla_man': html_man }

def reservas(request):
    from models import Reserva
    reservas = Reserva.filter(socio=request.user, hasta__gt=datetime.now())
