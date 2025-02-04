from django.db import models

class Directorboard(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='director/', blank=True, null=True)

    def __str__(self):
        return self.name