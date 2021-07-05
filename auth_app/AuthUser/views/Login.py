from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView

class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        
        return Response(
            {
                "user" : {
                    "user" : user.username,
                    "email" : user.email,
                    "first_name" : user.first_name,
                    "last_name" : user.last_name,
                    "position": user.position.name,
                },
                "msg": "You are Logged",
                "status": status.HTTP_200_OK,
                "Token": token.key,
                "token_created": created,
            }
        )
        
