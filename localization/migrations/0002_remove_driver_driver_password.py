# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='driver_password',
        ),
    ]