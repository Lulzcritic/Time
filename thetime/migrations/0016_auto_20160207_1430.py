# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0015_auto_20160207_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 14, 30, 47, 914992)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 14, 30, 47, 914893)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 14, 30, 47, 913864)),
        ),
    ]
