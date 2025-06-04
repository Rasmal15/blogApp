from rest_framework import serializers
from . models import ReplayComment
from userApp.serializer import UserSerializer

class ReplaySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ReplayComment
        fields = '__all__'