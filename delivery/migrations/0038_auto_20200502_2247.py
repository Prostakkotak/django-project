# Generated by Django 3.0.1 on 2020-05-02 19:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0037_auto_20200427_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 22, 47, 52, 154594)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 22, 47, 52, 153596), editable=False),
        ),
        migrations.AlterField(
            model_name='proposednews',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 2, 22, 47, 52, 156595)),
        ),
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_weight', models.IntegerField()),
                ('package_volume', models.IntegerField()),
                ('path_length', models.IntegerField()),
                ('cost', models.FloatField()),
                ('delivery_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryClass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]