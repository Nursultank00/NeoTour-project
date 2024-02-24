from django.urls import path, include
from .views import TourListAPIView, TourDetailAPIView, ReviewListAPIView

urlpatterns = [
    path('tours/', TourListAPIView.as_view(), name = 'tours'),
    path('tours/<int:pk>', TourDetailAPIView.as_view(), name = 'tours-detail'),
    path('tours/<int:pk>/reviews', ReviewListAPIView.as_view(), name = 'tours-reviews')
]