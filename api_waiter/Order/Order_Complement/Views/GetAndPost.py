from rest_framework import status, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from my_restaurant_app.validations import validate_user
from ...Model.ModelOrder import Order_Complement
from ..Serializer.OrderComplementSerializer import OrderComplementSerializer
from ...View.total_order import calculate_total_order
from api_admin.Complement.Model.ModelComplement import Complement


class GetAndPost(APIView):
    
    def get(self, request: Request):
        if validate_user(request):
            order_dish = Order_Complement.objects.filter(state=1)
            serializer = OrderComplementSerializer(
                order_dish, context={'request': request}, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request: Request):
        if validate_user(request):
            serializer = OrderComplementSerializer(
                data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                new_data = request.data.copy()
                """ add price to total of order """
                calculate_total_order(new_data["order_code"] , new_data["complement_id"] , Complement)
                
                return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "user invalid"}, status=status.HTTP_401_UNAUTHORIZED)
