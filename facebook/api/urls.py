from django.urls import path,include

from rest_framework import renderers
# from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from  rest_framework.authtoken.views import  obtain_auth_token

from api import views



# router= DefaultRouter()

# router.register(r'users_profile',views.UserProfileViewset)
# router.register(r'f_request_list', views.FriendRequestViewset)
# router.register(r'post-list', views.PostViewset)
# router.register(r'comment_list',views.CommentViewset)
# router.register(r'reply_list', views.ReplyViewset)



# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', views.api_root),
    path('user-create/', views.UserCreate.as_view(),name='user_create'),
    path('user-list/', views.UserList.as_view(),name='user_list'),
    path('user-profile-create/', views.UserProfileCreate.as_view(),name='user_profile_create'),
    path('user-profile-list/', views.UserProfileList.as_view(),name='user_profile_list'),
    path('friend-list/', views.FriendRequestList.as_view(),name='friend_list'),
    path('friend-create/', views.FriendRequestCreate.as_view(),name='friend_create'),
    path('friend-detail/<int:pk>/', views.FriendRequestDetail.as_view(),name='friend_detail'),



    path('post-list/', views.PostList.as_view(),name='post_list'),
    path('post-create/', views.PostCreate.as_view(),name='posts_create'),
    path('post-delete/<str:pk>/', views.PostDelete.as_view(), name='posts_delete'),
    path('comment-list/', views.CommentList.as_view(),name='comment_list'),
    path('comment-create/', views.CommentCreate.as_view(),name='comment_create'),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth')



    
    # path('users-profile/<int:pk>/', views.UserList.as_view(),name='users_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)