# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-13 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_covenant_comparison'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covenant',
            name='indicator',
            field=models.CharField(choices=[('Debt Service Coverage Ratio', 'Debt Service Coverage Ratio'), ('Total Liabilities', 'Total Liabilities'), ('Current Ratio', 'Current Ratio')], max_length=50),
        ),
        migrations.AlterField(
            model_name='covenant',
            name='operator_options',
            field=models.CharField(choices=[('Greater Than', '>'), ('Less Than', '<'), ('Equal to', '='), ('NOT Equal to', '≠')], max_length=15),
        ),
        migrations.AlterField(
            model_name='loan',
            name='payment_schedule',
            field=models.CharField(choices=[('Weekly', 'weekly'), ('Monthly', 'monthly'), ('Quarterly', 'quarterly'), ('Semi-annually', 'semi-annually'), ('Annually', 'annually')], max_length=25),
        ),
    ]
