from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.response import Response

from .permissions import UserPermission
from postapp.models import Post, Comment
from account.models import UserProfile, FriendRequest
from .serializers import *


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
        else:
            print("bad request")
        return Response(serializer.data)


# user views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]


class UserProfileCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# FriendRequest views
class FriendRequestList(generics.ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,UserPermission]


class FriendRequestDetail(generics.DestroyAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer


class FriendRequestCreate(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(request_sender=self.request.user)


# post api views

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# post api views

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    urlslink = {'users_profile_list': reverse('user_profile_list', request=request, format=format),
                'users_profile_create': reverse('user_profile_create', request=request, format=format),
                'users_create': reverse('user_create', request=request, format=format),
                'users_list': reverse('user_list', request=request, format=format),
                'friend_list': reverse('friend_list', request=request, format=format),
                'friend_create': reverse('friend_create', request=request, format=format),
                'comment_list': reverse('comment_list', request=request, format=format),
                'comment_create': reverse('comment_create', request=request, format=format),

                # 'posts_delete': reverse('posts_delete', request=request, format=format),

                # 'friend_detail': reverse('/friend-detail/', request=request, format=format),

                'posts_list': reverse('post_list', request=request, format=format),

                }

    return Response(urlslink)
    # 'posts_list': reverse('post-list', request=request, format=format),
    # 'f_request_list': reverse('f-request-list', request=request, format=format),
    # 'comment_list': reverse('comment-list', request=request, format=format),
    # 'reply_list': reverse('reply-list', request=request, format=format)

# class UserProfileViewset(viewsets.ModelViewSet):

#     queryset=UserProfile.objects.all()
#     serializer_class=UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,UserPermission]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class FriendRequestViewset(viewsets.ReadOnlyModelViewSet):

#     queryset=FriendRequest.objects.all()
#     serializer_class=FriendRequestSerializer


# class PostViewset(viewsets.ModelViewSet):

#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CommentViewset(viewsets.ModelViewSet):

#     queryset=Comment.objects.all()
#     serializer_class=CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# # class ReplyViewset(viewsets.ModelViewSet):

# #     queryset=Comment.objects.all()
# #     post=Post.objects.all()
# #     serializer_class=ReplySerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

# #     def perform_create(self, serializer):
# #         serializer.save(user=self.request.user)

# #     def perform_create(self, serializer):
# #         serializer.save(post=self.post)
