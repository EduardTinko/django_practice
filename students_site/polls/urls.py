from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.get_student, name='get_student'),
    path("generate-students/", views.get_students, name='get_students')
]
