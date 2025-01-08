from django.db import models

# Create your models here.

class catDb(models.Model):
    CategoryName = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    Image = models.ImageField(upload_to="Category Images",null=True, blank=True)

class proDb(models.Model):
    Catgories = models.CharField(max_length=200, null=True, blank=True)
    Products = models.CharField(max_length=200, null=True, blank=True)
    Price = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    ProductImage = models.ImageField(upload_to="product Images",null=True, blank=True)
