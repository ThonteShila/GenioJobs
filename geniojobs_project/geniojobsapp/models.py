from django.db import models

# Create your models here.
class Data(models.Model):
    name=str
    is_employeer=bool


class Grade(models.Model):
  #  id=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', default=1)
    gradename=models.CharField(max_length=40,default="Grade")
    
class student(models.Model):
  #  id=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', default=1)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    stud_gender=models.CharField(max_length=20)
    stud_age=models.IntegerField()
    iscurrent=models.BooleanField(default=True)
    stud_grade=models.ForeignKey(Grade, on_delete=models.CASCADE)

class GenioUsers(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    is_employer=models.BooleanField(default=False)
    password=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    organization_name=models.CharField(max_length=100,default="")
    last_update_date=models.DateTimeField(auto_now_add=True)

class Job_Listing(models.Model):
    job_title=models.CharField(max_length=100)
    skills=models.CharField(max_length=200)
    experience=models.IntegerField(default=0)
    no_of_vacancies=models.IntegerField(default=1)
    expiration_date=models.DateTimeField()
    
