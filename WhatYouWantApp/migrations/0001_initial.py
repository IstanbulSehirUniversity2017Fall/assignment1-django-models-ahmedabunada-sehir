# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Director', models.CharField(max_length=15)),
                ('ProductionCompany', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Creator', models.CharField(max_length=15)),
                ('Producor', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WhatYouWantApp.Season'),
        ),
    ]