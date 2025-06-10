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
from django.http import JsonResponse

# Create your views here.

class ReplayOnCommentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(username = request.user)
        print (request.data)
        # print(request.data.get('comment_id'))
        # print(request.data)
        # comment_id = kwargs.get('id')
        # print(comment_id)
        replayed_comment = Comment.objects.get(id = kwargs.get('id'))
        replay = request.data.get('replay')
        uploaded_replay = ReplayComment(replay = replay, comment = replayed_comment, user = user)
        uploaded_replay.save()
        serialized_replay = ReplaySerializer(uploaded_replay)
        respone_data = {
            'status_code' : status.HTTP_201_CREATED,
            'replay' : serialized_replay.data
        }
        return JsonResponse(respone_data)
    
    def delete(self,request,*args,**kwargs):
        user = UserProfile.objects.get(username = request.user)
        replayTODelete = ReplayComment.objects.get(id = kwargs.get('id'))
        if user == replayTODelete.user:
            if request.data == 'True':
                replayTODelete.delete()
                response_data = {
                    'status' : 'success',
                }
                return JsonResponse(response_data)
            else:
                response_data = {
                    'status' : 'false'
                }
                return JsonResponse(response_data) 
        else:
            return JsonResponse({
                'message' : 'You do not have the permission to delete this comment'
            }) 
