# my_project/blog/urls.py

from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import custom_logout, post_list
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', post_list, name='post_list'),
    path('ultimos-posts/', views.mostrar_ultimos_posts, name='mostrar_ultimos_posts'),
]
