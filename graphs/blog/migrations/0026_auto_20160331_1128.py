# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0025_auto_20160331_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='client',
        ),
        migrations.AddField(
            model_name='clients',
            name='clientz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
