# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_covenant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
