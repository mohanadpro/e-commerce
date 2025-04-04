# Generated by Django 4.2 on 2025-01-10 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='../product_defult_name_image_ufzxtf', upload_to='images/')),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('color', models.CharField(blank=True, choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Lilac', 'Lilac'), ('Brown', 'Brown'), ('Beige', 'Beige'), ('Gray', 'Gray'), ('Salmon', 'Salmon')], max_length=35)),
                ('size', models.CharField(blank=True, choices=[('2XS', '2XS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL')], max_length=35)),
                ('genders', models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women'), ('Babys', 'Babys'), ('Girls', 'Girls'), ('Unisex', 'Unisex'), ('Youth', 'youth')], max_length=35)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]
