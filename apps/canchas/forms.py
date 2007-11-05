from django.utils.translation import ugettext_lazy as _
from django import newforms as forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label=_(u'Usuario'), max_length=100)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)
