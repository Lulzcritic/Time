# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0017_auto_20160208_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='hungry',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 11, 18, 20, 35, 274554)),
        ),
        migrations.AddField(
            model_name='character',
            name='state',
            field=models.CharField(default=b'Aucun', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 11, 18, 20, 35, 274687)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 15, 18, 20, 35, 274423)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 11, 18, 20, 35, 272704)),
        ),
    ]
