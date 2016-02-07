# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0007_auto_20160202_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 9, 18, 20, 32, 737447)),
        ),
    ]
