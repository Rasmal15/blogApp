from django.urls import path
from . views import ReplayOnCommentView

urlpatterns = [
    path('replay',ReplayOnCommentView.as_view(), name='replay')
]
