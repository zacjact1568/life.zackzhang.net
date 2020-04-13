from django.urls import path
from . import views

# 命名空间
app_name = 'blog'
urlpatterns = [
    # 匹配 /
    path('', views.IndexView.as_view(), name='index'),
    # 匹配 /post/<label>.html
    path('post/<label>.html', views.PostView.as_view(), name='detail'),
]
