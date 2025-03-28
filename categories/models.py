from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=75, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.name
