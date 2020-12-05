from django.http import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..Model.ModelOrder import Order, Order_Complement, Order_Dish, Order_Drinks, Order_User
from ..Serializer.SerializerOrder import OrderSerializer

from api_admin.Dish.models.DishModel import Dish
from api_admin.Dish.serializers.DishSerializer import DishSerializer
from ..Order_Dish.Serializer.OrderDishSerializer import OrderDishSerializer
from api_admin.Dish.serializers.DishSerializer import DishSerializer
from api_admin.Dish.models.DishModel import Dish


from my_restaurant_app.validations import user_validate_required


@api_view(["GET"])
@user_validate_required
def find_order(request: Request, code: str):
    order = Order.objects.exclude(active=3).get(code=code)
    order_dish = Order_Dish.objects.filter(order=order)
    dishes_id = [od.dish.id for od in order_dish]
    order_serializer = OrderSerializer(order, context={'request': request})
    dishes = [
        DishSerializer(
            dish,
            context={'request': request}
        ).data for dish in Dish.objects.filter(id__in=dishes_id)
    ]

    return Response(
        {
            "order": order_serializer.data,
            "dishes": dishes
        },
        status=status.HTTP_200_OK
    )
