from django.urls import path

from institutions.views import InstitutionView

urlpatterns = [
    path('', InstitutionView.as_view()),
]
