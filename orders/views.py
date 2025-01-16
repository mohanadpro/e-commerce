from rest_framework import generics
from .models import Order
from .models import Order_Product
from .serializers import OrderSerializer, OrderDetailsSerializer
from e_commerce.permissions import IsOwnerOrReadOnly
import json
# Create your views here.
class OrderList(generics.ListCreateAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            order = serializer.save()
            cart = self.request.POST.get('cart')
            products = json.loads(cart)
            for prod in products:
                try:
                    prod['order'] = 5
                    saved_product = OrderDetailsSerializer(data=prod)
                    if saved_product.is_valid():
                        print('serializer is valid')
                        print(saved_product)
                        saved_product.save()
                    else:
                        print('serializer is not valid')
                    # print('success')
                except ValidationError as e:
                    print(str(e))
                except Exception as ex:
                    print(str(ex))

class OrderDetails(generics.RetrieveAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = 'id'
    print(lookup_url_kwarg)    
    queryset = Order_Product.objects.all()
