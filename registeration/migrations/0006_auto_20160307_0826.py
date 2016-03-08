# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0005_auto_20160307_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='first_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='first_time_day',
        ),
        migrations.AddField(
            model_name='event',
            name='first_time_preference',
            field=models.CharField(choices=[(b'01', b'Day 1, 9:00am'), (b'02', b'Day 1, 11:00am'), (b'03', b'Day 1, 1:00pm'), (b'04', b'Day 1, 3:00pm'), (b'05', b'Day 1, 5:00pm'), (b'11', b'Day 2, 9:00am'), (b'12', b'Day 2, 11:00am'), (b'13', b'Day 2, 1:00pm'), (b'14', b'Day 2, 3:00pm'), (b'15', b'Day 2, 5:00pm')], default=b'01', max_length=2),
        ),
    ]