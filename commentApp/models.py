from django.db import models
from profileApp.models import UserProfile
from postApp.models import Posts

# Create your models here.

class Comment(models.Model):
    comment = models.TextField(max_length=200,null=True)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='posted_comment')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='commented_post')
    likes = models.ManyToManyField(UserProfile,related_name='liked_comment')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.comment