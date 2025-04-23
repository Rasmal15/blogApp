from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from userApp.models import UserProfile
from .serializer import PostsSerializer
import json
from .models import Posts
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.request import Request as DRFRequest
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from django.http import JsonResponse

# Create your views here.

class PostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostsSerializer
    parser_classes =[FormParser,MultiPartParser,JSONParser]
    
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(username = request.user)
        posted_image = request.data.get('post')
        description = request.data.get('description')
        post = Posts(post = posted_image, description=description, user=user)
        post.save()
        post_serializer = PostsSerializer(post)
        
        status_code = status.HTTP_201_CREATED
        response_data = {
            'post' : post_serializer.data,
            'status' : status_code
        }
        return Response(response_data)
        
    def likePostFunction(self,request):
        print(request)
        if request.method == 'POST':
            print(request.user)
            data = json.loads(request.body.decode('utf-8'))
            post_id = data.get('post_id')
            print(post_id)
            user = UserProfile.objects.get(username = request.user)
            liked_post = Posts.objects.get(id = post_id)
            if user in liked_post.likes.all():
                liked_post.likes.remove(user)
                response_data = {
                    'liked' : False,
                    'like_count' : liked_post.likes.count()
                }
            else:
                liked_post.likes.add(user)
                response_data = {
                    'liked' : True,
                    'like_count' : liked_post.likes.count()
                }
            return JsonResponse(response_data)
            
    
    def dispatch(self, request, *args, **kwargs):
        if request.path_info == '/post/post/like' and request.method == 'POST':
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
            

            return self.likePostFunction(drf_request)

        return super().dispatch(request, *args, **kwargs)
    
