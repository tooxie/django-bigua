# coding=UTF-8
from django.utils.translation import ugettext_lazy as _

def mes_to_string(int_mes):
    mes = {
        1: _(u'Enero'),
        2: _(u'Febrero'),
        3: _(u'Marzo'),
        4: _(u'Abril'),
        5: _(u'Mayo'),
        6: _(u'Junio'),
        7: _(u'Julio'),
        8: _(u'Agosto'),
        9: _(u'Setiembre'),
        10: _(u'Octubre'),
        11: _(u'Noviembre'),
        12: _(u'Diciembre')
    }

    return mes[int_mes]

def ntp_time():
    from socket import socket, AF_INET, SOCK_DGRAM
    from exceptions import NTPInvalidResponseError, NTPNoDataReturnedError

    time_server = ('0.us.pool.ntp.org', 123)
    TIME1970 = 2208988800L      # Thanks to F.Lundh
    client = socket( AF_INET, SOCK_DGRAM )
    data = '\x1b' + 47 * '\0'
    client.sendto(data, time_server)
    data, address = client.recvfrom( 1024 )
    if data:
        print 'Response received from', address
        t = struct.unpack( '!12I', data )[10]
        if t == 0:
            raise NTPInvalidResponseError, _(u'Respuesta inválida.')
        ct = time.ctime(t - TIME1970)
        print 'Current time = %s' % ct
        return time.strptime(ct)
    else:
        raise NTPNoDataReturnedError, _(u'El servidor no devolvió datos.')
