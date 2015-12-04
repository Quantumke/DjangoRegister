# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=100)),
                ('profile_pic', models.CharField(max_length=100)),
                ('web_url', models.URLField(unique=True, max_length=100)),
                ('date_created', models.DateField(verbose_name=datetime.datetime(2015, 12, 4, 11, 2, 31, 23992, tzinfo=utc))),
                ('date_updated', models.DateField(verbose_name=datetime.datetime(2015, 12, 4, 11, 2, 31, 24052, tzinfo=utc))),
                ('languages', models.CharField(max_length=100, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
        ),
    ]
