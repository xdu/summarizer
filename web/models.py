from django.db import models


class Feed(models.Model):

    title = models.CharField(max_length=200)

    desc = models.TextField(max_length=1000)

    link = models.URLField(unique=True)

    pubDate = models.DateTimeField(auto_now_add=True, blank=True)

    lang = models.CharField(max_length=2, default="en")

    def __str__(self) -> str:
        return self.title


class Item(models.Model):

    feed = models.ForeignKey("Feed", on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=500)

    description = models.TextField(max_length=5000)

    link = models.URLField()

    guid = models.CharField(max_length=200, unique=True)

    pubDate = models.DateTimeField(auto_now_add=True, blank=True)
