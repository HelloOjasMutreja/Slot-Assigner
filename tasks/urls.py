from django.urls import path
from . import views

urlpatterns = [
    path('', views.listTasks, name='home'),
    path('tasks/create/', views.createTask, name='create_task'),
    path('tasks/update/<int:pk>/', views.updateTask, name='update_task'),
    path('tasks/view/<int:pk>/', views.viewTask, name='view_task'),
]