from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.main_page, name='main_page'),
]
