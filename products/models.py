from django.db import models
from categories.models import Category
# Create your models here.


class Product(models.Model):
    colors = [
        ('Black', 'Black'),
        ('White', 'White'),
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Blue', 'Blue'),
        ('Pink', 'Pink'),
        ('Lilac', 'Lilac'),
        ('Brown', 'Brown'),
        ('Beige', 'Beige'),
        ('Gray', 'Gray'),
        ('Salmon', 'Salmon'),
    ]
    sizes = [
        ('2XS', '2XS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
    ]
    genders = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Babys', 'Babys'),
        ('Girls', 'Girls'),
        ('Unisex', 'Unisex'),
        ('Youth', 'youth'),
    ]
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../product_defult_name_image_ufzxtf'
    )
    price = models.FloatField()
    description = models.TextField()
    color = models.CharField(max_length=35, choices=colors, blank=True)
    size = models.CharField(max_length=35, choices=sizes, blank=True)
    genders = models.CharField(max_length=35, choices=genders, blank=True)
