from django.urls import path

from courses.views.room import list_rooms, create_room, room_update, delete_room

urlpatterns = [
    path('list/', list_rooms,name='rooms'),
    path('create/', create_room,name='room-create'),
    path('update/<int:pk>/', room_update,name='room-update'),
    path('delete/<int:pk>/', delete_room,name='room-delete'),


]
