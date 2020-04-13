from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField('标题', max_length=100)

    excerpt = models.TextField('摘要')

    content = models.TextField('正文')

    created_at = models.DateTimeField('创建于', auto_now_add=True)

    updated_at = models.DateTimeField('更新于', auto_now=True)

    label = models.CharField('标签', max_length=100)

    def __str__(self):
        return self.title

    # 生成文章 URL，用于在 HTML 中获取某篇文章的链接
    def get_absolute_url(self):
        # blog:detail 表示 urls.py 中 app_name='blog'，name='detail' 的视图函数
        return reverse('blog:detail', kwargs={'label': self.label})

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']
