# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0004_detection_metadata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='bucket',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='key',
        ),
        migrations.AddField(
            model_name='frame',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
