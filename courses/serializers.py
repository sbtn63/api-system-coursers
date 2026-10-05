from rest_framework import serializers

from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    institution_id = serializers.ReadOnlyField(source='institution.id')
    wallpaper_id = serializers.ReadOnlyField(source='wallpaper.id')
    class Meta:
        model = Course
        fields = (
            'id', 
            'code', 
            'name', 
            'block', 
            'period', 
            'status', 
            'start_date', 
            'end_date', 
            'institution_id', 
            'wallpaper_id', 
            'created_at'
        )
    
class CourseSaveSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )
    block = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )
    period = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )
    class Meta:
        model = Course
        fields = (
            'code',
            'name',
            'block',
            'period',
            'status',
            'start_date',
            'end_date',
            'institution',
            'wallpeper'
        )
    
    def validate_name(self, value):
            user = self.context['request'].user
            institution = self.context['request'].institution
            instance = self.instance
            queryset = Course.objects.filter(user=user, name=value, institution=institution)
            
            if instance:
                queryset = queryset.exclude(pk=instance.pk)
            
            if queryset.exists():
                raise serializers.ValidationError("Name already exists for this name and Institution")
            
            return value