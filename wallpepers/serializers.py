from rest_framework import serializers

from wallpepers.models import WallPeper

class WallPeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallPeper
        fields =  ('id', 'wallpeper', 'created_at')