from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/create/', views.TasksCreate.as_view(), name='tasks_create'),
]

