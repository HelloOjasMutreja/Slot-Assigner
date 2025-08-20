from django.shortcuts import render, redirect
from .forms import ClubForm
from .models import Club

# Create your views here.

def createClub(request):
    form = ClubForm()

    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clubs')

    context = {'form' : form}
    return render(request, 'clubs/form.html', context)

# def updateClub(request, club_id):
    # edit admins

def deleteClub(request, pk):
    club = Club.objects.get(id=pk)
    if not club:
        return redirect('list_clubs')
    if request.method == 'POST':
        club.delete()
        return redirect('list_clubs')
    
    context = {'club': club}
    return render(request, 'clubs/delete.html', {'obj' : club})

def viewClub(request, pk):
    club = Club.objects.get(id=pk)
    context = {'club': club}
    return render(request, 'clubs/read.html', context)

def listClubs(request):
    clubs = Club.objects.all()
    context = {'clubs': clubs}
    return render(request, 'clubs/list.html', context)

