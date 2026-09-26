from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms.teacher import TeacherEditForm
from accounts.models import  TeacherProfile
from courses.models import Group


def get_teacher(request):
    teachers=TeacherProfile.objects.all()
    context={
        "teachers":teachers
    }
    return render(request,'accounts/teacher/list.html',context)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms.teacher import TeacherEditForm
from accounts.models import TeacherProfile


@login_required
def get_profile(request):
    teacher = get_object_or_404(TeacherProfile.objects.select_related("user"), user=request.user)
    return render(request, "accounts/teacher/teacher_profile.html", {"teacher": teacher})


@login_required
def edit_teacher_view(request):
    profile = get_object_or_404(TeacherProfile.objects.select_related("user"), user=request.user)
    user = profile.user

    if request.method == "POST":
        form = TeacherEditForm(request.POST, user=user)
        if form.is_valid():
            form.save(profile=profile)
            if form.cleaned_data.get("password"):
                update_session_auth_hash(request, user)
            return redirect("teacher_profile")
    else:
        form = TeacherEditForm(user=user, initial={
            "username": user.username,
            "specialization": profile.specialization,
            "bio": profile.bio,
        })

    return render(request, "accounts/teacher/edit_teacher.html", {"form": form})


def get_my_groups(request):
    user=request.user
    teacher=TeacherProfile.objects.get(user=user)
    groups=Group.objects.filter(teacher=teacher)
    context={
        "groups":groups,
        "teacher":teacher
    }
    return render(request,"accounts/teacher/teacher_group.html",context)
