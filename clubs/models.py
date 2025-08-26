from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established_date = models.DateField()
    # logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)  # Optional field for club logos
    # domain (such as Technical, Cultural, etc.) can be added later if needed
    # club_abreaviation = models.CharField(max_length=10, unique=True)  # Optional field for club abbreviation

    def __str__(self):
        return self.name