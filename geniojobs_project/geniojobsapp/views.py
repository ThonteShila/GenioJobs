from django.shortcuts import render,redirect
from geniojobsapp.models import Data,student,Grade
from django.http import HttpResponse,HttpResponseRedirect
from .forms import FeedbackForm
from django.contrib.auth.models import User  
# Create your views here.
def home(request):
        return render(request,'home.html',{})
def grade_function(request):
        print("grade")
        grade=Grade.objects.all()
        print(grade)
        context={
               "grade":grade
               }
        return render(request, 'add_stud.html',context)
def display_stud(request):
        stud=student.objects.all()
        context={
                'stud':stud
                }
        return render(request,'display_stud.html',context)
def add_stud(request):
        if request.method=="POST":
                firstname=request.POST.get('first_name')
                lastname=request.POST.get('last_name')
                studgender=request.POST.get('stud_gender')  
                studage=request.POST.get('stud_age')  
                studgrade=request.POST.get('gradename')
                grade = Grade()
                grade.id = studgrade
              
                stud=student(first_name=firstname,last_name=lastname,
                             stud_gender=studgender,stud_age=studage,
                             stud_grade=grade,iscurrent=False)
                
                stud.save()                
                print("Student added successfully.")    
                message="Student added successfully."
                grade=Grade.objects.all()       
                context={
                "grade":grade,
                "message":message
                }
                return render(request, 'add_stud.html',context)      
        elif request.method == 'GET':
                print("grade")
                grade=Grade.objects.all()
                for g in grade:
                        print(g.gradename)
                print("grade")

                context={
                "grade":grade
                }
                return render(request, 'add_stud.html',context)
        else:
                return HttpResponse("Else and handled, studnot Added.")
def employeer_login_page(request):
        data=Data()
        data.name='Employeer Login'
        if request.method=="POST":
                login_email=request.POST.get('emailLogin')
                login_password=request.POST.get('passwordLogin')
                print(login_email,login_password)
                print("if")
        return render(request,"login.html",{'data':data})

def jobseeker_login_page(request):
        data=Data()
        data.name='Job Seeker Login'
        return render(request,"login.html",{'data':data})

def employeer_new(request):
        data=Data()
        data.name='Employeer Registation Form'
        if request.method=="POST":
                email=request.POST.get('email')
                password=request.POST.get('password')
                conformpassword=request.POST.get('conformPassword')
                data.is_employeer=True
                print(email,password,conformpassword)
                if password!=conformpassword:
                        return HttpResponse("Password and conform password not matching")
                else:

                        userobj=User.objects.create_user(email,password,conformpassword)
                        userobj.save()
                        return redirect('login')
        return render(request,'register.html',{'data':data})

def jobseeker_new_page(request):
        data=Data()
        data.name='Job Seeker Registration Form'
        return render(request,'register.html',{'data':data})

def re_login(request):
        data=Data()
        data.name='Job Seeker Login'
        return render(request,"login.html",{'data':data})
def employeer_dashboard(request):
        return render(request,"employeer_dashboard.html")
def jobseeker_dashboard(request):
        return render(request,"jobseeker_dashboard.html")