from rest_framework import serializers
from ..models.RestaurantModel import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['code', 'name', 'cellphone', 'phone', 'address']
