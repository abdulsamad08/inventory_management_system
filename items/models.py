from django.db import models
from product.models import Product
from warehouse.models import Warehouse

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='items')
    total_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} in {self.warehouse} - {self.total_quantity}"

    class Meta:
        db_table = 'items'
