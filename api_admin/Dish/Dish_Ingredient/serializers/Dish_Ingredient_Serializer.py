from rest_framework import serializers
from ...models.DishModel import Dish_Ingredient
from ...models.DishModel import Dish
from ....Ingredient.models.IngredientModel import Ingredient
from ...serializers.DishSerializer import DishSerializer
from ....Ingredient.serializers.IngredientSerializer import IngredientSerializer


class Dish_Ingredient_Serializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Dish.objects.filter(state=1),
        source="dish"
    )

    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Ingredient.objects.filter(state=1),
        source='ingredient'
    )

    class Meta:
        model = Dish_Ingredient
        fields = ['id', 'dish', 'dish_id', 'ingredient', 'ingredient_id']
