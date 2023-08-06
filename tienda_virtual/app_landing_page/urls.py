from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('usuarios/', views.lista_usuarios , name='usuarios'),
    path('registrarse/', views.registrarse , name='registrarse'),
    path('iniciar_sesion/', views.iniciar_sesion, name= 'iniciar_sesion'),
    path('sesion_iniciada/', views.sesion_iniciada, name= 'sesion_iniciada'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion')
]   