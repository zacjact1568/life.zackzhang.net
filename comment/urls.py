from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('comment/post/<label>/', views.post_comment, name='post_comment'),
]
