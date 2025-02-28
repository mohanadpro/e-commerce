# users/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    profile_id = serializers.ReadOnlyField(source='profile.id')

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'profile_image', 'profile_id']
