"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('fbapp.urls')),
    path('', include('account.urls')),
    path('post/', include('postapp.urls')),


# social login 
    path("login/", views.login, name="login1"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout1"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home1"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
