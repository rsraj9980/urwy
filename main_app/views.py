from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Task, Bid
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BiddingForm


# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def tasks_index(request):
  tasks = Task.objects.exclude(user=request.user)
  return render(request, 'tasks/index.html',{'tasks': tasks}) 

@login_required
def my_tasks(request):
  tasks = Task.objects.filter(user=request.user)
  return render(request, 'tasks/mytasks.html',{'tasks': tasks}) 

@login_required
def bids_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  max_bid = Bid.objects.filter(task_id=task_id).order_by('amount').first()
  if max_bid:
    max_bid = max_bid.amount - 1
  else:
    max_bid = task.budget
  bidding_form = BiddingForm()
  return render(request,'tasks/bid.html',{
    'task': task,
    'bidding_form': bidding_form,
    'max_bid': max_bid
  })


@login_required
def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  bidding_form = BiddingForm()
  return render(request,'tasks/detail.html',{
    'task': task, 
    'bidding_form': bidding_form
  })

class TasksCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'desc', 'endDate', 'budget', 'categories'] #ask instructors about to auto generate today's date

  def form_valid(self, form):
    form.instance.user = self.request.user
    # Let tthe CreateView's form_valid method do its job
    return super().form_valid(form)

class TasksUpdate(UpdateView,LoginRequiredMixin):
  model = Task
  fields = ['desc', 'endDate' ,'budget','categories']

class TasksDelete(DeleteView,LoginRequiredMixin):
  model = Task
  success_url = '/tasks/'

class CategoriesCreate(CreateView,LoginRequiredMixin):
  model = Category
  fields = '__all__'


@login_required
def add_bid(request, task_id):
  # create a ModelForm instance using the data in the posted form
  form = BiddingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_bid = form.save(commit=False)
    new_bid.task_id = task_id
    new_bid.save()
  return redirect('bids_detail', task_id=task_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)