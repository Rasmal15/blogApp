from django.shortcuts import render,redirect
from . models import *
from . forms import *
from userApp.models import UserProfile
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from commentApp.serializer import CommentSerializer
from commentApp.models import Comment
from replayApp.models import ReplayComment
from postApp.models import Posts
from postApp.serializer import PostsSerializer

# Create your views here.

@login_required(login_url='users/sign-in')
def profileDataFunction(request):
    user = UserProfile.objects.get(username = request.user)
    if request.POST:
        print(user)
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = user
            profile_data.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ProfileForm()
        return render(request,'profile/profile_form.html',{'form':form})
    
@login_required(login_url='users/sign-in')
def updateProfile(request):
    user = UserProfile.objects.get(username = request.user)
    profile = ProfileData.objects.get(user = user)
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = user
            profile_data.save()
            return redirect('home')
        else:   
            print(form.errors)
    else:
        form = ProfileForm(instance=profile)
        return render(request,'profile/profile_form.html',{'form':form})
    
@login_required(login_url='users/sign-in')
def createNewPost(request):
    user = UserProfile.objects.get(username = request.user)
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posted_data = form.save(commit=False)
            posted_data.user = user
            posted_data.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request,'profile/post_form.html',{'form' : form})

@login_required(login_url='users/sign-in')
def viewSinglePost(request,id):
    user = UserProfile.objects.get(username = request.user)
    single_post = Posts.objects.get(id = id)
    like_conut = single_post.likes.count()
    comments = Comment.objects.filter(post = single_post)
    liked_comments = user.liked_comment.all()
    replay_comments_dictionary = {}
    replay_comments_list = []
    for comment_id in comments:
        replay_comment = ReplayComment.objects.filter(comment = comment_id)
        replay_comments_dictionary[comment_id] = replay_comment
    # Loop through each item in the dictionary to fetch the replay comments
    for comment, replay_comments in replay_comments_dictionary.items():        
        # Check if there are any replay comments for the current comment
        if replay_comments.exists():
            for replay_comment in replay_comments:
                replay_comments_list.append(replay_comment)
    return render(request, 'profile/post.html', {'post' : single_post, 'form' : form,
                                                 'comments' : comments, 'liked_comments' : liked_comments,
                                                 'replay_comments' : replay_comments_list, 'count' : like_conut})

@login_required(login_url='users/sign-in')
def myPostsFunction(request):
    user = UserProfile.objects.get(username = request.user)
    posts= Posts.objects.filter(user = user)
    liked_posts = user.liked_post.all()
    like_count = {}
    for post in posts:
        like_count[post.id] = post.likes.count()
    return render(request, 'home/home.html',{'posts' : posts, 'like_count' : like_count,
                                             'liked_posts' : liked_posts, 'user' : user})

@login_required(login_url='users/sign-in')
def likePostFunction(request,id):
    user = UserProfile.objects.get(username = request.user)
    likable_post = Posts.objects.get(id = id)
    if user in likable_post.likes.all():
        liked = False
        likable_post.likes.remove(user)
    else:
        liked = True
        likable_post.likes.add(user)

    return JsonResponse({
            'liked' : liked,
            'like_count' : likable_post.likes.count()
        })

@login_required(login_url='users/sign-in')
def deletePostFunction(request,id):
    user = UserProfile.objects.get(username = request.user)
    deleted_post = Posts.objects.get(id = id)
    if deleted_post.user == user:
        if request.method == 'POST':
            data = data = json.loads(request.body.decode('utf-8'))
            data_status = data.get('deleted_post')
            if data_status == 'True':
                deleted_post.delete()
                response_data = {
                    'status' : 'success',
                    'post' : deleted_post,
                }
                return JsonResponse(response_data)
            else:
                response_data = {
                    'status' : 'false'
                }
                return JsonResponse(response_data)
        else:
            print('error')
    else:
        print('You can not delete this post')

