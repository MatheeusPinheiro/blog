from django.urls import path
from . import views


urlpatterns = [
    path('', views.processa_login, name='login'),
    path('autenticacao/logout', views.processa_logout, name='logout'),
]