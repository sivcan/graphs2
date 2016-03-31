# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20160331_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
