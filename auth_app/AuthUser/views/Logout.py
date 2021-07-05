from django.contrib.auth import logout
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({"data": "You are Logout", "status": status.HTTP_200_OK})
