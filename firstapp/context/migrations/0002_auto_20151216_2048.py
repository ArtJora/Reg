# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='context_dancer',
            name='context_dancer_treaner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='context_dancer',
            name='context_name',
            field=models.ForeignKey(to='context.Context'),
        ),
        migrations.AddField(
            model_name='context',
            name='context_age_category',
            field=models.ManyToManyField(to='context.Age_category'),
        ),
        migrations.AddField(
            model_name='context',
            name='context_dance_league',
            field=models.ManyToManyField(to='context.Dance_league'),
        ),
        migrations.AddField(
            model_name='context',
            name='context_dance_program',
            field=models.ManyToManyField(to='context.Dance_program'),
        ),
    ]
