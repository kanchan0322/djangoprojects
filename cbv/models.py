from django.db import models
from django.urls import reverse
# Create your models here.
class StudentInfo(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    address=models.TextField()

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse("home")