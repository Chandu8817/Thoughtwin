from django.urls import path
from django.contrib.auth.decorators import login_required , permission_required
from postapp.views import CreateView ,PostDetailView, RetrieveView,PostDeleteView ,ReplyView,CommentView,LikePostView, PostUpdateView
# from account import views

# app_name = 'postapp'

urlpatterns =[
    path('create',CreateView.as_view(),name='createpost'),
    path('',RetrieveView.as_view(),name='postlist'),
    path('<int:id>/',PostDetailView.as_view(),name='detailpost'),
    # path('update/<int:id>/',views.updateView,name='update'),
    path('update/<pk>/',PostUpdateView.as_view(),name='update'),
    # path('delete/<int:id>/',PostDeleteView.as_view(),name='delete'),
    path('delete/',PostDeleteView.as_view(),name='delete'),
    path('comments/',CommentView.as_view(),name='comments'),
    path('reply/',ReplyView.as_view(),name='reply'),
    # path('like/<int:id>/',views.postLike,name='likepost'),
    path('likepost/',LikePostView.as_view(),name='likepost'),

]