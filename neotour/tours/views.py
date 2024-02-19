from django.shortcuts import render
from rest_framework.views import Response, status
from rest_framework.views import APIView
from .models import Tour, Category
from .serializers import CategoryListSerializer, TourListSerializer, TourDetailSerializer
from .serializers import TourReviewListSerializer, ReservationSerializer

from datetime import datetime

def parse_month(cur_month):
    if cur_month in (12,1,2):
        return 'Winter'
    elif cur_month in (3,4,5):
        return 'Spring'
    elif cur_month in (6,7,8):
        return 'Summer'
    else:
        return 'Autumn'

class TourListAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        category_tours = Tour.objects.all()
        current_month = datetime.now().month
        current_season = parse_month(current_month)
        recommended_tours = Tour.objects.all().filter(season = current_season)
        categories_serializer = CategoryListSerializer(categories, many = True)
        category_tours_serializer = TourListSerializer(category_tours, many = True)
        recommended_tours_serializer = TourListSerializer(recommended_tours, many = True)
        content = {
            "Categories": categories_serializer.data, 
            "Tours": category_tours_serializer.data,
            "Recommended tours": recommended_tours_serializer.data,
        }
        return Response(content)

class TourDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            tour = Tour.objects.all().get(id = kwargs['pk'])
        except Exception as e:
            return Response({"data": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        reviews = tour.reviews.all()
        tour_serializer = TourDetailSerializer(tour)
        reviews_serializer = TourReviewListSerializer(reviews, many = True)
        content = {
            "Tour info" : tour_serializer.data,
            "Reviews" : reviews_serializer.data
        }
        return Response(content, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        request.data['tour_reserved'] = kwargs['pk']
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)