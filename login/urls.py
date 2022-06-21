from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('login1', views.login1),
]