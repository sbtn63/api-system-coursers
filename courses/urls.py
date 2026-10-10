from django.urls import path

from courses.views import CourseView, CourseDetailView

urlpatterns = [
    path('', CourseView.as_view()),
    path('<int:pk>/', CourseDetailView.as_view()),
]
