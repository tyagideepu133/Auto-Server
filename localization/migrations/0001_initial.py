# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 07:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=150)),
                ('driver_dob', models.DateField()),
                ('driver_uidai', models.IntegerField(unique=True)),
                ('driver_password', models.CharField(default='123456', max_length=30)),
                ('driver_dl', models.IntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]