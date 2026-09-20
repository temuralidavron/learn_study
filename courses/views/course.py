from django.shortcuts import render, redirect

from courses.forms.course import CourseForm
from courses.models import Course


def list_course(request):
    courses=Course.objects.all()
    context={
        'courses':courses
    }
    return render(request,"courses/course/list.html",context)

def create_course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_course")
    else:
        form=CourseForm()
    return render(request,"courses/room/create.html",{'form':form})
