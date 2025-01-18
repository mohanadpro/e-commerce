from rest_framework import generics
from rest_framework.response import Response
from .models import Order
from .models import Order_Product
from .serializers import OrderSerializer, OrderDetailsSerializer
from e_commerce.permissions import IsOwnerOrReadOnly
import json
# Create your views here.
class OrderList(generics.ListCreateAPIView):

    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OrderSerializer


    def list(self, request):
        queryset = Order.objects.filter(customer=self.request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        if serializer.is_valid():
            order = serializer.save()
            cart = self.request.POST.get('cart')
            delivery_place = self.request.POST.get('delivery_place')
            products = json.loads(cart)
            for prod in products:
                try:
                    prod['order'] = order.id
                    saved_product = OrderDetailsSerializer(data=prod)
                    if saved_product.is_valid():
                        saved_product.save()
                    else:
                        print('serializer is not valid')
                except ValidationError as e:
                    print(str(e))
                except Exception as ex:
                    print(str(ex))

class OrderDetails(generics.ListCreateAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        queryset = Order_Product.objects.filter(order=order_id)
        serializer = OrderDetailsSerializer(queryset, many=True)
        return Response(serializer.data)
