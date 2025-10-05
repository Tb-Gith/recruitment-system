from django.urls import path
from . import views

urlpatterns = [
    path("", views.applications_list, name="home"),          # root -> list
    path("applications", views.applications_list, name="applications_list"),
    path("apply", views.apply, name="apply"),
]