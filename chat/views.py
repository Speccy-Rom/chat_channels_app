from django.shortcuts import render

from chat.models import Room


def index_view(request):
    context = {}
    rooms = Room.objects.all()
    context['rooms'] = rooms

    return render(request, 'index.html', context)


def room_view(request, room_name):
    context = {}
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context['chat_room'] = chat_room

    return render(request, 'room.html', context)
