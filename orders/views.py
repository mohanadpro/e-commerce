from rest_framework import generics
from .models import Order
from .models import Order_Product
from .serializers import OrderSerializer, OrderDetailsSerializer
from e_commerce.permissions import IsOwnerOrReadOnly
import simplejson
# Create your views here.
class OrderList(generics.ListCreateAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        cart = self.request.POST.get('cart')
        

        # order = serializer.save()

class OrderDetails(generics.RetrieveAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'
    print(lookup_url_kwarg)    
    queryset = Order_Product.objects.all()
