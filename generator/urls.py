from django.urls import path
from . import views

# app_name = "genpass"

urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about')
]
