from django.urls import path

from . import views

app_name = 'viagens'

urlpatterns = [
    path('agendar_viagem/', views.agendar_viagem, name='agendar_viagem'),
]
