# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0015_auto_20170809_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.State'),
        ),
        migrations.AlterField(
            model_name='stateexception',
            name='name',
            field=models.CharField(default='', help_text="'<STATE>_<DESCRIPTION>, ex: GA_ILLNESS", max_length=20),
        ),
        migrations.AlterField(
            model_name='staterule',
            name='name',
            field=models.CharField(default='', help_text='Generic name (may be used in forms)', max_length=20),
        ),
    ]