from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .models import Profile


# Create your views here.

class LoginUser(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect('profiles')

        return render(request, 'users/login_register.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Creates session for the user in db (in session table) its gonna add in browsers cookies
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')

        return render(request, 'users/login_register.html')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.error(request, 'User was logged out')
        return redirect('login')


class Profiles(View):
    def get(self, request):
        profiles = Profile.objects.all()
        context = {'profiles': profiles}
        return render(request, 'users/profiles.html', context)


class UserProfile(View):
    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)

        topSkills = profile.skill_set.exclude(description__exact="")
        otherSkills = profile.skill_set.filter(description="")

        context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
        return render(request, 'users/user-profile.html', context)

    def post(self, request):
        pass

#
# class Profiles(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
