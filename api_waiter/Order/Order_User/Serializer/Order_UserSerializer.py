from rest_framework import serializers
from ...Model.ModelOrder import Order_Dish

from auth_app.AuthUser.serializers.UserSerializer import UserSerializer
from auth_app.CustomUser import CustomUser

from ...Model.ModelOrder import Order
from ...Serializer.SerializerOrder import OrderSerializer


class OrderUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CustomUser.objects.filter(state=1),
        source='user'
    )

    order = OrderSerializer(read_only=True)
    order_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Order.objects.filter(action=1),
        source='order'
    )

    class Meta:
        model = Order_Dish
        fields = [
            'id',
            'user', 'user_id',
            'order', 'order_code'
        ]
