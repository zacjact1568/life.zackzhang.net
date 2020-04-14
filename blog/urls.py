from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<label>.html', views.PostView.as_view(), name='detail'),
    # 返回文章列表（不包括正文）
    path('blog/get-post-list/', views.GetPostListView.as_view()),
    # 返回指定 label 的文章（包括正文）
    path('blog/get-post/<label>/', views.GetPostView.as_view())
]
