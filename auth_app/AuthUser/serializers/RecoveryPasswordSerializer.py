from rest_framework import serializers
from auth_app.models import CustomUser
class RecoveryPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()
    # class Meta:
    #     model = CustomUser
    #     fields  = ('email', "new_password" ,"confirm_new_password")