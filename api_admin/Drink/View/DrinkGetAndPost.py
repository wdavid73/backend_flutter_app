from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user
from ..Model.ModelDrink import Drink
from ..Serializer.SerializerDrink import DrinkSerializer


class GetAndPost(generics.GenericAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.filter(state=1)

    def get(self, request: Request):
        if validate_user(request):
            drinks = self.get_queryset()
            serializer = self.get_serializer(drinks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            drink = request.data.copy()
            drink["restaurant_code"] = request.user.restaurant.code
            serializer = self.get_serializer(data=drink)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
