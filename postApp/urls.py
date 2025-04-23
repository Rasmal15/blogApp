from django.urls import path
from .views import PostView

urlpatterns = [
    path('post',PostView.as_view(),name='post'),
    path('post/like',PostView.as_view(), name='like_post')
]
