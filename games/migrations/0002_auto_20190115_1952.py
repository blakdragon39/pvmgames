# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-15 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='slayer',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boss',
            name='slayer_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boss',
            name='wilderness',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drop',
            name='drop_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
