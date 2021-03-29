from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user, validate_restaurant_code
from ..models.DishModel import Dish
from ..serializers.DishSerializer import DishSerializer


class GetAndPost(APIView):
    def get(self, request: Request):
        if validate_user(request):
            restaurant_code = request.user.restaurant.code
            dish = Dish.objects.filter(state=1, restaurant_id = restaurant_code).order_by("id")
            serializer = DishSerializer(
                dish, many=True, context={'request': request})
            return Response({"dish": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            if validate_restaurant_code(request):
                dish = request.data.copy()
                dish["restaurant_code"] = request.user.restaurant.code
                serializer = DishSerializer(
                    data=dish, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({"dish": serializer.data}, status=status.HTTP_201_CREATED)
                return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"errors": "invalid restaurant code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"errors": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
