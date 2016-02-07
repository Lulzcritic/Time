# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0009_auto_20160202_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='d_encours',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 18, 1, 14, 542686)),
        ),
        migrations.AddField(
            model_name='character',
            name='encours',
            field=models.CharField(default=datetime.datetime(2016, 2, 3, 18, 2, 7, 421629, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 10, 18, 1, 14, 542504)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='membres',
            field=models.IntegerField(default=1),
        ),
    ]
