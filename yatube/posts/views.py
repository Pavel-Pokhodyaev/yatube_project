# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse(
        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        '<a href="https://praktikum.yandex.ru/profile/backend-developer/">'
        'Начать учиться</a><br>'
        '<a href="http://127.0.0.1:8000/group/">'
        'Страница group </a> '
        )


# Страница со списком мороженого
def group_posts(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}') 

def any_slug(request):
    return HttpResponse('Группа уточнение')
