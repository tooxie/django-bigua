# coding=UTF-8
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Link(models.Model):
    nombre = models.CharField(_(u'nombre'), maxlength=20)
    pagina = models.ForeignKey(FlatPage, blank=True, null=True)
    url = models.CharField(_(u'dirección'), maxlength=255, help_text=_(u'Puede elegir una página ya creada o un sitio en Internet, por ej "http://www.brasil.gov.br/". Si elige ámbas se le dará preferencia a la página.'), blank=True)
    padre = models.ForeignKey('Link', null=True, blank=True, help_text=_(u'Si elige otro link en esta lista, este item del menú se mostrará como un subitem del elegido.'))
    posicion = models.PositiveIntegerField(_(u'posición en lista'), default=1)
    desactivar = models.BooleanField(_(u'desactivar'), help_text=_(u'Si desactiva un link no se mostrará en el menú pero no será borrado.'))
    class Meta:
        ordering = ('posicion','nombre')
    class Admin:
        list_filter = ('nombre',)
        search_fields = ('nombre', 'pagina', 'url')
    def __str__(self):
        return self.nombre
    def get_href(self):
        if self.pagina:
            return self.pagina.url
        elif self.url:
            return self.url
        else:
            return ""
    href = property(get_href)

class Menu(models.Model):
    nombre = models.CharField(_(u'nombre'), maxlength=20)
    descripcion = models.TextField(_(u'descripción'))
    links = models.ManyToManyField(Link, blank=True)
    template = models.CharField(_('plantilla'), maxlength=255, blank=True, null=True, help_text=_(u"Ejemplo: 'menu/principal.html'. Si no es proporcionado, el sistema usará 'menu/default.html'."))
    class Meta:
        verbose_name = _(u'menu')
        verbose_name_plural = _(u'menues')
        ordering = ('nombre',)
    class Admin:
        list_filter = ('nombre',)
        search_fields = ('nombre','descripcion')
    def __str__(self):
        return self.nombre
