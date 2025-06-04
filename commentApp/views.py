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
import json
from rest_framework.request import Request as DRFRequest
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from django.http import JsonResponse

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
    
    def commentLikeFunction(self, request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            comment_id = data.get('comment')
            print(comment_id)
            user = UserProfile.objects.get(username = request.user)
            comment = Comment.objects.get(id = comment_id)
            if user in comment.likes.all():
                comment.likes.remove(user)
                response_data = {
                    'liked' : False,
                    'like_count' : comment.likes.count()
                }
            else:
                comment.likes.add(user)
                response_data = {
                    'liked' : True,
                    'like_count' : comment.likes.count()
                }
            return JsonResponse(response_data)
            
    def delete(self, request, *args, **kwargs) :
        user = UserProfile.objects.get(username = request.user)
        print(request)
        print(kwargs.get('id'))
        
        
    def dispatch(self, request, *args, **kwargs):
        if request.path_info == '/comment/comment/like' and request.method == 'POST':
            drf_request = DRFRequest(request)
            for auth in self.authentication_classes:
                auth_instance = auth()
                user, _ = auth_instance.authenticate(drf_request)
                if user:
                    drf_request.user = user
                    break
            else:
                raise NotAuthenticated()

            # Check permissions
            self.check_permissions(drf_request)
            

            return self.commentLikeFunction(drf_request)

        return super().dispatch(request, *args, **kwargs)