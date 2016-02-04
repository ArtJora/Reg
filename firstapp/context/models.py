# -*- coding: utf-8 -*-

from django.db import models
from extuser.models import ExtUser



class Dance_program(models.Model):
    class Meta:
        db_table = "Танцевальная программа"
    dance_program_name = models.CharField(
        'Танцевальная программа',
        max_length = 200,
        unique=True,
        db_index=True)
    def __unicode__(self):
        return self.dance_program_name
    class Meta:
        verbose_name = 'Танцевальная программа'
        verbose_name_plural = 'Танцевальная программа'


class Age_category(models.Model):
    class Meta:
        db_table = "Возрастная категория"
    age_category_name = models.CharField(
        'Возрастная категория',
        max_length = 200
    )
    def __unicode__(self):
        return self.age_category_name
    # dance_programs = models.ManyToManyField(Dance_program)
    class Meta:
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастная категория'
class Dance_league(models.Model):
    class Meta:
        db_table = "Танцевальная лига"
    dance_league_name = models.CharField(
        'Лига',
        max_length = 200)
    def __unicode__(self):
        return self.dance_league_name
    class Meta:
        verbose_name = 'Танцевальная лига'
        verbose_name_plural = 'Танцевальная лига'

class Context(models.Model):
    class Meta:
        db_table = "Конкурсы"
    context_name = models.CharField(
        'Название Конкурса',
        max_length = 200)
    context_dance_program = models.ManyToManyField(Dance_program)
    context_age_category = models.ManyToManyField(Age_category)
    context_dance_league = models.ManyToManyField(Dance_league)
    context_date = models.DateField(
        'Дата'
    )
    context_place = models.CharField(
        'Место проведения',
        max_length = 100)
    context_organizer = models.CharField(
        'Организатор конкурса',
        max_length = 200)
    context_sity = models.CharField(
        'Город',
        max_length = 50)
    def __unicode__(self):
        return self.context_name
    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурс'


class Context_dancer(models.Model):
    class Meta:
        db_table = "Участник"
    context_dancer_name = models.CharField(
        'Имя танцора',
        max_length = 200)
    context_dancer_treaner = models.ForeignKey(ExtUser)
    context_dancer_sum = models.IntegerField(default=0)
    context_dance_program = models.CharField(
        'Танц прог',
        max_length = 50)
    context_age_category = models.CharField(
        'Возрастная категория',
        max_length = 50)
    context_dance_league = models.CharField(
        'Лига',
        blank=True,
        null=True,
        max_length = 50)
    context_name = models.ForeignKey(Context)
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участник'