from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('grade_function/', views.grade_function, name='grade_function'),
     path('add_listing/<int:job_id>', views.add_listing, name='add_listing'),
     path('display_stud/', views.display_stud, name='display_stud'),
     path('add_stud/', views.add_stud, name='add_stud'),
     path('login/', views.employer_login, name='login'),
     path('jslogin/', views.jobseeker_login, name='jslogin'),
     path('register/', views.employer_new, name='register'),
     path('jsregister/', views.jobseeker_new, name='jsregister'),
     path('re_login/', views.re_login, name='jsregister'),
     path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
     path('jobseeker_dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
     path('delete/<int:id>', views.delete_job, name='delete_job'),
     path('logout/', views.employer_logout, name='logout'),
]