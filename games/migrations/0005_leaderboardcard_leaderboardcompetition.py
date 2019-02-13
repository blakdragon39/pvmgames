# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-13 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20190125_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoardCard',
            fields=[
                ('gamecard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.GameCard')),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('games.gamecard',),
        ),
        migrations.CreateModel(
            name='LeaderBoardCompetition',
            fields=[
                ('competition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Competition')),
                ('abyssal_sire', models.BooleanField()),
                ('cerberus', models.BooleanField()),
                ('grotesque_guardians', models.BooleanField()),
                ('kraken', models.BooleanField()),
                ('thermonuclear_smoke_devil', models.BooleanField()),
                ('callisto', models.BooleanField()),
                ('chaos_elemental', models.BooleanField()),
                ('scorpia', models.BooleanField()),
                ('venenatis', models.BooleanField()),
                ('vetion', models.BooleanField()),
                ('zilyana', models.BooleanField()),
                ('graardor', models.BooleanField()),
                ('kree_arra', models.BooleanField()),
                ('kril_tsutsaroth', models.BooleanField()),
                ('prime', models.BooleanField()),
                ('rex', models.BooleanField()),
                ('supreme', models.BooleanField()),
                ('kalphite_queen', models.BooleanField()),
                ('king_black_dragon', models.BooleanField()),
                ('vorkath', models.BooleanField()),
                ('zulrah', models.BooleanField()),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('games.competition',),
        ),
    ]
