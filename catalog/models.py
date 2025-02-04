from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator
# Create your models here.
class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='catalog/',)
    pdf_file = models.FileField(upload_to='catalog/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],default='catalogs/default.pdf')
    
    def __str__(self):
        return self.name
