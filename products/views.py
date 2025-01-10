from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from e_commerce.permissions import IsOwnerOrReadOnly
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()