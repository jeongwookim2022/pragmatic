# Generated by Django 4.0.6 on 2022-08-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0007_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
    ]
