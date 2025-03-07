from rest_framework import serializers
from .models import Order, Order_Product


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = [
            'id', 'created_at',
            'customer', 'total_price',
            'delivery_place',
            'is_delivered',
            'customer_name'
            ]


class OrderDetailsSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Order_Product
        fields = [
            'id', 'product',
            'order', 'count',
            'price', 'total_price',
            'product_name', 'customer'
        ]
