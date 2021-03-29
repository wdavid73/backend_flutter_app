from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user
from ...models.DishModel import Dish_Ingredient
from ..serializers.Dish_Ingredient_Serializer import Dish_Ingredient_Serializer


class GetAndPost(APIView):
    def get(self, request):
        if validate_user(request):
            dish_ingredient = Dish_Ingredient.objects.filter(state=1)
            serializer = Dish_Ingredient_Serializer(
                dish_ingredient, many=True, context={'request': request})
            return Response({"dish_ingredient": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "user invalid", "status": status.HTTP_400_BAD_REQUEST})

    def post(self, request):
        if validate_user(request):
            dish_id = request.data["dish_id"]
            ingredient_id = request.data["ingredient_id"]
            if not Dish_Ingredient.objects.filter(dish_id=dish_id, ingredient_id=ingredient_id).exists():
                serializer = Dish_Ingredient_Serializer(
                    data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({"dish_ingredient": serializer.data}, status=status.HTTP_200_OK)
                return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "The Dish Already Has That Ingredient"}, status=status.HTTP_226_IM_USED)
        return Response({"errors": "user invalid", "stauts": status.HTTP_401_UNAUTHORIZED})
