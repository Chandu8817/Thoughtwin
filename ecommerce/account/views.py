import pdb

from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import UserProfile
from .forms import ProfileForm, ExtendedUser, UserLoginForm


class UserSignUpView(View):
    try:
        def get(self, request):
            user_form = ExtendedUser()
            profile_form = ProfileForm()
            return render(request, 'signup1.html', {
                'user_form': user_form, 'profile_form': profile_form})

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
                return HttpResponseRedirect(reverse('list_products'))
            else:
                login_form = UserLoginForm()
                return render(request, "signup1.html", {'user_form': user_form,
                                                                'login_form': login_form})
            profile_form = ProfileForm()
            user_form = ExtendedUser()
            login_form = UserLoginForm()
            return render(request, "signup1.html", {'profile_form': profile_form,
                                                            'user_form': user_form, 'login_form': login_form})
    except Exception as e:
        print(e)


class UserLoginView(View):
        # def get(self, request):
        #     login_form = UserLoginForm()
        #     return render(request, 'login.html', {'login_form': login_form})
        def get(self, request):
            # login_form = UserLoginForm(request, request.POST)
            # if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_products')
            else:
                print("error")
            return render(request, 'login.html')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("list_products"))


class ProfileView(View):
    def get(self, request):
        profiledetial = UserProfile.objects.get(user=request.user)
        # pdb.set_trace()
        return render(request, 'account.html', {
            "profile": profiledetial, })


class UpdateProfilePhoto(View):
    def post(self, request):
        image = request.FILES.get('image')
        profile_object = UserProfile.objects.get(user=request.user)
        profile_object.profile_pic = image
        profile_object.save()
        return redirect('/profile/')



