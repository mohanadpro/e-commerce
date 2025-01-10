from django.db import models
from categories.models import Category
# Create your models here.
class Product(models.Model):
    colors = [
        ('Black','Black'),
        ('White','White'),
        ('Red','Red'),
        ('Green','Green'),
        ('Yellow','Yellow'),
        ('Blue','Blue'),
        ('Pink','Pink'),
        ('Lilac','Lilac'),
        ('Brown','Brown'),
        ('Beige','Beige'),
        ('Gray','Gray'),
        ('Salmon','Salmon'),
    ]
    sizes = [
        ('2XS','2XS'),
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('2XL','2XL'),
        ('3XL','3XL'),
        ('4XL','4XL')
    ]
    genders = [
        ('Men','Men'),
        ('Women','Women'),
        ('Babys','Babys'),
        ('Girls','Girls'),
        ('Unisex','Unisex'),
        ('Youth','youth'),
    ]
    name = models.CharField(max_length=100)
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