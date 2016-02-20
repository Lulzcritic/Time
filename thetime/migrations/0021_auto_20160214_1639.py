# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0020_auto_20160213_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='quantity_sell',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 16, 39, 16, 863803)),
        ),
        migrations.AlterField(
            model_name='character',
            name='hungry',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 16, 39, 16, 863693)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 18, 16, 39, 16, 863569)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 16, 39, 16, 862327)),
        ),
    ]
