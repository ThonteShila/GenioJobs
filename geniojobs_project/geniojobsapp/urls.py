from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('grade_function/', views.grade_function, name='grade_function'),
     path('display_stud/', views.display_stud, name='display_stud'),
     path('add_stud/', views.add_stud, name='add_stud'),
     path('login/', views.employeer_login_page, name='login'),
     path('jslogin/', views.jobseeker_login_page, name='jslogin'),
     path('register/', views.employeer_new, name='register'),
     path('jsregister/', views.jobseeker_new_page, name='jsregister'),
     path('re_login/', views.re_login, name='jsregister'),
     path('employeer_dashboard/', views.employeer_dashboard, name='employeer_dashboardr'),
     path('jobseeker_dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
]