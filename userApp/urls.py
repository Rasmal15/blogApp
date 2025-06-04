from django.urls import path
from . import views
from .views import UserInfoView

urlpatterns = [
    path('signup/', views.userCreation, name='signup'),
    path('sign-in/', views.userLogin, name='sign-in'),
    path('logout',views.userLogout,name="logout"),
    path('forgot_password/', views.forgotPasswordFunction, name='forgot_password'),
    path('userinfo', UserInfoView.as_view(), name='userinfo')
]
