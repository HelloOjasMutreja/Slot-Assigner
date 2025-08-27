from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established_date = models.DateField()
    # logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)  # Optional field for club logos
    # domain (such as Technical, Cultural, etc.) can be added later if needed
    club_abreaviation = models.CharField(max_length=10, unique=True, blank=True, null=True)
    admin_user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, related_name='administered_clubs')
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.name