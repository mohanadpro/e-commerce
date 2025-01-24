from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter
from .models import Category
from .serializers import CategorySerializer
from e_commerce.permissions import IsOwnerOrReadOnly
# Create your views here.


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_class = CategoryFilter

    queryset = Category.objects.all()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
