from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import localtime, now


# 音乐类
class Music(models.Model):

    title = models.CharField('标题', max_length=100)

    artist = models.CharField('歌手', max_length=100)

    album = models.CharField('专辑', max_length=100)

    year = models.PositiveSmallIntegerField(
        '年份',
        validators=[
            MinValueValidator(1970),
            MaxValueValidator(2038)
        ]
    )

    cover = models.CharField('封面', max_length=100)

    link = models.CharField('链接', max_length=100, blank=True)

    time = models.DateTimeField('时间', default=now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = '音乐'
        ordering = ['-time']
