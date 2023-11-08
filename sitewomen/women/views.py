from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse


def index(request):
    return render(request,
                  'women/index.html')


def about(request):
    return render(request,
                  'women/about.html')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Posts by categories - ID: {cat_id}</h1>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Posts by categories - SLUG: {cat_slug}</h1>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport',))
        return HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Archive by years - YEAR: {year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND!!!</h1>")
