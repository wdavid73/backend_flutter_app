from datetime import date
import random
from typing import Union, List, Dict
from django.db.models import QuerySet
from django.http.request import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from api_admin.Table.Model.ModelTable import Table
from api_waiter.Order.Order_Dish.Serializer.OrderDishSerializer import OrderDishSerializer
from api_waiter.Order.Order_Drinks.Serializer.OrderDrinkSerializer import OrderDrinkSerializer
from my_restaurant_app.validations import validate_user, type_user_valid
from my_restaurant_app.customPermissions import TokenPermission
from auth_app.models import CustomUser
from ..Order_User.Serializer.Order_UserSerializer import OrderUserSerializer
from ..Model.ModelOrder import Order, Order_User, Order_Dish, Order_Drinks, Order_Complement
from ..Serializer.SerializerOrder import OrderSerializer


class GetAndPost(APIView):
    permission_classes = [TokenPermission]

    def get(self, request: Request) -> Response:
        if validate_user(request):
            orders = Order.objects.filter(action=1)
            serializer = OrderSerializer(
                orders, many=True, context={'request': request})
            return Response({"order": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request) -> Response:
        if validate_user(request):
            if type_user_valid(request):
                new_order = request.data.copy()
                date_now = date.today()
                code = generate_code(
                    Order.objects.filter(action=1), dictLetter
                )
                new_order["code"] = code
                new_order["date"] = date_now
                dishesSelected = new_order["dishes_selected"]
                drinksSelected = new_order["drinks_selected"]

                # Remove Elements from dict
                del new_order["dishes_selected"]
                del new_order["drinks_selected"]

                serializer = OrderSerializer(
                    data=new_order, context={'request': request}
                )

                if serializer.is_valid():
                    serializer.save()

                    table_id = new_order["table_id"]
                    table = Table.objects.get(id=table_id)
                    table.state = 0
                    table.save()

                    serializer_order_dish = save_order_dishes(
                        new_order["code"], dishesSelected, request)

                    serializer_order_drink = save_order_drinks(
                        new_order["code"], drinksSelected, request)

                    serializer_order_user = save_order_user(
                        new_order["code"], request.user, request
                    )

                    return Response(
                        {
                            "data": serializer.data,
                            "order_user": serializer_order_user.data,
                            "dishesSelected": serializer_order_dish,
                            "drinksSelected": serializer_order_drink,
                        },
                        status=status.HTTP_201_CREATED
                    )
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)


def save_order_user(code: str, user: CustomUser, request: Request) -> OrderUserSerializer:
    order = Order.objects.get(code=code)
    order_user = Order_User.objects.create(user=user, order=order)
    serializer = OrderUserSerializer(order_user, context={'request': request})
    return serializer


def save_order_dishes(code: str, dishes, request: Request):
    items = []
    for dish in dishes:
        data = {}
        data["dish_id"] = dish["id"]
        data["order_code"] = code
        serializer = OrderDishSerializer(
            data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            items.append(serializer.data)
        else:
            return serializer.errors
    return items


def save_order_drinks(code: str, drinks, request: Request):
    items = []
    for drink in drinks:
        data = {}
        data["drink_id"] = drink["id"]
        data["order_code"] = code
        serializer = OrderDrinkSerializer(
            data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            items.append(serializer.data)
        else:
            return serializer.errors
    return items


def generate_code(row: Union[QuerySet, List[Order]], dictLetter: Dict) -> str:
    cant = row.count() + 1
    number = random.randint(100, 999)
    txt = ""
    while len(txt) < 3:
        n = random.randint(0, len(dictLetter)-1)
        txt += str(dictLetter[n])
    return str(cant) + str(number) + txt + str(cant*2)


dictLetter = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
    26: "Ñ",
}
