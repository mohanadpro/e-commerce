from django.urls import path
from .views import OrderList, OrderDetails, OrderlistAllOrders, OrderDestroy
urlpatterns = [
    path('', OrderList.as_view()),
    path('<int:pk>/', OrderDestroy.as_view()),
    path('allOrders/', OrderlistAllOrders.as_view()),
    path('orderDetails/<int:pk>/', OrderDetails.as_view()),
]
