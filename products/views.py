from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from e_commerce.permissions import IsAdminOrReadOnly
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'category'
    ]
    queryset = Product.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Product.objects.all()
