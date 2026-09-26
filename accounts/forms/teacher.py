from django import forms

# from accounts.models import  TeacherProfile






class TeacherForm(forms.Form):
    phone=forms.CharField()
    username=forms.CharField()
    password=forms.CharField()
    specialization=forms.CharField()
    bio=forms.CharField()
from django import forms
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class TeacherEditForm(forms.Form):
    username = forms.CharField(max_length=150)
    specialization = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False,
                               help_text="O'zgartirmasangiz bo'sh qoldiring")

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("Bu username band.")
        return username

    @transaction.atomic
    def save(self, profile):
        user = profile.user
        user.username = self.cleaned_data["username"]
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        user.save()

        profile.specialization = self.cleaned_data["specialization"]
        profile.bio = self.cleaned_data["bio"]
        profile.save()
        return profile

# class TeacherEditForm(forms.Form):
#     username=forms.CharField()
#     specialization=forms.CharField()
#     bio=forms.CharField()
#     password=forms.CharField()
#
#
#     def save(self):
#         specialization=self.cleaned_data.get('specialization')
#         bio=self.cleaned_data.get('bio')
#         return
#
#
# from django import forms
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class TeacherEditForm(forms.Form):
#     username = forms.CharField()
#     specialization = forms.CharField()
#     bio = forms.CharField(widget=forms.Textarea)
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def save(self, profile):
#         """
#         Mavjud TeacherProfile va unga bog'liq CustomUser'ni yangilash
#         """
#         # 1. CustomUser ma'lumotlarini yangilash
#         user = profile.user  # TeacherProfile modelida user maydoni bor deb hisoblaymiz
#         user.username = self.cleaned_data['username']
#         user.set_password(self.cleaned_data['password']) # Parolni xavfsiz xesh qilish
#         user.save()
#
#         # 2. TeacherProfile ma'lumotlarini yangilash
#         profile.specialization = self.cleaned_data['specialization']
#         profile.bio = self.cleaned_data['bio']
#         profile.save()
#
#         return profile




