from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    STATUSES = {'craft':'Draft','in progress':'In progress','completed':'Completed'}
    status = models.CharField(max_length=100, choices=STATUSES)