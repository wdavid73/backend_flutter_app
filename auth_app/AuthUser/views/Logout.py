from django.contrib.auth import logout
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class Logout(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

    """ def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({"data": "You are Logout", "status": status.HTTP_200_OK}) """

    def post(self, request):
        try:
            token = Token.objects.get(key=request.data)
            token.delete()
            return Response({"data": "You are Logout"}, status= status.HTTP_200_OK)
        except Token.DoesNotExist as e:
            return Response({"error" : str(e)} , status=status.HTTP_400_BAD_REQUEST)

