# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manapy', '0005_auto_20170727_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_tasks',
            name='tasks_id',
        ),
        migrations.RemoveField(
            model_name='users_tasks',
            name='users_id',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='users_tasts_id',
        ),
        migrations.AddField(
            model_name='tasks',
            name='users',
            field=models.ManyToManyField(to='manapy.Users'),
        ),
        migrations.DeleteModel(
            name='Users_Tasks',
        ),
    ]
