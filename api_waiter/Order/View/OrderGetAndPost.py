import random
from typing import Union, List, Dict
from django.db.models import QuerySet
from django.http.request import QueryDict
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user

from auth_app.CustomUser import CustomUser
from ..Order_User.Serializer.Order_UserSerializer import OrderUserSerializer
from ..Model.ModelOrder import Order, Order_User, Order_Dish
from ..Serializer.SerializerOrder import OrderSerializer


class GetAndPost(APIView):

    def get(self, request: Request):
        if validate_user(request):
            orders = Order.objects.filter(action=1)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            new_order = request.data.copy()
            new_order["code"] = generate_code(
                Order.objects.filter(action=1), dictLetter
            )
            serializer = OrderSerializer(
                data=new_order, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                serializer_order_user = save_order_user(
                    new_order["code"], request.user, request
                )
                return Response(
                    {
                        "data": serializer.data,
                        "order_user": serializer_order_user.data
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)


def save_order_user(code: str, user: CustomUser, request: Request):
    order = Order.objects.get(code=code)
    order_user = Order_User.objects.create(user=user, order=order)
    serializer = OrderUserSerializer(order_user, context={'request': request})
    return serializer


def generate_code(row: Union[QuerySet, List[Order]], dictLetter: Dict):
    cant = row.count() + 1
    number = random.randint(100, 999)
    txt = ""
    while len(txt) < 3:
        n = random.randint(0, len(dictLetter))
        txt += dictLetter[n]
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
}
