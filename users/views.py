from django.shortcuts import render, redirect
from django.views import View
from .models import Profile


# Create your views here.

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
#
# class Profiles(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
#
#
# class Profiles(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass