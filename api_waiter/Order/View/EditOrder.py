from django.http import Http404
from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_restaurant_app.validations import validate_user, user_validate_required

from ..Model.ModelOrder import Order
from ..Serializer.SerializerOrder import OrderSerializer


class EditOrder(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get_object(self, code: str):
        try:
            return Order.objects.get(code=code)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request: Request, code: str):
        if validate_user(request):
            order = self.get_object(code)
            serializer = self.get_serializer(
                order, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
@user_validate_required
def edit_order(request: Request, code: str):
    return Response({"data": "data"}, status=status.HTTP_200_OK)
