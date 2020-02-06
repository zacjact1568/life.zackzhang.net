from django.views.generic import ListView
from .models import Music
from utils import pagination
from posts.views import IndexView as PostsIndexView
from posts.models import Post


class IndexView(ListView):

    model = Music
    queryset = model.objects.filter(time__year=2019, essential__gt=-1)
    ordering = "essential"
    template_name = "music/index.html"

    def get_queryset(self):
        music_list = super().get_queryset()
        for music in music_list:
            music.cover = f"https://image.zacjact1568.com/music/{music.cover}.jpg"
            music.track = self.model.ESSENTIAL_CHOICES[music.essential + 1][1]
        return music_list


class ListenMemoView(ListView):

    model = Music

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
        context.update({'update_time': Music.objects.first().time})

        return context


# 年度总结实际上是写在 Post 中的，这里只是将所有 Post 中的年度总结过滤出来做的一个列表
# 点进列表项还是 Post Detail 页面
class AnnualSummaryView(PostsIndexView):

    # 将 file 字段开头为 annual-summary-on-music-listening- 的 Post 选出，这就是年度总结
    # i.e. 所有年度总结 Post 的 file 字段必须使用这样的格式
    queryset = Post.objects.filter(file__startswith='annual-summary-on-music-listening-')
