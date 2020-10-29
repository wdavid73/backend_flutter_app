from rest_framework import serializers
from ..models.PositionModel import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']
