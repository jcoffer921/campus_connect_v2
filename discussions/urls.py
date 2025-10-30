from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_home, name='discussion_home'),
]
