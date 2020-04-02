from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # 这些是必需的字段
        fields = ("title", "artist", "album", "year", "cover")
