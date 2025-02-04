from django.db import models

# Create your models here.
class Executive(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='executive/', blank=True, null=True)
    

    def __str__(self):
        return self.name