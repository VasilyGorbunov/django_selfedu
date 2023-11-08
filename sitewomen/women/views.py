from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Page app women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Posts by categories - ID: {cat_id}</h1>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Posts by categories - SLUG: {cat_slug}</h1>")


def archive(request, year):
    return HttpResponse(f"<h1>Archive by years - YEAR: {year}</h1>")