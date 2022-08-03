from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class DisLikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name='dislike_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='dislike_record')

    class Meta:
        unique_together = ('user', 'article')
