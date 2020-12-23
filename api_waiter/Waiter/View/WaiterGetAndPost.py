from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user

from auth_app.CustomUser import CustomUser
from auth_app.AuthUser.serializers.UserSerializer import UserSerializer
from auth_app.AuthUser.serializers.RegisterSerializer import RegisterSerializer
from auth_app.Position.models.PositionModel import Position
from rest_framework.authtoken.models import Token
from auth_app.AuthUser.serializers.TokenSerializer import TokenSerializer


class GetAndPostFromAdmin(APIView):

    def get(self, request: Request):
        if validate_user(request):
            positions_id = [
                position.id for position in Position.objects.filter(state=1, name="waiter")]
            serializer = UserSerializer(
                CustomUser.objects.filter(
                    state=1,
                    position__in=positions_id
                ), many=True, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})

    def post(self, request: Request):
        if validate_user(request):
            position_waiter = Position.objects.get(state=1, name="waiter")
            new_waiter = request.data.copy()
            new_waiter["position_id"] = position_waiter.id
            new_waiter["restaurant_code"] = request.user.restaurant.code
            serializer = RegisterSerializer(data=new_waiter)
            if serializer.is_valid():
                user = serializer.save()
                token = Token.objects.create(user=user)
                serializer_token = TokenSerializer(
                    token, context={'request': request})
                return Response(
                    {
                        "user_waiter": UserSerializer(user, context={'request': request}).data,
                        "token": serializer_token.data,
                    },
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
