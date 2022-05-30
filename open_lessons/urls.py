from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', views.blogs ,name = 'open_lesson'),
    path("<slug>", PostDetailView.as_view(), name='open_lesson'),
    path("table/<slug>", PostDetailView_Register.as_view(), name='open_lesson_register'),
    path("q/", views.searchBlog, name='search_open_lesson'),
    path('open-lesson-create/', views.open_create, name = 'open_create'),
    path('open-lesson-delete/<int:pk>', views.delete_open, name='open_delete'),
    path('open-lesson-update/<int:pk>', views.update_open, name='update_open'),



]