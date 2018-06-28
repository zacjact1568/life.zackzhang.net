from django.urls import path
from . import views

# 命名空间
app_name = 'posts'
urlpatterns = [
    # 匹配 /
    path('', views.IndexView.as_view(), name='index'),
    # 匹配 /post/<file>/
    path('post/<file>.html', views.PostView.as_view(), name='detail'),
    # 匹配 /about.html
    path('about.html', views.about, name='about'),
]
