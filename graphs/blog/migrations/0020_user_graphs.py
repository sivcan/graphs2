# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_clients_graphs'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='graphs',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
