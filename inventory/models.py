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
    image = models.ImageField()
    name = models.CharField(max_length=50) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    stock = models.IntegerField()
    selling_price = models.FloatField() 

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    # Non Mandatory Fields
    sku = models.CharField(max_length=50, blank=True, null=True) 
    barcode = models.IntegerField(blank=True, null=True) 
    brand = models.CharField(max_length=50, blank=True, null=True) 
    tags = models.ManyToManyField(Tag, blank=True) 
    exp_date= models.DateField(auto_now=False, blank=True, null=True)
    manufacturing_price = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return self.name
