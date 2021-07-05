from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user, user_validate_required
from ...Model.ModelOrder import Order_Complement


@api_view(["POST"])
@user_validate_required
@permission_classes([IsAuthenticated])
def delete_complement(request: Request, id: int):
    object = get_object_or_404(Order_Complement, id=id)
    object.state = 0
    object.save()
    return Response({"data": "complement in order deleted"}, status=status.HTTP_200_OK)
