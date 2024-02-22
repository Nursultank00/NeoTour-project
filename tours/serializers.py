from rest_framework.serializers import ModelSerializer
from .models import Category, Tour, Reservation, Review

class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class TourListSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['tour_name', 'image', 'category']

class RecommendedTourListSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['tour_name', 'image']
class TourDetailSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['tour_name', 'location', 'description', 'image']

class TourReviewListSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['nickname', 'review_image', 'commentary']

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


