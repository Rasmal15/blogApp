from rest_framework import serializers
from . models import ProfileData
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileData
        fields = '__all__' 
           