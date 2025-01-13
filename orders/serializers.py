from rest_framework import serializers
from .models import Order, Order_Product
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'created_at',
            'customer', 'total_price'
            ]

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = [
            'id', 'product',
            'order', 'count',
            'price', 'total_price'
        ]