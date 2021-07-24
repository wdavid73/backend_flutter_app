from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user, user_validate_required
from my_restaurant_app.customPermissions import TokenPermission
from ..Model.ModelOrder import Order, Order_Dish
from ..Serializer.SerializerOrder import OrderSerializer
from api_admin.Dish.models.DishModel import Dish
from api_admin.Dish.serializers.DishSerializer import DishSerializer


@api_view(["POST"])
@user_validate_required
@permission_classes([TokenPermission])
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
@permission_classes([TokenPermission])
def edit_order_dish(request: Request, code: str, list_dish_id: list):
    print(code)
    print(list_dish_id)
    pass


@api_view(["POST"])
@user_validate_required
@permission_classes([TokenPermission])
def edit_order_complement(request: Request, code: str, list_comple_id: list):
    print(code)
    print(list_comple_id)
    pass


@api_view(["POST"])
@user_validate_required
@permission_classes([TokenPermission])
def edit_order_drink(request: Request, code: str, list_drink_id: list):
    print(code)
    print(list_drink_id)
    pass


class EditOrder(APIView):
    permission_classes = [TokenPermission]

    def get_object(self, code: str):
        try:
            return Order.objects.get(code=code)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request: Request, code: str):
        if validate_user(request):
            order = self.get_object(code)
            serializer = OrderSerializer(
                order, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
