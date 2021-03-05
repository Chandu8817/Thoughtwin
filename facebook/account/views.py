from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
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

                return render(request, 'account/index.html', {'user_form': user_form, 'profile_form': profile_form,
                                                              'login_form': login_form})

        else:
            profile_form = ProfileForm()
            user_form = ExtendedUser()
            login_form = UserLoginForm()

        print("error")

        return render(request, 'account/index.html', {'profile_form': profile_form, 'user_form': user_form, 'login_form': login_form})
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
            print(username, password)

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
            return render(request, 'account/index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})

        # return redirect('/home')

    else:
        # Get Request here comes
        login_form = UserLoginForm()
        user_form = ExtendedUser()
        profile_form = ProfileForm()
        return render(request, 'account/index.html', {'login_form': login_form, 'user_form': user_form, 'profile_form': profile_form})

def logoutuser(request):
    logout(request)
    return redirect('home/')

@login_required(login_url='login')
def profile_page(request):
    profiledetial = UserProfile.objects.get(user=request.user)
    # print(profiledetial)
    return render(request, 'account/profile.html', {"profile": profiledetial})

def searchUser(request):

    searchname=request.GET.get('search_name')
    user_list=User.objects.filter(first_name__startswith=searchname)
    profiledetial = UserProfile.objects.get(user=request.user)
    params={'user_list':user_list,"profile": profiledetial}
    return render(request,'account/profile.html',params)

@login_required(login_url='login')
def updateprofile(request):
    user_form = ExtendedUser(request.POST)
    upd_profile=UserProfile.objects.get(user=request.user)
    update_form=ProfileForm(request.POST,instance=upd_profile)
    profiledetial = UserProfile.objects.get(user=request.user)



    if user_form.is_valid() and update_form.is_valid():
        user = user_form.save()
        updprofile = update_form.save(commit=False)
        updprofile.user = user
        updprofile.save()
        params={'upd_profile':update_form,"profile": profiledetial}
        return redirect('profle/')    
    else:
        params={'upd_profile':update_form,"profile": profiledetial}
    return render(request,'account/profile.html',params)










        




