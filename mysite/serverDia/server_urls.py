from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page, name='home page'),
    path('user_login/', views.user_login, name='user login request'),
    path('get_all/', views.get_all_users, name='get all users')
]
