from django.urls import path
from django.contrib.auth.decorators import login_required , permission_required
from postapp.views import CreateView ,DetailView, RetrieveView,DeleteView ,ReplyView,CommentView,PostUpdateView
from . import views
urlpatterns =[
    path('create',login_required(CreateView.as_view()),name='createpost'),
    path('',login_required(RetrieveView.as_view()),name='postlist'),
    path('<int:id>/',login_required(DetailView.as_view()),name='detailpost'),
    # path('update/<int:id>/',views.updateView,name='update'),
    path('update/<pk>/',login_required(PostUpdateView.as_view()),name='update'),

    path('delete/<int:id>/',login_required(DeleteView.as_view()),name='delete'),
    path('comments/',login_required(CommentView.as_view()),name='comments'),
    path('reply/',login_required(ReplyView.as_view()),name='reply'),






]