# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_auto_20170806_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenteeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an address type', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'address types',
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='type',
        ),
        migrations.AlterField(
            model_name='state',
            name='absentee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.AbsenteeType'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vote.AddressType'),
            preserve_default=False,
        ),
    ]