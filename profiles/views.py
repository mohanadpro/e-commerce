from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from e_commerce.permissions import IsOwnerOrReadOnly

# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.all()