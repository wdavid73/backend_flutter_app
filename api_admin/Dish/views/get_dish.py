from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import validate_user, validate_restaurant_code, user_validate_required

from ..models.DishModel import Dish, Dish_Ingredient
from ...Ingredient.models.IngredientModel import Ingredient
from ..Dish_Ingredient.serializers.Dish_Ingredient_Serializer import Dish_Ingredient_Serializer
from ..serializers.DishSerializer import DishSerializer
from ...Ingredient.serializers.IngredientSerializer import IngredientSerializer


@api_view(["GET"])
@user_validate_required
def get_dish_with_ingredient(request: Request, id: int):
    dish = DishSerializer(
        Dish.objects.filter(state=1,
                            id=Dish_Ingredient.objects.filter(
                                state=1,
                                dish_id=id)[0].dish.id
                            # primer platillo ya que se repiten
                            ), many=True, context={'request': request}
    ).data
    response_ingredients = [
        IngredientSerializer(
            ingredient, context={"request": request}
        ).data for ingredient in Ingredient.objects.filter(
            id__in=[
                ingredients.ingredient.id for ingredients in list(
                    Dish_Ingredient.objects.filter(state=1, dish_id=id)
                    # lista de id de los ingredientes del platillo
                )
            ], state=1
        )
    ]
    return Response(
        {
            "dish": dish,
            "ingredients": response_ingredients,
            "status": status.HTTP_200_OK}
    )