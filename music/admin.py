from django.contrib import admin
from .models import Song, AnnualSummary


class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'time', 'essential']


class AnnualSummaryAdmin(admin.ModelAdmin):
    list_display = ['year', 'song_of_this_year']


admin.site.register(Song, SongAdmin)
admin.site.register(AnnualSummary, AnnualSummaryAdmin)
