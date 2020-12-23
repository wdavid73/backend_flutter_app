from rest_framework import serializers
from ...Model.ModelOrder import Order_Dish

from api_admin.Dish.serializers.DishSerializer import DishSerializer
from api_admin.Dish.models.DishModel import Dish

from ...Model.ModelOrder import Order
from ...Serializer.SerializerOrder import OrderSerializer


class OrderDishSerializer(serializers.ModelSerializer):

    dish = DishSerializer(read_only=True)
    dish_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Dish.objects.filter(state=1),
        source='dish'
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
            'dish', 'dish_id',
            'order', 'order_code'
        ]
