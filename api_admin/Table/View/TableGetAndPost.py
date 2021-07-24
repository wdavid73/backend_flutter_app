from typing import Union, List, Dict
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user
from ..Model.ModelTable import Table
from ..Serializer.SerializerTable import TableSerializer
from my_restaurant_app.customPermissions import TokenPermission

class GetAndPost(APIView):
    permission_classes = [TokenPermission]

    def get(self, request: Request):
        if validate_user(request):
            tables = Table.objects.filter(state=1)
            serializer = TableSerializer(tables, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})

    def post(self, request: Request):
        if validate_user(request):
            table = request.data.copy()
            table["restaurant_code"] = request.user.restaurant.code
            if table["ref"] == "":
                table["ref"] = "table #" + \
                    str(numb_row(Table.objects.filter(state=1)))
            serializer = TableSerializer(
                data=table, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid", "status": status.HTTP_401_UNAUTHORIZED})


def numb_row(row: Union[QuerySet, List[Table]]) -> int:
    return row.count() + 1
