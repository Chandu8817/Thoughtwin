import pdb

from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, CreateView,UpdateView
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import UserProfile
from .forms import ProfileForm, ExtendedUser, UserLoginForm


class UserSignUpView(View):
    try:
        def post(self, request):
            profile_form = ProfileForm(request.POST, request.FILES)
            user_form = ExtendedUser(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                username = user_form.cleaned_data.get("username")
                password = user_form.cleaned_data.get("password1")
                signupuserlogin = authenticate(
                    username=username, password=password)
                login(request, signupuserlogin)
                return HttpResponseRedirect(reverse('profile'))
            else:
                login_form = UserLoginForm()
                return render(request, 'index.html', {'user_form': user_form,
                                                      'profile_form': profile_form, 'login_form': login_form})
            profile_form = ProfileForm()
            user_form = ExtendedUser()
            login_form = UserLoginForm()
            return render(request, 'index.html', {'profile_form': profile_form,
                                                  'user_form': user_form, 'login_form': login_form})
    except Exception as e:
        print(e)


class UserLoginView(View):
    try:
        def get(self, request):
            login_form = UserLoginForm()
            user_form = ExtendedUser()
            profile_form = ProfileForm()
            return render(request, 'index.html', {'login_form': login_form,
                                                  'user_form': user_form, 'profile_form': profile_form})

        def post(self, request):
            login_form = UserLoginForm(request, request.POST)
            if login_form.is_valid():
                username = login_form
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                    
                else:
                    print("error")
            else:
                user_form = ExtendedUser()
                profile_form = ProfileForm()
                return render(request, 'index.html', {'login_form': login_form,
                                                      'user_form': user_form, 'profile_form': profile_form})
    except Exception as e:
        print(e)

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))


class ProfileView(View): 
    def get(self,request):
        profiledetial = UserProfile.objects.get(user=request.user)
        from postapp.models import Post
        from postapp.forms import PostForm
        post_form = PostForm()
        postlist = Post.objects.all()
        return render(request, 'profile.html', {"profile": profiledetial,
                                                'postlist': postlist, "post_form": post_form})

class SearchView(View):
    def get(self,request):
        searchname = request.GET.get('search_name')
        user_list = User.objects.filter(first_name__startswith=searchname)
        profiledetial = UserProfile.objects.get(user=request.user)
        params = {'user_list': user_list, "profile": profiledetial}
        return render(request, 'profile.html', params)

class UpdateProfilePhoto(View):
    def post(self,request):       
        image = request.FILES.get('image')
        profile_object = UserProfile.objects.get(user=request.user)
        profile_object.profile_pic = image
        profile_object.save()
        return redirect('/profile/')


class UpdateCoverPhoto(View):
    def post(self,request):
        coverimage = request.FILES.get('coverimage')
        profile_object = UserProfile.objects.get(user=request.user)
        profile_object.profile_cover = coverimage
        profile_object.save()
        return redirect('/profile/')































# def signUp(request):
#     try:
#         if request.method == "POST":
#             profile_form = ProfileForm(request.POST, request.FILES)
#             user_form = ExtendedUser(request.POST)

#             if user_form.is_valid() and profile_form.is_valid():
#                 user = user_form.save()
#                 profile = profile_form.save(commit=False)
#                 profile.user = user
#                 profile.save()
#                 username = user_form.cleaned_data.get('username')
#                 password = user_form.cleaned_data.get('password1')
#                 puser = authenticate(username=username, password=password)
#                 login(request, puser)
#                 return redirect('profile')
#             else:
#                 # pdb.set_trace()
#                 # if user_form.password1 != user_form.password2:
#                 #     raise forms.validationError("password not match")

#                 messages.error(request, 'please enter correct detials')

#                 # return redirect('home/')
#                 login_form = UserLoginForm()

#                 return render(request, 'index.html', {'user_form': user_form, 'profile_form': profile_form,
#                                                             'login_form': login_form})

#         else:
#             profile_form = ProfileForm()
#             user_form = ExtendedUser()
#             login_form = UserLoginForm()

#         return render(request, 'index.html', {'profile_form': profile_form, 'user_form': user_form, 'login_form': login_form})
#     except Exception as e:
#         print(e)

# def signupAndLogin(request):
#     if request.method == 'POST':
#         login_form = UserLoginForm(request, request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data.get('username')
#             password = login_form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 print("error")
#         else:
#             print("user not found")
#         user_form = ExtendedUser()
#         profile_form = ProfileForm()
#         return render(request, 'index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})


#     else:
#         # Get Request here comes
#         login_form = UserLoginForm()
#         user_form = ExtendedUser()
#         profile_form = ProfileForm()
#         return render(request, 'index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})
# def profile_page(request):
#         from postapp.models import Post
#         from postapp.forms import PostForm
#         profiledetial = UserProfile.objects.get(user=request.user)

#         post_form = PostForm()

#         postlist = Post.objects.all()
#         return render(request, 'profile.html', {"profile": profiledetial,
#                                                 'postlist': postlist, "post_form": post_form})

# @login_required(login_url='login')
# def updateprofile(request):
#     if request.method == "POST":
#         image = request.FILES.get('image')
#         profile_object = UserProfile.objects.get(user=request.user)
#         profile_object.profile_pic = image
#         profile_object.save()
#         return redirect('/profile/')
