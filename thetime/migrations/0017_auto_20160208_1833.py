# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0016_auto_20160207_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='role_exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='role',
            name='min_first',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='role',
            name='min_second',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 8, 18, 33, 20, 269680)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 15, 18, 33, 20, 269572)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 8, 18, 33, 20, 268558)),
        ),
    ]
