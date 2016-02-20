# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0018_auto_20160211_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('damage', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('obj_type', models.IntegerField(choices=[(1, b'food'), (2, b'bandage')])),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='d_pending',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 47, 41, 566890)),
        ),
        migrations.AlterField(
            model_name='character',
            name='hungry',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 47, 41, 566669)),
        ),
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 17, 19, 47, 41, 566524)),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='banque',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 13, 19, 47, 41, 564610)),
        ),
        migrations.AddField(
            model_name='object',
            name='character',
            field=models.ForeignKey(related_name='object', blank=True, to='thetime.Character', null=True),
        ),
    ]
