from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


def current_year():
    return int(timezone.localtime(timezone.now()).strftime('%Y'))


# 音乐类
class Music(models.Model):

    title = models.CharField('标题', max_length=100)

    artist = models.CharField('歌手', max_length=100)

    album = models.CharField('专辑', max_length=100)

    ALBUM_TYPE_ALBUM = 'album'
    ALBUM_TYPE_EP = 'ep'
    ALBUM_TYPE_SINGLE = 'single'

    ALBUM_TYPE_CHOICES = (
        (ALBUM_TYPE_ALBUM, '专辑'),
        (ALBUM_TYPE_EP, 'EP'),
        (ALBUM_TYPE_SINGLE, '单曲'),
    )

    album_type = models.CharField(
        '专辑类型',
        max_length=10,
        choices=ALBUM_TYPE_CHOICES,
        default=ALBUM_TYPE_ALBUM
    )

    year = models.PositiveSmallIntegerField(
        '年份',
        validators=[
            MinValueValidator(1970),
            # 当前年份 + 1，可能有预购专辑下一年才发行
            MaxValueValidator(current_year() + 1)
        ]
    )

    album_cover = models.CharField('专辑封面', max_length=100)

    genius = models.CharField('Genius', max_length=100, blank=True)

    netease_cloud_music = models.CharField('网易云音乐', max_length=100, blank=True)

    time = models.DateTimeField('时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = '音乐'
        ordering = ['-time']
