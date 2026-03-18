from rest_framework import serializers

from institutions.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Institution
        fields =  ('id', 'name', 'description', 'emblem', 'user_id', 'created_at')

class InstitutionSaveSerializer(serializers.ModelSerializer):
    description = serializers.CharField(
        required=False, 
        allow_blank=True, 
        default=""
    )
    emblem = serializers.CharField(
        required=False, 
        allow_null=True, 
        allow_blank=True, 
        default=None
    )
    class Meta:
        model = Institution
        fields = ('name', 'description', 'emblem')
    
    def validate_name(self, value):
        user = self.context['request'].user
        instance = self.instance
        queryset = Institution.objects.filter(user=user, name=value)
        
        if instance:
            queryset = queryset.exclude(pk=instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("Name already exists for this name")
        
        return value