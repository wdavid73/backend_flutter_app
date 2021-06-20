from django.contrib.auth import login
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class LoginAPI(generics.GenericAPIView):
    #permission_classes = (permissions.AllowAny,)
    #authentication_classes = [TokenAuthentication]
    #serializer_class = AuthTokenSerializer

    def post(self, request):
        if not request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            print(login(request, user))
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "user_position": user.position.name,
                    "msg": "You are Logged",
                    "status": status.HTTP_200_OK,
                    "Token": token.key,
                    "token_created": created,
                }
            )
        else:
            token, created = Token.objects.get_or_create(user=request.user)
            return Response(
                {
                    "user_position": request.user.position.name,
                    "msg": "already logged in ",
                    "status": status.HTTP_200_OK,
                    "Token": token,
                    "token_created": created,
                }
            )
