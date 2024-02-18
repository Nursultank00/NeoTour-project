from rest_framework.serializers import ModelSerializer
from .models import Tour, Reservation, Review

class TourListSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class TourDetailSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class TourReviewListSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['nickname', 'review_image', 'commentary']

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


