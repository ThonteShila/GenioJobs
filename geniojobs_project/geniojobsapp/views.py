from django.shortcuts import redirect, render,get_object_or_404
from django.template import RequestContext
from geniojobsapp.models import Data,student,Grade,GenioUsers,Job_Listing
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

login_user_name = "user here"
geniousers_id=0
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

def stud_detail(request,first_name):    
        print(first_name)
        stud=None
        stud_list=student.objects.filter(first_name=str(first_name))
        if len(stud_list)>0:
                stud=stud_list[0]
        else:
                stud=None
        return render(request,'stud_deatil.html',
                  {'stud': stud})
def home(request):
        print("inside home")
        return render(request,'home.html',{})
def employer_login(request): 
        global login_user_name       
        print("inside employer_login")
        data=Data()
        data.name='Employer Login'
        global login_success
        login_success=False
        global geniousers_id
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
                                login_user_name=geniouser.first_name + ' ' + geniouser.last_name
                                break    
                        else :
                                message="Email or Password do not match" 
                                print("message:",message)                              
                                login_success=False
                                break
                if login_success==True:
                        geniousers_id=geniouser.pk
                        print ("id",geniousers_id)
                        context={
                                'message':message,
                                'login_user_name':login_user_name,
                                 'geniousers_id':geniousers_id
                        }
                        print("login_user_name",context)
                        return redirect('../employer_dashboard',context)
                

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
        print("login_user_name",login_user_name)
        if request.method=="POST":                
                if 'addlisting' in request.POST:
                        return redirect("../add_listing")                
                return render(request,"employer_dashboard.html")
        else:   
                job_listing=Job_Listing.objects.all()
                context={
                        'job_listing':job_listing,
                        'login_user_name':login_user_name
                }
                return render(request,"employer_dashboard.html",context)
                        
def jobseeker_dashboard(request):
        return render(request,"jobseeker_dashboard.html")


#######################################################################################
def add_listing(request):
        global job_id
        print(geniousers_id)
        if request.method=="POST":
                        request.POST.get('btn_create_list')
                        cancle=request.POST.get('btn_cancle')
                        jobtitle=request.POST.get('job_title')
                        skill=request.POST.get('skills')
                        experience=request.POST.get('experience')
                        no_of_vacancies=request.POST.get('no_of_vacancies')
                        expiration_date=request.POST.get('expiration_date')
                        if 'btn_create_list' in request.POST:
                                geniousers=GenioUsers()
                                geniousers.id=geniousers_id
                                job_listing_obj=Job_Listing(job_title=jobtitle,skills=skill,experience=experience,
                                                        no_of_vacancies=no_of_vacancies,
                                                        expiration_date=expiration_date,genio_user_id=geniousers)
                                job_id=job_listing_obj.id
                                job_listing_obj.save()
                                message="Job added successfully."
                                return render(request,"add_listing.html",{'message':message})
                        if 'btn_cancle' in request.POST:
                                message="Job Not added."
                                return render(request,"employer_dashboard.html",{'message':message})        
                                #return render(request, 'employer_dashboard.html', context)
        else:        
                return render(request,"add_listing.html")
        
def delete(request,id):
        #job=Job_Listing.objects.filter(id=request.session['jobs.id']).delete()
        print("in delete:", id)
        print("login_user_name",login_user_name)
        print("in request.method:", request.method)
        global message
        message = "some msg"
        if request.method=="GET":
                job=Job_Listing.objects.get(pk=id).delete()              
                print("in Get:", id)
                message="One Record Removed"
                print("in message:", message)
                return redirect("../employer_dashboard")
        return render(request,"employer_dashboard.html",{'message':message})
        
