# Generated by Django 4.2.2 on 2023-08-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="lang",
            field=models.CharField(default="en", max_length=2),
        ),
        migrations.AlterField(
            model_name="feed",
            name="pubDate",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
