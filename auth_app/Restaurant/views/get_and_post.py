from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.RestaurantModel import Restaurant
from ..serializers.RestaurantSerializer import RestaurantSerializer


class GetAndPost(APIView):
    def get(self, request: Request):
        restaurants = Restaurant.objects.filter(state=1)
        serializer = RestaurantSerializer(
            restaurants, many=True, context={'request': request})
        return Response({'restaurants': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = RestaurantSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
