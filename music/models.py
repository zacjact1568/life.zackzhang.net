from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils.timezone import now

from utils.time import current_year


class Song(models.Model):

    title = models.CharField("标题", max_length=100)

    artist = models.CharField("歌手", max_length=100)

    album = models.CharField("专辑", max_length=100)

    year = models.IntegerField("年份")

    cover = models.CharField("封面", max_length=100)

    link = models.CharField("链接", max_length=100, blank=True)

    time = models.DateTimeField("时间", default=now)

    essential = models.BooleanField("精选", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "歌曲"
        verbose_name_plural = "歌曲"
        ordering = ["-time"]


class AnnualSummary(models.Model):

    year = models.IntegerField("年份", primary_key=True, default=current_year)

    # 存放 Song 的默认主键 id
    song_of_this_year = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        # + 代表不指定反向关系
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="年度歌曲"
    )

    song_of_this_year_color = models.CharField("年度歌曲颜色", max_length=6, validators=[MaxLengthValidator(6)])

    song_of_this_year_lyric = models.CharField("年度歌曲歌词", max_length=100)

    song_of_this_year_link_apple_music = models.CharField("年度歌曲 Apple Music 链接", max_length=100)

    song_of_this_year_link_spotify = models.CharField("年度歌曲 Spotify 链接", max_length=100)

    song_of_this_year_link_youtube = models.CharField("年度歌曲 YouTube 链接", max_length=100, blank=True)

    essentials_intro = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Intro"
    )

    essentials_track_1 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 1"
    )

    essentials_track_2 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 2"
    )

    essentials_track_3 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 3"
    )

    essentials_track_4 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 4"
    )

    essentials_track_5 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 5"
    )

    essentials_track_6 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 6"
    )

    essentials_track_7 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 7"
    )

    essentials_track_8 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 8"
    )

    essentials_track_9 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 9"
    )

    essentials_track_10 = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Track 10"
    )

    essentials_outro = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"essential": True},
        verbose_name="精选集 Outro"
    )

    essentials_color = models.CharField("精选集颜色", max_length=6, validators=[MaxLengthValidator(6)])

    essentials_link_apple_music = models.CharField("精选集 Apple Music 链接", max_length=100)

    essentials_link_spotify = models.CharField("精选集 Spotify 链接", max_length=100)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "年度总结"
        verbose_name_plural = "年度总结"
        ordering = ["-year"]
