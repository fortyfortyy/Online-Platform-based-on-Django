from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Project
from .forms import ProjectForm


class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()  # TODO
        return render(request, 'projects/projects.html', context={'projects': projects})

    def post(self, request):
        pass


class ProjectView(View):
    def get(self, request, pk):
        projectObj = Project.objects.get(id=pk)
        return render(request, 'projects/single-project.html', context={'project': projectObj})

    def post(self, request):
        pass


class CreateProject(View):
    def get(self, request):
        form = ProjectForm()
        context = {'form': form}
        return render(request, 'projects/project_form.html', context)

    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():  # Django checks if everything is valid, if somethings wasn't manipulated in user's form
            form.save()  # Django will create that object to the db
            return redirect('projects')  # Send back user to the projects page


class UpdateProject(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)    # return a form of user's chosen project to update
        context = {'form': form}
        return render(request, 'projects/project_form.html', context)

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():  # Django checks if everything is valid, if somethings wasn't manipulated in user's form
            form.save()  # Django will update that project in db
            return redirect('projects')  # Send back user to the projects page


class DeleteProject(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        context = {'object': project}
        return render(request, 'projects/delete_template.html', context)

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('projects')
