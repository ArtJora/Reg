# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dancer_name', models.CharField(max_length=200)),
                ('dancer_birthday', models.DateField()),
                ('dancer_balls', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dancer',
            },
        ),
    ]
