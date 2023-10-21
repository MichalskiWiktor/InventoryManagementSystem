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
    # Mandatory Fields
    name = models.CharField(max_length=50) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    # Non Mandatory Fields
    image = models.ImageField(blank=True, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True) 
    barcode = models.IntegerField(blank=True, null=True) 
    brand = models.CharField(max_length=50, blank=True, null=True) 
    tags = models.ManyToManyField(Tag, blank=True, null=True) 
    exp_date= models.DateField(auto_now=False, blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True) 
    manufacturing_price = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return self.name
