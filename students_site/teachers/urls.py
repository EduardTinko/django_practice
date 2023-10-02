from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_teachers, name="get_teachers"),
]
