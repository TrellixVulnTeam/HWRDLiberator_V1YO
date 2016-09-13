# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_document_file_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='SCH_type',
        ),
        migrations.RemoveField(
            model_name='element',
            name='attrs',
        ),
        migrations.RemoveField(
            model_name='element',
            name='head',
        ),
        migrations.AddField(
            model_name='session',
            name='SCH_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='head',
            field=models.TextField(null=True),
        ),
    ]
