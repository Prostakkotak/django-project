# Generated by Django 3.0.1 on 2020-05-02 20:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0038_auto_20200502_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='vehisle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Vehisle'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 23, 8, 1, 309486)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 23, 8, 1, 308484), editable=False),
        ),
        migrations.AlterField(
            model_name='proposednews',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 23, 8, 1, 311485)),
        ),
    ]
