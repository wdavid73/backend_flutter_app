from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from my_restaurant_app.validations import validate_user
from ..Model.ModelDrink import Drink
from ..Serializer.SerializerDrink import DrinkSerializer


class GetAndPost(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request: Request):
        if validate_user(request):
            drinks = Drink.objects.filter(state=1)()
            serializer = DrinkSerializer(drinks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            drink = request.data.copy()
            drink["restaurant_code"] = request.user.restaurant.code
            serializer = DrinkSerializer(data=drink)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
