from django.urls import path
from . import views

urlpatterns = [

path('courses-page/', views.courses_page, name = 'courses_page'),
path('course-create', views.course_create, name = 'course_create'),
path('course-delete/<int:pk>', views.delete_course, name='course_delete'),
path('course-update/<int:pk>', views.update_course, name='course_update'),
#GROUP CRUD
path('groups-page/', views.groups_page, name = 'groups_page'),
path('group-create/', views.group_create, name = 'group_create'),
path('group-delete/<int:pk>', views.delete_group, name='group_delete'),
path('group-update/<int:pk>', views.update_group, name='group_update'),
#MENTOR CRUD
path('mentors-page/', views.mentors_page, name = 'mentors_page'),
path('mentor-create/', views.mentor_create, name = 'mentor_create'),
path('mentor-delete/<int:pk>', views.delete_mentor, name='mentor_delete'),
path('mentor-update/<int:pk>', views.update_mentor, name='mentor_update'),
#MENTEE CRUD
path('mentees-page/', views.mentees_page, name = 'mentees_page'),
path('mentee-create/', views.mentee_create, name = 'mentee_create'),
path('mentee-delete/<int:pk>', views.delete_mentee, name='mentee_delete'),
path('mentee-update/<int:pk>', views.update_mentee, name='mentee_update'),


]