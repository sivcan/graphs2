# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160331_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='graphs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]