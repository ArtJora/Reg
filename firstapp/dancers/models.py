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
    try: # raised when birth day is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)

    if birthday.month >= today.month and birthday.day >= today.day :

        return today.year - born.year
    else:
        return today.year - born.year - 1
