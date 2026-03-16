from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from institutions.models import Institution
from institutions.serializers import InstitutionSerializer, InstitutionSaveSerializer

class InstitutionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        institutions = Institution.objects.filter(user=request.user)
        serializer = InstitutionSerializer(institutions, many=True)
        return Response({
            "message": "List Institutions",
            "path": request.path,
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = InstitutionSaveSerializer(data=request.data)
        if serializer.is_valid():
            institution = serializer.save(user=request.user)
            
            return Response({
                "message": "Create Institution Success",
                "path": request.path,
                "status": status.HTTP_201_CREATED,
                "data": InstitutionSerializer(institution).data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
                "message": "Create Institution Error",
                "path": request.path,
                "status": status.HTTP_400_BAD_REQUEST,
                "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)    
