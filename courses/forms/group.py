
from courses.models import Group, GroupStudent


from django import forms
from accounts.models import StudentProfile


class GroupStudentAddForm(forms.Form):
    students = forms.ModelMultipleChoiceField(
        queryset=StudentProfile.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def __init__(self, *args, group=None, **kwargs):
        super().__init__(*args, **kwargs)
        already_in = GroupStudent.objects.filter(
            group=group, is_active=True
        ).values_list('student_id', flat=True)
        self.fields['students'].queryset = StudentProfile.objects.exclude(
            id__in=already_in
        ).select_related('user')


class GroupStudentRemoveForm(forms.Form):
    students = forms.ModelMultipleChoiceField(
        queryset=StudentProfile.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def __init__(self, *args, group=None, **kwargs):
        super().__init__(*args, **kwargs)
        active_ids = GroupStudent.objects.filter(
            group=group, is_active=True
        ).values_list('student_id', flat=True)
        self.fields['students'].queryset = StudentProfile.objects.filter(
            id__in=active_ids
        ).select_related('user')

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=[
            'course',
            'teacher',
            'mentor',
            'name',
            'start_date',

        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }