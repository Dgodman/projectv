# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0013_auto_20170809_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_short', models.CharField(help_text='Enter state abbreviation', max_length=2)),
                ('name_long', models.CharField(help_text='Enter state name', max_length=30)),
                ('can_vote_by_mail', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StateException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Generic name used in forms', max_length=20)),
                ('description', models.TextField(default='')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.State')),
            ],
            options={
                'verbose_name_plural': 'state exceptions',
            },
        ),
        migrations.CreateModel(
            name='StateRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Generic name used in forms', max_length=20)),
                ('description', models.TextField(default='')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.State')),
            ],
            options={
                'verbose_name_plural': 'state rules',
            },
        ),
        migrations.RemoveField(
            model_name='stateinfo',
            name='absentee_exceptions',
        ),
        migrations.RemoveField(
            model_name='stateinfo',
            name='absentee_rules',
        ),
        migrations.DeleteModel(
            name='AbsenteeException',
        ),
        migrations.DeleteModel(
            name='AbsenteeRule',
        ),
        migrations.DeleteModel(
            name='StateInfo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exceptions',
            field=models.ManyToManyField(blank=True, help_text='Select the absentee exceptions for this user (based on state)', null=True, to='vote.StateException'),
        ),
    ]
