from django.db import models
from product.models import Product
from order.models import Order

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.FloatField()

    def __str__(self):
        return f"{self.order} - {self.product}"
    
    class Meta:
        db_table = 'order_details'

