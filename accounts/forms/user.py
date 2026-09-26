
from django import forms

from accounts.models import CustomUser, TeacherProfile, StudentProfile


class CustomUserForm(forms.ModelForm):
    is_teacher=forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = [
            'phone',
            'username',
            "password",
            "is_teacher"

        ]
    # def clean_phone(self):
    #     phone=self.cleaned_data.get('phone')

    def save(self, commit = True):
        phone=self.cleaned_data.get("phone")
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        is_teacher=self.cleaned_data.get('is_teacher')
        user=CustomUser.objects.create_user(
            phone=phone,
            password=password,
            username=username
        )
        if is_teacher:

            TeacherProfile.objects.create(user=user)
            user.role='teacher'
            user.save()
        else:
            StudentProfile.objects.create(user=user)
            user.role='student'
            user.save()


        return user


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)