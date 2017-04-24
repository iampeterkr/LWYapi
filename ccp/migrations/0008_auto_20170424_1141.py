# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccp', '0007_auto_20170424_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='irs_usd',
            field=models.CharField(choices=[('n', 'NO'), ('y', 'YES')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='irs_won',
            field=models.CharField(choices=[('n', 'NO'), ('y', 'YES')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='market',
            field=models.CharField(choices=[('ccp', 'CCP'), ('tr', 'TR')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='ndf',
            field=models.CharField(choices=[('n', 'NO'), ('y', 'YES')], default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='urlmeta',
            name='item',
            field=models.CharField(blank=True, choices=[('all', 'ALL'), (None, 'None')], max_length=20),
        ),
        migrations.AlterField(
            model_name='urlmeta',
            name='market',
            field=models.CharField(choices=[('ccp', 'CCP'), ('tr', 'TR')], max_length=20),
        ),
        migrations.AlterField(
            model_name='urlmeta',
            name='process',
            field=models.CharField(choices=[('list', 'LIST'), ('data', 'DATA')], max_length=20),
        ),
    ]
