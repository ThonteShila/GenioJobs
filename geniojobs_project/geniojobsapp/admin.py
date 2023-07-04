
from django.contrib import admin
from .models import student,Grade,GenioUsers


# Register your models here.
#admin.py  to create and show all modeules after going into admin portal

admin.site.register(student)
admin.site.register(Grade)
admin.site.register(GenioUsers)