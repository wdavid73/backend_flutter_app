from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import user_validate_required
from my_restaurant_app.customPermissions import TokenPermission
from ..Model.ModelTable import Table
from ..Serializer.SerializerTable import TableSerializer


@api_view(["GET"])
@user_validate_required
@permission_classes([TokenPermission])
def list_tables_by_restaurant(request: Request):
    restaurant_code = request.user.restaurant.code
    serializer = TableSerializer(
        Table.objects.filter(restaurant=restaurant_code),
        context={'request': request},
        many=True
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
