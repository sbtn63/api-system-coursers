from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskSaveSerializer
from utils.responses import api_response

class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(course__institution__user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return api_response(request, serializer.data, "List Tasks!!");
    
    def post(self, request, *args, **kwargs):
        serializer = TaskSaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            task = serializer.save()
            return api_response(
                request,
                TaskSerializer(task).data,
                "Create Task Success",
                status.HTTP_201_CREATED
            )
            
        return api_response(
            request,
            serializer.errors,
            "Create Task Failed",
            status.HTTP_400_BAD_REQUEST
        )
        
class TaskDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk, course__institution__user=request.user)
        serializer = TaskSerializer(task)
        return api_response(request, serializer.data, "Get Task Success")
    
    def put(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk, course__institution__user=request.user)
        serializer = TaskSaveSerializer(
            task,
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            task = serializer.save()
            return api_response(
                request,
                TaskSerializer(task).data,
                "Update Task Sucess"
            )
            
        return api_response(
            request,
            serializer.errors,
            "Update Failed Task",
            status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk, course__institution__user=request.user)
        task.delete()
        return api_response(
            request,
            TaskSerializer(task).data,
            "Delete Task Success"
        )