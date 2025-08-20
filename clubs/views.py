from django.shortcuts import render, redirect
from .forms import ClubForm

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

# def deleteClub(request, club_id):

# def viewClub(request, club_id):

def listClubs(request):
    return render(request, 'clubs/list.html')

