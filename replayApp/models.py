from django.db import models
from commentApp.models import Comment
from profileApp.models import UserProfile

# Create your models here.

class ReplayComment(models.Model):
    replay = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='replayed_comment')
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name='replayed_user', null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)