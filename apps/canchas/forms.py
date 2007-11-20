# coding=UTF-8
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import newforms as forms
from django.newforms.util import ValidationError
from datetime import date, datetime, timedelta

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
    from models import Cuota
    from choices import SEXO_CHOICES

    cedula = forms.CharField(label=_(u'Cédula de Identidad'), max_length=15)
    numero_de_socio = forms.IntegerField(label=_(u'Número de Socio'))
    primer_nombre = forms.CharField(label=_(u'Primer Nombre'), max_length=30)
    segundo_nombre = forms.CharField(label=_(u'Segundo Nombre'), max_length=30, required=False)
    primer_apellido = forms.CharField(label=_(u'Primer Apellido'), max_length=30)
    segundo_apellido = forms.CharField(label=_(u'Segundo Apellido'), max_length=30, required=False)
    fecha_de_nacimiento = forms.DateField(label=_(u'Fecha de Nacimiento'), required=False)
    sexo = forms.ChoiceField(label=_(u'Sexo'), choices=SEXO_CHOICES, widget=forms.RadioSelect)
    domicilio = forms.CharField(label=_(u'Dirección'), max_length=150, required=False)
    email = forms.EmailField(label=_(u'e-Mail'), required=False)
    vencimiento_ficha_medica = forms.DateField(label=_(u'Vencimiento de Ficha Médica'))
    ultima_cuota_paga = forms.ModelChoiceField(label=_(u'Última Cuota Paga'), queryset=Cuota.objects.all())
    password1 = forms.CharField(label=_(u'Contraseña'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u'Repita la Contraseña'), widget=forms.PasswordInput)

    def clean_numero_de_socio(self):
        nds=self.cleaned_data['numero_de_socio']
        try:
            User.objects.get(username=nds)
            raise ValidationError(_(u'Ya existe un usuario con número de socio %i, por favor verifique.') % nds)
        except User.DoesNotExist:
            return self.cleaned_data['numero_de_socio']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError(_(u'Ambas contraseñas deben coincidir.'))
        else:
            return self.cleaned_data['password2']

class AdminReservarForm(forms.Form):
    from models import Cancha
    from exceptions import FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError
    from choices import CUANDO_DIA_CHOICES

    socio = forms.ModelChoiceField(label=_(u'Socio'), queryset=User.objects.exclude(is_staff=True))
    cuando_dia = forms.ChoiceField(label=_(u'¿Cuando?'), widget=forms.RadioSelect, choices=CUANDO_DIA_CHOICES)
    cuando_hora = forms.IntegerField(label=_(u'¿A qué hora?'), min_value=0, max_value=23,
        help_text=_(u'Ingrese solo la hora, de 00 a 24, sin minutos ni segundos.'))
    junto_a_socio = forms.ModelChoiceField(label=_(u'Compañero'), queryset=User.objects.exclude(is_staff=True), required=False,
        help_text=_(u'¿Va a jugar con un socio del club?'))
    junto_a_invitado_nombre = forms.CharField(label=_(u'Nombre'), max_length=150, required=False,
        help_text=_(u'¿O con una persona ajena al club?'))
    junto_a_invitado_documento = forms.CharField(label=_(u'Documento'), max_length=15, required=False,
        help_text=_(u'Si el compañero no es un socio del club, solicite nombre y documento del mismo.'))
    cancha = forms.ModelChoiceField(label=_(u'Cancha'), queryset=Cancha.objects.all().exclude(desactivada=True))

    def clean_socio(self):
        from exceptions import FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError

        try:
            socio = User.objects.get(id=self.cleaned_data['socio'].id)
        except User.DoesNotExist:
            raise ValidationError('El socio especificado no existe.')
        try:
            socio.get_profile().en_regla()
        except (FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError), e:
            raise ValidationError(e.message)
        return self.cleaned_data['socio']

    def clean_junto_a_socio(self):
        from exceptions import FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError

        if 'socio' in self.cleaned_data:
            if self.cleaned_data['socio'] == self.cleaned_data['junto_a_socio']:
                raise ValidationError('Un socio no puede jugar consigo mismo.')
        try:
            socio = User.objects.get(id=self.cleaned_data['junto_a_socio'].id)
        except User.DoesNotExist:
            raise ValidationError('El socio especificado no existe.')
        try:
            socio.get_profile().en_regla()
        except (FichaMedicaVencidaError, SocioDeudorError, SocioSancionadoError), e:
            raise ValidationError(e.message)
        return self.cleaned_data['junto_a_socio']

    def clean_cuando_hora(self):
        from models import Club

        club=Club.objects.get(id=1)
        horas=club.get_horas()
        if self.cleaned_data['cuando_hora'] not in horas:
            raise ValidationError('No se puede alquilar en esa hora, el rango va de %i:00 a %i:00.' % (horas[0], horas[len(horas)-1]))
        return self.cleaned_data['cuando_hora']
