from rest_framework import serializers
from django.contrib.auth.models import User

from ..Restaurant.models.RestaurantModel import Restaurant
from ..Position.models.PositionModel import Position


class UserSerializer(serializers.ModelSerializer):

    # restaurant_code =

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'phone',
            'email'
            'restaurant_code'
            'position_id'
        )
