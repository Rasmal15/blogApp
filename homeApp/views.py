from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from profileApp.models import Posts,ProfileData,Comment,ReplayComment
from userApp.models import UserProfile
from django.http import JsonResponse
from django.utils import timezone
from profileApp.serializers import PostsSerializer

# Create your views here.

@login_required(login_url='users/sign-in')
def homeFunction(request):
    user = UserProfile.objects.get(username = request.user)
    profiles = ProfileData.objects.exclude(user = user)
    posts = Posts.objects.exclude(user = user.id)
    all_comments = Comment.objects.all()
    serializer = PostsSerializer(posts, many = True)
    print(serializer.data)
    liked_posts = user.liked_post.all()
    like_count = {}
    followers = user.follower.all()
    like_count = {}
    comment_count = {}
    replay_count = {}
    comments = {}
    replays = {}
    comment_like_count = {}
    liked_comments = user.liked_comment.all()
    print(followers)
    for post in posts:
        like_count[post.id] = post.likes.count()
        comment_count[post.id] = post.posted_comment.count()
        comments[post.id] = Comment.objects.filter(post = post.id)
        for comment in comments[post.id]:
                replays[comment.id] = comment.replayed_comment.all()
                replay_count[comment.id] = comment.replayed_comment.count()
                comment_like_count[comment.id] = comment.likes.count()
    return render(request,'home/home.html',{'user':user,'posts':posts,
                                            'liked_posts':liked_posts, 'like_count' : like_count,
                                            'profiles' : profiles, 'follower' : followers, 'comments' : comments,
                                            'comment_count' : comment_count, 'replays' : replays,
                                            'liked_comments' : liked_comments, 'replays' : replays,
                                            'comment_like_count' : comment_like_count, 'replay_count' : replay_count})
    
@login_required(login_url='users/sign-in')
def viewProfileFunction(request):
    user = UserProfile.objects.get(username = request.user)
    now = timezone.localtime()
    if hasattr(user, 'user_profile'):
        profile = ProfileData.objects.get(user = user.id)
        followers = profile.followers.all()
        follower_count = followers.count()
        posts = Posts.objects.filter(user = user.id)
        post_count = posts.count()
        following = user.follower.all()
        following_count = following.count()
        like_count = {}
        comment_count = {}
        replay_count = {}
        comments = {}
        replays = {}
        comment_like_count = {}
        liked_posts = user.liked_post.all()
        liked_comments = user.liked_comment.all()
        for post in posts:
            like_count[post.id] = post.likes.count()
            comment_count[post.id] = post.posted_comment.count()
            comments[post.id] = Comment.objects.filter(post = post.id)
            for comment in comments[post.id]:
                replays[comment.id] = comment.replayed_comment.all()
                replay_count[comment.id] = comment.replayed_comment.count()
                comment_like_count[comment.id] = comment.likes.count()
        return render(request, 'home/user_profile.html',{'user' : user, 'profile' : profile, 'posts' : posts,
                                                         'post_count' : post_count, 'following_count' : following_count,
                                                         'follower_count' : follower_count, 'like_count' : like_count,
                                                         'comments' : comments, 'comment_count' : comment_count,
                                                         'replays' : replays, 'replay_count' : replay_count,
                                                         'comment_like_count' : comment_like_count, 'liked_posts' : liked_posts,
                                                         'now' : now, 'liked_comments' : liked_comments})
    else:
        return redirect('profile')