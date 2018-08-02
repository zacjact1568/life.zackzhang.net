from django.contrib import admin
from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'time']


admin.site.register(Music, MusicAdmin)
