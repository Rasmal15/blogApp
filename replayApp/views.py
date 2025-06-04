from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
from .models import ReplayComment
from . serializer import ReplaySerializer
from userApp.models import UserProfile
from commentApp.models import Comment

# Create your views here.

class ReplayOnCommentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(username = request.user)
        print(request.data.get('comment_id'))
        print(request.data)
        comment_id = request.data.get('comment_id')
        replayed_comment = Comment.objects.get(id = comment_id)
        replay = request.data.get('replay')['replay']
        uploaded_replay = ReplayComment(replay = replay, comment = replayed_comment, user = user)
        uploaded_replay.save()
        serialized_replay = ReplaySerializer(uploaded_replay)
        respone_data = {
            'status_code' : status.HTTP_201_CREATED,
            'replay' : serialized_replay.data
        }
        return Response(respone_data)