from rest_framework import serializers
from .models import UserProfile
from profileApp.serializers import ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    
