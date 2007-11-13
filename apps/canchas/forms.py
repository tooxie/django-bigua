# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import newforms as forms
from django.newforms.util import ValidationError

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)

class ReservaSocioForm(forms.Form):
    socio = forms.CharField(label=_(u'Número de Socio'), max_length=10)

    def clean_socio(self):
        try:
            socio = User.objects.get(id=self.cleaned_data['socio'])
        except User.DoesNotExist:
            raise ValidationError('El socio especificado no existe.')
        return self.cleaned_data['socio']

class ReservaInvitadoForm(forms.Form):
    nombre = forms.CharField(label=_(u'Nombre'), max_length=50)
    cedula = forms.CharField(label=_(u'Cédula de Identidad'), max_length=11)
