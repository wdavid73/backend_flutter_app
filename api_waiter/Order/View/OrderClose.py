from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import user_validate_required

from ..Model.ModelOrder import Order
from ..Serializer.SerializerOrder import OrderSerializer


@api_view(["POST"])
@user_validate_required
@permission_classes([IsAuthenticated])
def order_close(request: Request, code: str):
    order = get_object_or_404(Order, code=code)
    order.state = 0
    order.save()
    serializer = OrderSerializer(order, context={'request': request})
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)
