from django.urls import path
from . import views


urlpatterns = [
    path('', views.contato, name='contato'),
    path('processa_contato/', views.processa_contato, name='processa_contato'),
]