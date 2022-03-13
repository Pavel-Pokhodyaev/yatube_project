# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком постов
    path('group_list.html', views.group_posts, name='group_posts'),
    # Отдельная страница
    path('group_list/any_slug',views.any_slug),
    path(
        'group_list/<int:pk>/',
        views.posts_detail
    ),
    path('index.html', views.index),
] 