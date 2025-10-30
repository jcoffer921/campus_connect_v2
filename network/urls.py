from django.urls import path
from . import views

urlpatterns = [
    path('', views.network_home, name='network_home'),
]
