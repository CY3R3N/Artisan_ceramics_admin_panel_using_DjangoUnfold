from django.db import models
from django.utils.timezone import now

# Create your models here.
class Inbox(models.Model):
    DEPARTMENT_CHOICES = [
        ('General', 'General'),
        ('Corporate', 'Corporate'),
        ('International Marketing', 'International Marketing'),
        
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='General')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f"{self.name} - {self.department}"