@login_required(login_url='users/sign-in')
def commentOnPost(request,id):
    user = UserProfile.objects.get(username = request.user)
    commented_post = Posts.objects.get(id = id)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        comment_input = data.get('comment')
        comment = Comment(comment = comment_input, user = user, post = commented_post)
        comment.save()
        serializer = CommentSerializer(comment)
        # response_data = {
        #     'status' : True,
        #     'comment' : {
        #         'id' : comment.id,
        #         'comment' : comment.comment,
        #         'post' : id,
        #         'created_at' : comment.created_at,
        #         'count' : commented_post.posted_comment.count(),
        #         'user' : comment.user.user_profile.name if comment.user.user_profile else comment.user.username,
        #         'profile_picture' : comment.user.user_profile.profile_picture.url if comment.user.user_profile else None,
        #     }
        # }
        response_data = serializer.data
        print(response_data)
        return JsonResponse(response_data, safe=False)
    

@login_required(login_url='users/sign-in')
def likeCommentFunction(request,id):
    user = UserProfile.objects.get(username = request.user)
    likable_comment = Comment.objects.get(id = id)
    if user in likable_comment.likes.all():
        likable_comment.likes.remove(user)
        response_data = {
            'liked' :False,
            'comment' : likable_comment.id,
            'count' : likable_comment.likes.count()
        }
    else:
        likable_comment.likes.add(user)
        response_data = {
            'liked' :True,
            'comment' : likable_comment.id,
            'count' : likable_comment.likes.count()
        }
    return JsonResponse(response_data)

@login_required(login_url='users/sign-in')
def deleteCommentFunction(request, id):
    user = UserProfile.objects.get(username = request.user)
    comment = Comment.objects.get(id = id)
    commented_post = comment.post
    print(commented_post.id)
    if comment.user == user:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            delete_status = data.get('deleted_comment')
            if delete_status == 'True':
                deleted_comment = comment
                deleted_comment.delete()
                comment_count = commented_post.posted_comment.count()
                respone_data = {
                    'status' : 'deleted',
                    'messege' : 'comment deleted',
                    'comment' : {
                        'id' : id,
                        'count' : comment_count,
                        'post' : commented_post.id
                    }
                }
            else:
                respone_data = {
                    'status' : 'not_deleted',
                    'messege' : 'comment not deleted',
                    'comment' : {
                        'id' : id
                    }
                }
            return JsonResponse(respone_data)
    else:
        print('you can not delete this message')

@login_required(login_url='users/sign-in')
def ReplayCommentFunction(request,id):
    user = UserProfile.objects.get(username = request.user)
    comment = Comment.objects.get(id = id)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        replay = data.get('replay_comment')
        repaly_comment = ReplayComment(user = user, comment = comment, replay = replay)
        repaly_comment.save()
        response_data = {
            'status': 'success',
            'message': 'Replay added successfully',
            'replay': {
                'id' : repaly_comment.id,
                'replay': repaly_comment.replay,
                'user' : repaly_comment.user.user_profile.profile_picture.url if repaly_comment.user.user_profile.profile_picture else None,
                'username': repaly_comment.user.username,
                'comment':repaly_comment.comment.id,
                'created_at':repaly_comment.created_at
            }
        }
        return JsonResponse(response_data)

@login_required(login_url='users/sign-in')
def deleteReplayCommentFunction(request,id):
    user = UserProfile.objects.get(username = request.user)
    deleted_replay_comment = ReplayComment.objects.get(id = id)
    if deleted_replay_comment.user == user:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            confirmation = data.get('delete_replay')
            if confirmation == 'True':
                response_data = {
                    'status' : True,
                    'id' : id
                }
                deleted_replay_comment.delete()
                return JsonResponse(response_data)
            else:
                response_data = {
                    'status' : False,
                    'id' : id
                }
                return JsonResponse(response_data)
  
@login_required(login_url='users/sign-in')          
def userProfileFollow(request, id):
    user = UserProfile.objects.get(username = request.user)
    profile = ProfileData.objects.get(id = id)
    if user in profile.followers.all():
        profile.followers.remove(user)
        response_data = {
            'status' : 'unfollow',
            'profile' : id
        }
        return JsonResponse(response_data)
    else:
        profile.followers.add(user)
        response_data = {
            'status' : 'follow',
            'profile' : id
        }
        return JsonResponse(response_data)