from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('content',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
