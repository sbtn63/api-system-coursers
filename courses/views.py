from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from courses.models import Course
from courses.serializers import CourseSaveSerializer, CourseSerializer
from utils.responses import api_response


class CourseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(user=request.user)
        serializer = CourseSerializer(courses, many=True)
        return api_response(request, serializer.data, "List Courses")
    
    def post(self, request, *args, **kwargs):
        serializer = CourseSaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            course = serializer.save(user=request.user)
            return api_response(
                request,
                CourseSerializer(course).data,
                "Create Course Success",
                status.HTTP_201_CREATED
            )
            
        return api_response(
            request,
            serializer.errors,
            "Create Course Failed",
            status.HTTP_400_BAD_REQUEST
        )

class CourseDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk, user=request.user)
        serializer = CourseSerializer(course)
        return api_response(request, serializer.data, "Get Course Success")
    
    def put(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk, user=request.user)
        serializer = CourseSaveSerializer(
            course,
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            course = serializer.save()
            return api_response(
                request,
                CourseSerializer(course).data,
                "Update Course Success"
            )
        
        return api_response(
            request,
            serializer.errors,
            "Update Course Failed",
            status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk, user=request.user)
        course.delete()
        return api_response(
            request,
            CourseSerializer(course).data,
            "Delete Course Success"
        )
