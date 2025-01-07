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
    street = models.CharField(max_length=75)
    street_number = models.IntegerField()
    zipcode = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    country = models.CharField(max_length=75)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)