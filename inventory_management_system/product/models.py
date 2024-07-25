from django.db import models
from category.models import Category

class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.image.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    images = models.ManyToManyField(Image, related_name='products')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'