from django.shortcuts import render

from .models import student
def studentlist(request):
    students = student.objects.all()
    return render(request, 'studentApp/studentlist.html', {'students': students})

