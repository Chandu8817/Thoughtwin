from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View


# Create your views here.
from .forms import PostForm
from .models import Post,Comment

from account.models import UserProfile
from django.contrib.auth.models import User


# @login_required(login_url='/')

# def createView(request):

#     context={}
#     if request.method=="POST":
#         post_form=PostForm(request.POST,request.FILES)

#         if post_form.is_valid():
#             post = post_form.save()
#             post.user = request.user
#             post.save()

#             context['post_form']=post_form
#             return HttpResponseRedirect(reverse('postlist'))
#         else:
#             print("data not post")
#     else:
#         post_form=PostForm()
#     context['post_form']=post_form
#     return  render(request,'postapp/createpost.html',context)'



@login_required(login_url='/')

def detailView(request,id):

    context={}
    profiledetial = UserProfile.objects.get(user=request.user)

    obj=get_object_or_404(Post,id=id)
    usercomment=Comment.objects.filter(reply=None)
    count=usercomment.count

    singlepost=Post.objects.get(id=id)
    context['singlepost']=singlepost
    context['comment']=usercomment
    context['profiledetial']=profiledetial
    context['count']=count

    return render(request,'postapp/detailpost.html',context)


@login_required(login_url='/')

def retrieveView(request):

    context={}
    
    # obj=get_object_or_404(Post,id=id)
    profiledetial = UserProfile.objects.get(user=request.user)
    usercomment=Comment.objects.filter(reply=None)
    count=usercomment.count

   
    post_list=Post.objects.all()
    post_form=PostForm()
    context['post_form']=post_form
    context['postlist']=post_list
    context['profiledetial']=profiledetial
    context['comment']=usercomment
    context['count']=count

    return render(request,'postapp/home.html',context)



def updateView(request,id):

    context={}
    obj=get_object_or_404(Post,id=id)
    update_form=PostForm(request.POST,request.FILES,instance=obj)
    
    if update_form.is_valid():
        update_form.save()  
        return HttpResponseRedirect(reverse('postlist'))

    context['update_form']=update_form
    return render(request,"postapp/updatepost.html",context)

def deleteView(request,id):
    obj=get_object_or_404(Post,id=id)

    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect(reverse('postlist'))

    return render(request,"postapp/delete.html")
def comment(request):
    try:
        # import pdb; pdb.set_trace()

        post_id=request.GET.get("postid")
        comment=request.GET.get("comment")
        post_obj=Post.objects.get(id=post_id)
        profiledetial = UserProfile.objects.get(user=request.user)

        Comment.objects.create(profile=profiledetial,post=post_obj,comment=comment)
        

    except Exception as e:
        print(e)

    return HttpResponseRedirect(reverse("postlist" ))
def reply(request):
    try:
        # import pdb; pdb.set_trace()
        comment=request.GET.get("comment")
        comment_id=request.GET.get("commentid")
        comment_obj=Comment.objects.get(id=comment_id)
        post_id=request.GET.get("postid")
        post_obj=Post.objects.get(id=post_id)
       
        profiledetial = UserProfile.objects.get(user=request.user)
        Comment.objects.create(profile=profiledetial,post=post_obj,comment=comment,reply=comment_obj)
        


        return HttpResponseRedirect(reverse("postlist"))
    except Exception as e:
        print(e)
        print("profile not found ")


# @login_required(login_url='/')

class CreateView(View):
    context={}
    template='postapp/createpost.html'

    def post(self,request):
        post_form= PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            post.user = request.user
            self.context['post_form']=post_form
            post.save()
        return HttpResponseRedirect(reverse('postlist'))

    def get(self,request):
        return render(request,self.template,self.context)
    
    



    
    
    






    









