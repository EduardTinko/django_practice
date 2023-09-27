from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Students

fake = Faker()


def get_student(request):
    Students.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date())
    students = Students.objects.all()
    context = {'students': students, 'count': 1}
    return render(request, "get_students.html", context)


def get_students(request):
    count = int(request.GET.get('count'))
    if not isinstance(count, int) or count > 100 or count <= 0:
        return HttpResponse(f'<h3>Error! Enter a natural number from 1 to 100</h3>')
    for _ in range(count):
        Students.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date())
    students = Students.objects.all()
    context = {'students': students, 'count': count}
    return render(request, "get_students.html", context)

