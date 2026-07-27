from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from accounts.forms.user import CustomUseForm, LoginForm
from accounts.models import TeacherProfile


def create_user(request):
    if request.method=="POST":
        form=CustomUseForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            # user=form.save(commit=False)
            # user.role='teacher'
            # user.save()
            # TeacherProfile.objects.create(user=user)
            if user:
                login(request,user)
                return redirect("base")
    else:
        form=CustomUseForm()
    return render(request,"accounts/register.html",{'form':form})

def login_view(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request, user)
                return redirect("base")
    else:
        form=LoginForm()
    return render(request, "accounts/login.html", {'form': form})





def logout_view(request):
    logout(request)
    return redirect("base")



