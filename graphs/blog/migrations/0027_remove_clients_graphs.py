# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20160331_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='graphs',
        ),
    ]
