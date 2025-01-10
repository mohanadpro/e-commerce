from django.urls import path
from .views import CategoryList, CategoryDetails
urlpatterns = [
    path('', CategoryList.as_view()),
    path('<int:pk>/', CategoryDetails.as_view()),
]