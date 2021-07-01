from django.shortcuts import render
from django.views import View
from .models import Project


class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        for project in projects:

            print(project)
            print("--------")
        return render(request, 'projects/projects.html', context={'projects': projects})

    def post(self, request):
        pass


class ProjectView(View):
    def get(self, request, pk):
        projectObj = Project.objects.get(pk=pk)
        return render(request, 'projects/single-project.html', context={'project': projectObj})

    def post(self, request):
        pass



