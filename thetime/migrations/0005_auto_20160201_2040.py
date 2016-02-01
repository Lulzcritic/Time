# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0004_auto_20160201_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='time',
            field=models.DateTimeField(default=datetime.timedelta(6, 86399, 999966)),
        ),
    ]
