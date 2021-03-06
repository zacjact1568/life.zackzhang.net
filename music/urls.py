from django.urls import path

from . import views


app_name = 'music'

urlpatterns = [
    path('music/', views.IndexView.as_view(), name='index'),
    path('music/listen_memo.html', views.ListenMemoView.as_view(), name='listen_memo'),
    path('music/annual_summary.html', views.AnnualSummaryView.as_view(), name='annual_summary'),
    path("music/add-song/", views.AddSongView.as_view())
]
