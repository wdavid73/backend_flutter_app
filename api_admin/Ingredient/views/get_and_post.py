from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user

from ..models.IngredientModel import Ingredient
from ..serializers.IngredientSerializer import IngredientSerializer


class GetAndPost(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request: Request):
        if validate_user(request):
            ingredient = Ingredient.objects.filter(state=1)
            serializer = IngredientSerializer(
                ingredient, many=True, context={'request': request})
            return Response({"ingredients": serializer.data, "status": status.HTTP_200_OK})
        return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})

    def post(self, request: Request):
        if validate_user(request):
            serializer = IngredientSerializer(
                data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})
            return Response({"erros" : serializer.errors , "status" : status.HTTP_400_BAD_REQUEST})
        return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})
