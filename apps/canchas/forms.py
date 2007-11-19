# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import newforms as forms
from django.newforms.util import ValidationError

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)

class ReservaSocioForm(forms.Form):
    numero = forms.CharField(label=_(u'Número de Socio'), max_length=10)

    def clean_socio(self):
        try:
            socio = User.objects.get(id=self.cleaned_data['socio'])
        except User.DoesNotExist:
            raise ValidationError('El socio especificado no existe.')
        return self.cleaned_data['socio']

class ReservaInvitadoForm(forms.Form):
    nombre = forms.CharField(label=_(u'Nombre'), max_length=50)
    cedula = forms.CharField(label=_(u'Cédula de Identidad'), max_length=11)

class AdminLoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=150)
    password = forms.CharField(label=_(u'Contraseña'), widget=forms.PasswordInput)

class NuevoSocioForm(forms.Form):
    from choices import SEXO_CHOICES
    from models import Cuota

    cedula = forms.CharField(label=_(u'Cédula de Identidad'), max_length=15)
    numero_de_socio = forms.IntegerField(label=_(u'Número de Socio'))
    primer_nombre = forms.CharField(label=_(u'Primer Nombre'), max_length=30)
    segundo_nombre = forms.CharField(label=_(u'Segundo Nombre'), max_length=30, required=False)
    primer_apellido = forms.CharField(label=_(u'Primer Apellido'), max_length=30)
    segundo_apellido = forms.CharField(label=_(u'Segundo Apellido'), max_length=30, required=False)
    fecha_de_nacimiento = forms.DateField(label=_(u'Fecha de Nacimiento'))
    sexo = forms.ChoiceField(label=_(u'Sexo'), choices=SEXO_CHOICES, widget=forms.RadioSelect)
    direccion = forms.CharField(label=_(u'Dirección'), max_length=150)
    vencimiento_ficha_medica = forms.DateField(label=_(u'Vencimiento de Ficha Médica'))
    ultima_cuota_paga = forms.ModelChoiceField(label=_(u'Última Cuota Paga'), queryset=Cuota.objects.all())
    password1 = forms.CharField(label=_(u'Contraseña'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u'Repita la Contraseña'), widget=forms.PasswordInput)

