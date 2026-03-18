from django.urls import path

from institutions.views import InstitutionView, InstitutionDetailView

urlpatterns = [
    path('', InstitutionView.as_view()),
    path('<int:pk>/', InstitutionDetailView.as_view()),
]
