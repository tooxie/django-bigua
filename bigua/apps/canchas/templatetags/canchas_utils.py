# coding=UTF-8
from django.template import Library, Node, Template, TemplateSyntaxError
from django.utils.translation import ugettext as u_
from canchas.models import Cancha
from datetime import date, timedelta

register = Library()

class EstaLibreNode(Node):
    def __init__(self, cancha, hora, dia):
        self.cancha = cancha
        self.hora = hora
        self.dia = dia
        self.libre = '<td class="libre"><a href="/reservar/%(cancha)i/%(dia)i/%(hora)i/" title="%(reservar)s" class="reserva_link"><span class="escondido">%(reservar)s</span>&nbsp;</a></td>'
        self.ocupada = '<td class="ocupada" title="%(ocupada)s"><span class="escondido">%(ocupada)s</span>&nbsp;</td>'

    def render(self, context):
        cancha=context['cancha']
        hora=context[self.hora]
        if self.dia == 'hoy':
            dia=date.today().day
        else:
            maniana=date.today()+timedelta(1)
            dia=maniana.day
        if cancha.esta_libre(hora, dia):
            estado=self.libre % { 'reservar': u_('Reservar'), 'cancha': cancha.id, 'dia': dia, 'hora': hora }
        else:
            estado=self.ocupada % { 'ocupada': u_('Ocupada') }
        return estado

def EstaLibre(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, u_(u'templatetag "estado_cancha" recibe tres parametros, "cancha", "hora" y "dia"')
    return EstaLibreNode(bits[1], bits[2], bits[3])

cancha_libre = register.tag('estado_cancha', EstaLibre)
