from django.urls import path
from . import views
urlpatterns =[
    path('create',views.createView,name='createpost'),
    path('',views.retrieveView,name='postlist'),
    path('<int:id>/',views.detailView,name='detailpost'),
    path('update/<int:id>/',views.updateView,name='detailpost'),
    path('delete/<int:id>/',views.deleteView,name='delete'),
    path('comments/',views.likesnComments,name='comments'),





]