from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_place = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-created_at']

class Order_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True)
    count = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
