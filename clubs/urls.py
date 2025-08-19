from django.urls import path
from . import views

urlpatterns = [
    path('', views.listClubs, name='list_clubs'),
    # path('create/', views.createClub, name='create_club'),
    # path('update/<int:club_id>/', views.updateClub, name='update_club'),
    # path('delete/<int:club_id>/', views.deleteClub, name='delete_club'),
    # path('view/<int:club_id>/', views.viewClub, name='view_club'),
]