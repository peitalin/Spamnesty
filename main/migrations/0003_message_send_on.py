# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160928_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='send_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]