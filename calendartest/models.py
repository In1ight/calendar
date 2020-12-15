from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=512)
    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время окончания')
    user = models.ForeignKey(User, related_name='event', on_delete=models.CASCADE)

