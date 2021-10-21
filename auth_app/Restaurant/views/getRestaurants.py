
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request

from ..models.RestaurantModel import Restaurant
from ..serializers.RestaurantSerializer import RestaurantSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def getRestaurants(request: Request):
    restaurants = Restaurant.objects.filter(state=1)
    serializer = RestaurantSerializer(
        restaurants, many=True, context={'request': request})
    return Response({'restaurants': serializer.data}, status=status.HTTP_200_OK)
