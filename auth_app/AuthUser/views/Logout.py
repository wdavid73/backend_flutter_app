from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return Response({"data": "You are Logout", "status": status.HTTP_200_OK})
