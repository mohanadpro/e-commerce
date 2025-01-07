from django.urls import path
from .views import ProfileList, ProfileDetails
urlpatterns = [
    path('', ProfileList.as_view()),
    path('<int:pk>/', ProfileDetails.as_view()),
]