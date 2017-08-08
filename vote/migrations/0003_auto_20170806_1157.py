# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20170805_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_short', models.CharField(help_text='Enter state abbreviation', max_length=2)),
                ('name_long', models.CharField(help_text='Enter state name', max_length=30)),
                ('absentee_type', models.CharField(choices=[('NONE', 'no absentee ballots'), ('ALL', 'every election'), ('1_YEAR', 'every year'), ('2_YEAR', 'every two years')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('MAILING_1', 'mailing address'), ('MAILING_2', 'other mailing'), ('HOME_1', 'home address')], max_length=20),
        ),
        migrations.DeleteModel(
            name='AddressType',
        ),
    ]