# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_auto_20170807_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='absenteetype',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
