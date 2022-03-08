# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница Posts')


# Страница со списком мороженого
def group_posts(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}') 

def any_slug(request):
    return HttpResponse('Группа уточнение')
