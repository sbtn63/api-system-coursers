from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from accounts.serializers import RegisterSerializer, LoginSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serilizer = LoginSerializer(data=request.data)
        
        if serilizer.is_valid():
            user = serilizer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                "message": "Login exitoso",
                "path": request.path,
                "status": status.HTTP_200_OK,
                "data": {
                    "token": token.key
                }
            }, status=status.HTTP_200_OK)
            
        return Response({
            "message": "Login fallido",
            "path": request.path,
            "status": status.HTTP_400_BAD_REQUEST,
            "data": serilizer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                "message": "Registro exitoso",
                "path": request.path,
                "status": status.HTTP_201_CREATED,
                "data": {
                    "token": token.key
                }
            }, status=status.HTTP_201_CREATED)
            
        return Response({
                "message": "Registro fallido",
                "path": request.path,
                "status": status.HTTP_400_BAD_REQUEST,
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({
                "message": "Logout realizado",
                "path": request.path,
                "status": status.HTTP_200_OK,
                "data": None
            }, status=status.HTTP_200_OK)       