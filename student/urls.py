from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name = 'dashboard'),
    path('register/',views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('error-page/', views.error_page, name='error_page'),
    path('profile/', views.profile, name = 'profile'),



]