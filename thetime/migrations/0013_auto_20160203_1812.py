# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0012_auto_20160203_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='encours',
            new_name='pending',
        ),
        migrations.RemoveField(
            model_name='character',
            name='d_encours',
        ),
        migrations.AddField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 18, 12, 2, 607054)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 18, 12, 2, 606842)),
        ),
    ]
