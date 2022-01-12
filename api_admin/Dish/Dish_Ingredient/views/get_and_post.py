from typing import List
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user
from ...models.DishModel import Dish_Ingredient
from ..serializers.Dish_Ingredient_Serializer import Dish_Ingredient_Serializer
from ....Ingredient.models.IngredientModel import Ingredient
from ....Ingredient.serializers.IngredientSerializer import IngredientSerializer



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
            ingredients_id = request.data["ingredients_id"]
            if(len(ingredients_id) > 0):
                ingredients_duplicate = []
                dish_id = request.data["dish_id"]
                for _id in ingredients_id:
                    if not Dish_Ingredient.objects.filter(dish_id=dish_id, ingredient_id=_id).exists():
                        request.data["ingredient_id"] = _id
                        serializer = Dish_Ingredient_Serializer(data=request.data, context={'request': request})
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        ingredients_duplicate.append(Ingredient.objects.get(id=_id))
                
                duplicates = serializeIngredients(ingredients_duplicate, request)
                return Response(
                    {"data":"Ingredients added successfully", "ingredients_duplicate" : duplicates},
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"detail": "Ingredients Empty"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors": "user invalid", "stauts": status.HTTP_401_UNAUTHORIZED})


def serializeIngredients(ingredients: List, request: Request):
    return [
        IngredientSerializer(
            ingredient, context={'request':request},
        ).data for ingredient in ingredients
    ]