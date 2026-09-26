from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from accounts.forms.user import CustomUserForm, LoginForm
from accounts.models import TeacherProfile, CustomUser


def dashboard(request):
    return render(request,"base.html")



def create_user(request):
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            # user=form.save(commit=False)
            # user.role='teacher'
            # user.save()
            # TeacherProfile.objects.create(user=user)
            if user:
                login(request,user)
                return redirect("dashboard")
    else:
        form=CustomUserForm()
    return render(request,"accounts/register.html",{'form':form})

def login_view(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                teacher=user
                login(request, user)
                if teacher.role==CustomUser.Role.TEACHER:
                    return redirect("teacher_dashboard")
                return redirect("base")
    else:
        form=LoginForm()
    return render(request, "accounts/login.html", {'form': form})





def logout_view(request):
    logout(request)
    return redirect("dashboard")


def teacher_dashboard(request):
    return render(request,"accounts/teacher/teacher.html")


