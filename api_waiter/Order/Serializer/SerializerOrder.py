from rest_framework import serializers
from ..Model.ModelOrder import Order

from api_admin.Table.Model.ModelTable import Table
from api_admin.Drink.Model.ModelDrink import Drink
from api_admin.Complement.Model.ModelComplement import Complement
from api_admin.Dish.models.DishModel import Dish
from auth_app.models import CustomUser

from api_admin.Table.Serializer.SerializerTable import TableSerializer
from api_admin.Drink.Serializer.SerializerDrink import DrinkSerializer
from api_admin.Complement.Serializer.SerializerComplement import ComplementSerializer
from api_admin.Dish.serializers.DishSerializer import DishSerializer
from auth_app.AuthUser.serializers.UserSerializer import UserSerializer


class OrderSerializer(serializers.ModelSerializer):

    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Table.objects.filter(state=1),
        source='table'
    )

    """
    drink = DrinkSerializer(read_only=True)
    drink_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Drink.objects.filter(state=1),
        source='drink'
    )

    complement = ComplementSerializer(read_only=True)
    complement_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Complement.objects.filter(state=1),
        source='complement'
    )

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CustomUser.objects.filter(state=1),
        source="user"
    ) """

    class Meta:
        model = Order
        fields = [
            'code', 'date', 'total',
            'action',
            'table', 'table_id',
            # 'drink', 'drink_id',
            # 'complement', 'complement_id',
            # 'dish', 'dish_id',
            # 'user', 'user_id',
        ]
