# Generated by Django 4.0.6 on 2022-07-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_alter_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='when',
            field=models.DateTimeField(auto_now=True),
        ),
    ]