from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    # 匹配 /about.html
    path('about.html', views.index, name='index'),
]
