from django.db import models
from user.models import User
from enum import Enum

class OrderStatus(Enum):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in OrderStatus])
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.order_status} - {self.order_price}"
    
    class Meta:
        db_table = 'order'

