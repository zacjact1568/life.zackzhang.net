from django.db import models
from django.urls import reverse
from django.utils.timezone import now


# 文章类
class Post(models.Model):

    # 标题，存储较短的字符串使用 CharField，设定最长为 100
    title = models.CharField('标题', max_length=100)

    # 摘要
    excerpt = models.TextField('摘要')

    # 正文，使用 TextField 来存储大段文本
    content = models.TextField('正文')

    # 日期 TODO 改成时间，方便同一天添加的文章排序
    date = models.DateField('日期', default=now)

    # 文件名
    file = models.CharField('文件', max_length=100)

    # TODO 添加是否启用评论

    # 解释器显示的数据为此函数的返回值
    def __str__(self):
        return self.title

    # 生成文章 URL
    # 用于在 HTML 中获取某篇文章的链接
    def get_absolute_url(self):
        # blog:detail 表示 urls.py 中的 app_name 为 blog，name 为 detail 的视图函数
        return reverse('blog:detail', kwargs={'file': self.file})

    class Meta:
        # 管理页面显示的中文名
        verbose_name = '文章'
        # 管理页面显示的复数中文名，不设置的话会加 s
        verbose_name_plural = '文章'
        # 日期逆序（-）排列
        ordering = ['-date']
