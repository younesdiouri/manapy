# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manapy', '0003_auto_20170726_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_fin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Echeance'),
        ),
    ]
