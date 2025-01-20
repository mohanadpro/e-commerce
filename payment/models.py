from django.db import models

# Create your models here.

class Card(models.Model):
    card_number = models.BigIntegerField()
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=4)
    cvv = models.IntegerField()