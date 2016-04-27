# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0021_auto_20160214_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='syndicat',
            field=models.ForeignKey(related_name='ressource', blank=True, to='thetime.Syndicat', null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 15, 29, 2, 538379)),
        ),
        migrations.AlterField(
            model_name='character',
            name='hungry',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 15, 29, 2, 538214)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 15, 29, 2, 538055)),
        ),
        migrations.AlterField(
            model_name='object',
            name='obj_type',
            field=models.IntegerField(choices=[(1, b'food'), (2, b'bandage'), (3, b'alimentary'), (4, b'chimical'), (5, b'oil'), (6, b'electronic'), (7, b'Scrap')]),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 15, 29, 2, 535956)),
        ),
        migrations.AlterField(
            model_name='territory',
            name='ressource_type',
            field=models.IntegerField(choices=[(1, b'food'), (2, b'bandage'), (3, b'alimentary'), (4, b'chimical'), (5, b'oil'), (6, b'electronic'), (7, b'Scrap')]),
        ),
    ]
