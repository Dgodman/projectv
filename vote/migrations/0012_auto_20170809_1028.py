# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0011_auto_20170809_1025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AbsenteeExceptions',
            new_name='AbsenteeException',
        ),
        migrations.RenameModel(
            old_name='AbsenteeRules',
            new_name='AbsenteeRule',
        ),
        migrations.AddField(
            model_name='stateinfo',
            name='absentee_exceptions',
            field=models.ManyToManyField(help_text='Select the absentee exceptions for this state', to='vote.AbsenteeException'),
        ),
    ]
