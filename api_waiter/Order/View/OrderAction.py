from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import user_validate_required

from ..Model.ModelOrder import Order
from ..Serializer.SerializerOrder import OrderSerializer

types_actions = {1: "delivery", 2: "cancelled", 3: "pending"}


@api_view(["POST"])
@user_validate_required
def order_action(request: Request, code: str, action: int):
    if action in types_actions:
        order = get_object_or_404(Order, code=code)
        order.action = action
        order.save()
        serializer = OrderSerializer(order, context={'request': request})
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"data": "action don't exist'"}, status=status.HTTP_400_BAD_REQUEST)
