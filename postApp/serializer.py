from rest_framework import serializers
from commentApp.serializer import CommentSerializer
from userApp.serializer import UserSerializer
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    posted_comment = CommentSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Posts
        fields = '__all__'
    