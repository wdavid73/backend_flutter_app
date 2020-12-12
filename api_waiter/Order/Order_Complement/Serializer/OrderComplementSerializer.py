from rest_framework import serializers
from ...Model.ModelOrder import Order_Complement

from api_admin.Complement.Serializer.SerializerComplement import ComplementSerializer
from api_admin.Complement.Model.ModelComplement import Complement

from ...Model.ModelOrder import Order
from ...Serializer.SerializerOrder import OrderSerializer


class OrderComplementSerializer(serializers.ModelSerializer):

    complement = ComplementSerializer(read_only=True)
    complement_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Complement.objects.filter(state=1),
        source='complement'
    )

    order = OrderSerializer(read_only=True)
    order_code = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Order.objects.filter(action=1),
        source='order'
    )

    class Meta:
        model = Order_Complement
        fields = [
            'id',
            'complement', 'complement_id',
            'order', 'order_code'
        ]
