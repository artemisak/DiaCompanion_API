from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('getUser/', views.get_user, name='get user'),
    path('addUser/', views.add_user, name='add user')
]
