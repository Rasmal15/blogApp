from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    # path('',views.homeFunction,name='home'),
    path('view_profile', views.viewProfileFunction,name='view_profile'),
    path('', HomeView.as_view(), name = 'home')
]
