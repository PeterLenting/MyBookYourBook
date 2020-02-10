# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-08 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200208_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_for_rent',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='Yes', max_length=10),
        ),
    ]
