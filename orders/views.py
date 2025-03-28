from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order
from .models import Order_Product
from .serializers import OrderSerializer, OrderDetailsSerializer
from e_commerce.permissions import IsOwner, IsAdminOrReadOnly, IsOwnerOrReadOnly, IsAdminOrOwner
import json
from rest_framework import status
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib

def sendEmail(body, email_receiver):
    email_sender = 'ebuy.13.1993@gmail.com'
    email_password = os.environ.get('EMAIL_PASSWORD')
    email_receiver = email_receiver
    subject = "confirmation of your order"
    part2 = MIMEText(body, 'html')

    em = MIMEMultipart('alternative')
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def create_email_body(delivery_place, user, order_id, total_price, products):
    body = """
    <html>
    <head>
        <style>
            table, th, td{
                border: 1px solid black;
            }
            th,td{
                padding: 3px 6px;
            }
            table
            {
                border-collapse:collapse;        
            }
            td{
                text-align: center;
            }
            th{
                background-color:#f44804;
                color:white;
            }
    </style>
    </head>
    <body style="font-size:15px">
    """
    body+=f"""<p>Hello Dear {user}! <br>
    Thanks for your order <br>
    The Order Number is : {order_id} <br>
    Total Price : {total_price} <br>
    Your order will be delivered to the address {delivery_place}
    You can see Details in the below table
    </p>
    <table>
    <thead>
        <th> Item</th>
        <th> Number</th>
        <th> Price</th>
        <th> Total Price</th>
    </thead>
    <tbody>
    """
    for prod in products:
        body +=f"""
            <tr> 
                <td> {prod['name']} </td>
                <td> {prod['count']} </td>
                <td> {prod['price']} </td>
                <td> {prod['total_price']} </td>
            </tr>
        """
    body+="""
    </tbody>
    </table>
    <p>You will receive another email with the tracking number after we send your order<br><br>
    If you have another problem with the order<br><br>
    Please don't hesitate to contact us on the below email <br>
    </p>
    <p>
    With special regards <br> 
    EBuy Customer Service <br>
    ebuy-customerservice@gmail.com
    </p>
    </body>
    </html>
    """
    return body


class OrderlistAllOrders(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(is_delivered=False)


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OrderSerializer

    def list(self, request):
        try:
            if self.request.user == 'AnonymousUser':
                data = {'message': 'User is not authorized '}
                return Response(data, status=401)
            else:
                queryset = Order.objects.filter(customer=self.request.user)
                serializer = OrderSerializer(queryset, many=True)
                return Response(serializer.data)
        except Exception as e:
            data = {'message': 'error exception '}
            return Response(data, status=401)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        if order is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def perform_create(self, serializer):
        if serializer.is_valid():
            
            order = serializer.save()
            cart = self.request.POST.get('cart')
            total_price = self.request.POST.get('total_price')
            email = self.request.POST.get('email')
            delivery_place = self.request.POST.get('delivery_place')
            products = json.loads(cart)
            for prod in products:
                try:
                    prod['order'] = order.id
                    prod['customer'] = self.request.user.id
                    saved_product = OrderDetailsSerializer(data=prod)
                    if saved_product.is_valid():
                        saved_product.save()
                    else:
                        print('serializer is not valid')
                except Exception as ex:
                    print(str(ex))
            if email != "":
                body = create_email_body(delivery_place,'', order.id, total_price, products)
                sendEmail(body, email)

class OrderDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetails(generics.ListCreateAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAdminOrOwner]

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        queryset = Order_Product.objects.filter(order=order_id)
        serializer = OrderDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            order_id = self.kwargs['pk']
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
