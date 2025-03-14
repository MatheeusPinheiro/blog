from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('posts/<int:pk>/post_detail/', views.post_detail, name='post_detail'),
]