from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import user_validate_required
from my_restaurant_app.customPermissions import TokenPermission
from ..Model.ModelOrder import Order
from ..Serializer.SerializerOrder import OrderSerializer

types_actions = {
    1: "pending",
    2: "cancelled",
    3: "delivery",
    4: "padded"
}


@api_view(["POST"])
@user_validate_required
@permission_classes([TokenPermission])
def order_action(request: Request, code: str, action: int):
    if action in types_actions:
        order = get_object_or_404(Order, code=code)
        order.action = action
        order.save()
        serializer = OrderSerializer(order, context={'request': request})
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"data": "action don't exist'"}, status=status.HTTP_400_BAD_REQUEST)
