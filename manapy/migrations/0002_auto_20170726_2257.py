# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manapy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='checked',
            field=models.IntegerField(),
        ),
    ]