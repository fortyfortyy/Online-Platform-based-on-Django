from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsView.as_view(), name="projects"),
    path('project/<str:pk>', views.ProjectView.as_view(), name="project"),
    path('create-project/', views.CreateProject.as_view(), name="create-project"),
    path('update-project/<str:pk>', views.UpdateProject.as_view(), name="update-project"),
    path('delete-project/<str:pk>', views.DeleteProject.as_view(), name="delete-project"),
]
