from django.conf import settings
from django.forms import DateField, DateInput
from django.shortcuts import redirect, render,get_object_or_404
from django.template import RequestContext
import pytz
from geniojobsapp.models import applied_jobs,Data,student,Grade,GenioUsers,Job_Listing,Job_Seeker_Profile
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import make_aware
from time import strptime
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
        print("inside employer_login")
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
                message="Login again,record not found" 
                for geniouser in geniousers:
                        if geniousers.count()==1:
                                message="Successfully login" 
                                print("message:",message)
                                login_success=True
                                request.session['login_user_name']=geniouser.first_name + ' ' + geniouser.last_name
                                break    
                        else :
                                message="Email or Password do not match" 
                                print("message:",message)                              
                                login_success=False
                                break
                if login_success==True:
                        request.session['login_success']=True
                        request.session['geniousers_id']=geniouser.pk                         
                        context={
                                'message':message,
                                'login_user_name':request.session['login_user_name']
                        }
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
                        request.session['login_success']=True
                        request.session['geniousers_id']=geniouser.pk                         
                        context={
                                'message':message,
                                'login_user_name':request.session['login_user_name']
                        }
                        return redirect('../jobseeker_dashboard',context)
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
        print("login_user_name",request.session['login_user_name'])
        if request.method=="POST":                
                if 'addlisting' in request.POST:
                        return redirect("../add_listing")                
                return render(request,"employer_dashboard.html")
        else:   
                job_listing=Job_Listing.objects.all()
                context={
                        'job_listing':job_listing,
                        'login_user_name':request.session['login_user_name']
                }
                return render(request,"employer_dashboard.html",context)                       
def jobseeker_dashboard(request):
        print("1 jobseeker_dashboard method is:",request.method)
        if request.method=="POST":
                search_input=request.POST.get('search_input')
                print("2 in search_input",search_input)    
                job_listing=Job_Listing.objects.filter(job_title__icontains=search_input)
                context={
                        'job_listing':job_listing,
                        'login_user_name':request.session['login_user_name']
                }
                return render(request,"jobseeker_dashboard.html",context)
        elif request.method=="GET":          
                job_listing=Job_Listing.objects.all()
                context={
                        'job_listing':job_listing,
                        'login_user_name':request.session['login_user_name']
                }
        return render(request,"jobseeker_dashboard.html",context)
#######################################################################################

def add_listing(request, job_id):
        global message
        print("request.method:add_listing method:",request.method)
        if request.method=="POST":
                if 'btn_create_list' in request.POST:
                        print("request btn_create_list",request.method)
                        jobtitle=request.POST.get('job_title')
                        skill=request.POST.get('skills')
                        experience=request.POST.get('experience')
                        no_of_vacancies=request.POST.get('no_of_vacancies')
                        new_date=request.POST.get('expiration_date')
                        print("HIIIIIIIIII",new_date)

                        geniousers=GenioUsers()
                        geniousers.id=request.session['geniousers_id']
                        job_listing_obj=Job_Listing(job_title=jobtitle,skills=skill,experience=experience,
                                                no_of_vacancies=no_of_vacancies,
                                                expiration_date=new_date,
                                                genio_user_id=geniousers)
                        job_listing_obj.save()
                        message="Job added successfully."
                        
                        context={         
                        'login_user_name':request.session['login_user_name'],              
                        'functionality_name':"Create New",
                        'message':message,
                        'job':job_listing_obj,
                        'experience_years':range(0, 41)
                        }    
                        return render(request,"add_listing.html",context)
        elif request.method=="GET":
                print("add_listing else GET")
                if job_id==0:
                        job=Job_Listing()
                        func_name="Create New" 
                else:
                        job=Job_Listing.objects.get(pk=job_id)  
                        func_name="Modify"  
                        print("add_listing else GET date",job.expiration_date)  

                message=""
                context={
                        'login_user_name':request.session['login_user_name'],              
                        'functionality_name':func_name,
                        'message':message,
                        'job':job,
                        'experience_years':range(0, 41),
                }
              
                print("add_listing else before render")
                return render(request,'add_listing.html',context)
        else:
                print("add_listing outer else ")
                message=""
                context={
                        'login_user_name':request.session['login_user_name'],              
                        'functionality_name':"Create New",
                        'message':message,
                        'experience_years':range(0, 41)
                }   
                print("add_listing outer else before render")
                return render(request,"add_listing.html",context)
