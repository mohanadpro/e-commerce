from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from e_commerce.permissions import IsOwner


# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    queryset = Profile.objects.all()
