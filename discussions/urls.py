from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_home, name='discussions_home'),
    path('new/', views.new_discussion, name='new_discussion'),
    path('<int:pk>/', views.discussion_detail, name='discussion_detail'),
]
