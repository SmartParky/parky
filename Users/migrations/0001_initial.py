# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-15 21:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Telefon numarası formatı şu şekilde olmalıdır: '05xx xxx xxxx'.", regex='^(05(\\d{2}) (\\d{3}) (\\d{4}))$')], verbose_name='Phone Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Staff')),
                ('type', models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('park-owner', 'Park Owner')], default='customer', max_length=50, verbose_name='Type')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.City', verbose_name='City')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
