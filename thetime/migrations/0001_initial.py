# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('time', models.CharField(max_length=50)),
                ('pa', models.IntegerField(default=0)),
                ('role', models.CharField(max_length=50)),
                ('stamina', models.IntegerField(default=0)),
                ('intelligence', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=0)),
                ('social', models.IntegerField(default=0)),
                ('observation', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Syndicat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('banque', models.IntegerField(default=0)),
                ('president', models.OneToOneField(related_name='character', to='thetime.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ressource_type', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=1000)),
                ('factory', models.BooleanField(default=False)),
                ('level_factory', models.IntegerField(default=0)),
                ('owner', models.OneToOneField(to='thetime.Syndicat')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='syndicat',
            field=models.ForeignKey(related_name='character', to='thetime.Syndicat'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
