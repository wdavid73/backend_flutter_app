from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import validate_user, validate_restaurant_code
from auth_app.Position.models.PositionModel import Position
from auth_app.CustomUser import CustomUser
from auth_app.AuthUser.serializers.UserSerializer import UserSerializer


@api_view(["GET"])
def list_chefs(request: Request):
    if validate_user(request):
        positions_id = [
            position.id for position in Position.objects.filter(state=1, name="chef")]
        serializer = UserSerializer(
            CustomUser.objects.filter(
                state=1,
                position__in=positions_id
            ), many=True, context={'request': request}
        )
        return Response({"chefs": serializer.data, "status": status.HTTP_200_OK})
    return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})


@api_view(["GET"])
def list_waiters(request: Request):
    if validate_user(request):
        positions_id = [
            position.id for position in Position.objects.filter(state=1, name="waiter")]
        serializer = UserSerializer(
            CustomUser.objects.filter(
                state=1,
                position__in=positions_id
            ), many=True, context={'request': request}
        )
        return Response({"chefs": serializer.data, "status": status.HTTP_200_OK})
    return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})
