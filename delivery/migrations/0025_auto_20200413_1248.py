# Generated by Django 3.0.1 on 2020-04-13 09:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0024_auto_20200412_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 13, 12, 48, 37, 17021)),
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.NewsComment')),
            ],
        ),
    ]