def delete_job(request,id):
        global message
        message = ""
        if request.method=="GET":
                job=Job_Listing.objects.get(pk=id).delete()              
                print("in Get:", id)
                message="One Record Removed"
                print("in message:", message)
                return redirect("../employer_dashboard")
        return render(request,"employer_dashboard.html",{'message':message})
def employer_logout(request):
        return redirect("../login",{'message':"Loggedout Here"})
def my_profile(request,id):
        print("id id ",id)
        print("request.method:add_listing method:",request.method)
        if request.method=="POST":
                if 'btn_save_profile' in request.POST:
                        skill=request.POST.get('skills')
                        education=request.POST.get('education')
                        percentage=request.POST.get('percentage')
                        resume_attach=request.POST.get('resume_attach')
                        cover_letter=request.POST.get('cover_letter')
                        experience=request.POST.get('experience')
                        geniousers=GenioUsers()
                        geniousers.id=request.session['geniousers_id']
                        print(request.session['geniousers_id'])
                        job_listing_obj=Job_Seeker_Profile(skills=skill,education=education,percentage=percentage,
                                                        resume=resume_attach,
                                                        cover_letter=cover_letter,
                                                        total_experience=experience,
                                                        genio_user_id=geniousers)
                        job_listing_obj.save()
                        message="My profile added successfully."
                        #List<string>education_list={'Post Graduation','Graduation','HSC','SSC'}
                context={         
                'login_user_name':request.session['login_user_name'],              
                'message':message,
                'job':job_listing_obj,
                'experience_years':range(0, 41),
                #'education_list':education_list
                }    
                return render(request,"myprofile.html",context)
        elif request.method=="GET":
                geniousers=GenioUsers()    
                job=Job_Seeker_Profile.objects.all()
                print(job)
                for jobs in job:
                        profile_data=True
                        print("profile_data:",profile_data)
                        print(jobs.skills)
                        print(jobs.resume)
                        request.session['geniousers_id']=geniousers.pk                       
                education_list=["Post Graduate","graduate","HSC","SSC"]
                context={
                                'job':jobs,
                                'login_user_name':request.session['login_user_name'],
                                'experience_years':range(0, 41),
                                'education_list':education_list
                        }
                return render(request,"myprofile.html",context)
def apply_job(request,id):
        global message
        message = "One Job Applied"
        if request.method=="GET":
                print("in GET")
                message="Successfully applied for job"
                job=Job_Listing.objects.get(pk=id)  
                Job_Profile=Job_Seeker_Profile.objects.get() 
                applied_job=applied_jobs(job_listing_id=job,Job_Seeker_Profile_id=Job_Profile)
                applied_job.save()
                context={
                                'login_user_name':request.session['login_user_name'],  
                                'message':message,
                                'job':job,
                                'Job_Profile':Job_Profile
                        }  
                return render(request,"apply_job.html",context)
        elif request.method=="POST":
                print("in POST")
                if 'btn_apply' in request.POST:
                        message="One Job Applied"
                        context={
                                'login_user_name':request.session['login_user_name'],  
                                'message':message,
                                'job':job
                        }
                        return render(request,"apply_job.html",context)
        else:
                return render(request,"apply_job.html",{'message':message})
def my_applications(request,id):   
        message = "My Applications"
        if request.method=="GET":
                print("in GET")
                message="My Applications"
                job=Job_Listing.objects.filter(pk=id)  
                Job_Profile=Job_Seeker_Profile.objects.get() 
                applied_job=applied_jobs.objects.all()
                for job in applied_job:
                        print(job.job_listing_id)
                context={
                                'login_user_name':request.session['login_user_name'],  
                                'message':message,
                                'applied_job':applied_job,
                                'job':job,
                                'Job_Profile':Job_Profile
                        }     
                return render(request,"myapplictions.html",context)
        elif request.method=="POST":
                if 'my_applications' in request.POST:
                        message="My applications"
                        context={
                                'login_user_name':request.session['login_user_name'],  
                                'message':message
                        }
                        return render(request,"myapplictions.html",context)
        else:
                return render(request,"myapplictions.html",{'message':message})
    

