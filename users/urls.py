from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profiles.as_view(), name="profiles"),
    path('profile/<str:pk>', views.UserProfile.as_view(), name="user-profile"),
]
