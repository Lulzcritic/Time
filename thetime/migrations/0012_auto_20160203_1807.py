# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0011_auto_20160203_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='d_encours',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 18, 7, 48, 973033)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 18, 7, 48, 972783)),
        ),
    ]
