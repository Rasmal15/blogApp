from django import forms
from . models import *

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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        