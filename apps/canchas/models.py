# coding=UTF-8
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.db import models
from multilingual.translation import Translation
from datetime import datetime, timedelta

# Create your models here.
class Club(models.Model):
    nombre = models.CharField(_(u'Club'), max_length=50,
        help_text=_(u'Nombre del club dueño de las canchas.'))
    sitio = models.ForeignKey(Site, blank=True, null=True,
        help_text=_(u'Dirección en Internet del club. Puede quedar vacío.'))

    class Translation(Translation):
        direccion = models.CharField(_(u'Dirección'), max_length=150, blank=True, null=True,
            help_text=_(u'Dirección física del club. Puede quedar vacío.'))

    def __unicode__(self):
        return self.nombre

    class Admin:
        pass

    class Meta:
        verbose_name = _(u'Club')
        verbose_name_plural = _(u'Clubes')

class Cuota(models.Model):
    mes = models.PositiveSmallIntegerField(_(u'Mes'),
        help_text=_(u'¿A qué número de mes corresponde la cuota?'))
    ano = models.PositiveIntegerField(_(u'Año'),
        help_text=_(u'¿A qué año corresponde la cuota?'))

    class Translation(Translation):
        observaciones = models.TextField(_(u'Observaciones'), blank=True, null=True,
            help_text=_(u'Observaciones que crea pertinentes.'))

    class Admin:
        pass

    class Meta:
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas'

class Socio(models.Model):
    from choices import SEXO_CHOICES

    user = models.ForeignKey(User, unique=True)
    cedula = models.CharField(_(u'Documento de Identidad'), max_length=15,
        help_text=_(u'Documento de Identidad del nuevo socio.'))
    domicilio = models.CharField(_(u'Domicilio'), max_length=255,
        help_text=_(u'Domicilio donde vive el socio.'))
#    numero_de_socio = models.PositiveIntegerField(_(u'Número de Socio'))
    fecha_de_nacimiento = models.DateField(_(u'Fecha de Nacimiento'),
        help_text=_(u'Formato: aaaa-mm-dd'))
    sexo = models.CharField(_(u'Sexo'), max_length=1, choices=SEXO_CHOICES)
    vencimiento_ficha_medica = models.DateField(_(u'Vencimiento de ficha médica'),
        help_text=_(u'Fecha de vencimiento de la ficha médica del socio. Formato: aaaa-mm-dd'))
    ultima_cuota_paga = models.ForeignKey(Cuota, related_name='socios_al_dia')

    def get_numero_de_socio(self):
        if self.id is not None:
            return self.id
        else:
            return None
    numero_de_socio = property(get_numero_de_socio)

    class Admin:
        pass

    class Meta:
        verbose_name = _(u'Socio')
        verbose_name_plural = _(u'Socios')

class Sancion(models.Model):
    socio = models.ForeignKey(User, related_name='sancion',
        help_text=_(u'Socio sancionado.'))
    hasta = models.PositiveIntegerField(_(u'¿Hasta cuando?'),
        help_text=_(u'¿Cuándo termina la sanción?'))

    class Translation(Translation):
        razon = models.CharField(_(u'Razón'), max_length=255,
            help_text=_(u'Breve razón de la sanción.'))

    class Admin:
        pass

    class Meta:
        verbose_name = _(u'Sanción')
        verbose_name_plural = _(u'Sanciones')

class Configuracion(models.Model):
    clave = models.CharField(_(u'Dato'), max_length=150,
        help_text=_(u''))
    valor = models.CharField(_(u'Valor'), max_length=255,
        help_text=_(u''))
    core = models.BooleanField(_(u'¿Administrador?'),
        help_text=_(u'¿Es un dato modificable únicamente por el administrador del sistema?'))

    def __unicode__(self):
        return _(u'%(clave)s: %(valor)s') % { 'clave':self.clave, 'valor': self.valor }

    class Admin:
        pass

    class Meta:
        verbose_name = _(u'Configuración')
        verbose_name_plural = _(u'Configuraciones')

class Cancha(models.Model):
    club = models.ForeignKey(Club, related_name='canchas')
    costo = models.DecimalField(_(u'Costo'), max_digits=5, decimal_places=2,
        help_text=_(u'Costo por hora de la cancha.'))
    desactivada = models.BooleanField(_(u'Desactivar'),
        help_text=_(u'Desactivar una cancha permite darla de baja sin la necesidad de eliminarla. Esto es útil cuando la cancha está en reparación y no podrá ser reservada por un tiempo indeterminado.'))

    class Translation(Translation):
        nombre = models.CharField(_(u'Nombre'), max_length=50,
            help_text=_(u'Nombre de la cancha.'))

    def __unicode__(self):
        return _(u'%(id)d (%(nombre)s)') % { 'nombre': self.nombre, 'id': self.id }

    def esta_habilitada(self):
        pass#self.

    class Admin:
        pass

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Cancha')
        verbose_name_plural = _(u'Canchas')

class CanchaInhabilitada(models.Model):
    cancha = models.ForeignKey(Cancha,
        help_text=_(u'¿Qué cancha se encuentra inhabilitada para jugar?'))
    hora = models.DateTimeField(_(u'Hora'),
        help_text=_(u'Fecha a la que comienza/comenzó la inhabilitación. Formato de fecha: aaaa-mm-dd'))
    duracion = models.PositiveIntegerField(_(u'Duración'),
        help_text=_(u'¿Cuántos minutos durará el bloqueo?'))

    class Translation(Translation):
        razon = models.CharField(_(u'Razón'), max_length=255,
            help_text=_(u'Una breve razón de porqué se inhabilitó.'))

    class Admin:
        pass

    class Meta:
        ordering = ['-hora']
        verbose_name = _(u'Cancha Inhabilitada')
        verbose_name_plural = _(u'Canchas Inhabilitadas')

