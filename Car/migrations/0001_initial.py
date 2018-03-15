# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-15 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=50, verbose_name='Plate')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('type', models.CharField(choices=[('long', 'Long Car'), ('short', 'Short Car')], default='short', max_length=50, verbose_name='Model')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
