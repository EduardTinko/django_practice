from django.shortcuts import render

from .models import Teacher


# Create your views here.


def get_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "get_teachers.html", {"teachers": teachers})
