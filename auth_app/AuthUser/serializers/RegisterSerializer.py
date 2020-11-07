from rest_framework import serializers
from django.contrib.auth.models import User

from ...CustomUser import CustomUser
from ...Restaurant.models.RestaurantModel import Restaurant
from ...Position.models.PositionModel import Position
from ...Restaurant.serializers.RestaurantSerializer import RestaurantSerializer
from ...Position.serializers.PositionSerializer import PositionSerializer


class RegisterSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    restaurant_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Restaurant.objects.filter(state=1),
        source='restaurant'
    )

    position = PositionSerializer(read_only=True)
    position_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Position.objects.filter(state=1),
        source='position'
    )

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone',
            'restaurant_code',
            'restaurant',
            'position_id',
            'position'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
            username, email, password, first_name, last_name, phone, restaurant_code, position_id
        """

        user = CustomUser.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
            validated_data["first_name"],
            validated_data["last_name"],
            validated_data["phone"],
            validated_data["restaurant"],
            validated_data["position"]
        )

        return user
