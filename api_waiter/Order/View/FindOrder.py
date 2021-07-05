from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from my_restaurant_app.validations import user_validate_required
from ..Model.ModelOrder import Order, Order_Complement, Order_Dish, Order_Drinks, Order_User
from ..Serializer.SerializerOrder import OrderSerializer

from api_admin.Dish.models.DishModel import Dish
from api_admin.Dish.serializers.DishSerializer import DishSerializer
from api_admin.Drink.Model.ModelDrink import Drink
from api_admin.Drink.Serializer.SerializerDrink import DrinkSerializer
from api_admin.Complement.Model.ModelComplement import Complement
from api_admin.Complement.Serializer.SerializerComplement import ComplementSerializer


@api_view(["GET"])
@user_validate_required
@permission_classes([IsAuthenticated])
def find_order(request: Request, code: str):

    # find order
    order = Order.objects.exclude(action=3).get(code=code)
    order_dish = Order_Dish.objects.filter(order=order)
    order_drink = Order_Drinks.objects.filter(order=order)
    order_complement = Order_Complement.objects.filter(order=order)
    order_serializer = OrderSerializer(order, context={'request': request})

    # find dishes in order
    dishes_id = [od.dish.id for od in order_dish]
    dishes = [
        DishSerializer(
            dish,
            context={'request': request}
        ).data for dish in Dish.objects.filter(id__in=dishes_id)
    ]

    # find drinks in order
    drinks_id = [odrink.drink.id for odrink in order_drink]
    drinks = [
        DrinkSerializer(
            drink,
            context={'request': request}
        ).data for drink in Drink.objects.filter(id__in=drinks_id)
    ]

    # find complemnets in order
    complements_id = [oc.complement.id for oc in order_complement]
    complements = [
        ComplementSerializer(
            complement,
            context={'request': request}
        ).data for complement in Complement.objects.filter(id__in=complements_id)
    ]

    return Response(
        {
            "order": order_serializer.data,
            "dishes": dishes,
            "drinks": drinks,
            "complements": complements
        },
        status=status.HTTP_200_OK
    )
