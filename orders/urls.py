from django.urls import path
from .views import OrderList, OrderDetails
urlpatterns = [
    path('', OrderList.as_view()),
    path('<int:id>/', OrderDetails.as_view()),
]