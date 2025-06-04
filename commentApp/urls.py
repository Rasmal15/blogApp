from django.urls import path
from .views import CommentOnPostView

urlpatterns = [
    path('comment/<int:id>',CommentOnPostView.as_view(),name='comment'),
    path('comment/like',CommentOnPostView.as_view(), name='like_comment')
]
