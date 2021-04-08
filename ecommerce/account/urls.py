from django.urls import path
from django.contrib.auth.decorators import login_required

# from . import views
from account.views import (UserSignUpView, UserLoginView, UserLogoutView,
                           ProfileView,  UpdateProfilePhoto)

urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('update/', UpdateProfilePhoto.as_view(), name='update'),


]
