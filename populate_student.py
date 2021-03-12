import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','classbasedview.settings')
import django
django.setup()
from cbv.models import StudentInfo
from faker import Faker
from random import *

faker=Faker()
def populate(n):
    for i in range(n):
        frollno=faker.random_int(min=1,max=999)
        fname=faker.name()
        fdob=faker.date()
        fmarks=faker.random_int(min=1,max=100)
        femail=faker.email()
        fphonenumber=faker.phone_number()
        faddress=faker.address()
        student_record=StudentInfo.objects.create(rollno=frollno,name=fname,dob=fdob,
                                                  marks=fmarks,email=femail,phonenumber=fphonenumber,
                                                  address=faddress)

populate(30)