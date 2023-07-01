from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('index/', views.index, name='index'),
     path('login/', views.employeer_login_page, name='login'),
     path('jslogin/', views.jobseeker_login_page, name='jslogin'),
     path('register/', views.employeer_new, name='register'),
     path('jsregister/', views.jobseeker_new_page, name='jsregister'),
     path('re_login/', views.re_login, name='jsregister'),
]