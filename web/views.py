from django.shortcuts import render
from django.http import HttpResponse
from web import feed
from .models import Item


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def update(request):
    feed.update("https://www.rtl.lu/rss/headlines")
    return HttpResponse("Feed updated")

def display(request):
    items = Item.objects.all()[:10]
    return render(request, "report.html", { "items": items })