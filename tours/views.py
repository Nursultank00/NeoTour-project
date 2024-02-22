from django.shortcuts import render
from rest_framework.views import Response, status
from rest_framework.views import APIView
from .models import Tour, Category
from .serializers import CategoryListSerializer, TourListSerializer, TourDetailSerializer
from .serializers import TourReviewListSerializer, ReservationSerializer, RecommendedTourListSerializer

from drf_spectacular.utils import extend_schema

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
    
    @extend_schema(
            summary = "Вывод списков туров",
            description = "Этот эндпоинт позволяет получить информацию о турах, разбитых по категориям и список рекомендованных туров",
    )
    def get(self, request):
        categories = Category.objects.all()
        category_tours = Tour.objects.all()
        current_month = datetime.now().month
        current_season = parse_month(current_month)
        recommended_tours = Tour.objects.all().filter(season = current_season)
        categories_serializer = CategoryListSerializer(categories, many = True)
        category_tours_serializer = TourListSerializer(category_tours, many = True)
        recommended_tours_serializer = RecommendedTourListSerializer(recommended_tours, many = True)
        content = {
            "Categories": categories_serializer.data, 
            "Tours": category_tours_serializer.data,
            "Recommended tours": recommended_tours_serializer.data,
        }
        return Response(content, status = status.HTTP_200_OK)

class TourDetailAPIView(APIView):

    @extend_schema(
            summary = "Вывод детальной информации о туре",
            description = "Этот эндпоинт позволяет получить детальную информацию о туре: название, локацию, описание и ревью, оставленные клиентами,тура",
    )
    def get(self, request, *args, **kwargs):
        """Эндпоинт для детальной информации о туре"""
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
    
    @extend_schema(
            summary = "Отправка информации о бронировании",
            description = "Этот эндпоинт позволяет забронировать тур с помощью номера телефона и указанием количества людей",
    )
    def post(self, request, *args, **kwargs):
        """Эндпоинт для бронирования туров"""
        request.data['tour_reserved'] = kwargs['pk']
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)