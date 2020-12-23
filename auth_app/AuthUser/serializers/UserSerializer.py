from rest_framework import serializers
from django.contrib.auth import authenticate
from ...CustomUser import CustomUser
from ...Restaurant.models.RestaurantModel import Restaurant
from ...Position.models.PositionModel import Position
from ...Restaurant.serializers.RestaurantSerializer import RestaurantSerializer
from ...Position.serializers.PositionSerializer import PositionSerializer


class UserSerializer(serializers.ModelSerializer):

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
            # 'password',
            'phone',
            'restaurant_code',
            'restaurant',
            'position_id',
            'position'
        )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
