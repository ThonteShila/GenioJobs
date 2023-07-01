from django.shortcuts import render
from geniojobsapp.models import Data,Data1
from django.http import HttpResponse,HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.
def home(request):
        return render(request,'home.html',{})
def index(request):
        return render(request,'index.html',{})

def employeer_login_page(request):
        data=Data()
        data.name='Employeer Login'
        return render(request,"login.html",{'data':data})

def jobseeker_login_page(request):
        data=Data()
        data.name='Job Seeker Login'
        return render(request,"login.html",{'data':data})

def employeer_new(request):
        data=Data()
        data.name='Employeer Registation Form'
        return render(request,'register.html',{'data':data})

def jobseeker_new_page(request):
        data=Data()
        data.name='Job Seeker Registration Form'
        return render(request,'register.html',{'data':data})

def re_login(request):
        data=Data()
        data.name='Job Seeker Login'
        return render(request,"login.html",{'data':data})
        