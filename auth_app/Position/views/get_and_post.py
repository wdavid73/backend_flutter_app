import random
from typing import Union, List, Dict
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.PositionModel import Position
from ..serializers.PositionSerializer import PositionSerializer


class GetAndPost(APIView):
    def get(self, request: Request):
        restaurants = Position.objects.filter(state=1)
        serializer = PositionSerializer(
            restaurants, many=True, context={'request': request})
        return Response({'positions': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = PositionSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
