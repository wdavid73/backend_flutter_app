from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from my_restaurant_app.validations import user_validate_required


@api_view(["GET"])
@user_validate_required
def api_chef(request):
    if request.user.is_authenticated:
        return Response({"msg":"api chef , user is authenticated "} , status=status.HTTP_200_OK)
    else:
        return Response({"msg":"api chef , user is not authenticated"} , status=status.HTTP_401_UNAUTHORIZED)
