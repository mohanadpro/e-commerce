from django.urls import path
from .views import OrderList, OrderDetails
urlpatterns = [
    path('', OrderList.as_view()),
    path('orderDetails/<int:pk>/', OrderDetails.as_view()),
]
