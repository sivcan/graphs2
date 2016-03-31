# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160324_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='x',
            new_name='x_Attribute',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='y',
            new_name='y_Attribute',
        ),
        migrations.AlterField(
            model_name='user',
            name='type_Of_Graph',
            field=models.CharField(choices=[('Bar Graph', 'Bar Graph'), ('Line Graph', 'Line Graph'), ('Pie Graph', 'Pie Graph')], default=1, max_length=10),
        ),
    ]