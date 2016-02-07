# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0013_auto_20160203_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 18, 30, 32, 635721)),
        ),
        migrations.AlterField(
            model_name='character',
            name='pending',
            field=models.CharField(default=b'Rien', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='role',
            field=models.CharField(default=b'Rien', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 18, 30, 32, 635546)),
        ),
    ]
