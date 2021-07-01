from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsView.as_view(), name="projects"),
    path('project/<str:pk>', views.ProjectView.as_view(), name="project"),
]
