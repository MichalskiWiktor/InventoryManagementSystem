from django.db import models
from PIL import Image

class Tag(models.Model):
    name = models.CharField(max_length=30)
    usage_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    usage_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=50) 
    category = models.ManyToManyField(Category) 
    selling_price = models.FloatField() 
    manufacturing_price = models.FloatField() 
    stock = models.IntegerField()
    brand = models.CharField(max_length=50) 
    tags = models.ManyToManyField(Tag) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
