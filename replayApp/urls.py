from django.urls import path
from . views import ReplayOnCommentView

urlpatterns = [
    path('replay/<int:id>',ReplayOnCommentView.as_view(), name='replay')
]
