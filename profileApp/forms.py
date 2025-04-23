from django import forms
from . models import *
from postApp.models import Posts

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = ['profile_picture','name']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            "post",
            "description"
        ]
        

        