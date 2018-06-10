# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-09 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('race', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]