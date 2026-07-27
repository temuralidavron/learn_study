from django.shortcuts import redirect, render

from courses.forms.course import CourseForm
from courses.models import Course


def create_course(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base")
    else:
        form=CourseForm()
    return render(request,"course/create.html",{'form':form})

def course_list(request):
    courses=Course.objects.all()
    context={
        "courses":courses
    }
    return render(request,"course/list.html",context)

def course_detail(request,pk):
    course=Course.objects.get(pk=pk)
    context={
        "course":course
    }
    return render(request,"course/detail.html",context)



def course_edit(request,pk):
    course=Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect("base")
    else:
        form = CourseForm(instance=course)
    return render(request, "course/create.html", {'form': form})


def course_delete(request,pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    else:
        return render(request, "course/delete.html", {'course': course})


