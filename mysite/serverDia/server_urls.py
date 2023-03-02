from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('getUser/', views.getUser, name='get user'),
    path('addUser/', views.addUser, name='add user')
]
