# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_icon_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='icon',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
