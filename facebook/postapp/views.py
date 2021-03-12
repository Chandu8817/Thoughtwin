from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from .forms import PostForm
from .models import UserPost,LikesnComments

from account.models import UserProfile
from django.contrib.auth.models import User


@login_required(login_url='/')
def createView(request):

    context={}
    if request.method=="POST":
        post_form=PostForm(request.POST,request.FILES)

        if post_form.is_valid():
            post = post_form.save()
            post.user = request.user
            post.save()

            context['post_form']=post_form
            return HttpResponseRedirect(reverse('postlist'))
        else:
            print("data not post")
    else:
        post_form=PostForm()
    context['post_form']=post_form
    return  render(request,'postapp/createpost.html',context)

def retrieveView(request):

    context={}
    profiledetial = UserProfile.objects.get(user=request.user)

    userpost_list=UserPost.objects.all()
    post_form=PostForm()
    context['post_form']=post_form
    context['postlist']=userpost_list
    context['profiledetial']=profiledetial

    return render(request,'postapp/home.html',context)

def detailView(request,id):

    context={}
    singlepost=UserPost.objects.get(id=id)
    context['singlepost']=singlepost
    return render(request,'postapp/detailpost.html',context)

def updateView(request,id):

    context={}
    obj=get_object_or_404(UserPost,id=id)
    update_form=PostForm(request.POST,request.FILES,instance=obj)
    
    if update_form.is_valid():
        update_form.save()  
        return HttpResponseRedirect(reverse('postlist'))

    context['update_form']=update_form
    return render(request,"postapp/updatepost.html",context)

def deleteView(request,id):
    obj=get_object_or_404(UserPost,id=id)

    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect(reverse('postlist'))

    return render(request,"postapp/delete.html")

def likesnComments(request,id):
    # context={}

    comments=request.GET.get("comment")

    likes_comments=LikesnComments.objects.create(comments=comments)
    likes_comments.save()
    return render(request,'postapp/home.html')






    









