from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from ..Model.ModelComplement import Complement
from ..Serializer.SerializerComplement import ComplementSerializer
from my_restaurant_app.validations import validate_user


class GetAndPost(generics.GenericAPIView):
    serializer_class = ComplementSerializer
    queryset = Complement.objects.filter(state=1)

    def get(self, request: Request):
        if validate_user(request):
            complements = self.get_queryset()
            serializer = self.get_serializer(
                complements, context={'request': request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            serializer = self.get_serializer(
                data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
