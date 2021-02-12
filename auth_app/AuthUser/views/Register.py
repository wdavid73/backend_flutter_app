from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from ..serializers.UserSerializer import UserSerializer
from ..serializers.RegisterSerializer import RegisterSerializer
from ..serializers.TokenSerializer import TokenSerializer
from ...Restaurant.models.RestaurantModel import Restaurant
from my_restaurant_app.validations import validate_restaurant_code


class RegisterAPI(APIView):
    # serializer_class = RegisterSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if validate_restaurant_code(request):
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = Token.objects.create(user=user)
            serializer_token = TokenSerializer(
                token, context={'request': request})
            return Response(
                {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": serializer_token.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response({"data": "the restaurant does not exist"}, status=status.HTTP_404_NOT_FOUND)
