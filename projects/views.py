from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


class Projects(View):
    def get(self, request):
        msg = "hello you are ob the project page"
        return render(request, 'projects/projects.html', context={'msg': msg})

    def post(self, request):
        pass


class Project(View):
    def get(self, request, pk):
        return render(request, 'projects/single-project.html', context={'pk': pk})

    def post(self, request):
        pass



