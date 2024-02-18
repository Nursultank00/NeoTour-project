from django.shortcuts import render
from rest_framework.views import Response, status
from rest_framework.views import APIView
from .models import Tour, Review
from .serializers import TourListSerializer, TourDetailSerializer
from .serializers import TourReviewListSerializer, ReservationSerializer


class TourListAPIView(APIView):

    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourListSerializer(tours, many = True)
        return Response(serializer.data)

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