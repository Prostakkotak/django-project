# Generated by Django 3.0.1 on 2020-04-11 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0021_auto_20200412_0055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='views',
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 12, 0, 58, 33, 211966)),
        ),
    ]