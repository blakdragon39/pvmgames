# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-11 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20190110_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boss',
            old_name='image',
            new_name='_image',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='_image',
        ),
    ]