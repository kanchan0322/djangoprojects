from django.shortcuts import render

from .models import StudentInfo
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy

class StudentViewList(ListView):
    model = StudentInfo

class StudentViewCreate(CreateView):
    model = StudentInfo
    fields ='__all__'

class StudentViewDelete(DeleteView):
    model = StudentInfo
    success_url = reverse_lazy('home')

class StudentViewUpdate(UpdateView):
    model = StudentInfo
    fields = '__all__'

class StudentViewDetail(DetailView):
    model = StudentInfo
