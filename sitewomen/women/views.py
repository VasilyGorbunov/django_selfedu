from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Women

menu = [
    {'title': 'О сайте', 'url_name': 'about', },
    {'title': 'Добавить статью', 'url_name': 'add_page', },
    {'title': 'Обратная связь', 'url_name': 'contact', },
    {'title': 'Войти', 'url_name': 'login', },
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    posts = Women.published.all()
    return render(request,
                  'women/index.html',
                  {
                      'title': 'Главная страница',
                      'menu': menu,
                      'posts': posts,
                      'cat_selected': 0
                  })


def about(request):
    return render(request=request,
                  template_name='women/about.html',
                  context={
                      'title': 'О сайте',
                      'menu': menu
                  })


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND!!!</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }

    return render(request=request,
                  template_name='women/post.html',
                  context=data)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход в систему')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=data)
