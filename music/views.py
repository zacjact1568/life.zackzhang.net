from django.shortcuts import render
from django.views.generic import ListView
from .models import Music
from utils import pagination
from posts.views import IndexView
from posts.models import Post


def index(request):
    return render(request, 'music/index.html')


class ListenMemoView(ListView):

    model = Music

    template_name = 'music/listen_memo.html'

    context_object_name = 'music_list'

    paginate_by = 10

    def get_queryset(self):
        music_list = super(ListenMemoView, self).get_queryset()
        for music in music_list:
            music.album_cover = 'https://upload-images.jianshu.io/upload_images/1771371-%s.jpg' % music.album_cover
            music.show_genius = False
            if music.genius != '':
                music.show_genius = True
                music.genius = 'https://genius.com/%s-lyrics' % music.genius
            music.show_netease_cloud_music = False
            if music.netease_cloud_music != '':
                music.show_netease_cloud_music = True
                music.netease_cloud_music = 'http://music.163.com/%s/' % music.netease_cloud_music
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
class AnnualSummaryView(IndexView):

    # 将 file 字段开头为 music-listen-annual-summary- 的 Post 选出，这就是年度总结
    # i.e. 所有年度总结 Post 的 file 字段必须使用这样的格式
    queryset = Post.objects.filter(file__startswith='music-listen-annual-summary-')
