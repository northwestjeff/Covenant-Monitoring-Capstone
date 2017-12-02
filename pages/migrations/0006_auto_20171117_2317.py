# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-17 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171113_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statement',
            options={'ordering': ['-end_period']},
        ),
        migrations.AlterField(
            model_name='covenant',
            name='indicator',
            field=models.CharField(choices=[('Total Liabilities', 'Total Liabilities'), ('Current Ratio', 'Current Ratio')], max_length=50),
        ),
    ]