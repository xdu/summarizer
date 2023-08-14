from rss_parser import Parser
from requests import get
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from web.models import *
import logging

logger = logging.getLogger(__name__)

def update(url) :

    checkURL(url)

    response = get(url)

    rss = Parser.parse(response.text)
    print(rss)

    try:
        feed = Feed.objects.get(link=rss.channel.link)
    except ObjectDoesNotExist:
        feed = Feed(title=rss.channel.title,
                    desc=rss.channel.description,
                    link=rss.channel.link,
                    pubDate=rss.channel.pub_date.content,
                    lang=rss.channel.language)
        feed.save()

    for e in rss.channel.items:
        try :
            item = Item.objects.get(guid=e.guid)
        except ObjectDoesNotExist :
            item = Item.objects.create(guid=e.guid)
        item.title = e.title
        item.description = e.description
        # item.pubDate = e.pub_date.content
        item.link = e.link

        item.feed = feed
        item.save()


def checkURL(url) :
    val = URLValidator()
    try : 
        val(url)
    except ValidationError as e:
        print(e)