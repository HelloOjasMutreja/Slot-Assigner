from django.db import models
from clubs.models import Club

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_by = models.ForeignKey(Club, on_delete=models.CASCADE, null=False)
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) (multiple users can be assigned to a task)

    def __str__(self):
        assigned_by_name = self.assigned_by.name if self.assigned_by else "Unassigned"
        category_name = self.category.name if self.category else "No Category"
        return f"{assigned_by_name}'s {category_name}"
