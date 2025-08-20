from django.shortcuts import render

# Create your views here.

def listTasks(request):
    return render(request, 'tasks/home.html')
