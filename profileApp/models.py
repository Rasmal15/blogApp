from django.db import models
from userApp.models import *

# Create your models here.

class ProfileData(models.Model):
    profile_picture = models.ImageField(upload_to='profile_picture',null=True)
    name = models.CharField(max_length=50)
    user = models.OneToOneField(UserProfile,on_delete=models.SET_NULL,related_name='user_profile',null=True)
    followers = models.ManyToManyField(UserProfile,related_name='follower')
    
class Posts(models.Model):
    post = models.ImageField(upload_to='post',null=True)
    description = models.TextField(max_length=200,null=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='posts')
    likes = models.ManyToManyField(UserProfile,related_name='liked_post')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.description
    
class Comment(models.Model):
    comment = models.TextField(max_length=200,null=True)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='posted_comment')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='commented_post')
    likes = models.ManyToManyField(UserProfile,related_name='liked_comment')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.comment

class ReplayComment(models.Model):
    replay = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='replayed_comment')
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name='replayed_user', null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)