from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')  # Upload images to 'categories/' folder

    def __str__(self):
        return self.name


class Shape(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shapes/')  # Upload images to 'shapes/' folder
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shapes')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    measurement = models.CharField(max_length=100)
    diameter = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Upload images to 'products/' folder
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.shape.name})"
