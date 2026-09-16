from django import forms
from .models import StudentProfile


class StudentSelectForm(forms.Form):
    """Ko'p studentni birdan tanlash uchun form."""

    students = forms.ModelMultipleChoiceField(
        queryset=StudentProfile.objects.none(),   # boshida bo'sh
        widget=forms.SelectMultiple(attrs={'size': 15, 'class': 'student-list'}),
        label='',
    )

    def __init__(self, *args, **kwargs):
        # view'dan kelgan queryset'ni olamiz
        queryset = kwargs.pop('queryset')
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = queryset


from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Group, GroupStudent, StudentProfile
from .forms import StudentSelectForm


def group_students_view(request, pk):
    group = get_object_or_404(Group, pk=pk)

    # 1) Guruhdagi aktiv studentlarning id'lari
    in_group_ids = GroupStudent.objects.filter(
        group=group, is_active=True
    ).values_list('student_id', flat=True)

    # 2) Ikkita ro'yxat
    in_group = StudentProfile.objects.filter(id__in=in_group_ids)
    available = StudentProfile.objects.exclude(id__in=in_group_ids)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            form = StudentSelectForm(request.POST, queryset=available)
            if form.is_valid():
                for student in form.cleaned_data['students']:
                    GroupStudent.objects.update_or_create(
                        group=group,
                        student=student,
                        defaults={
                            'joined_at': timezone.localdate(),
                            'left_at': None,
                            'is_active': True,
                        },
                    )
                return redirect('group-students', pk=group.pk)

        elif action == 'remove':
            form = StudentSelectForm(request.POST, queryset=in_group)
            if form.is_valid():
                GroupStudent.objects.filter(
                    group=group,
                    student__in=form.cleaned_data['students'],
                    is_active=True,
                ).update(is_active=False, left_at=timezone.localdate())
                return redirect('group-students', pk=group.pk)

    # GET so'rov — ikkita bo'sh form
    return render(request, 'groups/students.html', {
        'group': group,
        'add_form': StudentSelectForm(queryset=available),
        'remove_form': StudentSelectForm(queryset=in_group),
    })


{% extends "base.html" %}

{% block content %}
<h2>{{ group.name }} — guruh tarkibi</h2>

<div class="transfer">

  <!-- CHAP TOMON: hamma studentlar -->
  <div class="panel">
    <h3>Barcha studentlar</h3>
    <form method="post">
      {% csrf_token %}
      {{ add_form.students }}
      <button type="submit" name="action" value="add">
        Guruhga qo'shish &rarr;
      </button>
    </form>
  </div>

  <!-- O'NG TOMON: guruhdagilar -->
  <div class="panel">
    <h3>Guruhdagilar ({{ remove_form.students.field.queryset.count }} ta)</h3>
    <form method="post">
      {% csrf_token %}
      {{ remove_form.students }}
      <button type="submit" name="action" value="remove">
        &larr; Guruhdan chiqarish
      </button>
    </form>
  </div>

</div>
{% endblock %}