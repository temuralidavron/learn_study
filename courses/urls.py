from django.urls import path

from courses.views.course import list_course, create_course
from courses.views.group import list_group, create_group, group_students_manage
from courses.views.room import list_rooms, create_room, room_update, delete_room

urlpatterns = [
    path('list/', list_rooms,name='rooms'),
    path('create/', create_room,name='room-create'),
    path('update/<int:pk>/', room_update,name='room-update'),
    path('delete/<int:pk>/', delete_room,name='room-delete'),

    #courses CRUD
    path('courses/list/', list_course, name='list_course'),
    path('courses/create/', create_course, name='create_course'),
    # path('courses/update/<int:pk>/', room_update, name='room-update'),
    # path('courses/delete/<int:pk>/', delete_room, name='room-delete'),

    # group CRUD add STudent
    path("group/list/",list_group,name='group-list'),
    path("group/create/",create_group,name='group-create'),
    path('<int:group_id>/students/', group_students_manage, name='group-students-manage'),



]
