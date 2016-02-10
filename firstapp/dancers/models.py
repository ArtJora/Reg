# -*- coding: utf-8 -*-

from django.db import models
from extuser.models import ExtUser
from django.utils import timezone
import datetime

# Create your models here.
class Dancer(models.Model):
    class Meta:
        db_table = "dancer"
    dancer_name = models.CharField(max_length = 200)
    dancer_birthday = models.DateField()
    dancer_trainer = models.ForeignKey(ExtUser)
    dancer_balls = models.IntegerField(default=0)
    def age(self):
        return calculate_age(self.dancer_birthday)


def calculate_age(born):
    today = datetime.date.today()
    birthday = born
    if birthday.month <= today.month:
        if birthday.month < today.month:
            return today.year - birthday.year
        if birthday.month == today.month:
            if birthday.day <= today.day:
                return today.year - birthday.year
            else:
                return today.year - birthday.year - 1
    else:
        return today.year - birthday.year - 1