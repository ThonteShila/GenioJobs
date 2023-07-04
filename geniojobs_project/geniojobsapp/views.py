from django.shortcuts import redirect, render
from django.template import RequestContext
from geniojobsapp.models import Data,student,Grade,GenioUsers
from django.http import HttpResponse
from django.contrib.auth.models import User  

# Create your views here.

def grade_function(request):
        grade=Grade.objects.all()
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
                message="Student added successfully."
                grade=Grade.objects.all()       
                context={
                "grade":grade,
                "message":message
                }
                return render(request, 'add_stud.html',context)      
        elif request.method == 'GET':
                grade=Grade.objects.all()
                context={
                "grade":grade
                }
                return render(request, 'add_stud.html',context)
        else:
                return HttpResponse("Else and handled, studnot Added.")

def get_resource(self):    
        print("inside home")
        return "my resource"

def home(request):
        print("inside home")
        return render(request,'home.html',{})
def employer_login(request):
        data=Data()
        data.name='Employer Login'
        global login_success
        login_success=False

        if request.method=="POST":                
                emailLogin=request.POST.get('emailLogin')
                passwordLogin=request.POST.get('passwordLogin')
                geniousers = GenioUsers.objects.filter(is_employer=True
                                                       ,email=emailLogin
                                                       ,password=passwordLogin)
                print("geniousers count:",geniousers.count())
                message="Record for this email and password is not present"
                for geniouser in geniousers:
                        if geniousers.count()==1:
                                message="Successfully login" 
                                print("message:",message)
                                login_success=True
                                break    
                        else :
                                message="Email or Password do not match" 
                                print("message:",message)                              
                                login_success=False
                                break
                if login_success==True:
                        return redirect('../employer_dashboard', {'message':message})
                else:
                        return render(request,"login.html",{'message':message})                              
        
        elif request.method=="GET":
                print("message:","GET")
                return render(request,"login.html",{'data':data})
 
        print("message:","out")
        return render(request,"login.html",{'data':data})                  
def jobseeker_login(request):
        data=Data()
        data.name='Job Seeker Login'
        global login_success
        login_success=False

        if request.method=="POST":                
                emailLogin=request.POST.get('emailLogin')
                passwordLogin=request.POST.get('passwordLogin')
                geniousers = GenioUsers.objects.filter(is_employer=False
                                                       ,email=emailLogin
                                                       ,password=passwordLogin)
                print("geniousers count:",geniousers.count())
                message="Record for this email and password is not present"
                for geniouser in geniousers:
                        if geniousers.count()==1:
                                message="Successfully login" 
                                print("message:",message)
                                login_success=True
                                break    
                        else :
                                message="Email or Password do not match" 
                                print("message:",message)                              
                                login_success=False
                                break
                if login_success==True:
                        return render(request,"jobseeker_dashboard.html",{'message':message})      
                else:
                        return render(request,"login.html",{'message':message})                              
        
        elif request.method=="GET":
                print("message:","GET")
                return render(request,"login.html",{'data':data})
 
        print("message:","out")
        return render(request,"login.html",{'data':data})                  
def employer_new(request):
        data=Data()
        data.name='Employer'
        print("Method is",request.method)
        if request.method=="POST":
                firstname=request.POST.get('first_name')
                lastname=request.POST.get('last_name')
                employee_email=request.POST.get('email')
                employee_password=request.POST.get('password')
                conformpassword=request.POST.get('conform_password')
                organizationname=request.POST.get('organization_name')
                if employee_password!=conformpassword:
                        Passwordmessage="Password and Conform password not matching"
                        return render(request,'register.html',{'Passwordmessage':Passwordmessage})
                else:
                        geniousersobj=GenioUsers(first_name=firstname,last_name=lastname,email=employee_email,
                                                                is_employer=True,password=employee_password,
                                                                organization_name=organizationname)
                        geniousersobj.save()
                        message="Employer added successfully."
                        return render(request,'register.html',{'message':message})
                
        print("data.name is",data.name)
        return render(request,'register.html',{'data':data})
def jobseeker_new(request):
        data=Data()
        data.name='Job Seeker'       
        print("Method is",request.method) 
        print("data.name is:",data.name)
        if request.method=="POST":
                firstname=request.POST.get('first_name')
                lastname=request.POST.get('last_name')
                employee_email=request.POST.get('email')
                employee_password=request.POST.get('password')
                conformpassword=request.POST.get('conform_password')
                if employee_password!=conformpassword:
                        Passwordmessage="Password and Conform password not matching"
                        return render(request,'register.html',{'Passwordmessage':Passwordmessage})
                else:
                        geniousersobj=GenioUsers(first_name=firstname,last_name=lastname,email=employee_email,
                                                        is_employer=False,password=employee_password)
                        geniousersobj.save()
                        message="Job Seeker added successfully."
                        return render(request,'register.html',{'message':message})

        return render(request,'register.html',{'data':data})
def re_login(request):
        data=Data()
        data.name='Job Seeker Login'
        return render(request,"login.html",{'data':data})
def employer_dashboard(request):
        if request.method=="POST":
                return render(request,'home.html',{})
        else:     
                return render(request,"employer_dashboard.html")
def jobseeker_dashboard(request):
        return render(request,"jobseeker_dashboard.html")

#######################################################################################
