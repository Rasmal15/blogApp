from django.db import models
from userApp.models import *

# Create your models here.

class ProfileData(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture',null=True)
    name = models.CharField(max_length=50)
    user = models.OneToOneField(UserProfile,on_delete=models.SET_NULL,related_name='user_profile',null=True)
    followers = models.ManyToManyField(UserProfile,related_name='follower')
    
    


