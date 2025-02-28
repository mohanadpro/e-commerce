from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer
class CustomLoginView(LoginView):
    def get_response(self):
        # Get the default response from the parent class
        response = super().get_response()
        is_admin = False
        # Check if the user is authenticated
        if self.user and self.user.is_authenticated:
            # Check if the user is an admin
            if self.user.is_staff:
                is_admin = True
    
        response.data['is_admin'] = is_admin
        
        return response
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the currently authenticated user
        user = request.user
        # user.is_admin = True
        serializer = UserSerializer(user)
        is_admin = False
        if user and user.is_authenticated:
        # Check if the user is an admin
            if user.is_staff:
                is_admin = True

        sended_data = {'user':serializer.data, 'is_admin': is_admin}
        return Response(sended_data)
