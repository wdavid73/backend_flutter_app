from rest_framework import serializers
from ..models.DishModel import Dish
from auth_app.Restaurant.models.RestaurantModel import Restaurant
from auth_app.Restaurant.serializers.RestaurantSerializer import RestaurantSerializer


class DishSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    restaurant_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Restaurant.objects.filter(state=1),
        source='restaurant'
    )

    class Meta:
        model = Dish
        fields = ['name', 'price', 'type',
                  'restaurant', 'restaurant_code', 'photo']
