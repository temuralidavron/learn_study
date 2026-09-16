from django import forms

from courses.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=[
            'name',
            'capacity'

        ]