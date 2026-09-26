from django.urls import path

from accounts.views import user,teacher

urlpatterns = [
    path('dashboard/', user.dashboard,name="dashboard"),
    path('', user.create_user,name="register"),
    path('login/', user.login_view,name="login"),
    path('logout/', user.logout_view,name="logout"),
    path('teacher_dashboard/', user.teacher_dashboard,name="teacher_dashboard"),


    #teacher crud
    path('', teacher.get_teacher,name="teacher"),
    path("teacher/profile/", teacher.get_profile, name="teacher_profile"),
    path("teacher/profile/edit/", teacher.edit_teacher_view, name="edit_teacher"),
    path("teacher/profile/group/", teacher.get_my_groups, name="get_my_groups"),
    # path('teacher_profile/', teacher.get_profile, name='teacher_profile'),
    # path('teacher_edit/<int:profile_id>/', teacher.edit_teacher_view, name='edit_teacher_view'),
    # path('teacher_profile/', teacher.get_profile,name="teacher_profile"),
    # path('teacher_profile/<int:profile_id>/', teacher.edit_teacher_view,name="edit_teacher_view"),
]
