# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-08 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200207_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_for_rent',
            field=models.BooleanField(default=False, verbose_name='For rent?'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_for_sale',
            field=models.BooleanField(default=False, verbose_name='For sale?'),
        ),
    ]
