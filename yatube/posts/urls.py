# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов
    path('group/', views.group_posts),
    # Отдельная страница
    path('group/any_slug',views.any_slug),
    path(
        'group/<int:pk>/',
        views.posts_detail
    ),
] 