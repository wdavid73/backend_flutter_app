from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from ..serializers.UserSerializer import UserSerializer
from ..serializers.RegisterSerializer import RegisterSerializer
from ..serializers.TokenSerializer import TokenSerializer
from my_restaurant_app.validations import validate_restaurant_code

from rest_framework import generics
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if validate_restaurant_code(request):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = Token.objects.create(user=user)
            serializer_token = TokenSerializer(
                token, context={'request': request})
            return Response(
                {
                    # "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "user": UserSerializer(user, context={'request': request}).data,
                    "token": serializer_token.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response({"data": "the restaurant does not exist"}, status=status.HTTP_404_NOT_FOUND)
