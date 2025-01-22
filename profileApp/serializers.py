from rest_framework import serializers
from . models import Posts,Comment,ProfileData
from userApp.models import UserProfile

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProfileData
        fields = '__all__' 
           
class CommentSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField() 
    post = PostsSerializer()
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        
    def get_profile(self, obj):
        return ProfileSerializer(obj.user.user_profile).data