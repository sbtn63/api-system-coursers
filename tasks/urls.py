from django.urls import path

from tasks.views import TaskView, TaskDetailView

urlpatterns = [
    path('', TaskView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view()),
]
