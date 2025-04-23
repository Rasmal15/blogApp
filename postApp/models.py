from django.db import models
from userApp.models import UserProfile

# Create your models here.

class Posts(models.Model):
    post = models.ImageField(upload_to='post',null=True)
    description = models.TextField(max_length=200,null=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='posts')
    likes = models.ManyToManyField(UserProfile,related_name='liked_post')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.description