from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..serializers.UserSerializer import UserSerializer
from ..serializers.RegisterSerializer import RegisterSerializer
from ..serializers.TokenSerializer import TokenSerializer

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        serializer_token = TokenSerializer(token, context={'request': request})
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": serializer_token.data
            },
            status=status.HTTP_201_CREATED
        )
