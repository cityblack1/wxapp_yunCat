# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-29 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_images', '0003_userimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catimage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='catimage',
            name='describe',
        ),
    ]
