
from django.contrib import admin
from .models import student,Grade,GenioUsers,Job_Listing,Job_Seeker_Profile,applied_jobs


# Register your models here.
#admin.py  to create and show all modeules after going into admin portal

admin.site.register(student)
admin.site.register(Grade)
admin.site.register(GenioUsers)
admin.site.register(Job_Listing)
admin.site.register(Job_Seeker_Profile)
admin.site.register(applied_jobs)