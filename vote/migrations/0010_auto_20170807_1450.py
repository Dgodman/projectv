# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20170807_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('MAILING_1', 'mailing address'), ('MAILING_2', 'other mailing'), ('HOME_1', 'home address')], max_length=20),
        ),
        migrations.DeleteModel(
            name='AddressType',
        ),
    ]
