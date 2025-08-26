from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect

# Create your views here.

def createTask(request):
    form = TaskForm()

    if request.method == 'POST':
        form =  TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'tasks/form.html', context)

def listTasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/home.html', context)
