# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_category_name', models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context_name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\x9a\xd0\xbe\xd0\xbd\xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd0\xb0')),
                ('context_date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
                ('context_place', models.CharField(max_length=100, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('context_organizer', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80 \xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd0\xb0')),
                ('context_sity', models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u043a\u0443\u0440\u0441',
                'verbose_name_plural': '\u041a\u043e\u043d\u043a\u0443\u0440\u0441',
            },
        ),
        migrations.CreateModel(
            name='Context_dancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context_dancer_name', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xbe\xd1\x80\xd0\xb0')),
                ('context_dancer_sum', models.IntegerField(default=0)),
                ('context_dance_program', models.CharField(max_length=50, verbose_name=b'\xd0\xa2\xd0\xb0\xd0\xbd\xd1\x86 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3')),
                ('context_age_category', models.CharField(max_length=50, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
                ('context_dance_league', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9b\xd0\xb8\xd0\xb3\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a',
                'verbose_name_plural': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a',
            },
        ),
        migrations.CreateModel(
            name='Dance_league',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dance_league_name', models.CharField(max_length=200, verbose_name=b'\xd0\x9b\xd0\xb8\xd0\xb3\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u0430\u044f \u043b\u0438\u0433\u0430',
                'verbose_name_plural': '\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u0430\u044f \u043b\u0438\u0433\u0430',
            },
        ),
        migrations.CreateModel(
            name='Dance_program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dance_program_name', models.CharField(unique=True, max_length=200, verbose_name=b'\xd0\xa2\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb5\xd0\xb2\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0', db_index=True)),
            ],
            options={
                'verbose_name': '\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430',
                'verbose_name_plural': '\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430',
            },
        ),
    ]
