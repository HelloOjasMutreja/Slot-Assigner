from django.db import models
from clubs.models import Club

# Create your models here.

class Task(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_by = models.ForeignKey(Club, on_delete=models.CASCADE, null=False)
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) (multiple users can be assigned to a task)

    def __str__(self):
        return self.assigned_by.name + " - " + self.description[:50]
                                # self.category