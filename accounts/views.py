from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from django.utils import timezone

from accounts.serializers import RegisterSerializer, LoginSerializer
from utils.responses import api_response

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            data = {"token": token.key}
            return api_response(request, data, "Login Success!!")
            
        return api_response(
            request, 
            serializer.errors, 
            "Login Failed!!", 
            status.HTTP_400_BAD_REQUEST
        )

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            data = {"token": token.key}
            return api_response(request, data, "Register Success!!", status.HTTP_201_CREATED)
            
        return api_response(
            request, 
            serializer.errors, 
            "Register Failed!!", 
            status.HTTP_400_BAD_REQUEST
        )

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        data =  {
            "user": request.user.username,
            "logout_at": timezone.now()
        }
        return api_response(request, data, "Logout Success!!")      