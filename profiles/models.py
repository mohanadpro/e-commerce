from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_iy5ppe'
    )
    street = models.CharField(max_length=75, blank=True)
    street_number = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=75, blank=True)
    city = models.CharField(max_length=75, blank=True)
    state = models.CharField(max_length=75, blank=True)
    country = models.CharField(max_length=75, blank=True)
    email = models.EmailField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
