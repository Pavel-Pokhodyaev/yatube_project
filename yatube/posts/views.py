# posts/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

# Страница со списком мороженого
def group_posts(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context) 


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}') 

def any_slug(request):
    return HttpResponse('Группа уточнение')
