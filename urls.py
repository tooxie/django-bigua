from django.conf.urls.defaults import *
from os.path import abspath, dirname
from canchas.models import Reserva, Socio

path_to_media = '%s/media' % dirname(abspath(__file__))
urlpatterns = patterns('',
    (r'^$', 'canchas.views.index'),
    (r'^login/$', 'canchas.views.login'),
    (r'^logout/$', 'canchas.views.do_logout'),
    (r'^lang/(?P<lang>\w{2})/$', 'canchas.views.set_lang'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': path_to_media }),
    (r'^reservar/(?P<cancha>\d*)/(?P<dia>\d*)/(?P<hora>\d*)/$', 'canchas.views.reservar'),
    (r'^reservar/$', 'canchas.views.do_reservar'),
    (r'^cancelar/reserva/$', 'canchas.views.cancelar'),
    (r'^administrador/$', 'canchas.views_admin.index'),
    (r'^administrador/socio/nuevo/$', 'canchas.views_admin.socio_nuevo'),
    (r'^administrador/socio/formulario/$', 'canchas.views_ajax.get_form_socio'),
    (r'^administrador/reservar/$', 'canchas.views_admin.reservar'),
    (r'^administrador/reserva/sancionar/$', 'canchas.views.sancionar'),

    (r'^admin/', include('django.contrib.admin.urls')),
)

reservas_info_dict = {
    'queryset': Reserva.objects.all().order_by('cancelada', '-desde'),
    'paginate_by': 5,
}

socios_info_dict = {
    'queryset': Socio.objects.all().exclude(administrador=True),
    'paginate_by': 5,
}

urlpatterns += patterns('django.views.generic.list_detail',
    (r'^administrador/reservas/$', 'object_list', reservas_info_dict),
    (r'^administrador/socios/$', 'object_list', socios_info_dict),
)
