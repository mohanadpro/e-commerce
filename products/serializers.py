from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category',
            'created_at', 'updated_at',
            'image', 'price', 'description',
            'color', 'size', 'genders'
            ]