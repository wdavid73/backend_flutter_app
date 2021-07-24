from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user, validate_restaurant_code, user_validate_required
from my_restaurant_app.customPermissions import TokenPermission
from ..models.DishModel import Dish, Dish_Ingredient
from ...Ingredient.models.IngredientModel import Ingredient
from ..Dish_Ingredient.serializers.Dish_Ingredient_Serializer import Dish_Ingredient_Serializer
from ..serializers.DishSerializer import DishSerializer
from ...Ingredient.serializers.IngredientSerializer import IngredientSerializer


@api_view(["GET"])
@user_validate_required
@permission_classes([TokenPermission])
def get_dish_with_ingredient(request: Request, id: int):
    if len(Dish_Ingredient.objects.filter(state=1, dish_id=id)) > 0:
        dish = DishSerializer(
            Dish.objects.get(state=1, id=id),
            context={'request': request}
        ).data
        response_ingredients = [
            IngredientSerializer(
                ingredient,
                context={'request': request}
            ).data for ingredient in Ingredient.objects.filter(
                id__in=Ingredient.objects.filter(
                    state=1,
                    id__in=Dish_Ingredient.objects.filter(
                        dish_id=id
                    ).values_list(
                        "ingredient",
                        flat=True
                    )
                ),
                state=1
            )
        ]
        return Response(
            {
                "dish": dish,
                "ingredients": response_ingredients,
            }, status=status.HTTP_200_OK
        )
    else:
        return Response("Dish without Ingredients", status=status.HTTP_404_NOT_FOUND)
