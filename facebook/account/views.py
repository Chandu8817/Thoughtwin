from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from postapp.models import Post
from postapp.forms import PostForm
from django.contrib import messages
from .forms import ProfileForm, ExtendedUser, UserLoginForm

import pdb
# Create your views here.

def signUp(request):
    try:
        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES)
            user_form = ExtendedUser(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password1')
                puser = authenticate(username=username, password=password)
                login(request, puser)
                return redirect('profile')
            else:
                # pdb.set_trace()
                # if user_form.password1 != user_form.password2:
                #     raise forms.validationError("password not match")

                messages.error(request, 'please enter correct detials')

                # return redirect('home/')
                login_form = UserLoginForm()

                return render(request, 'index.html', {'user_form': user_form, 'profile_form': profile_form,
                                                            'login_form': login_form})

        else:
            profile_form = ProfileForm()
            user_form = ExtendedUser()
            login_form = UserLoginForm()

        return render(request, 'index.html', {'profile_form': profile_form, 'user_form': user_form, 'login_form': login_form})
    except Exception as e:
        print(e)

def signupAndLogin(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request, request.POST)
        # user_form = ExtendedUser(request.POST)
        # profile_form = ProfileForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

            else:
                print("error")
        else:
            print("user not found")
            # login_form = UserLoginForm()
        user_form = ExtendedUser()
        profile_form = ProfileForm()
        return render(request, 'index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})

        # return redirect('/home')

    else:
        # Get Request here comes
        login_form = UserLoginForm()
        user_form = ExtendedUser()
        profile_form = ProfileForm()
        return render(request, 'index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url='/')
def profile_page(request):
    profiledetial = UserProfile.objects.get(user=request.user)
     
    post_form=PostForm()
    
    post_list=Post.objects.all()
    return render(request, 'profile.html', {"profile": profiledetial,
    'post_list':post_list,"post_form":post_form})

def searchUser(request):
    if request.method=="GET":

        searchname=request.GET.get('search_name')
        user_list=User.objects.filter(first_name__startswith=searchname)
        profiledetial = UserProfile.objects.get(user=request.user)
        # return HttpResponseRedirect(reverse('profile'))

    params={'user_list':user_list,"profile": profiledetial}
    return render(request,'profile.html',params)

@login_required(login_url='login')
def updateprofile(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        profile_object = UserProfile.objects.get(user=request.user)
        profile_object.profile_pic = image
        profile_object.save()
        return redirect('/profile/')

def updateprofilecover(request):
    if request.method == "POST":
        coverimage = request.FILES.get('coverimage')
        profile_object = UserProfile.objects.get(user=request.user)
        profile_object.profile_cover = coverimage
        profile_object.save()
        return redirect('/profile/')







        




