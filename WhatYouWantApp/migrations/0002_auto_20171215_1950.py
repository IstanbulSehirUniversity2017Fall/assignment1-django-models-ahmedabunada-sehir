# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhatYouWantApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='EpisodeNumber',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='Length',
            field=models.CharField(default=50, max_length=6),
            preserve_default=False,
        ),
    ]