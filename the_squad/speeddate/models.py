from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    insert_date = models.DateTimeField('Date published')
    modified_date = models.DateTimeField('When changed',default=timezone.now())
    def __str__(self):
        return self.question_text
    def is_new(self):
        return self.insert_date >= timezone.now() - datetime.timedelta(days=1)
    def recently_changed(self):
        return self.modified_date >= timezone.now() - datetime.timedelta(minutes=5)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text