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
