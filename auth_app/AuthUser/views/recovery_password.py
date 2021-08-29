from django.contrib.auth.hashers import make_password , MD5PasswordHasher
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.models import CustomUser
from auth_app.AuthUser.serializers.RecoveryPasswordSerializer import  RecoveryPasswordSerializer



class RecoveryPasswordAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self , request):
        serializer = RecoveryPasswordSerializer(data=request.data,  context={'request': request})
        serializer.is_valid(raise_exception=True)
        if(serializer.data["new_password"] == serializer.data["confirm_new_password"]):
            user = CustomUser.objects.get(email=serializer.data["email"])
            user.password = make_password(serializer.data["new_password"])
            user.save()
            return Response("Password Updated" , status = status.HTTP_200_OK)
        return Response("Passwords do not match. Please try again",status = status.HTTP_400_BAD_REQUEST)