class Reserva(models.Model):
    socio = models.ForeignKey(User, related_name='reservas',
        help_text=_(u'Socio a quien se le realiza la reserva.'))
    cancha = models.ForeignKey(Cancha, related_name='reservas',
        help_text=_(u'Cancha que se desea alquilar.'))
    desde = models.DateTimeField(_(u'Fecha'),
        help_text=_(u'Día y hora de comienzo de la reserva. Formato de fecha: aaaa-mm-dd'))
    permitir_admin_cancelar = models.BooleanField(_(u'Administrador puede cancelar'), default=True,
        help_text=_(u'¿Desea permitir que un administrador pueda cancelar su reserva? Esto es útil para cancelar reservas por teléfono, recuerde que si no puede cancelar su reserva con anticipación será sancionado.'))
    marca_temporal = models.DateTimeField(_(u'Reservado el'), editable=False,
        help_text=_(u'Fecha y hora en que fue creada la reserva. Formato de fecha: aaaa-mm-dd'))
    cancelada = models.BooleanField(_(u'Cancelar'),
        help_text=_(u'Dar de baja la reserva.'))
    cancelada_por = models.BooleanField(_(u'Cancelar'), editable=False, blank=True, null=True,
        help_text=_(u'Dar de baja la reserva.'))
    cancelada_el = models.DateTimeField(_(u'Cancelar'), editable=False, blank=True, null=True,
        help_text=_(u'Dar de baja la reserva. Formato de fecha: aaaa-mm-dd'))

    def __unicode__(self):
        return _(u'Cancha %(cancha)s reservada por %(socio)s de %(desde)s a %(hasta)s')

    #TODO: Chequear que Reservera.cancelar() ande.
    def cancelar(self, usuario=None):
        self.cancelada=True
        if usuario is None:
            self.cancelado_por=self.socio
        else:
            self.cancelado_por=usuario
        self.cancelado_el=datetime.now()
        super(Reserva, self).save()

    #FIXME: Traer la hora hasta la que la reserva esta vigente.
    def get_hasta(self):
        desde = timedelta()
        super(Reserva, self).save()

    #TODO: Traer una cancha libre cualquiera a una hora determinada. Cumpliendo que:
    # No este desactivada.
    # Se encuentre libre.
    # No este inhabilitada.
    def get_cancha_aleatoria_segun_hora(self, hora):
        canchas = Canchas.objects.filter(desactivada=False)
        for cancha in canchas:
            pass

    def save(self):
        if not self.id:
            # ¿La cancha está habilitada?
            if self.cancha.desactivada:
                from exceptions import CanchaNoDisponibleError
                raise CanchaNoDisponibleError, self.cancha
            # ¿Existen reservas para esta cancha?
            if self.cancha_reservada():
                from exceptions import CanchaNoDisponibleError
                raise ReservaSuperpuestaError, self

            self.marca_temporal = datetime.now()
        super(Reserva, self).save()

    #FIXME: Refucktion!!!
    def cancha_reservada(self):
        if self.id is None:
            canchas = Reserva.objects.filter(desde_dia__lte=self.hasta).exclude(hasta__lt=self.desde)
        else:
            canchas = Reserva.objects.exclude(id=self.id).filter(desde_dia__lte=self.hasta).exclude(hasta__lt=self.desde)
        if len(alquileres) > 0:
            return True
        else:
            return False
        reservas = Reserva.objects.filter(desde_dia__exact=self.desde_dia).exclude(desde_hora__lte=self.desde_hora-self.duracion)
        print reservas
        if reservas:
            return True
        else:
            return False

    class Admin:
        pass

    class Meta:
        verbose_name = _(u'Reserva')
        verbose_name_plural = _(u'Reservas')

class ListaDeEspera(models.Model):
    socio = models.ForeignKey(User, related_name='en_cola')
    cancha = models.ForeignKey(Cancha, related_name='socios_en_espera', blank=True, null=True,
        help_text=_(u'¿Desea alguna cancha en particular?'))
    hora = models.TimeField(_(u'Hora'), blank=True, null=True,
        help_text=_(u'¿Desea alguna hora en particular?'))

    def save(self):
        if not self.cancha and not self.hora:
            from exceptions import ListaDeEsperaIncompletaError
            raise ListaDeEsperaIncompletaError
        super(ListaDeEspera, self).save()

    class Meta:
        verbose_name = _(u'Lista de Espera')
        verbose_name_plural = _(u'Listas de Espera')

class Registro(models.Model):
    """
    Logging
    """
    marca_temporal = models.DateTimeField(_(u'Fecha'),
        help_text=_(u'Fecha y hora del evento. Formato de fecha: aaaa-mm-dd'))
    mensaje = models.CharField(_(u'Mensaje'), max_length=255,
        help_text=_(u'Mensaje grabado.'))
    usuario = models.CharField(_(u'Usuario'), max_length=255,
        help_text=_(u'Usuario logueado.'))

    def save(self):
        if not self.id:
            self.marca_temporal=datetime.now()
        super(Registro, self).save()

    class Meta:
        ordering = ['-marca_temporal']
        verbose_name = _(u'Registro')
        verbose_name_plural = _(u'Registros')

