# Generated by Django 3.0.1 on 2020-04-17 15:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0033_auto_20200417_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 18, 28, 2, 830289)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 18, 28, 2, 830289), editable=False),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
