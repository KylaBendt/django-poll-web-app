import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_text = models.CharField('category', max_length=100)

    def __str__(self):
        return self.category_text


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

