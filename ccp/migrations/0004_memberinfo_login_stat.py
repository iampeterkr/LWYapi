# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-31 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccp', '0003_auto_20170828_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberinfo',
            name='login_stat',
            field=models.CharField(choices=[('n', 'NO'), ('y', 'YES')], default='', max_length=3, null=True),
        ),
    ]
