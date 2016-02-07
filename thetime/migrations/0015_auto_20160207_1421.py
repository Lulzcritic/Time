# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0014_auto_20160203_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('first_stat', models.CharField(max_length=50)),
                ('second_stat', models.CharField(max_length=50)),
                ('pay', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='character',
            name='pending',
        ),
        migrations.AddField(
            model_name='character',
            name='pay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='role_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 14, 21, 39, 78550)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 14, 21, 39, 78367)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 14, 21, 39, 76636)),
        ),
    ]
