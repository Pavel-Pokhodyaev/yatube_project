# posts/views.py
from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context) 

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
