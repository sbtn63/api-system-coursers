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
            'course_status', 
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
            'course_status',
            'start_date',
            'end_date',
            'institution',
            'wallpaper'
        )
    
    def validate_institution(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("Institution not exists!!")  
        return value
    
    def validate_name(self, value):
        user = self.context['request'].user
        instance = self.instance
        institution = self.initial_data.get('institution')
        queryset = Course.objects.filter(
            name=value, 
            institution=institution, 
            institution__user=user
        )
            
        if instance:
            queryset = queryset.exclude(pk=instance.pk)
            
        if queryset.exists():
            raise serializers.ValidationError("Name already exists for this name and Institution")
            
        return value