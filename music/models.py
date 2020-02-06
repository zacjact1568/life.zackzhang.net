from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


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

    ESSENTIAL_CHOICES = [
        (-1, "否"),
        (0, "Intro"),
        (1, "Track 1"),
        (2, "Track 2"),
        (3, "Track 3"),
        (4, "Track 4"),
        (5, "Track 5"),
        (6, "Track 6"),
        (7, "Track 7"),
        (8, "Track 8"),
        (9, "Track 7"),
        (10, "Track 10"),
        (11, "Outro")
    ]
    essential = models.SmallIntegerField("精选", default=-1, choices=ESSENTIAL_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = '音乐'
        ordering = ['-time']
