from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from institutions.models import Institution
from institutions.serializers import InstitutionSerializer, InstitutionSaveSerializer
from utils.responses import api_response 

class InstitutionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        institutions = Institution.objects.filter(user=request.user)
        serializer = InstitutionSerializer(institutions, many=True)
        return api_response(request, serializer.data, "List Institutions")
    
    def post(self, request, *args, **kwargs):
        serializer = InstitutionSaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            institution = serializer.save(user=request.user)
            return api_response(
                request, 
                InstitutionSerializer(institution).data,
                "Create Institution Success", 
                status.HTTP_201_CREATED
            )
               
        return api_response(
            request, 
            serializer.errors,
            "Create Institution Error",
            status.HTTP_400_BAD_REQUEST
        )

class InstitutionDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, pk, *args, **kwargs):
        institution = get_object_or_404(Institution, pk=pk, user=request.user)
        serializer = InstitutionSerializer(institution)
        return api_response(request, serializer.data, "Get Institution")
    
    def put(self, request, pk, *args, **kwargs):
        institution = get_object_or_404(Institution, pk=pk, user=request.user)
        serializer = InstitutionSaveSerializer(
            institution, 
            data=request.data, 
            context={'request': request}
        )
        
        if serializer.is_valid():
            institution = serializer.save()
            return api_response(
                request,
                InstitutionSerializer(institution).data,
                "Update Institution Success",
            )
        
        return api_response(
            request,
            serializer.errors,
            "Update Institution Error",
            status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk, *args, **kwargs):
        institution = get_object_or_404(Institution, pk=pk, user=request.user)
        institution.delete()
        return api_response(
            request,
            InstitutionSerializer(institution).data,
            "Delete Institution Success",
        )