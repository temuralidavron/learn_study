from django.shortcuts import redirect, render

from courses.forms.room import RoomForm
from courses.models import Room


def create_room(request):
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rooms")
    else:
        form=RoomForm()
    return render(request,"courses/room/create.html",{'form':form})


def list_rooms(request):
    rooms=Room.objects.all()
    context={
        'rooms':rooms
    }
    return render(request,"courses/room/list.html",context)


def room_update(request,pk):
    room=Room.objects.get(pk=pk)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form=RoomForm(instance=room)
    return render(request,"courses/room/create.html",{'form':form,"room":room})



def delete_room(request,pk):
    room=Room.objects.get(pk=pk)
    if request.method=='POST':
        room.delete()
        return redirect('rooms')
    else:
        return render(request,"courses/room/delete.html",{"room":room})





