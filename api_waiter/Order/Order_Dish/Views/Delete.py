from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import user_validate_required
from ...Model.ModelOrder import Order_Dish


@api_view(["POST"])
@user_validate_required
def delete_dish(request: Request, id: int):
    object = get_object_or_404(Order_Dish, id=id)
    object.state = 0
    object.save()
    return Response({"data": "dish in order deleted"}, status=status.HTTP_200_OK)
