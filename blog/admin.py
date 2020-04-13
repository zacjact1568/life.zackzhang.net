from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']


admin.site.register(Post, PostAdmin)
