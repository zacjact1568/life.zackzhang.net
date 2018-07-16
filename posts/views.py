import markdown
from django.views.generic import ListView, DetailView
from comments.forms import CommentForm
from .models import Post
from utils import pagination


class IndexView(ListView):
    # 要获取的模型
    model = Post
    # 指定视图渲染的模板
    template_name = 'posts/index.html'
    # 指定获取的模型列表数据保存的变量名，此变量会被传递给模板
    context_object_name = 'post_list'
    # 指定每一页包含的文章数量
    paginate_by = 5

    def get_queryset(self):
        post_list = super(IndexView, self).get_queryset()
        for post in post_list:
            # 对摘要进行基础 Markdown 渲染
            post.excerpt = markdown.markdown(post.excerpt)
        return post_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # 获取父类生成的字典的模板变量
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = pagination.get_data(paginator, page, is_paginated)

        context.update(pagination_data)

        return context


class PostView(DetailView):
    # 指定该类控制显示的 model 类型，此处显示某篇文章，传入 Post 类
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
    # 指定 URL 中模板的参数
    slug_url_kwarg = 'file'
    # 指定 Post 中哪个字段对应 URL 中模板的参数
    slug_field = 'file'

    def get_object(self, queryset=None):
        # 对 content 进行 Markdown 渲染
        # 如果不指定 slug_*，就会自动根据 pk 获取文章？
        post = super(PostView, self).get_object(queryset=None)
        post.content = markdown.markdown(post.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             # 语法高亮
                                             'markdown.extensions.codehilite',
                                         ])
        return post

    def get_context_data(self, **kwargs):
        # 将评论列表和表单传递给模板
        context = super(PostView, self).get_context_data(**kwargs)
        form = CommentForm()
        # 获取这篇 post 下的全部评论
        comment_list = self.object.comment_set.all()
        context.update({'form': form, 'comment_list': comment_list, 'enable_comments': False})
        return context
