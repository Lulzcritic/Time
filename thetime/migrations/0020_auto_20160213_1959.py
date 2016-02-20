# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0019_auto_20160213_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 59, 16, 280811)),
        ),
        migrations.AlterField(
            model_name='character',
            name='hungry',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 59, 16, 280704)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 19, 59, 16, 280538)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 59, 16, 279100)),
        ),
    ]
