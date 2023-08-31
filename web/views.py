from django.shortcuts import render
from django.http import HttpResponse
from web import feed
from .models import Item
from datetime import date


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def update(request):
    feed.update("https://www.rtl.lu/rss/headlines")
    feed.update("https://www.lemonde.fr/rss/une.xml")
    feed.update("https://feeds.a.dj.com/rss/RSSWorldNews.xml")

    return HttpResponse("Feed updated")

def display(request):
    items = Item.objects.filter(
        pubDate__gt = date.today()
    ).order_by('-pubDate')
    return render(request, "report.html", { "items": items })