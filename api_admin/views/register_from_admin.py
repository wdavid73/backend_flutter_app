from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import validate_user
from api_waiter.Waiter.View.WaiterGetAndPost import GetAndPostFromAdmin


@api_view(["POST"])
def register_chef_from_admin(request: Request):
    return Response({"chef": "chef", "status": status.HTTP_201_CREATED})
