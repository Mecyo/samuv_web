from django.conf.urls import url
from api_rest import views


app_name = 'api_rest'
urlpatterns = [
	url(r'^logar/', views.LoginServiceView.as_view(), name='logar'),
    url(r'^iniciar_atendimento/', views.IniciarAtendimentoServiceView.as_view(), name='iniciar_atendimento'),
    #url(r'^exibir_objeto/(?P<objeto_id>\d+)', views.ObjetoServiceView.as_view(), name='exibir_objeto'),
    #url(r'^emprestar_objeto/', views.EmprestarObjetoServiceView.as_view(), name='emprestar_objeto'),
	
	#recebe foto + info-usuario/paciente/
	#
	#
	#
	#
	#
	#
	#
	#
]
