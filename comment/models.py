from django.db import models

from blog.models import Post


class Item(models.Model):

    name = models.CharField('名字', max_length=50)

    website = models.URLField('网站', blank=True)

    content = models.TextField('内容')

    created_at = models.DateTimeField('发表于', auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-created_at']
