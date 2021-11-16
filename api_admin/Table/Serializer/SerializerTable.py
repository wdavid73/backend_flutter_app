from rest_framework import serializers
from ..Model.ModelTable import Table
from auth_app.Restaurant.models.RestaurantModel import Restaurant
from auth_app.Restaurant.serializers.RestaurantSerializer import RestaurantSerializer


class TableSerializer(serializers.ModelSerializer):

    restaurant = RestaurantSerializer(read_only=True)
    restaurant_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Restaurant.objects.filter(state=1),
        source='restaurant'
    )

    class Meta:
        model = Table
        fields = ('id', 'ref', "state", 'restaurant', 'restaurant_code')
