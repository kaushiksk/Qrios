# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20161216_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=10),
        ),
    ]