from django.conf.urls import url, include
from . import views
#
urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^index/$', views.login_feito, name='login_feito'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^novo/usuario/$', views.usuario_auth, name='usuario_auth'),
    url(r'^novo/usuario/(?P<pk>[0-9]+)/$', views.usuario_registro, name='usuario_registro'),
    url(r'^perfil/(?P<pk>[0-9]+)/editar/$', views.usuario_edicao, name='usuario_edicao'),
    url(r'^perfil/(?P<pk>[0-9]+)/editar/estado/$', views.usuario_edicao_estado, name='usuario_edicao_estado'),
    #SOB_REFORMA url(r'^perfil/(?P<pk>[0-9]+)/editar/bairro/$', views.usuario_edicao_bairro, name='usuario_edicao_bairro')
    url(r'^perfil/(?P<pk>[0-9]+)/editar/municipio/$', views.usuario_edicao_municipio, name='usuario_edicao_municipio'),
    url(r'^perfil/(?P<pk>[0-9]+)/$', views.usuario_perfil, name='usuario_perfil'),
    url(r'^perfil/(?P<pk>[0-9]+)/notificacoes/$', views.usuario_notificacoes, name='usuario_notificacoes'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.usuario_profile, name='usuario_profile'),
	url(r'^usuarios/$', views.listar_usuarios, name='listar_usuarios'),
    url(r'^novo/evento/$', views.evento_registro, name='evento_registro'),
    url(r'^evento/(?P<pk>[0-9]+)/editar/$', views.evento_edicao, name='evento_edicao'),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.evento_perfil, name='evento_perfil'),
	url(r'^eventos/$', views.listar_eventos, name='listar_eventos'),
    url(r'^evento/(?P<pk>[0-9]+)/convidar/$', views.evento_convidar, name="evento_convidar"),
]

'''
django.contrib.auth.urls:
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
'''
