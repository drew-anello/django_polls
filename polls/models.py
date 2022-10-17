from django.contrib import admin
from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
