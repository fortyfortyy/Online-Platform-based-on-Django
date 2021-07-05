from django.shortcuts import render, redirect
from django.views import View
from .models import Profile


# Create your views here.

class Profiles(View):
    def get(self, request):
        return render(request, 'users/profiles.html')

    def post(self, request):
        pass


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
#
#
# class Profiles(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass