from django.urls import path

from courses.views import course

urlpatterns = [
    path('create/', course.create_course,name="create_course"),
    path('list/', course.course_list,name="course_list"),
    path('course_detail/<int:pk>/', course.course_detail,name="course_detail"),
    path('course_edit/<int:pk>/', course.course_edit,name="course_edit"),
    path('course_delete/<int:pk>/', course.course_delete,name="course_delete"),

]
