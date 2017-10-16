# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.IntegerField(default=0)),
                ('activity_name', models.CharField(max_length=64)),
                ('employee_id', models.IntegerField(default=0)),
                ('group_number', models.IntegerField(default=1)),
                ('week_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField(default=0)),
                ('event_name', models.CharField(max_length=256)),
                ('event_date', models.DateField()),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('hex_id', models.IntegerField(default=0)),
                ('event_comment', models.CharField(max_length=256)),
                ('employee_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_id', models.IntegerField(default=0)),
                ('event_id', models.IntegerField(default=0)),
                ('attendance', models.BooleanField()),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=256)),
                ('note_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email_address', models.CharField(max_length=64)),
                ('group_number', models.IntegerField(default=1)),
                ('territory', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=16)),
                ('employee_id', models.IntegerField(default=0)),
                ('training_program', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('user_password', models.CharField(max_length=64)),
            ],
        ),
    ]