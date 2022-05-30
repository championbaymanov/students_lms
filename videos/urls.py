from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', views.blogs ,name = 'videos'),
    path("<slug>", PostDetailView.as_view(), name='video'),
    path("q/", views.searchBlog, name='search_videos'),
    path('video-create/', views.video_create, name = 'video_create'),
    path('video-delete/<int:pk>', views.delete_video, name='video_delete'),
    path('video-update/<int:pk>', views.update_video, name='update_video'),


]