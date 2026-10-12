from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    course_id = serializers.ReadOnlyField(source='course.id')
    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'avaliable_date',
            'deadline',
            'completed',
            'task_status',
            'course_id',
            'created_at'
        )
        
class TaskSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name',
            'avaliable_date',
            'deadline',
            'completed',
            'task_status',
            'course'
        )
    
    def validate_course(self, value):
        user = self.context['request'].user
        if value.institution.user != user:
            raise serializers.ValidationError("Course not exists!!")
        return value