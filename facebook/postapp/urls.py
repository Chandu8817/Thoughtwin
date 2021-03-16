from django.urls import path
from postapp.views import CreateView
from . import views
urlpatterns =[
    path('create',CreateView.as_view(),name='createpost'),
    path('',views.retrieveView,name='postlist'),
    path('<int:id>/',views.detailView,name='detailpost'),
    path('update/<int:id>/',views.updateView,name='update'),
    path('delete/<int:id>/',views.deleteView,name='delete'),
    path('comments/',views.comment,name='comments'),
    path('reply/',views.reply,name='reply'),






]