from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from account.views import UserSignUpView,UserLoginView,UserLogoutView,ProfileView,SearchView,UpdateProfilePhoto,UpdateCoverPhoto


urlpatterns=[
# path('',views.signupAndLogin,name='home'),
# path('signup/',views.signUp, name='signup'),
# path('logout', views.logoutuser, name='logout'),
# path('profile/',views.profile_page,name='profile'),
# path('search/', views.searchUser, name='search'),
# path('update/', views.updateprofile, name='update'),
# path('updatecover/', views.updateprofilecover, name='updatecover'),


path('',UserLoginView.as_view(),name='home'),
path('profile/',ProfileView.as_view(),name='profile'),
path('signup/',UserSignUpView.as_view(), name='signup'),
path('logout', UserLogoutView.as_view(), name='logout'),
path('search/', SearchView.as_view(), name='search'),
path('update/', UpdateProfilePhoto.as_view(), name='update'),
path('updatecover/',UpdateCoverPhoto.as_view(), name='updatecover'),




]