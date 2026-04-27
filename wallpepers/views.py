from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from wallpepers.models import WallPeper
from wallpepers.serializers import WallPeperSerializer
from utils.responses import api_response 

class WallPeperView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        wallpepers = WallPeper.objects.all()
        serializer = WallPeperSerializer(wallpepers, many=True)
        return api_response(request, serializer.data, "List WallPepers")

class WallPeperDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, *args, **kwargs):
        wallpeper = get_object_or_404(WallPeper, pk=pk)
        serializer = WallPeperSerializer(wallpeper)
        return api_response(request, serializer.data, "Get WallPeper")
