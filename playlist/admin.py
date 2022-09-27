from django.contrib import admin
from .models import Playlist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Playlist)
class PlaylistAdmin(SummernoteModelAdmin):

    summernote_fields = ('note_on_songs')


