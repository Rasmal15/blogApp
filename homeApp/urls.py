from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeFunction,name='home'),
    path('view_profile', views.viewProfileFunction,name='view_profile')
]
