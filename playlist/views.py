from django.shortcuts import render
from django.views import generic
from .models import Playlist


class PlayList(generic.ListView):

    model = Playlist
    queryset = Playlist.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
