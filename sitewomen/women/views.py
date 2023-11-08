from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Page app women")


def categories(request):
    return HttpResponse("<h1>Posts by categories</h1>")
