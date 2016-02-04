# -*- coding: utf-8 -*-

from django.db import models
from extuser.models import ExtUser

# Create your models here.
class Dancer(models.Model):
    class Meta:
        db_table = "dancer"
    dancer_name = models.CharField(max_length = 200)
    dancer_birthday = models.DateField()
    dancer_trainer = models.ForeignKey(ExtUser)
    dancer_balls = models.IntegerField(default=0)


