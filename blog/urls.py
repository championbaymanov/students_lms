from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', views.blog ,name = 'blog'),
    path("<slug>", PostDetailView.as_view(), name='post'),
    path("q/", views.searchBlog, name='search'),
    path('blogs/', views.blogs ,name = 'blogs'),
    path('blog-create/', views.post_create, name = 'blog_create'),
    path('blog-delete/<int:pk>', views.delete_post, name='blog_delete'),
    path('blog-update/<int:pk>', views.update_blog, name='update_blog'),

]