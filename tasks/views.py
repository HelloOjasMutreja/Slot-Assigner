from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime

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

# def now():
#     raise NotImplementedError

def viewTask(request, pk):
    task = Task.objects.get(id=pk)
    now = timezone.now()

    # Convert dates to full datetime objects for comparison
    start_time = datetime.combine(task.start_date, datetime.min.time())
    end_time = datetime.combine(task.end_date, datetime.max.time())

    # Make them timezone-aware
    start_time = timezone.make_aware(start_time)
    end_time = timezone.make_aware(end_time)

    # Determine status
    if now < start_time:
        status = "Unstarted"
    elif start_time <= now <= end_time:
        status = "Ongoing"
    elif now > end_time:
        status = "Completed"
    else:
        status = "Unknown"

    assignees = task.assigned_to.all()

    context = {
        'task': task,
        'assignees': assignees,
        'status': status
    }
    return render(request, 'tasks/read.html', context)

def listTasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/home.html', context)
