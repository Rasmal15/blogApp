from rest_framework import serializers
from .models import Comment
from replayApp.serializer import ReplaySerializer
from userApp.serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    replayed_comment = ReplaySerializer(many=True)
    class Meta:
        model = Comment
        fields = '__all__'
