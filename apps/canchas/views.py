from django.contrib.auth.models import User
from decorators import render_response
from django.http import HttpResponseRedirect, HttpResponse
from django import newforms as forms
from django.contrib import auth
to_response = render_response('canchas/')

# Create your views here.
@to_response
def index(request):
    if request.user.is_authenticated():
        return main(request)
    else:
        return login(request)

def main(request):
    return 'index.html', {}

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

"""
def tablas(request):
    from models import 
"""

def reservas(request):
    from models import Reserva
    reservas = Reserva.filter(socio=request.user, hasta__gt=datetime.now())
