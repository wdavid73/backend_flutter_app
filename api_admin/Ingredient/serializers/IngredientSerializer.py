from rest_framework import serializers
from rest_framework import fields
from ..models.IngredientModel import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit']
