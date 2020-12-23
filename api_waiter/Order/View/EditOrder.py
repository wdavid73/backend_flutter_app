from django.http import Http404
from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import validate_user, user_validate_required

from ..Model.ModelOrder import Order, Order_Dish
from ..Serializer.SerializerOrder import OrderSerializer
from api_admin.Dish.models.DishModel import Dish
from api_admin.Dish.serializers.DishSerializer import DishSerializer


class EditOrder(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get_object(self, code: str):
        try:
            return Order.objects.get(code=code)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request: Request, code: str):
        if validate_user(request):
            order = self.get_object(code)
            serializer = self.get_serializer(
                order, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@user_validate_required
def edit_order(request: Request, code: str):
    order = Order.objects.get(code=code)
    # update order
    data = request.data.copy()
    data["code"] = order.code
    data["date"] = order.date
    serializer = OrderSerializer(
        order, data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"order": serializer.data}, status=status.HTTP_200_OK)
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@user_validate_required
def edit_order_items(request: Request, code: str):
    pass
