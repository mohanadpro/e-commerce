from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category',
            'created_at', 'updated_at',
            'image', 'price', 'description',
            'color', 'size', 'genders',
            'category_name'
            ]
