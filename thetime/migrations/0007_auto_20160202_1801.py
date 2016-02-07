# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0006_auto_20160201_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='syndicat',
            name='membres',
            field=models.IntegerField(default=13),
        ),
        migrations.AddField(
            model_name='syndicat',
            name='niveau',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 9, 18, 1, 41, 431997)),
        ),
    ]
