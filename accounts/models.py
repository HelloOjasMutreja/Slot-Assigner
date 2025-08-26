from django.db import models

# Create your models here.

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    current_year_of_study = models.IntegerField()
    belongs_to_club = models.ManyToManyField('clubs.Club', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name