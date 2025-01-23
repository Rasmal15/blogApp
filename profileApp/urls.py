from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profileDataFunction, name='profile'),
    path('post_form/', views.createNewPost, name='post_form'),
    path('single_post/<int:id>', views.viewSinglePost, name='single_post'),
    path('comment/<int:id>', views.commentOnPost, name='comment'),
    path('like_post/<int:id>', views.likePostFunction, name='like_post'),
    path('like_comment/<int:id>', views.likeCommentFunction, name='like_comment'),
    path('replay_comment/<int:id>', views.ReplayCommentFunction, name="replay_comment"),
    path('edit_profile/', views.updateProfile, name='edit_profile'),
    path('delete_comment/<int:id>', views.deleteCommentFunction, name='delete_comment'),
    path('my_posts', views.myPostsFunction, name='my_posts'),
    path('delete_post/<int:id>', views.deletePostFunction, name='delete_post'),
    path('delete_replay/<int:id>', views.deleteReplayCommentFunction, name='delete_replay'),
    path('follow/<int:id>', views.userProfileFollow, name='follow')
]
