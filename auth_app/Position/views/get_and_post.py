from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , AllowAny


from ..models.PositionModel import Position
from ..serializers.PositionSerializer import PositionSerializer
from ...models import CustomUser
from my_restaurant_app.customPermissions import TokenPermission

class GetAndPost(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request: Request):
        positions = Position.objects.filter(state=1)
        serializer = PositionSerializer(
            positions, many=True, context={'request': request})
        return Response({'positions': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = PositionSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetByUser(APIView):
    permission_classes = [TokenPermission]
    
    
    def get(self, request: Request, id: int):
        user = CustomUser.objects.get(id=id, state=1)
        serializer = PositionSerializer(
            user.position, context={"request": request})
        return Response({"id": user.position.id, "name": user.position.name})


class GetByName(APIView):
    permission_classes = [TokenPermission]
    
    
    def get(self, request: Request, name: str):
        position = Position.objects.get(name=name)
        serializer = PositionSerializer(position, context={"request": request})
        return Response({"position": serializer.data}, status=status.HTTP_200_OK)
