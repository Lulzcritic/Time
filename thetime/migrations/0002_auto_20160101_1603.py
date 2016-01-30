# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thetime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='syndicat',
            field=models.ForeignKey(related_name='character', blank=True, to='thetime.Syndicat', null=True),
        ),
        migrations.AlterField(
            model_name='syndicat',
            name='president',
            field=models.OneToOneField(related_name='syndicat_president', to='thetime.Character'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='owner',
            field=models.OneToOneField(related_name='territory', to='thetime.Syndicat'),
        ),
    ]
