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

    if request.user.is_authenticated():
        if request.user.is_staff == 1:
            socio=NuevoSocioForm()
            if request.method == "POST":
                post=request.POST.copy()
                socio=NuevoSocioForm(post)
                if socio.is_valid():
                    pass
            return 'socio.html', { 'socio_form': socio }
        else:
             return HttpResponseRedirect('/')
    else:
         return HttpResponseRedirect('/')

