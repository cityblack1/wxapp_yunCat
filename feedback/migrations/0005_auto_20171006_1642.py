# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20171006_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
