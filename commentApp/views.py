from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from userApp.models import UserProfile
from postApp.models import Posts
from .models import Comment
from .serializer import CommentSerializer
from rest_framework import status

# Create your views here.

class CommentOnPostView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(username = request.user)
        id = kwargs.get('id')
        commented_post = Posts.objects.get(id = id)
        comment = request.data.get('comment')
        print(id,commented_post,comment)
        posted_comment = Comment(user = user, post = commented_post, comment = comment)
        posted_comment.save()
        comment_serializer = CommentSerializer(posted_comment)
        status_code = status.HTTP_201_CREATED
        response_data = {
            'comment' : comment_serializer.data,
            'status' : status_code
        }
        return Response(response_data)
    
    def delete(self, request, *args, **kwargs) :
        user = UserProfile.objects.get(username = request.user)
        print(request)
        print(kwargs.get('id'))