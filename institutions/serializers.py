from rest_framework import serializers

from institutions.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Institution
        fields =  ('id', 'name', 'description', 'emblem', 'user_id', 'created_at')

class InstitutionSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'description', 'emblem')