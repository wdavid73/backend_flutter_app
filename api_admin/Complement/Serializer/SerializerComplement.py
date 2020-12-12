from rest_framework import serializers
from ..Model.ModelComplement import Complement


class ComplementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complement
        fields = ['id', 'name', 'price', 'quantity', 'unit']
