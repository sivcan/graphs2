# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20160331_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='clientz',
        ),
    ]