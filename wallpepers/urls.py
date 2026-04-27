from django.urls import path

from wallpepers.views import WallPeperView, WallPeperDetailView

urlpatterns = [
    path('', WallPeperView.as_view()),
    path('<int:pk>/', WallPeperDetailView.as_view())
]
