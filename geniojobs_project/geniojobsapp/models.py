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
    genio_user_id=models.ForeignKey(GenioUsers,on_delete=models.CASCADE,default=0)
    def __str__(self):
      return self.job_title 
    def __str__(self):
      return self.skills 

class Job_Seeker_Profile(models.Model):
    genio_user_id=models.ForeignKey(GenioUsers,on_delete=models.CASCADE,default=0)
    skills=models.CharField(max_length=200)
    resume=models.FileField (upload_to=None, max_length=254)
    cover_letter=models.TextField(default="")
    education=models.CharField(max_length=100,default="")
    percentage=models.FloatField(default=0)
    total_experience=models.IntegerField(default=0)
    def __str__(self):
        return self.resume 
    def __str__(self):
        return self.cover_letter 
    
class applied_jobs(models.Model):
    job_listing_id=models.ForeignKey(Job_Listing,on_delete=models.CASCADE,default=0)
    Job_Seeker_Profile_id=models.ForeignKey(Job_Seeker_Profile,on_delete=models.CASCADE,default=0)
    is_pending=models.BooleanField(default="False")
    is_rejected=models.BooleanField(default="False")
