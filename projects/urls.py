from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projects.as_view(), name="projects"),
    path('project/<str:pk>', views.Project.as_view(), name="project"),
]
