from django.urls import path

from ajaxapp import views

urlpatterns = [
    path('create',views.PostFbView.as_view(),name='create'),

]