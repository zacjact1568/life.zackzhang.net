from django.views.generic import ListView
from rest_framework.generics import CreateAPIView

from utils import pagination
from blog.views import IndexView as PostsIndexView
from blog.models import Post
from .models import Song, AnnualSummary
from .serializers import SongSerializer


def complete_fragment(type_, fragment):
    if type_ == "color":
        return f"#{fragment}"
    elif type_ == "cover":
        return f"https://image.zacjact1568.com/music/{fragment}.jpg"
    elif type_ == "apple_music":
        return f"https://music.apple.com/us/{fragment}"
    elif type_ == "spotify":
        return f"https://open.spotify.com/{fragment}"
    elif type_ == "youtube":
        return f"https://youtu.be/{fragment}"
    else:
        raise ValueError(f"No type named \"{type_}\"")


class IndexView(ListView):

    year = 2019
    annual_summary = AnnualSummary.objects.get(year=year)
    template_name = "music/index.html"
    # 由于 get_queryset 没有返回 QuerySet 对象
    # 所以不能自动合成为 song_list，需要自行指定
    # 或者 object_list 也可
    context_object_name = "essentials"

    def get_queryset(self):
        tracks = ["Intro"]
        tracks.extend([f"Track {i}" for i in range(1, 11)])
        tracks.append("Outro")
        essentials = []
        for track in tracks:
            song = getattr(self.annual_summary, f"essentials_{track.lower().replace(' ', '_')}")
            song.track = track
            song.cover = complete_fragment("cover", song.cover)
            essentials.append(song)
        return essentials

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list)
        # 年份
        context["year"] = self.annual_summary.year
        # 年度歌曲
        song_of_this_year = self.annual_summary.song_of_this_year
        song_of_this_year.color = complete_fragment("color", self.annual_summary.song_of_this_year_color)
        song_of_this_year.cover = complete_fragment("cover", song_of_this_year.cover)
        song_of_this_year.lyric = self.annual_summary.song_of_this_year_lyric
        song_of_this_year.apple_music_link = complete_fragment(
            "apple_music", self.annual_summary.song_of_this_year_link_apple_music)
        song_of_this_year.spotify_link = complete_fragment(
            "spotify", self.annual_summary.song_of_this_year_link_spotify)
        youtube_link = self.annual_summary.song_of_this_year_link_youtube
        if youtube_link != "":
            song_of_this_year.show_youtube_link = True
            song_of_this_year.youtube_link = complete_fragment("youtube", youtube_link)
        else:
            song_of_this_year.show_youtube_link = False
        context["song_of_this_year"] = song_of_this_year
        # 精选集
        context["essentials_color"] = complete_fragment("color", self.annual_summary.essentials_color)
        context["essentials_link_apple_music"] = complete_fragment(
            "apple_music", self.annual_summary.essentials_link_apple_music)
        context["essentials_link_spotify"] = complete_fragment(
            "spotify", self.annual_summary.essentials_link_spotify)
        # 文章链接
        context["annual_summary_link"] = f"annual-summary-on-music-listening-{self.annual_summary.year}"
        return context


class ListenMemoView(ListView):

    model = Song

    template_name = 'music/listen_memo.html'

    context_object_name = 'music_list'

    paginate_by = 10

    def get_queryset(self):
        music_list = super(ListenMemoView, self).get_queryset()
        for music in music_list:
            # 补全专辑封面链接
            music.cover = 'https://image.zacjact1568.com/music/%s.jpg' % music.cover
            # 拼接专辑和年份
            music.album_year = '%s · %d' % (music.album, music.year)
            # 如果有听歌链接，补全网易云音乐链接
            music.show_link = False
            if music.link != '':
                music.show_link = True
                music.link = 'http://music.163.com/%s/' % music.link
        return music_list

    def get_context_data(self, **kwargs):
        context = super(ListenMemoView, self).get_context_data(**kwargs)

        # 分页
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = pagination.get_data(paginator, page, is_paginated)

        context.update(pagination_data)

        # 更新时间
        context.update({'update_time': Song.objects.first().time})

        return context


# 年度总结实际上是写在 Post 中的，这里只是将所有 Post 中的年度总结过滤出来做的一个列表
# 点进列表项还是 Post Detail 页面
class AnnualSummaryView(PostsIndexView):

    # 将 file 字段开头为 annual-summary-on-music-listening- 的 Post 选出，这就是年度总结
    # i.e. 所有年度总结 Post 的 file 字段必须使用这样的格式
    queryset = Post.objects.filter(file__startswith='annual-summary-on-music-listening-')


# CreateAPIView 会调用固定的 post 方法
class AddSongView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
