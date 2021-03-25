from datetime import datetime
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, UpdateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm
from .models import Post, Comment
from account.models import UserProfile


@method_decorator(login_required, name='dispatch')
class CreateView(View):
    context = {}
    context1 = {}
    template = 'postapp/createpost.html'
    template2 = 'postapp/newpostdata.html'

    def post(self,request, *args, **kwargs):
        print(request.POST)
        image=request.FILES.get('file')
        post_contain=request.POST.get('post_contain')
        post=Post.objects.create(user=request.user,contain=post_contain,image=image)
        self.context1['post']=post
        return render(request, self.template2, self.context1)
    def get(self, request):
        return render(request, self.template, self.context)
       


@method_decorator(login_required, name='dispatch')
class RetrieveView(ListView):
    def get(self, request):
        context = {}
        profiledetial = UserProfile.objects.get(user=request.user)
        usercomment = Comment.objects.filter(reply=None)
        count = usercomment.count
        post_list = Post.objects.all()
        list_of_friends = profiledetial.friends.all()

        post_form = PostForm()
        context['post_form'] = post_form
        context['postlist'] = post_list
        context['profile'] = profiledetial
        context['comment'] = usercomment
        context['count'] = count
        context['list_of_friends'] = list_of_friends

        return render(request, 'postapp/posts.html', context)


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    def get(self, request, id):
        context = {}
        profiledetial = UserProfile.objects.get(user=request.user)
        
        obj = get_object_or_404(Post, id=id)
        usercomment = Comment.objects.filter(reply=None, post=obj)
        count = usercomment.count
        singlepost = Post.objects.get(id=id)
        context['singlepost'] = singlepost
        context['comment'] = usercomment
        context['profile'] = profiledetial
        context['count'] = count 
        return render(request, 'postapp/detailpost.html', context)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'postapp/updatepost.html'
    context_object_name = 'update_form'
    fields = ('contain', 'image',)
    success_url = '/post/'


@method_decorator(login_required, name='dispatch')
class PostDeleteView(View):
    def post(self, request):
        id=request.POST.get('del_id')
        obj = Post.objects.get(id=id)
        user = UserProfile.objects.get(user=request.user)
        if request.method == "POST":
            if obj.user != user.user:
                print("user not valid")
            else:
                obj.delete()
        data={'message': 'delete successfully'}
        return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
class CommentView(View):
    def get(self, request):
        try:
            post_id = request.GET.get("postid")
            comment = request.GET.get("comment")
            post_obj = Post.objects.get(id=post_id)
            profiledetial = UserProfile.objects.get(user=request.user)
            Comment.objects.create(profile=profiledetial,
                                   post=post_obj, comment=comment)
        except Exception as e:
            print(e)
        return HttpResponseRedirect("/post/"+str(post_id))


@method_decorator(login_required, name='dispatch')
class ReplyView(View):
    def get(self, request):
        try:
            comment = request.GET.get("comment")
            comment_id = request.GET.get("commentid")
            comment_obj = Comment.objects.get(id=comment_id)
            post_id = request.GET.get("postid")
            post_obj = Post.objects.get(id=post_id)
            profiledetial = UserProfile.objects.get(user=request.user)
            Comment.objects.create(profile=profiledetial, post=post_obj,
                                   comment=comment, reply=comment_obj)
            return HttpResponseRedirect("/post/"+str(post_id))
        except Exception as e:
            print(e)
            print("profile not found ")


class LikePostView(View):
    def post(self,request):
    
        post_id=request.POST.get('like_id')
        user=request.user
        post=get_object_or_404(Post, id=post_id)
        if user in post.liked.all():
            post.liked.remove(user)
            data={}
            data['count']=post.likes_count
        else:
            post.liked.add(user)
            data={}
            data['count']=post.likes_count
        return JsonResponse(data)





















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


# @login_required(login_url='/')
# def detailView(request, id):

#     context = {}
#     profiledetial = UserProfile.objects.get(user=request.user)

#     obj = get_object_or_404(Post, id=id)
#     usercomment = Comment.objects.filter(reply=None, post=obj)
#     count = usercomment.count

#     singlepost = Post.objects.get(id=id)
#     context['singlepost'] = singlepost
#     context['comment'] = usercomment
#     context['profiledetial'] = profiledetial
#     context['count'] = count

#     return render(request, 'postapp/detailpost.html', context)


# @login_required(login_url='/')
# def retrieveView(request):

#     context = {}

#     # obj=get_object_or_404(Post,id=id)
#     profiledetial = UserProfile.objects.get(user=request.user)
#     usercomment = Comment.objects.filter(reply=None)
#     count = usercomment.count

#     post_list = Post.objects.all()
#     post_form = PostForm()
#     context['post_form'] = post_form
#     context['postlist'] = post_list
#     context['profiledetial'] = profiledetial
#     context['comment'] = usercomment
#     context['count'] = count

#     return render(request, 'postapp/home.html', context)


# def updateView(request, id):

#     context = {}
#     obj = get_object_or_404(Post, id=id)
#     update_form = PostForm(request.POST, request.FILES, instance=obj)

#     if update_form.is_valid():
#         update_form.save()
#         return HttpResponseRedirect(reverse('postlist'))

#     context['update_form'] = update_form
#     return render(request, "postapp/updatepost.html", context)


# def deleteView(request, id):
#     obj = get_object_or_404(Post, id=id)

#     user = UserProfile.objects.get(user=request.user)

#     if request.method == "POST":
#         if obj.user != user.user:
#             # import pdb; pdb.set_trace()
#             print("user not valid")
#         else:
#             obj.delete()
#     return HttpResponseRedirect(reverse('postlist'))
