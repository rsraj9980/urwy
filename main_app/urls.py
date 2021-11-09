from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks_index, name='index'),
    path('tasks/mytasks/', views.my_tasks, name='my_tasks'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/<int:task_id>/bid/', views.bids_detail, name='bids_detail'),
    path('tasks/create/', views.TasksCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TasksUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TasksDelete.as_view(), name='tasks_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]

