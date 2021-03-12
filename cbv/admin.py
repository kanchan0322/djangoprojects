from django.contrib import admin

from .models import StudentInfo

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dob','marks','email','phonenumber','address']

admin.site.register(StudentInfo,StudentAdmin)
