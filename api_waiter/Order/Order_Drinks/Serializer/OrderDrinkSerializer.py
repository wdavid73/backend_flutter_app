from rest_framework import serializers
from ...Model.ModelOrder import Order_Drinks

from api_admin.Drink.Serializer.SerializerDrink import DrinkSerializer
from api_admin.Drink.Model.ModelDrink import Drink

from ...Model.ModelOrder import Order
from ...Serializer.SerializerOrder import OrderSerializer


class OrderDrinkSerializer(serializers.ModelSerializer):

    drink = DrinkSerializer(read_only=True)
    drink_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Drink.objects.filter(state=1),
        source='drink'
    )

    order = OrderSerializer(read_only=True)
    order_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Order.objects.filter(action=1),
        source='order'
    )

    class Meta:
        model = Order_Drinks
        fields = [
            'id',
            'drink', 'drink_id',
            'order', 'order_code'
        ]
