from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Model.ModelComplement import Complement
from ..Serializer.SerializerComplement import ComplementSerializer

class GetAndPost(APIView):

    def get(self, request: Request):
        Complements = Complement.objects.filter(state=1)
        serializer = ComplementSerializer(
            Complements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = ComplementSerializer(
            data=request.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

