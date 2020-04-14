# Generated by Django 3.0.1 on 2020-04-14 19:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0030_auto_20200414_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 14, 22, 38, 26, 558939)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 22, 38, 26, 557939), editable=False),
        ),
    ]