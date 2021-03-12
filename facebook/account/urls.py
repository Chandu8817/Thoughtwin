from django.urls import path

from . import views

urlpatterns=[
# path('home',views.home,name='home'),
path('',views.signupAndLogin,name='home'),
path('profile/',views.profile_page,name='profile'),
path('signup/', views.signUp, name='signup'),
path('logout', views.logoutuser, name='logout'),
path('search/', views.searchUser, name='search'),
path('update/', views.updateprofile, name='update'),
path('updatecover/', views.updateprofilecover, name='updatecover'),




]