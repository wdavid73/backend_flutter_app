import random
from typing import Union, List, Dict
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


from auth_app.models import CustomUser
from ..models.RestaurantModel import Restaurant
from ..serializers.RestaurantSerializer import RestaurantSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def post(request: Request):
    code = generate_code(Restaurant.objects.filter(state=1), dictLetter)
    new_data = request.data.copy()
    new_data['code'] = code
    serializer = RestaurantSerializer(
        data=new_data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCodeByUserId(APIView):
    def get(self, request: Request, id: int):
        user = CustomUser.objects.get(id=id)
        return Response({"code": user.restaurant.code}, status=status.HTTP_200_OK)


def generate_code(row: Union[QuerySet, List[Restaurant]], dictLetter: Dict):
    cant = row.count() + 1
    number = random.randint(100, 999)
    txt = ""
    while len(txt) < 3:
        n = random.randint(0, len(dictLetter))
        txt += dictLetter[n]
    return str(cant) + txt + str(number)


dictLetter = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
}
