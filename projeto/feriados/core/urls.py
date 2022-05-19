from django.urls import path
from . import views

urlpatterns = [
    path('', views.natal),
    path('tiradentes', views.tiradentes),
    path('cadastro', views.cadastro, name='novo_feriado'),
]