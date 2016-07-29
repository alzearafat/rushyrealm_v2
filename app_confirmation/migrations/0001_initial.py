# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 09:36
from __future__ import unicode_literals

import app_confirmation.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_order', models.CharField(max_length=200)),
                ('nama', models.CharField(max_length=200)),
                ('jumlah_transfer', models.CharField(max_length=200)),
                ('tanggal_transfer', models.DateField(default=datetime.datetime.now)),
                ('tanggal_konfirmasi', models.DateField(blank=True, default=datetime.datetime.now, editable=False, null=True)),
                ('bukti_transfer', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', validators=[app_confirmation.models.validate_image])),
            ],
        ),
    ]