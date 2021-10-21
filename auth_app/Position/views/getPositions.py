

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.permissions import AllowAny


from ..models.PositionModel import Position
from ..serializers.PositionSerializer import PositionSerializer
from ...models import CustomUser

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET'])
@permission_classes([AllowAny])
def getPositions(request: Request):
    positions = Position.objects.filter(state=1)
    serializer = PositionSerializer(
        positions, many=True, context={'request': request})
    return Response({'positions': serializer.data}, status=status.HTTP_200_OK)
