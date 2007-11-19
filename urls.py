from django.conf.urls.defaults import *
from os.path import abspath, dirname
from canchas.models import Reserva

path_to_media = '%s/media' % dirname(abspath(__file__))
urlpatterns = patterns('',
    (r'^$', 'canchas.views.index'),
    (r'^login/$', 'canchas.views.login'),
    (r'^logout/$', 'canchas.views.do_logout'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': path_to_media }),
    (r'^reservar/(?P<cancha>\d*)/(?P<dia>\d*)/(?P<hora>\d*)/$', 'canchas.views.reservar'),
    (r'^reservar/$', 'canchas.views.do_reservar'),
    (r'^cancelar/reserva/$', 'canchas.views.cancelar'),
    (r'^administrador/$', 'canchas.views_admin.index'),
    (r'^administrador/socio/nuevo/$', 'canchas.views_admin.socio_nuevo'),

    (r'^admin/', include('django.contrib.admin.urls')),
)

info_dict = {
    'queryset': Reserva.objects.all().order_by('cancelada', '-desde'),
    'paginate_by': 5,
}

urlpatterns += patterns('django.views.generic.list_detail',
    (r'^administrador/reservas/$', 'object_list', info_dict),
)
