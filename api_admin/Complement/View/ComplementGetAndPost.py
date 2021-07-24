from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..Model.ModelComplement import Complement
from ..Serializer.SerializerComplement import ComplementSerializer
from my_restaurant_app.validations import validate_user
from my_restaurant_app.customPermissions import TokenPermission



class GetAndPost(APIView):
    permission_classes = [TokenPermission]
    

    def get(self, request: Request):
        if validate_user(request):
            complements = Complement.objects.filter(state=1)
            serializer = ComplementSerializer(
                complements, context={'request': request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            serializer = ComplementSerializer(
                data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
