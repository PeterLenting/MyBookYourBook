# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-28 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200417_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='want_to_rent',
            field=models.BooleanField(default=False, verbose_name='I want to be able to rent(-out) books*'),
        ),
    ]
