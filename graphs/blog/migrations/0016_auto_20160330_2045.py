# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160330_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='number_Of_Graph',
            new_name='ID_Of_Graph',
        ),
    ]