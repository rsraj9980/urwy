from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Task

# Create your views here.

def home(request):
  return render(request, 'home.html')

def tasks_index(request):
  return render(request, 'tasks/tasks_index.html') 

class TasksCreate(CreateView):
  model = Task
  fields = ['title', 'desc', 'endDate', 'createDate', 'bid', 'budget', 'category']

