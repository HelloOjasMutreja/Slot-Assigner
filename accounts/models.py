from django.db import models

# Create your models here.

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    current_year_of_study = models.IntegerField()
    belongs_to_club = models.ManyToManyField('clubs.Club', blank=True, related_name='members')
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional field for profile pictures
    # role_per_club (to identify domain they are part of) (should be many to many in each club) such as ALex is a "Technical" member and "Core" member in the Club A and is "Creative" member in Club B (can be implemented later if needed)
 
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"Profile of {self.user.username}"
